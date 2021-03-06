EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:switches
LIBS:Power_Management
LIBS:PCBdisplay-cache
EELAYER 26 0
EELAYER END
$Descr A4 8268 11693 portrait
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L LCD16X2 DS1
U 1 1 5953A57A
P 4600 7900
F 0 "DS1" H 3800 8300 50  0000 C CNN
F 1 "LCD16X2" H 5300 8300 50  0000 C CNN
F 2 "Displays:WC1602A" H 4600 7850 50  0001 C CIN
F 3 "" H 4600 7900 50  0001 C CNN
	1    4600 7900
	-1   0    0    1   
$EndComp
Wire Wire Line
	4050 7400 4050 7275
Wire Wire Line
	4150 7400 4150 7275
Wire Wire Line
	4250 7400 4250 7275
Wire Wire Line
	4350 7400 4350 7275
Wire Wire Line
	5050 7400 5050 7275
$Comp
L R R1
U 1 1 5953AA69
P 3450 2300
F 0 "R1" V 3530 2300 50  0000 C CNN
F 1 "R" V 3450 2300 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 3380 2300 50  0001 C CNN
F 3 "" H 3450 2300 50  0001 C CNN
	1    3450 2300
	1    0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 5953ABD6
P 3050 2300
F 0 "R2" V 3130 2300 50  0000 C CNN
F 1 "R" V 3050 2300 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2980 2300 50  0001 C CNN
F 3 "" H 3050 2300 50  0001 C CNN
	1    3050 2300
	-1   0    0    1   
$EndComp
$Comp
L R R3
U 1 1 5953ABFB
P 2600 2300
F 0 "R3" V 2680 2300 50  0000 C CNN
F 1 "R" V 2600 2300 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2530 2300 50  0001 C CNN
F 3 "" H 2600 2300 50  0001 C CNN
	1    2600 2300
	-1   0    0    1   
$EndComp
$Comp
L R R4
U 1 1 5953AC32
P 2150 2300
F 0 "R4" V 2230 2300 50  0000 C CNN
F 1 "R" V 2150 2300 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2080 2300 50  0001 C CNN
F 3 "" H 2150 2300 50  0001 C CNN
	1    2150 2300
	-1   0    0    1   
$EndComp
$Comp
L R R5
U 1 1 5953AC57
P 1700 2300
F 0 "R5" V 1780 2300 50  0000 C CNN
F 1 "R" V 1700 2300 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1630 2300 50  0001 C CNN
F 3 "" H 1700 2300 50  0001 C CNN
	1    1700 2300
	-1   0    0    1   
$EndComp
$Comp
L R R6
U 1 1 5953ACD0
P 6050 2400
F 0 "R6" V 6130 2400 50  0000 C CNN
F 1 "R" V 6050 2400 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5980 2400 50  0001 C CNN
F 3 "" H 6050 2400 50  0001 C CNN
	1    6050 2400
	-1   0    0    1   
$EndComp
$Comp
L R R7
U 1 1 5953AD5B
P 5250 2400
F 0 "R7" V 5330 2400 50  0000 C CNN
F 1 "R" V 5250 2400 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 5180 2400 50  0001 C CNN
F 3 "" H 5250 2400 50  0001 C CNN
	1    5250 2400
	-1   0    0    1   
