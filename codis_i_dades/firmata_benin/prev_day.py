#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Programa que llegeix el fitxer del dia anterior de la carpeta dades
i guarda màxims i mínims al fitxer yesterday. L'script serà cridat amb
cron cada dia a les 00:05 i a /etc/rc.local per a comprovar que s'ha
fet a les 12 (falta fer-ho)

Format del fitxer 'yesterday':

timestamp
temp_max, temp_max_t, temp_min, temp_min_t
hum_max, hum_max_t, hum_min, hum_min_t
bat_max, bat_max_t, bat_min, bat_min_t
consum_max, consum_max_t

"""

import sys, os
import datetime, time

DATA_DIR = "/home/pi/dades/"
#DATA_DIR = "/home/ababi/Benín/proves/"
YESTERDAY_F = DATA_DIR + "yesterday"

FILES_DIR = "/home/pi/firmata_benin/"
#FILES_DIR = "/home/ababi/Benín/proves/"
LOG_F = FILES_DIR+"prev_day.log"

DEBUG = 2       # 0- Sense prints, 1- Per terminal, 2- A fitxer

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


def send_yesterday():
    """
    Envia el fitxer yesterday a la RPi1
    """
    try:
        last_data_f = DATA_DIR+"yesterday"
        remote_f = "pi@192.168.33.1:/home/pi/display/yesterday"
        my_rsa_id = "/home/pi/.ssh/id_rsa"
        scp_command = "scp -i {} {} {}".format(my_rsa_id, last_data_f, remote_f)
        db_print("Enviant yesterday")
        if (os.system(scp_command) == 0):
            db_print("Fitxer yesterday enviat!")
            return True
        
    except Exception as ex:
        db_print("Error enviant yesterday")
        db_print(str(ex))
        
    return False
                            

if __name__ == "__main__":

    db_print("Comença script prev_day")

    try:
        now = datetime.datetime.now()
        t = datetime.datetime.strftime(now, "%Y/%m%d %H:%M:%S")
        db_print("Timestamp: {}".format(t))
    
        yesterday_datetime = datetime.datetime.now() - datetime.timedelta(days=1)
        y = yesterday_datetime.year
        m = yesterday_datetime.month
        d = yesterday_datetime.day

        
        filename = "{}_{:02d}_{:02d}".format(y,m,d)

        try:
            f2 = open(YESTERDAY_F, "r")
            lines = f2.readlines()
            f2.close()
            if filename in lines[0]:
                db_print("Fitxer yesterday OK. Sortint...")
                sys.exit(0)
            else:
                db_print("Fitxer yesterday no actualitzat")

        except Exception as ex:
            db_print("Fitxer yesterday no existeix")
                                                                                                                            

        db_print("Llegint fitxer {}".format(DATA_DIR+filename))
        f = open(DATA_DIR+filename, "r")

        lines = f.readlines()

        temp_max, temp_max_t = 0, 0
        temp_min, temp_min_t = 1000, 0
        hum_max, hum_max_t = 0, 0
        hum_min, hum_min_t = 1000, 0
        bat_max, bat_max_t = 0, 0
        bat_min, bat_min_t = 1000, 0
        cons_max, cons_max_t = 0, 0

        db_print("Calculant màxims i mínims")
        for line in lines:
            line = line.replace("\n", "")
            line = line.split(",")
            
            time = line[0][:5]
            hum = int(line[1])
            temp = float(line[2])
            bat = float(line[4])
            cons = float(line[6])*230

            if hum < hum_min:
                hum_min = hum
                hum_min_t = time
            if hum > hum_max:
                hum_max = hum
                hum_max_t = time

            if temp < temp_min:
                temp_min = temp
                temp_min_t = time
            if temp > temp_max:
                temp_max = temp
                temp_max_t = time

            if bat < bat_min:
                bat_min = bat
                bat_min_t = time
            if bat > bat_max:
                bat_max = bat
                bat_max_t = time
                
            if cons > cons_max:
                cons_max = cons
                cons_max_t = time

        db_print("Guardant dades a 'yesterday'")
        f = open(DATA_DIR+"yesterday", "w")
        f.write("{}\n".format(filename))
        f.write("{:.1f},{},{:.1f},{}\n".format(temp_max, temp_max_t, temp_min, temp_min_t))
        f.write("{:.0f},{},{:.0f},{}\n".format(hum_max, hum_max_t, hum_min, hum_min_t))
        f.write("{:.1f},{},{:.1f},{}\n".format(bat_max, bat_max_t, bat_min, bat_min_t))
        f.write("{},{}\n".format(cons_max, cons_max_t))
        f.flush()
        f.close()
            
        db_print("Temp max: {} ({}). Temp min: {} ({})".format(temp_max, temp_max_t, temp_min, temp_min_t))
        db_print("Hum max: {} ({}). Hum min: {} ({})".format(hum_max, hum_max_t, hum_min, hum_min_t))
        db_print("Bat max: {} ({}). Bat min: {} ({})".format(bat_max, bat_max_t, bat_min, bat_min_t))
        db_print("AC cons max: {} ({})".format(cons_max, cons_max_t))

        try:
            send_yesterday()
        except Exception as ex:
            db_print("No s'ha pogut enviar el fitxer yesterday")
                    
            
    except Exception as ex:
        db_print("No s'ha pogut actualitzar el fitxer yesterday")
        db_print(str(ex))
