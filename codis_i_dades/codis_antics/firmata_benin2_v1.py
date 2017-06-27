#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Programa que llegeix les entrades analògiques d'Arduino a través
de Firmata, les processa i n'emmagatzema el valor en un fitxer.
Opcionalment es poden pujar a https://thingspeak.com/channels/209407

A0 - Humitat ambient

A1 - Temperatura ambient

A2 - Corrent de plaques mesurat amb un sensor de corrent efecte hall
     ACS712 que dona una tensió = VCC/2 + 185mV/A (Max 5A)
     Aquest corrent prové d'un divisor de corrent. El corrent real 
     s'obté multiplicant per quatre

A3 - Tensió bateries (aprox. 24V)
     Divisor de tensió 4.61k-816ohm (30V => 4.5V)

A4 - Tensió en terminals de les plaques fotovoltaiques mesurades usant
     un optoacoplador, s'utilitza una taula per a transformar tensió
     plaques després optoacoplador (no és lineal)

A5 - Corrent de consum AC (230Vef) mesurat amb un sensor de corrent
     efecte hall ACS712 que dona una tensió = VCC/2 + 185mV/A (Max 5A)
     Aquest corrent prové d'un divisor de corrent. El corrent real 
     s'obté multiplicant per sis.
     L'Arduino ens dona el valor màxim després de fer 20 lectures cada ms.
