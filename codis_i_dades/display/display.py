#-*- coding: utf-8 -*-
#!/usr/bin/python

"""
Exemple modificat de Adafruit_Python_CharLCD/examles/char_lcd.py

Programa que mostra la informació dels fitxers 'last_data' i
'yesterday' en el display LCD. El bucle principal s'encarrega de:

1) Comprovar si s'ha apretat el polsador i mostrar dades en cas
afirmatiu

2) Comprovar si ha passat un temps de INTERVAL i actualitzar l'estat
dels leds en funció del fitxer 'last_data' (val3 -> tensió bateries)

Nota: Els fitxers 'last_data' i 'yesterday' s'envien periòdicament des
de la RPi2. En cas que no existeixin (i en el cas de 'yesterday' no
estigui actualitzat, els intenta copiar per SCP.
"""

import time, datetime
import sys, os
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

# Fitxers
DEBUG = 2
DIR = "/home/pi/display/"
LOG_F = DIR+"display.log"
LAST_DATA_F = DIR+"last_data"
YESTERDAY_F = DIR+"yesterday"

# Repetició display
TIME_1, TIME_2 = 2.5, 4
LAST_DATA_REPEAT = 2
YESTERDAY_REPEAT = 1

# Llindars LEDs
THRESHOLD_H = 26.5
THRESHOLD_L = 24

# Interval mostreig i timeout per a rebre 'yesterday'
INTERVAL = 60
TIMEOUT_SCP = 10

# Raspberry Pi pin configuration (canviats per a millor disposició)
led_yellow    = 21
led_red       = 9
button0       = 11
lcd_rs        = 23
lcd_en        = 24 
lcd_d4        = 5
lcd_d5        = 6
lcd_d6        = 13
lcd_d7        = 19
lcd_backlight = 26

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

if DEBUG == 2:
    SAVE_STDOUT = sys.stdout
    log_file = open(LOG_F, "a")
    sys.stdout = log_file

def db_print(msg):
    """
    Imprimeix el missatge 'msg' en funció del valor de DEBUG:
    1- Imprimeix per pantalla
    2- Imprimeix en el fitxer de log
    Altres- No s'imprimeix el missatge
    """
    if DEBUG == 1:
        print msg
    elif DEBUG == 2:
        # Alternativa: python display_benin.py > log
        log_file.write(msg+'\n')
        log_file.flush()

        
def get_file_scp(filename):
    """
    Copia el fitxer 'filename' de la RPi2 per SCP. Busca la clau rsa
    pròpia a ~/.ssh/id_rsa per a què funcioni per a tots els usuaris
    (pi i sudo).
    """
    try:
        dest_f = DIR+filename
        remote_f = "pi@192.168.33.2:/home/pi/dades/{}".format(filename)
        my_rsa_id = "/home/pi/.ssh/id_rsa"
        scp_command = "scp -i {} {} {}".format(my_rsa_id, remote_f, dest_f)
        db_print("Obtenint fitxer {}".format(filename))
        if (os.system(scp_command) == 0):
            db_print("Fitxer {} rebut!".format(filename))
            return True

    except Exception as ex:
        db_print("Error rebent fitxer {}".format(filename))
        db_print(str(ex))
    return False


def show_last_data():
    """
    Mostra en el display el contingut del fitxer 'last_data', en cas
    que no existeixi l'intenta copiar de la RPi2
    """
    # Lectura de fitxer
    last_data_ok = False
    prev_time = time.time()
    while (not last_data_ok) and (time.time() - prev_time < TIMEOUT_SCP):
        try:
            f = open(LAST_DATA_F, "r")
            lines = f.readlines()
            f.close()
            db_print("S'ha llegit el fitxer 'last_data'")
            last_data_ok = True
        except Exception as ex:
            db_print("Fitxer 'last_data' no existeix")
            get_file_scp("last_data")

    if not last_data_ok:
        db_print("No hi ha informació actual disponible")
        lcd.clear()
        lcd.message("Donnees actuel.\nnon disponible")
        time.sleep(TIME_2)
        return 0

    line = lines[0].replace("_", "/").replace("\n", "")
    msg = line.split(",")
    
    data_time = msg[0]
    val0 = msg[1]
    val1 = msg[2]
    i2 = msg[3]
    val3 = msg[4]
    val4 = msg[5]
    i5 = msg[6]
    
    val2 = float(i2)*float(val4)
    val5 = float(i5)*230

    # Display
    for i in range(LAST_DATA_REPEAT):
        t = datetime.datetime.strftime(datetime.datetime.now(),
                                       "%Y/%m/%d %H:%M")
                        
        lcd.clear()
        lcd.message("Donnees actuel.\n{}".format(t))
        db_print("Hora: {}".format(t))
        time.sleep(TIME_1)
        
        lcd.clear()
        lcd.message("Heure donnees\n{}".format(data_time))  # doneés
        db_print("Hora dades: {}".format(data_time))
        time.sleep(TIME_1)
        
        lcd.clear()
        lcd.message("Batteries\n{}V".format(val3))
        db_print("Bateries: {}V".format(val3))
        time.sleep(TIME_1)
                    
        lcd.clear()
        lcd.message("Consommation AC\n230V {}A {:.0f}W".format(i5, val5))
        db_print("Consum AC: {}A {:.0f}W".format(i5, val5))
        time.sleep(TIME_2)
        
        lcd.clear()
        lcd.message("Plaques//Turbine\n{}V {}A {:.0f}W".format(val4, i2, val2))
        db_print("Plaques: {}V {}A {:.0f}W".format(val4, i2, val2))
        time.sleep(TIME_2)
                
        lcd.clear()
        lcd.message("Humidite\n{} %".format(val0)) # humidité
        db_print("Humitat: {} %".format(val0))
        time.sleep(TIME_1)
        
        lcd.clear()
        lcd.message("Temperature\n{} oC".format(val1))
        db_print("Temperatura: {} ºC".format(val1))
        time.sleep(TIME_1)
    return 1    
    
