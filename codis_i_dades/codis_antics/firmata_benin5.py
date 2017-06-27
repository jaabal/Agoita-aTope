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
     Divisor de tensió 6.74k-816ohm (30V => 3.24V)


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
LAST_DATA_F = DATA_DIR + "last_data"

FILES_DIR = "/home/pi/firmata_benin/"
LOG_F = FILES_DIR+"firmata.log"
PREVIOUS_UPLOAD_F = FILES_DIR + "previous_upload"

DEBUG = 1       # 0- Sense prints, 1- Per terminal, 2- A fitxer
THINGSPEAK = 1  # Pujada de dades a IoT
SAVE_DATA = 1   # Emmagatzematge dades en fitxer

SAMPLING_INTERVAL = 1 * 60 # Temps entre mostres (minuts * segons)

# Paràmetres Thingspeak
HOUR_UPLOAD = []     # Llista amb les hores de pujada (0..23)
MINUTE_UPLOAD = [0]  # Llista amb els minuts de pujada de dades (0..59)
                     # Buits -> cada hora, cada minut
                     
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

# Mitjanes per a pujar a Thingspeak
averages = [0 for i in range(6)]
n_samples = 0

internet = 0

if DEBUG == 2:
    SAVE_STDOUT = sys.stdout
    log_file = open(LOG_F, "a")
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
        log_file.write(msg+'\n')
        log_file.flush()

def get_arduino():
    """
    Retorna una instància de pyfirmata.Arduino o 0 en cas que no
    s'hi hagi pogut connectar
    Nota: Si s'executa el programa d'inici es troba l'Arduino estigui
    al port que estigui. Però si es desconnecta a mig fer no el torna
    a trobar. Falta afegir flush???
    """
    devices = ["/dev/"+dev for dev in os.listdir("/dev") if "ttyACM" in dev]
    global board
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

def check_internet():
    """
    Comprova si hi ha sortida a internet
    """
    if (os.system("ping -c 1 -W 60 8.8.8.8") == 0):
        db_print("Hi ha connexió a internet.")
        return True
    else:
        db_print("No hi ha connexió a internet.")
        return False


def upload_required(prev, now):
    """
    Retorna True en cas que s'hagin de pujar les dades a ThingSpeak
    
    >>> prev = datetime.datetime(2017, 1, 20, 10, 20, 0)
    >>> now = datetime.datetime(2017, 1, 20, 11, 20, 0)
    >>> upload_required(prev, now)
    True
    
    >>> prev = datetime.datetime(2017, 1, 20, 1, 10, 0)
    >>> now = datetime.datetime(2017, 1, 20, 1, 20, 0)
    >>> upload_required(prev, now)
    False
    
    # Canvi de dia
    >>> prev = datetime.datetime(2017, 1, 20, 23, 1, 0)
    >>> now = datetime.datetime(2017, 1, 21, 0, 1, 0)
    >>> upload_required(prev, now)
    True
    """

    try:
        hours = HOUR_UPLOAD
        minutes = MINUTE_UPLOAD
        if hours == []:
            hours = range(24)
        if minutes == []:
            minutes = range(60)
        
        for h in hours:
            for m in minutes:
                next_upload = prev.replace(hour=h, minute=m, second=0, microsecond=0)
                if ((prev < next_upload) and (next_upload < now)):
                    db_print("Cal pujar dades. Prev: {}, Now: {}".format(prev, next_upload, now))
                    return True
        
        # Repetició per al següent dia
        d = int(prev.day)+1
        for h in hours:
            for m in minutes:
                next_upload = prev.replace(day=d, hour=h, minute=m, second=0, microsecond=0)
                if ((prev < next_upload) and (next_upload < now)):
                    db_print("Cal pujar dades. Prev: {}, Now: {}".format(prev, next_upload, now))
                    return True
        
                
        db_print("No cal pujar dades. Prev: {}, Now: {}".format(prev, now))
    except Exception as ex:
        db_print("Error calculant l'hora")
        db_print(str(ex))
    return False