"""

import pyfirmata
import sys, os
import datetime, time
import requests

DATA_DIR = "/home/pi/dades/"
LOG_FILE = "/home/pi/firmata_log.txt"

DEBUG = 0       # 0- Sense prints, 1- Per terminal, 2- A fitxer
THINGSPEAK = 1  # Pujada de dades a IoT
SAVE_DATA = 1   # Emmagatzematge dades en fitxer

SAMPLING_INTERVAL = 1 * 60 # Temps entre mostres (minuts * segons)
UPLOAD_INTERVAL = SAMPLING_INTERVAL * 60 # Pujada a ThingSpeak

# Temps d'espera de lectura de mostres (en relació amb l'Arduino)
T_A = 1
D_T = 0.5
T0 = T_A+D_T
T1 = T_A+D_T
T2 = T_A+D_T
T3 = T_A+D_T
T4 = T_A+D_T
T5 = T_A+D_T

# Per debugar es poden desactivar sensors. Per a guardar dades no
A0 = 1
A2 = 1
A3 = 1
A4 = 1
A5 = 1

if DEBUG == 2:
    save_stdout = sys.stdout
    log_file = open(LOG_FILE, "a")
    sys.stdout = log_file

def db_print(msg):
    """
    Imprimeix el missatge 'msg' en funció del valor de DEBUG:
    1 - Imprimeix per pantalla
    2 - Imprimeix en el fitxer de log
    Altres - No s'imprimeix el missatge
    """
    if DEBUG == 1:
        print msg
    elif DEBUG == 2:
        log_file.write(msg)
        log_file.flush()

def get_arduino():
    """
    Retorna una instància de pyfirmata.Arduino o 0 en cas que no
    s'hi hagi pogut connectar
    Nota: Si s'executa el programa d'inici es troba l'Arduino estigui
    al port que estigui. Però si es desconnecta a mig fer no el torna
    a trobar. Falta afegir flush???
    Millora: En comptes de mirar cada port fer-ho en funció del què
    hi hagi a /dev/ttyACM* 
    """
    devices = ["/dev/ttyACM0", "/dev/ttyACM1", "/dev/ttyACM2",
               "/dev/ttyACM3", "/dev/ttyACM4", "/dev/ttyACM5"]
    board = 0
    for device in devices:
        db_print("Connectant amb {}".format(device))
        try:
            board = pyfirmata.Arduino(device)
            db_print("Arduino connectat a {}".format(device))
            return board
        except:
            db_print("No s'ha pogut connectar amb {}".format(device))
    return 0

board = get_arduino()
if board == 0:
    db_print("No hi ha connexió amb Arduino!")
    sys.exit(0)
    
board.pass_time(1)
it = pyfirmata.util.Iterator(board)
it.start()
board.pass_time(1)

new_data = 0

previous_t = time.time()-SAMPLING_INTERVAL  # Temps entre presa de mostres 
previous_upload = previous_t-UPLOAD_INTERVAL+SAMPLING_INTERVAL  # Interval de pujada a Thingspeak

while 1:
    try:

        # Interval de mostreig
        while (time.time() - previous_t < SAMPLING_INTERVAL):
            time.sleep(1)
        previous_t = time.time()
        
        try:

            # A1 - Temperatura necessària per a calcular Vcc
            board.analog[1].enable_reporting()
            board.pass_time(T1)
            a1 = board.analog[1].read() # Sense correció per Vref=1.1
            val1 = a1*110-50
            db_print("\nTemperatura: {:.1f}".format(val1))

            # Vcc en funció de la temperatura
            if (val1 < 26):
                vcc = 4.74
            elif (val1 < 30):
                vcc = 4.72 - (val1-30)*0.005
            elif (val1 < 32):
                vcc = 4.68 - (val1-32)*0.020
            else:
                vcc = 4.68
            k = vcc/5.0
            db_print("Vcc: {:.2f}".format(vcc))
            
            if A0:
                board.analog[0].enable_reporting()
                board.pass_time(T0)
                a0 = k*board.analog[0].read()
                val0 = ((a0 - 0.16) / 0.0062)#/(1.0546-0.00216*val1) # val1 - temperatura en ºC
                if (val0 > 100):
                    val0 = 100
                if (val0 < 0):
                    val0 = 0
                db_print("Humitat: {:.0f}".format(val0))
            
            if A4:
                board.analog[4].enable_reporting()
                board.pass_time(T4)
                a4 = k*board.analog[4].read()
                if (val1 < 30):
                    if (a4*5 < 1.22):
                        val4 = 179+(a4*5-1.22)*(179/(1.22-0.1))
                    elif (a4*5 < 2.22):
                        val4 = 299+(a4*5-2.22)*120
                    else:
                        val4 = 299+(a4*5-2.22)*180
                elif (val1 < 32):
                    if (a4*5 < 1.67):
                        val4 = 209+(a4*5-1.67)*(209/(1.67-0.1))
                    else:
                        val4 = 339+(a4*5-2.67)*130
                else:
                    if (a4*5 < 0.79):
                        val4 = 140+(a4*5-0.79)*(140/(0.79-0.1))
                    elif (a4*5 < 1.75):
                        val4 = 200+(a4*5-1.75)*(60/(1.75-0.79))
                    else:
                        val4 = 350+(a4*5-2.75)*150                    
                if (val4 < 0):
                    val4 = 0
                db_print("Tensió plaques: {:.0f}".format(val4))
                
            if A2:
                board.analog[2].enable_reporting()
                board.pass_time(T2)
                a2 = k*board.analog[2].read()
                i2 = 4*((a2*5-vcc/2)/0.185) # Corrent DC
                if (i2 < 0):
                    i2 = 0
                val2 = i2*val4   # Potència
                db_print("Corrent plaques: {:.1f}".format(i2))
                db_print("Potencia plaques: {:.0f}".format(val2))
                            
            if A3:
                board.analog[3].enable_reporting()
                board.pass_time(T3)
                a3 = k*board.analog[3].read()
                val3 = a3*5/0.15
                if (val3 < 0):
                    val3 = 0
                db_print("Tensió bateries: {:.1f}".format(val3))

            if A5:
                board.analog[5].enable_reporting()
                board.pass_time(T5)
                a5 = k*board.analog[5].read()
                i5 = 6*a5*5/1.414/2/0.185  # Corrent eficaç
                val5 = i5*230   # Potència
                db_print("Corrent consum AC 1: {:.1f}".format(i5))
                db_print("Potència consum AC: {:.0f}".format(val5))
                                
            new_data = 1

        except Exception as ex:
            new_data = 0
            db_print("Exception: {}".format(str(ex)))
            board = get_arduino()
            #if board == 0:   # reboot si no troba Arduino 
            #    os.system("sudo reboot")  
            
        if SAVE_DATA and new_data:
            # Emmagatzematge de dades en fitxer
            current_datetime = datetime.datetime.now()
            timestamp = datetime.datetime.strftime(current_datetime, "%H:%M:%S")
            current_date = datetime.datetime.strftime(current_datetime, "%Y_%m_%d")
            
            # Format CSV dades a guardar
            # HH:MM, humitat, temperatura,corrent_dc,tensio_bat,tensio_plaques,corrent_ac(eficaç)
            results = "{},{:.0f},{:.1f},{:.1f},{:.1f},{:.0f},{:.1f}\n".format(timestamp, val0, val1, i2, val3, val4, i5)
            datafile = open(DATA_DIR + current_date, 'a')
            datafile.write(results)
            datafile.close()

            db_print("S'han guardat dades a les {}".format(timestamp))

            # Última dada es guarda per a la RPi 1
            lastdata = open(DATA_DIR + "last_data",'w')
            lastdata.write(current_date+" "+results)
            lastdata.close()

            new_data = 0

            # Pujada a ThingSpeak cada UPLOAD_INTERVAL de temps
            if THINGSPEAK and (time.time() - previous_upload > UPLOAD_INTERVAL):
                try:
                    # Els paràmetres de requests.get es passen com a dict
                    data_dict = {"key": "NISEZMXLKBW9GFUV"}
                    data_dict["field1"] = "{:.0f}".format(val0)
                    data_dict["field2"] = "{:.1f}".format(val1)
                    data_dict["field3"] = "{:.1f}".format(val3)
                    data_dict["field4"] = "{:.0f}".format(val4)
                    data_dict["field5"] = "{:.0f}".format(val2)
                    data_dict["field6"] = "{:.0f}".format(val5)
                    r = requests.get("http://api.thingspeak.com/update", params=data_dict, timeout=60)
                    db_print("ThingSpeak. Actualització núm. {}".format(r.text))
                except Exception as ex:
                    db_print(str(ex))
                    if (os.system("ping -c 1 8.8.8.8") != 0):
                        db_print("No hi ha connexió a internet")
                previous_upload = time.time()        
            
    except KeyboardInterrupt:
        db_print("Exiting")
        if DEBUG == 2:
            log_file.close()
            sys.stdout = save_stdout    
        board.exit()
        sys.exit(0)