$EndComp
$Comp
L R R8
U 1 1 5953AD82
P 1300 4600
F 0 "R8" V 1380 4600 50  0000 C CNN
F 1 "R" V 1300 4600 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 1230 4600 50  0001 C CNN
F 3 "" H 1300 4600 50  0001 C CNN
	1    1300 4600
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR01
U 1 1 5953AEB2
P 3450 2000
F 0 "#PWR01" H 3450 1750 50  0001 C CNN
F 1 "GND" H 3450 1850 50  0000 C CNN
F 2 "" H 3450 2000 50  0001 C CNN
F 3 "" H 3450 2000 50  0001 C CNN
	1    3450 2000
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR02
U 1 1 5953AED8
P 3050 2000
F 0 "#PWR02" H 3050 1750 50  0001 C CNN
F 1 "GND" H 3050 1850 50  0000 C CNN
F 2 "" H 3050 2000 50  0001 C CNN
F 3 "" H 3050 2000 50  0001 C CNN
	1    3050 2000
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR03
U 1 1 5953AEFE
P 2600 2000
F 0 "#PWR03" H 2600 1750 50  0001 C CNN
F 1 "GND" H 2600 1850 50  0000 C CNN
F 2 "" H 2600 2000 50  0001 C CNN
F 3 "" H 2600 2000 50  0001 C CNN
	1    2600 2000
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR04
U 1 1 5953AF24
P 2150 2000
F 0 "#PWR04" H 2150 1750 50  0001 C CNN
F 1 "GND" H 2150 1850 50  0000 C CNN
F 2 "" H 2150 2000 50  0001 C CNN
F 3 "" H 2150 2000 50  0001 C CNN
	1    2150 2000
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR05
U 1 1 5953AF4A
P 1700 2000
F 0 "#PWR05" H 1700 1750 50  0001 C CNN
F 1 "GND" H 1700 1850 50  0000 C CNN
F 2 "" H 1700 2000 50  0001 C CNN
F 3 "" H 1700 2000 50  0001 C CNN
	1    1700 2000
	-1   0    0    1   
$EndComp
Wire Wire Line
	1700 2150 1700 2000
Wire Wire Line
	2150 2150 2150 2000
Wire Wire Line
	2600 2150 2600 2000
Wire Wire Line
	3050 2150 3050 2000
Wire Wire Line
	3450 2150 3450 2000
$Comp
L LED D1
U 1 1 5953B04D
P 3450 2600
F 0 "D1" H 3450 2700 50  0000 C CNN
F 1 "LED" H 3450 2500 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 3450 2600 50  0001 C CNN
F 3 "" H 3450 2600 50  0001 C CNN
	1    3450 2600
	0    1    1    0   
$EndComp
$Comp
L LED D2
U 1 1 5953B0CA
P 3050 2600
F 0 "D2" H 3050 2700 50  0000 C CNN
F 1 "LED" H 3050 2500 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 3050 2600 50  0001 C CNN
F 3 "" H 3050 2600 50  0001 C CNN
	1    3050 2600
	0    1    1    0   
$EndComp
$Comp
L LED D3
U 1 1 5953B149
P 2600 2600
F 0 "D3" H 2600 2700 50  0000 C CNN
F 1 "LED" H 2600 2500 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 2600 2600 50  0001 C CNN
F 3 "" H 2600 2600 50  0001 C CNN
	1    2600 2600
	0    1    1    0   
$EndComp
$Comp
L LED D4
U 1 1 5953B286
P 2150 2600
F 0 "D4" H 2150 2700 50  0000 C CNN
F 1 "LED" H 2150 2500 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 2150 2600 50  0001 C CNN
F 3 "" H 2150 2600 50  0001 C CNN
	1    2150 2600
	0    1    1    0   
$EndComp
$Comp
L LED D5
U 1 1 5953B2BF
P 1700 2600
F 0 "D5" H 1700 2700 50  0000 C CNN
F 1 "LED" H 1700 2500 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 1700 2600 50  0001 C CNN
F 3 "" H 1700 2600 50  0001 C CNN
	1    1700 2600
	0    1    1    0   