def set_previous_upload(t):
    """
    Guarda l'hora en què s'han pujat les dades a Thingspeak
    en el fitxer previous_upload
    """
    f = open(PREVIOUS_UPLOAD_F, "w")
    f.write(t)
    f.close()
    db_print("previous_upload guardada a fitxer {}".format(t))

    
def get_previous_upload():
    """
    Llegeix l'hora de l'última pujada a ThingSpeak del fitxer
    previous_upload
    """
    f = open(PREVIOUS_UPLOAD_F, "r")
    line = f.readline().replace("\n", "")
    fields = line.replace("-", " ").replace(":", " ").split()
    f_int = [int(float(x)) for x in fields]
    f.close()
    db_print("previous_upload de fitxer: {}".format(line))
    return datetime.datetime(f_int[0],f_int[1],f_int[2],f_int[3],f_int[4],f_int[5])


def upload_thingspeak(av, n):
    """
    Pujada de les mitjanes a ThingSpeak. El càlcul es fa aquí per a
    conservar els valors al programa principal en cas que no vagi bé.
    """
    a = [0 for i in range(6)]
    for i in range(len(av)): 
        a[i] = av[i]/n

    db_print("S'han recollit {} mostres".format(n))
    db_print("Les mitjanes a pujar són {}".format(a))

    try:
        # Els paràmetres de requests.get es passen com a dict
        data_dict = {"key": "NISEZMXLKBW9GFUV"}
        data_dict["field1"] = "{:.0f}".format(a[0])
        data_dict["field2"] = "{:.1f}".format(a[1])
        data_dict["field3"] = "{:.1f}".format(a[3])
        data_dict["field4"] = "{:.0f}".format(a[4])
        data_dict["field5"] = "{:.0f}".format(a[2])
        data_dict["field6"] = "{:.0f}".format(a[5])

        r = requests.get("http://api.thingspeak.com/update", params=data_dict, timeout=60)
        db_print("ThingSpeak. Actualització núm. {}".format(r.text))
        
        return 1

    except Exception as ex:
        db_print(str(ex))
        check_internet()

    return 0

def store_data(val0, val1, i2, val3, val4, i5):
    """
    Emmagatzematge de les dades a fitxer. Si no hi ha hagut internet només
    es guarden a last_data
    """
    global internet
    try:
        db_print("Guardant dades")
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

        # En cas que no s'hagi pogut comprovar l'hora
        if not internet:
            current_date = "----/--/--"
        
        # Última dada es guarda per a la RPi 1
        lastdata = open(DATA_DIR + "last_data",'w')
        lastdata.write(current_date+" "+results)
        lastdata.close()

    except Exception as ex:
        db_print("Error guardant les dades")
        db_print(str(ex))

        
        