def show_yesterday():
    """
    Mostra en el display el contingut del fitxer 'yesterday'. En cas
    que no existeixi o no tingui la data del dia anterior, l'intenta
    copiar de la RPi2
    """
    yesterday_ok = False
    prev_time = time.time()
    while (not yesterday_ok) and (time.time() - prev_time < TIMEOUT_SCP):

        # Comprovem que 'yesterday' existeixi i correspongui al dia anterior
        try:
            f2 = open(YESTERDAY_F, "r")
            lines = f2.readlines()
            f2.close()
            
            yesterday_datetime = datetime.datetime.now() - datetime.timedelta(days=1)
            y = yesterday_datetime.year
            m = yesterday_datetime.month
            d = yesterday_datetime.day
            
            yesterday_date = "{}_{:02d}_{:02d}\n".format(y,m,d)

            if yesterday_date in lines[0]:
                db_print("Fitxer 'yesterday' OK")
                yesterday_ok = True
            else:
                db_print("Fitxer 'yesterday' no actualitzat")
                get_file_scp("yesterday")

        except Exception as ex:
            db_print("Fitxer 'yesterday' no existeix")
            get_file_scp("yesterday")
    
    # En cas que no tinguem el fitxer yesterday actualitzat
    if (not yesterday_ok):
        db_print("No hi ha informació d'ahir")
        lcd.clear()
        lcd.message("Donnees hier\nnon disponible")
        time.sleep(TIME_2)
        return 0
    
    # Dades del fitxer
    timestamp = lines[0].replace("_","/").replace("\n", "")
    db_print("Reading: {}".format(timestamp))

    db_print(lines[1])
    db_print(lines[2])
    db_print(lines[3])
    db_print(lines[4])
            
    temp_max, temp_max_t, temp_min, temp_min_t = lines[1].replace("\n", "").split(",")
    hum_max, hum_max_t, hum_min, hum_min_t = lines[2].replace("\n", "").split(",")
    bat_max, bat_max_t, bat_min, bat_min_t = lines[3].replace("\n", "").split(",")
    cons_max, cons_max_t = lines[4].replace("\n", "").split(",")
        
    # Display
    for i in range(YESTERDAY_REPEAT):
        lcd.clear()
        lcd.message("Donnees hier\n{}".format(timestamp))
        db_print("Dades d'ahir: {}".format(timestamp))
        time.sleep(TIME_2)
        
        lcd.clear()
        lcd.message("Batteries max.\n{}V - {}".format(bat_max, bat_max_t))
        db_print("Màxim bateries: {}V - {}".format(bat_max, bat_max_t))
        time.sleep(TIME_2)
    
        lcd.clear()
        lcd.message("Batteries min.\n{}V - {}".format(bat_min, bat_min_t))
        db_print("Mínim bateries: {}V - {}".format(bat_min, bat_min_t))
        time.sleep(TIME_2)
        
        lcd.clear()
        lcd.message("Consomattion max\n{}W - {}".format(cons_max, cons_max_t))
        db_print("Consum màxim: {}W - {}".format(cons_max, cons_max_t))
        time.sleep(TIME_2)
        
        lcd.clear()
        lcd.message("Temperature max.\n{}oC - {}".format(temp_max, temp_max_t))
        db_print("Temperatura màxima: {}oC - {}".format(temp_max, temp_max_t))
        time.sleep(TIME_2)
        
        lcd.clear()
        lcd.message("Temperature min.\n{}oC - {}".format(temp_min, temp_min_t))
        db_print("Temperatura mínima: {}oC - {}".format(temp_min, temp_min_t))
        time.sleep(TIME_2)
        
        lcd.clear()
        lcd.message("Humidite max.\n{}% - {}".format(hum_max, hum_max_t))
        db_print("Humitat màxima: {}% - {}".format(hum_max, hum_max_t))
        time.sleep(TIME_2)
            
        lcd.clear()
        lcd.message("Humidite min.\n{}% - {}".format(hum_min, hum_min_t))
        db_print("Humitat mínima: {}% - {}".format(hum_min, hum_min_t))
        time.sleep(TIME_2)
    return 1