$EndComp
$Comp
L GND #PWR06
U 1 1 5953B3AE
P 6050 2100
F 0 "#PWR06" H 6050 1850 50  0001 C CNN
F 1 "GND" H 6050 1950 50  0000 C CNN
F 2 "" H 6050 2100 50  0001 C CNN
F 3 "" H 6050 2100 50  0001 C CNN
	1    6050 2100
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR07
U 1 1 5953B3DE
P 5250 2100
F 0 "#PWR07" H 5250 1850 50  0001 C CNN
F 1 "GND" H 5250 1950 50  0000 C CNN
F 2 "" H 5250 2100 50  0001 C CNN
F 3 "" H 5250 2100 50  0001 C CNN
	1    5250 2100
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR08
U 1 1 5953B40E
P 1300 4400
F 0 "#PWR08" H 1300 4150 50  0001 C CNN
F 1 "GND" H 1300 4250 50  0000 C CNN
F 2 "" H 1300 4400 50  0001 C CNN
F 3 "" H 1300 4400 50  0001 C CNN
	1    1300 4400
	-1   0    0    1   
$EndComp
Wire Wire Line
	6050 2250 6050 2100
Wire Wire Line
	5250 2250 5250 2100
Wire Wire Line
	1300 4450 1300 4400
$Comp
L LED D6
U 1 1 5953B85E
P 6050 2700
F 0 "D6" H 6050 2800 50  0000 C CNN
F 1 "LED" H 6050 2600 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 6050 2700 50  0001 C CNN
F 3 "" H 6050 2700 50  0001 C CNN
	1    6050 2700
	0    1    1    0   
$EndComp
$Comp
L LED D7
U 1 1 5953B8F5
P 5250 2700
F 0 "D7" H 5250 2800 50  0000 C CNN
F 1 "LED" H 5250 2600 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 5250 2700 50  0001 C CNN
F 3 "" H 5250 2700 50  0001 C CNN
	1    5250 2700
	0    1    1    0   
$EndComp
$Comp
L LED D8
U 1 1 5953B956
P 1300 4900
F 0 "D8" H 1300 5000 50  0000 C CNN
F 1 "LED" H 1300 4800 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 1300 4900 50  0001 C CNN
F 3 "" H 1300 4900 50  0001 C CNN
	1    1300 4900
	0    1    1    0   
$EndComp
$Comp
L POT RV1
U 1 1 5953CDB7
P 6125 5150
F 0 "RV1" V 5950 5150 50  0000 C CNN
F 1 "POT" V 6025 5150 50  0000 C CNN
F 2 "Potentiometers:Potentiometer_Alps_RK09K_Vertical" H 6125 5150 50  0001 C CNN
F 3 "" H 6125 5150 50  0001 C CNN
	1    6125 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 7275 5350 7400
Wire Wire Line
	5250 7400 5250 7275
Wire Wire Line
	3950 7275 3950 7400
NoConn ~ 3850 7400
NoConn ~ 4450 7400
NoConn ~ 4550 7400
NoConn ~ 4650 7400
NoConn ~ 4750 7400
NoConn ~ 4950 7400
Wire Wire Line
	4850 7275 4850 7400
Wire Wire Line
	1700 3100 1700 2750
Wire Wire Line
	2150 3100 2150 2750
Wire Wire Line
	2600 3100 2600 2750
Wire Wire Line
	3050 3100 3050 2750
Wire Wire Line
	3450 3100 3450 2750
Wire Wire Line
	6050 3100 6050 2850
Wire Wire Line
	5250 3100 5250 2850
Wire Wire Line
	1300 5100 1300 5050
$Comp
L GND #PWR09
U 1 1 5953C85C
P 6125 4925
F 0 "#PWR09" H 6125 4675 50  0001 C CNN
F 1 "GND" H 6125 4775 50  0000 C CNN
F 2 "" H 6125 4925 50  0001 C CNN
F 3 "" H 6125 4925 50  0001 C CNN
	1    6125 4925
	-1   0    0    1   
$EndComp
Wire Wire Line
	6125 4925 6125 5000
Text Notes 5850 1850 0    60   ~ 0
V > Vmax
Text Notes 4300 1850 0    60   ~ 0
Vmin < V
Text Notes 4850 1850 0    60   ~ 0
Vmin < V < Vmax
Wire Notes Line
	6500 1250 6500 3750