if __name__ == "__main__":

    board = get_arduino()

    if board == 0:
        db_print("No hi ha connexió amb Arduino!")
        sys.exit(0)

    db_print("Inici de programa")
    board.pass_time(1)
    it = pyfirmata.util.Iterator(board)
    it.start()
    board.pass_time(1)

    new_data = 0

    previous_saved = time.time()-SAMPLING_INTERVAL  # Temps entre presa de mostres 
    previous_upload = get_previous_upload()

    internet = check_internet()
    
    while 1:
        try:
            # En cas que no s'hagi pogut comprovar l'internet
            if not internet:
                internet = check_internet()

            # Interval de mostreig
            while (time.time() - previous_saved < SAMPLING_INTERVAL):
                pass
            previous_saved = time.time()

            db_print("Prenent mostres")                    
            try:

                # A1 - Temperatura necessària per a calcular Vcc
                board.analog[1].enable_reporting()
                board.pass_time(T1)
                a1 = board.analog[1].read() # Sense correció per Vref=1.1
                val1 = a1*330-50
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
                    aref = 3.3
                    board.analog[0].enable_reporting()
                    board.pass_time(T0)
                    a0 = board.analog[0].read()
                    val0 = (a0*aref - 0.826)/0.0315 # Lectura màxima del 78% !
                    if (val0 < 0):
                        val0 = 0
                    db_print("Humitat: {:.0f}".format(val0))
                
                if A4:
                    aref = 3.3
                    board.analog[4].enable_reporting()
                    board.pass_time(T4)
                    a4 = board.analog[4].read()
                    db_print("A4 {}".format(a4))
                    if (val1 < 30):
                        if (a4*aref < 1.22):
                            val4 = 179+(a4*aref-1.22)*(179/(1.22-0.1))
                        elif (a4*aref < 2.22):
                            val4 = 299+(a4*aref-2.22)*120
                        else:
                            val4 = 299+(a4*aref-2.22)*180
                    elif (val1 < 32):
                        if (a4*aref < 1.67):
                            val4 = 209+(a4*aref-1.67)*(209/(1.67-0.1))
                        else:
                            val4 = 339+(a4*aref-2.67)*130
                    else:
                        if (a4*aref < 0.79):
                            val4 = 140+(a4*aref-0.79)*(140/(0.79-0.1))
                        elif (a4*aref < 1.75):
                            val4 = 200+(a4*aref-1.75)*(60/(1.75-0.79))
                        else:
                            val4 = 350+(a4*aref-2.75)*150 
                            
                            
                    #k3=19;k2=-101;k1=280;k0=-27;val4=k3*(a4*aref)**3+k2*(a4*aref)**2+k1*(a4*aref)+k0;


                            
                    if (val4 < 0):
                        val4 = 0
                    db_print("Tensió plaques: {:.0f}".format(val4))
                
                if A2:
                    aref = 3.3
                    board.analog[2].enable_reporting()
                    board.pass_time(T2)
                    a2 = board.analog[2].read()
                    i2 = 4*((a2*aref-vcc/2)/0.185) # Corrent DC, referida a vcc/2 (2.34V aprox)
                    if (i2 < 0):
                        i2 = 0
                    val2 = i2*val4   # Potència
                    db_print("Corrent plaques: {:.1f}".format(i2))
                    db_print("Potència plaques: {:.0f}".format(val2))

                if A3:
                    aref = 3.3
                    board.analog[3].enable_reporting()
                    board.pass_time(T3)
                    a3 = board.analog[3].read()
                    val3 = a3*aref/0.108    # divisor 820ohm i 6k8ohm
                    if (val3 < 0):
                        val3 = 0
                    db_print("Tensió bateries: {:.1f}".format(val3))

                if A5:
                    aref = 3.3
                    board.analog[5].enable_reporting()
                    board.pass_time(T5)
                    a5 = board.analog[5].read()
                    i5 = 6*a5*aref/1.414/2/0.185  # Corrent eficaç
                    val5 = i5*230   # Potència
                    db_print("A5: {}".format(a5))
                    db_print("Corrent consum AC: {:.1f}".format(i5))
                    db_print("Potència consum AC: {:.0f}".format(val5))
                                
                new_data = 1

                if THINGSPEAK:
                    # Fem les mitjanes per a pujar després a Thingspeak
                    averages[0] += val0
                    averages[1] += val1
                    averages[2] += val2
                    averages[3] += val3
                    averages[4] += val4
                    averages[5] += val5
                    n_samples += 1 

                
            except Exception as ex:
                new_data = 0
                db_print("Excepció: {}".format(str(ex)))
                board = get_arduino()

                
            # Emmagatzematge de dades i pujada a ThingSpeak
            if SAVE_DATA and new_data:
                store_data(val0, val1, i2, val3, val4, i5)
                new_data = 0

                if THINGSPEAK and (upload_required(previous_upload, datetime.datetime.now())):
                    db_print("Pujant a ThingSpeak")
                    if upload_thingspeak(averages, n_samples):
                        previous_upload = datetime.datetime.fromtimestamp(time.time())
                        set_previous_upload(str(previous_upload))
                        averages = [0 for i in range(6)]
                        n_samples = 0

                        
        except KeyboardInterrupt:
            # Sortida per teclat
            db_print("Sortint...")
            if DEBUG == 2:
                log_file.close()
                sys.stdout = SAVE_STDOUT
            board.exit()
            sys.exit(0)