def update_leds():
    """
    Llegeix el fitxer 'last_data' i activa els leds segons l'estat de
    les bateries. En cas que no existeixi l'intenta copiar SCP.
    * El led_red s'activa quan la tensió és inferior a THRESHOLD_L
    * El led_yellow s'activa quan la tensió és superior a THRESHOLD_H
    """
    last_data_ok = False
    prev_time = time.time()
    while (not last_data_ok) and (time.time() - prev_time < TIMEOUT_SCP):
        try:
            f = open(LAST_DATA_F, "r")
            lines = f.readlines()
            f.close()
            db_print("S'ha llegit el fitxer 'last_data'")
            last_data_ok = True
        except Exception as ex:
            db_print("Fitxer 'last_data' no existeix")
            get_file_scp("last_data")

    if not last_data_ok:
        db_print("No hi ha informació actual disponible")
        lcd.clear()
        lcd.message("Donnees actuel.\nnon disponible")
        time.sleep(TIME_2)
        return 0
    
    line = lines[0].replace("_", "/").replace("\n", "")
    msg = line.split(",")
    val3 = msg[4]

    # Missatge de debug
    now = datetime.datetime.now()
    t = datetime.datetime.strftime(now, "%Y/%m/%d %H:%M:%S")
    db_print(t)
    db_print("Bateries: {}. Llindar superior: {}. Llindar inferior {} ".format(val3, THRESHOLD_H, THRESHOLD_L))
    
    # LEDS
    if float(val3) <= THRESHOLD_L:
        GPIO.output(led_red, True)
        db_print("LED vermell encès")
    else:
        GPIO.output(led_red, False)
        db_print("LED vermell apagat")

    if float(val3) >= THRESHOLD_H:
        GPIO.output(led_yellow, True)
        db_print("LED groc encès")
    else:
        GPIO.output(led_yellow, False)
        db_print("LED groc apagat")
    return 1
            
# Botó declarat com a entrada amb pull down
GPIO.setmode(GPIO.BCM)
GPIO.setup(button0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LEDS declarats com a sortida i inicialment apagats
GPIO.setup(led_red, GPIO.OUT)
GPIO.output(led_red, False)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.output(led_yellow, False)

# Variable global pressed per a saber si s'ha apretat el polsador
pressed = False

def pressed_callback(channel):
    """
    Callback per a canviar l'estat de la variable global pressed
    """
    db_print("Callback cridat")
    global pressed
    pressed = True
    
GPIO.add_event_detect(button0, GPIO.RISING, callback=pressed_callback, bouncetime=300)

    
# Inicialització del display
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                           lcd_d7, lcd_columns, lcd_rows,
                           lcd_backlight)

db_print("Display inicialitzat correctament")
t = datetime.datetime.strftime(datetime.datetime.now(),"%Y/%m/%d %H:%M:%S")
db_print("Timestamp: {}".format(t))

previous_time = time.time()

while True:
    try:

        # Espera a què s'apreti el polsador o transcorri INTERVAL
        while (not pressed) and (time.time() - previous_time < INTERVAL):
            pass
        previous_time = time.time()
        
        # Comprovem si cal encendre LEDS
        update_leds()  #Millora: comprovar primer si last_data actualitzat

        # Si s'ha apretat el botó mostrem dades
        if pressed:
            db_print("Botó apretat")

            lcd.clear()
            lcd.set_backlight(0)

            if LAST_DATA_REPEAT > 0:
                try:
                    show_last_data()
                except Exception as ex:
                    db_print("No s'ha pogut mostrar last_data")

            if YESTERDAY_REPEAT > 0:
                try:
                    show_yesterday()
                except Exception as ex:
                    db_print("No s'ha pogut mostrar yesterday")
                    db_print(ex)
                    
            lcd.clear()
            lcd.set_backlight(1)
            pressed = False
            
    except Exception as ex:
        db_print("Ha petat!")
        db_print(str(ex))
                        
lcd.clear()
lcd.set_backlight(1)     
GPIO.cleanup()           # clean up GPIO on normal exit  
sys.exit(0)