Text Notes 5950 1700 0    60   ~ 0
Groc
Text Notes 5150 1700 0    60   ~ 0
Verd
Text Notes 4300 1700 0    60   ~ 0
Vermell
Text Notes 4150 1500 0    118  ~ 0
Estat de les bateries
Wire Notes Line
	4000 1250 6500 1250
Wire Notes Line
	6500 3750 4000 3750
Wire Notes Line
	4000 3750 4000 1250
Wire Notes Line
	3800 3750 3800 1250
Wire Notes Line
	3800 1250 1400 1250
Text Notes 1650 1700 0    118  ~ 0
5 leds 3V?\nMostreig Radiació
Wire Notes Line
	1400 1250 1400 3750
Wire Notes Line
	3200 9450 5700 9450
Wire Notes Line
	3200 6650 3200 9450
Text Notes 3400 9300 1    118  ~ 0
Display MC21605H6W-SPTL
Wire Notes Line
	5700 9450 5700 6650
Wire Notes Line
	5700 6650 3200 6650
Text Label 4050 7275 1    60   ~ 0
GPIO3
Wire Notes Line
	1400 3750 3800 3750
$Comp
L CONN_02X20 J1
U 1 1 4F83263C
P 4400 5400
F 0 "J1" H 4400 6450 50  0000 C CNN
F 1 "CONN_02X20" V 4400 5400 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Angled_2x20_Pitch2.00mm" H 4400 4450 50  0001 C CNN
F 3 "" H 4400 4450 50  0001 C CNN
	1    4400 5400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3450 4800 3450 5150
Wire Wire Line
	3750 5150 3750 4800
Wire Wire Line
	3850 5150 3850 4800
Wire Wire Line
	3950 5150 3950 4800
Wire Wire Line
	4150 5150 4150 4800
Wire Wire Line
	4250 5150 4250 4800
Wire Wire Line
	4450 5150 4450 4800
Wire Wire Line
	4550 5150 4550 4800
Wire Wire Line
	4650 5150 4650 4800
Wire Wire Line
	4950 5150 4950 4800
Wire Wire Line
	5150 5150 5150 4800
Wire Wire Line
	5250 5150 5250 4800
Wire Wire Line
	3550 5650 3550 6000
Wire Wire Line
	3650 5650 3650 6000
Wire Wire Line
	3750 5650 3750 6000
Wire Wire Line
	3950 5650 3950 6000
Wire Wire Line
	4050 5650 4050 6000
Wire Wire Line
	4350 5650 4350 6000
Wire Wire Line
	4550 5650 4550 6000
Wire Wire Line
	5150 5650 5150 6000
Wire Wire Line
	5250 5650 5250 6000
Text Label 3450 4800 1    60   ~ 0
5v
Text Label 5250 7275 1    60   ~ 0
5v
Text Label 3550 6000 3    60   ~ 0
GPIO2
Text Label 3650 6000 3    60   ~ 0
GPIO3
Text Label 3750 6000 3    60   ~ 0
GPIO4
Text Label 3950 6000 3    60   ~ 0
GPIO17
Text Label 4050 6000 3    60   ~ 0
GPIO27
Text Label 4350 6000 3    60   ~ 0
GPIO10
Text Label 4550 6000 3    60   ~ 0
GPIO11
Text Label 5150 6000 3    60   ~ 0
GPIO19
Text Label 5250 6000 3    60   ~ 0
GPIO26
Text Label 3750 4800 1    60   ~ 0
GPIO14
Text Label 3850 4800 1    60   ~ 0
GPIO15
Text Label 3950 4800 1    60   ~ 0
GPIO18
Text Label 4150 4800 1    60   ~ 0
GPIO23
Text Label 4250 4800 1    60   ~ 0
GPIO24
Text Label 4450 4800 1    60   ~ 0
GPIO25
Text Label 4550 4800 1    60   ~ 0
GPIO8
Text Label 4650 4800 1    60   ~ 0
GPIO7
Text Label 4950 4800 1    60   ~ 0
GPIO12
Text Label 5150 4800 1    60   ~ 0
GPIO16
Text Label 5250 4800 1    60   ~ 0
GPIO20
NoConn ~ 3550 5150
NoConn ~ 3450 5650
NoConn ~ 3650 5150
NoConn ~ 4050 5150
NoConn ~ 4350 5150
NoConn ~ 4750 5150
NoConn ~ 4850 5150
NoConn ~ 4750 5650
NoConn ~ 5050 5150
NoConn ~ 3850 5650
NoConn ~ 4250 5650
NoConn ~ 5350 5650
$Comp
L SW_DIP_x02 SW1
U 1 1 59562F17
P 2350 4950
F 0 "SW1" H 2350 5200 50  0000 C CNN
F 1 "SW_DIP_x02" H 2350 4800 50  0000 C CNN
F 2 "Buttons_Switches_THT:SW_PUSH-12mm" H 2350 4950 50  0001 C CNN
F 3 "" H 2350 4950 50  0001 C CNN
	1    2350 4950
	0    1    1    0   
$EndComp
Wire Notes Line
	3200 3950 3200 6550
Wire Notes Line
	3200 6550 5700 6550
Wire Notes Line
	5700 6550 5700 3950
Wire Notes Line
	5700 3950 3200 3950
Text Notes 3350 4200 0    118  ~ 0
Header Raspberry Pi 3
NoConn ~ 2350 5250
NoConn ~ 2350 4650
Wire Wire Line
	2450 4500 2450 4650
Wire Wire Line
	2450 5250 2450 5300
$Comp
L R R9
U 1 1 59566B6C
P 2700 4600
F 0 "R9" V 2780 4600 50  0000 C CNN
F 1 "R" V 2700 4600 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2630 4600 50  0001 C CNN
F 3 "" H 2700 4600 50  0001 C CNN
	1    2700 4600
	0    1    1    0   
$EndComp
Wire Wire Line
	2450 4600 2550 4600
Wire Wire Line
	2850 4600 2900 4600
$Comp
L GND #PWR010
U 1 1 59566EAD
P 2450 5300
F 0 "#PWR010" H 2450 5050 50  0001 C CNN
F 1 "GND" H 2450 5150 50  0000 C CNN
F 2 "" H 2450 5300 50  0001 C CNN
F 3 "" H 2450 5300 50  0001 C CNN
	1    2450 5300
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR011
U 1 1 59566F01
P 2900 4600
F 0 "#PWR011" H 2900 4350 50  0001 C CNN
F 1 "GND" H 2900 4450 50  0000 C CNN
F 2 "" H 2900 4600 50  0001 C CNN
F 3 "" H 2900 4600 50  0001 C CNN
	1    2900 4600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR012
U 1 1 595670DC
P 4650 5650
F 0 "#PWR012" H 4650 5400 50  0001 C CNN
F 1 "GND" H 4650 5500 50  0000 C CNN
F 2 "" H 4650 5650 50  0001 C CNN
F 3 "" H 4650 5650 50  0001 C CNN
	1    4650 5650
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR013
U 1 1 59567510
P 5350 7275
F 0 "#PWR013" H 5350 7025 50  0001 C CNN
F 1 "GND" H 5350 7125 50  0000 C CNN
F 2 "" H 5350 7275 50  0001 C CNN
F 3 "" H 5350 7275 50  0001 C CNN
	1    5350 7275
	-1   0    0    1   
$EndComp
Connection ~ 2450 4600
Text Label 2450 4500 1    60   ~ 0
GPIO15
Wire Notes Line
	3050 3950 3050 5475
Wire Notes Line
	3000 5400 3000 5400
Wire Notes Line
	3050 3950 1950 3950
Wire Notes Line
	1950 3950 1950 5475
Wire Notes Line
	1950 5475 3050 5475
Wire Notes Line
	1850 5475 800  5475
Wire Notes Line
	800  5475 800  3950
Wire Notes Line
	800  3950 1850 3950
Wire Notes Line
	1850 3950 1850 5475
Wire Wire Line
	1925 6225 2175 6225
$Comp
L Buzzer BZ1
U 1 1 59569201
P 2275 6125
F 0 "BZ1" H 2425 6175 50  0000 L CNN
F 1 "Buzzer" H 2425 6075 50  0000 L BNN
F 2 "Buzzers_Beepers:BUZZER" V 2250 6225 50  0001 C CNN
F 3 "" V 2250 6225 50  0001 C CNN
	1    2275 6125
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2375 6225 2375 6275
$Comp
L GND #PWR014
U 1 1 59569E95
P 2375 6275
F 0 "#PWR014" H 2375 6025 50  0001 C CNN
F 1 "GND" H 2375 6125 50  0000 C CNN
F 2 "" H 2375 6275 50  0001 C CNN
F 3 "" H 2375 6275 50  0001 C CNN
	1    2375 6275
	1    0    0    -1  
$EndComp
Wire Notes Line
	800  5550 3050 5550
Wire Notes Line
	3050 5550 3050 6550
Wire Notes Line
	3050 6550 800  6550
Wire Notes Line
	800  6550 800  5550
Text Notes 800  4150 0    98   ~ 0
Led d'alarma
Text Notes 2050 4100 0    59   ~ 0
Botó STOP alarma
Text Notes 850  5700 0    79   ~ 0
Brunzidor volum alarma
$Comp
L SW_DIP_x02 SW2
U 1 1 5956C52A
P 6300 7300
F 0 "SW2" H 6300 7550 50  0000 C CNN
F 1 "SW_DIP_x02" H 6300 7150 50  0000 C CNN
F 2 "Buttons_Switches_THT:SW_PUSH-12mm" H 6300 7300 50  0001 C CNN
F 3 "" H 6300 7300 50  0001 C CNN
	1    6300 7300
	0    1    1    0   
$EndComp
NoConn ~ 6300 7000
Wire Wire Line
	6400 6850 6400 7000
Wire Wire Line
	6400 7600 6400 7650
$Comp
L R R10
U 1 1 5956C535
P 6650 6950
F 0 "R10" V 6730 6950 50  0000 C CNN
F 1 "R" V 6650 6950 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 6580 6950 50  0001 C CNN
F 3 "" H 6650 6950 50  0001 C CNN
	1    6650 6950
	0    1    1    0   
$EndComp
Wire Wire Line
	6400 6950 6500 6950
Wire Wire Line
	6800 6950 6850 6950
$Comp
L GND #PWR015
U 1 1 5956C53D
P 6400 7650
F 0 "#PWR015" H 6400 7400 50  0001 C CNN
F 1 "GND" H 6400 7500 50  0000 C CNN
F 2 "" H 6400 7650 50  0001 C CNN
F 3 "" H 6400 7650 50  0001 C CNN
	1    6400 7650
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR016
U 1 1 5956C543
P 6850 6950
F 0 "#PWR016" H 6850 6700 50  0001 C CNN
F 1 "GND" H 6850 6800 50  0000 C CNN
F 2 "" H 6850 6950 50  0001 C CNN
F 3 "" H 6850 6950 50  0001 C CNN
	1    6850 6950
	1    0    0    -1  
$EndComp
Connection ~ 6400 6950
Text Label 6400 6850 1    60   ~ 0
GPIO26
Wire Notes Line
	7050 6300 7050 7750
Wire Notes Line
	6850 7750 6850 7750
Wire Notes Line
	7050 6300 5850 6300
Wire Notes Line
	5850 6300 5850 7750
Wire Notes Line
	5850 7750 7050 7750
Text Notes 5900 6450 0    59   ~ 0
Botó ON display
Wire Notes Line
	5850 4150 5850 6200
Wire Notes Line
	5850 6200 7050 6200
Wire Notes Line
	7050 6200 7050 4150
Wire Notes Line
	7050 4150 5850 4150
Text Notes 5900 4300 0    79   ~ 0
Brillantor Display\n
NoConn ~ 6300 7600
$Comp
L GND #PWR017
U 1 1 5957E295
P 1400 6225
F 0 "#PWR017" H 1400 5975 50  0001 C CNN
F 1 "GND" H 1400 6075 50  0000 C CNN
F 2 "" H 1400 6225 50  0001 C CNN
F 3 "" H 1400 6225 50  0001 C CNN
	1    1400 6225
	-1   0    0    1   
$EndComp
Wire Wire Line
	1650 6500 1775 6500
Wire Wire Line
	1400 6225 1625 6225
Text Label 1650 6500 2    60   ~ 0
GPIO18
$Comp
L R R11
U 1 1 5957E73B
P 4500 2425
F 0 "R11" V 4580 2425 50  0000 C CNN
F 1 "R" V 4500 2425 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 4430 2425 50  0001 C CNN
F 3 "" H 4500 2425 50  0001 C CNN
	1    4500 2425
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR018
U 1 1 5957E741
P 4500 2125
F 0 "#PWR018" H 4500 1875 50  0001 C CNN
F 1 "GND" H 4500 1975 50  0000 C CNN
F 2 "" H 4500 2125 50  0001 C CNN
F 3 "" H 4500 2125 50  0001 C CNN
	1    4500 2125
	-1   0    0    1   
$EndComp
Wire Wire Line
	4500 2275 4500 2125
$Comp
L LED D9
U 1 1 5957E748
P 4500 2725
F 0 "D9" H 4500 2825 50  0000 C CNN
F 1 "LED" H 4500 2625 50  0000 C CNN
F 2 "LEDs:LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm" H 4500 2725 50  0001 C CNN
F 3 "" H 4500 2725 50  0001 C CNN
	1    4500 2725
	0    1    1    0   
$EndComp
Wire Wire Line
	4500 3125 4500 2875
Text Label 1300 5100 3    60   ~ 0
GPIO14
Text Label 4150 7275 1    60   ~ 0
GPIO4
Text Label 4250 7275 1    60   ~ 0
GPIO17
Text Label 4350 7275 1    60   ~ 0
GPIO27
Wire Wire Line
	5150 7400 5150 7275
Text Label 3950 7275 1    60   ~ 0
5v
NoConn ~ 4150 5650
NoConn ~ 4450 5650
Text Label 4850 7275 1    60   ~ 0
GPIO10
Text Label 5050 7275 1    60   ~ 0
GPIO11
NoConn ~ 5350 5150
Text Label 1700 3100 3    60   ~ 0
GPIO23
Text Label 2150 3100 3    60   ~ 0
GPIO24
Text Label 2600 3100 3    60   ~ 0
GPIO25
Text Label 3050 3100 3    60   ~ 0
GPIO8
Text Label 3450 3100 3    60   ~ 0
GPIO7
Text Label 4500 3125 3    60   ~ 0
GPIO12
Text Label 5250 3100 3    60   ~ 0
GPIO16
Text Label 6050 3100 3    60   ~ 0
GPIO20
Wire Wire Line
	6125 5300 6125 5575
Text Label 6125 5575 3    60   ~ 0
GPIO19
Wire Wire Line
	6275 5150 6500 5150
Text Label 6500 5150 0    60   ~ 0
CONT_DISP
Text Label 5150 7275 1    60   ~ 0
CONT_DISP
$Comp
L POT RV2
U 1 1 595810A8
P 1775 6225
F 0 "RV2" V 1600 6225 50  0000 C CNN
F 1 "POT" V 1675 6225 50  0000 C CNN
F 2 "Potentiometers:Potentiometer_Alps_RK09K_Vertical" H 1775 6225 50  0001 C CNN
F 3 "" H 1775 6225 50  0001 C CNN
	1    1775 6225
	0    1    1    0   
$EndComp
Wire Wire Line
	1775 6500 1775 6375
$EndSCHEMATC
