EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "GHaumCube64 - Carte télécommande"
Date "2021"
Rev "1"
Comp "HAUM"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_Module:WeMos_D1_mini U1
U 1 1 6138611B
P 2650 4150
F 0 "U1" H 2650 3261 50  0000 C CNN
F 1 "WeMos_D1_mini" H 2650 3170 50  0000 C CNN
F 2 "Module:WEMOS_D1_mini_light" H 2650 3000 50  0001 C CNN
F 3 "https://wiki.wemos.cc/products:d1:d1_mini#documentation" H 800 3000 50  0001 C CNN
	1    2650 4150
	1    0    0    -1  
$EndComp
Text Notes 3000 5150 0    50   ~ 0
D8 (GPIO15): pull-down on wemos\nD3 (GPIO0): pull-up on wemos\nD4 (GPIO2): pull-up on wemos (should be 1 at boot)\n
$Comp
L Device:LED L1
U 1 1 61386DE4
P 3700 3100
F 0 "L1" V 3739 2982 50  0000 R CNN
F 1 "LED" V 3648 2982 50  0000 R CNN
F 2 "LED_THT:LED_D3.0mm" H 3700 3100 50  0001 C CNN
F 3 "~" H 3700 3100 50  0001 C CNN
	1    3700 3100
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED L2
U 1 1 613883E5
P 4050 3100
F 0 "L2" V 4089 2982 50  0000 R CNN
F 1 "LED" V 3998 2982 50  0000 R CNN
F 2 "LED_THT:LED_D3.0mm" H 4050 3100 50  0001 C CNN
F 3 "~" H 4050 3100 50  0001 C CNN
	1    4050 3100
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R1
U 1 1 61388849
P 3700 3450
F 0 "R1" H 3770 3496 50  0000 L CNN
F 1 "R" H 3770 3405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P15.24mm_Horizontal" V 3630 3450 50  0001 C CNN
F 3 "~" H 3700 3450 50  0001 C CNN
	1    3700 3450
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 61388C52
P 4050 3450
F 0 "R2" H 4120 3496 50  0000 L CNN
F 1 "R" H 4120 3405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P15.24mm_Horizontal" V 3980 3450 50  0001 C CNN
F 3 "~" H 4050 3450 50  0001 C CNN
	1    4050 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3700 3250 3700 3300
Wire Wire Line
	4050 3250 4050 3300
Wire Wire Line
	4050 2850 4050 2950
Wire Wire Line
	3700 2950 3700 2850
Wire Wire Line
	3700 2850 4050 2850
Wire Wire Line
	4050 3600 4050 4050
$Comp
L Switch:SW_Push S1
U 1 1 613916E0
P 7950 3600
F 0 "S1" H 7950 3885 50  0000 C CNN
F 1 "SW_Push" H 7950 3794 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 7950 3800 50  0001 C CNN
F 3 "~" H 7950 3800 50  0001 C CNN
	1    7950 3600
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D1
U 1 1 61391EEF
P 7450 3600
F 0 "D1" H 7450 3335 50  0000 C CNN
F 1 "DIODE" H 7450 3426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 7450 3600 50  0001 C CNN
F 3 "~" H 7450 3600 50  0001 C CNN
	1    7450 3600
	-1   0    0    1   
$EndComp
$Comp
L Switch:SW_Push S2
U 1 1 6139704B
P 9150 3600
F 0 "S2" H 9150 3885 50  0000 C CNN
F 1 "SW_Push" H 9150 3794 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 9150 3800 50  0001 C CNN
F 3 "~" H 9150 3800 50  0001 C CNN
	1    9150 3600
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D2
U 1 1 6139710B
P 8650 3600
F 0 "D2" H 8650 3335 50  0000 C CNN
F 1 "DIODE" H 8650 3426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 8650 3600 50  0001 C CNN
F 3 "~" H 8650 3600 50  0001 C CNN
	1    8650 3600
	-1   0    0    1   
$EndComp
$Comp
L Switch:SW_Push S0
U 1 1 61398D59
P 6700 3600
F 0 "S0" H 6700 3885 50  0000 C CNN
F 1 "SW_Push" H 6700 3794 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 6700 3800 50  0001 C CNN
F 3 "~" H 6700 3800 50  0001 C CNN
	1    6700 3600
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D0
U 1 1 61398D5F
P 6200 3600
F 0 "D0" H 6200 3335 50  0000 C CNN
F 1 "DIODE" H 6200 3426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 6200 3600 50  0001 C CNN
F 3 "~" H 6200 3600 50  0001 C CNN
	1    6200 3600
	-1   0    0    1   
$EndComp
Wire Wire Line
	6000 3600 6000 3850
Wire Wire Line
	6000 3850 5600 3850
Wire Wire Line
	6400 3600 6500 3600
Wire Wire Line
	7250 3600 7250 3850
Wire Wire Line
	7250 3850 6000 3850
Connection ~ 6000 3850
Wire Wire Line
	8450 3600 8450 3850
Wire Wire Line
	8450 3850 7250 3850
Connection ~ 7250 3850
Wire Wire Line
	7650 3600 7750 3600
Wire Wire Line
	8850 3600 8950 3600
$Comp
L Switch:SW_Push S4
U 1 1 613AA28B
P 7950 4200
F 0 "S4" H 7950 4485 50  0000 C CNN
F 1 "SW_Push" H 7950 4394 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 7950 4400 50  0001 C CNN
F 3 "~" H 7950 4400 50  0001 C CNN
	1    7950 4200
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D4
U 1 1 613AA347
P 7450 4200
F 0 "D4" H 7450 3935 50  0000 C CNN
F 1 "DIODE" H 7450 4026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 7450 4200 50  0001 C CNN
F 3 "~" H 7450 4200 50  0001 C CNN
	1    7450 4200
	-1   0    0    1   
$EndComp
$Comp
L Switch:SW_Push S5
U 1 1 613AA351
P 9150 4200
F 0 "S5" H 9150 4485 50  0000 C CNN
F 1 "SW_Push" H 9150 4394 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 9150 4400 50  0001 C CNN
F 3 "~" H 9150 4400 50  0001 C CNN
	1    9150 4200
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D5
U 1 1 613AA35B
P 8650 4200
F 0 "D5" H 8650 3935 50  0000 C CNN
F 1 "DIODE" H 8650 4026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 8650 4200 50  0001 C CNN
F 3 "~" H 8650 4200 50  0001 C CNN
	1    8650 4200
	-1   0    0    1   
$EndComp
$Comp
L Switch:SW_Push S3
U 1 1 613AA365
P 6700 4200
F 0 "S3" H 6700 4485 50  0000 C CNN
F 1 "SW_Push" H 6700 4394 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 6700 4400 50  0001 C CNN
F 3 "~" H 6700 4400 50  0001 C CNN
	1    6700 4200
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D3
U 1 1 613AA36F
P 6200 4200
F 0 "D3" H 6200 3935 50  0000 C CNN
F 1 "DIODE" H 6200 4026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 6200 4200 50  0001 C CNN
F 3 "~" H 6200 4200 50  0001 C CNN
	1    6200 4200
	-1   0    0    1   
$EndComp
Wire Wire Line
	6000 4200 6000 4450
Wire Wire Line
	6000 4450 5600 4450
Wire Wire Line
	6400 4200 6500 4200
Wire Wire Line
	7250 4200 7250 4450
Wire Wire Line
	7250 4450 6000 4450
Connection ~ 6000 4450
Wire Wire Line
	8450 4200 8450 4450
Wire Wire Line
	8450 4450 7250 4450
Connection ~ 7250 4450
Wire Wire Line
	7650 4200 7750 4200
Wire Wire Line
	8850 4200 8950 4200
$Comp
L Switch:SW_Push S7
U 1 1 613AF757
P 7950 4800
F 0 "S7" H 7950 5085 50  0000 C CNN
F 1 "SW_Push" H 7950 4994 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 7950 5000 50  0001 C CNN
F 3 "~" H 7950 5000 50  0001 C CNN
	1    7950 4800
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D7
U 1 1 613AF88B
P 7450 4800
F 0 "D7" H 7450 4535 50  0000 C CNN
F 1 "DIODE" H 7450 4626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 7450 4800 50  0001 C CNN
F 3 "~" H 7450 4800 50  0001 C CNN
	1    7450 4800
	-1   0    0    1   
$EndComp
$Comp
L Switch:SW_Push S8
U 1 1 613AF895
P 9150 4800
F 0 "S8" H 9150 5085 50  0000 C CNN
F 1 "SW_Push" H 9150 4994 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 9150 5000 50  0001 C CNN
F 3 "~" H 9150 5000 50  0001 C CNN
	1    9150 4800
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D8
U 1 1 613AF89F
P 8650 4800
F 0 "D8" H 8650 4535 50  0000 C CNN
F 1 "DIODE" H 8650 4626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 8650 4800 50  0001 C CNN
F 3 "~" H 8650 4800 50  0001 C CNN
	1    8650 4800
	-1   0    0    1   
$EndComp
$Comp
L Switch:SW_Push S6
U 1 1 613AF8A9
P 6700 4800
F 0 "S6" H 6700 5085 50  0000 C CNN
F 1 "SW_Push" H 6700 4994 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 6700 5000 50  0001 C CNN
F 3 "~" H 6700 5000 50  0001 C CNN
	1    6700 4800
	1    0    0    -1  
$EndComp
$Comp
L pspice:DIODE D6
U 1 1 613AF8B3
P 6200 4800
F 0 "D6" H 6200 4535 50  0000 C CNN
F 1 "DIODE" H 6200 4626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P10.16mm_Horizontal" H 6200 4800 50  0001 C CNN
F 3 "~" H 6200 4800 50  0001 C CNN
	1    6200 4800
	-1   0    0    1   
$EndComp
Wire Wire Line
	6000 4800 6000 5050
Wire Wire Line
	6000 5050 5600 5050
Wire Wire Line
	6400 4800 6500 4800
Wire Wire Line
	7250 4800 7250 5050
Wire Wire Line
	7250 5050 6000 5050
Connection ~ 6000 5050
Wire Wire Line
	8450 4800 8450 5050
Wire Wire Line
	8450 5050 7250 5050
Connection ~ 7250 5050
Wire Wire Line
	7650 4800 7750 4800
Wire Wire Line
	8850 4800 8950 4800
Text Label 5600 3850 0    50   ~ 0
L0
Text Label 5600 4450 0    50   ~ 0
L1
Text Label 5600 5050 0    50   ~ 0
L2
Wire Wire Line
	6900 4800 7000 4800
Wire Wire Line
	7000 4800 7000 4200
Wire Wire Line
	6900 3600 7000 3600
Connection ~ 7000 3600
Wire Wire Line
	7000 3600 7000 3100
Wire Wire Line
	6900 4200 7000 4200
Connection ~ 7000 4200
Wire Wire Line
	7000 4200 7000 3600
Wire Wire Line
	8150 4800 8250 4800
Wire Wire Line
	8250 4800 8250 4200
Wire Wire Line
	9350 4800 9450 4800
Wire Wire Line
	9450 4800 9450 4200
Wire Wire Line
	9350 3600 9450 3600
Connection ~ 9450 3600
Wire Wire Line
	9450 3600 9450 3100
Wire Wire Line
	9350 4200 9450 4200
Connection ~ 9450 4200
Wire Wire Line
	9450 4200 9450 3600
Wire Wire Line
	8150 4200 8250 4200
Connection ~ 8250 4200
Wire Wire Line
	8250 4200 8250 3600
Wire Wire Line
	8150 3600 8250 3600
Connection ~ 8250 3600
Wire Wire Line
	8250 3600 8250 3100
Text Notes 6850 3550 0    50   ~ 0
X+
Text Notes 6850 4150 0    50   ~ 0
X-
Text Notes 8100 4150 0    50   ~ 0
Y-
Text Notes 8100 3550 0    50   ~ 0
Y+
Text Notes 9300 4150 0    50   ~ 0
Z-
Text Notes 9300 3550 0    50   ~ 0
Z+
Text Label 7000 2800 0    50   ~ 0
C0
Text Label 8250 2800 0    50   ~ 0
C1
Text Label 9450 2800 0    50   ~ 0
C2
Text Notes 6850 4750 0    50   ~ 0
✓
Text Notes 9300 4750 0    50   ~ 0
✗
Text Notes 8100 4750 0    50   ~ 0
•
Text Label 3050 4350 0    50   ~ 0
C0
Text Label 3050 3950 0    50   ~ 0
L0
Text Label 3050 3850 0    50   ~ 0
L1
Text Label 3050 4250 0    50   ~ 0
L2
$Comp
L Device:LED L0
U 1 1 613EDE38
P 3350 3100
F 0 "L0" V 3389 2982 50  0000 R CNN
F 1 "LED" V 3298 2982 50  0000 R CNN
F 2 "LED_THT:LED_D3.0mm" H 3350 3100 50  0001 C CNN
F 3 "~" H 3350 3100 50  0001 C CNN
	1    3350 3100
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R0
U 1 1 613EE03A
P 3350 3450
F 0 "R0" H 3420 3496 50  0000 L CNN
F 1 "R" H 3420 3405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P15.24mm_Horizontal" V 3280 3450 50  0001 C CNN
F 3 "~" H 3350 3450 50  0001 C CNN
	1    3350 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 3250 3350 3300
Wire Wire Line
	3350 3750 3350 3600
Wire Wire Line
	3050 3750 3350 3750
Wire Wire Line
	2750 2850 3350 2850
Wire Wire Line
	2750 2850 2750 3350
Connection ~ 3700 2850
Wire Wire Line
	3350 2950 3350 2850
Connection ~ 3350 2850
Wire Wire Line
	3350 2850 3700 2850
NoConn ~ 3050 3650
NoConn ~ 2250 3750
NoConn ~ 2250 4050
NoConn ~ 2250 4150
NoConn ~ 2550 3350
NoConn ~ 2650 4950
Wire Wire Line
	3050 4150 3700 4150
Wire Wire Line
	3700 3600 3700 4150
Wire Wire Line
	3050 4050 4050 4050
$Comp
L Device:R R3
U 1 1 613A3F36
P 7000 2950
F 0 "R3" V 6793 2950 50  0000 C CNN
F 1 "R" V 6884 2950 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P15.24mm_Horizontal" V 6930 2950 50  0001 C CNN
F 3 "~" H 7000 2950 50  0001 C CNN
	1    7000 2950
	-1   0    0    1   
$EndComp
$Comp
L Device:R R4
U 1 1 613A4696
P 8250 2950
F 0 "R4" V 8043 2950 50  0000 C CNN
F 1 "R" V 8134 2950 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P15.24mm_Horizontal" V 8180 2950 50  0001 C CNN
F 3 "~" H 8250 2950 50  0001 C CNN
	1    8250 2950
	-1   0    0    1   
$EndComp
$Comp
L Device:R R5
U 1 1 613A4C60
P 9450 2950
F 0 "R5" V 9243 2950 50  0000 C CNN
F 1 "R" V 9334 2950 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P15.24mm_Horizontal" V 9380 2950 50  0001 C CNN
F 3 "~" H 9450 2950 50  0001 C CNN
	1    9450 2950
	-1   0    0    1   
$EndComp
Text Label 3050 4450 0    50   ~ 0
C2
Text Label 3050 4550 0    50   ~ 0
C1
$Comp
L Mechanical:MountingHole H1
U 1 1 61464065
P 7000 5450
F 0 "H1" H 7100 5496 50  0000 L CNN
F 1 "MountingHole" H 7100 5405 50  0000 L CNN
F 2 "MountingHole:MountingHole_5.3mm_M5" H 7000 5450 50  0001 C CNN
F 3 "~" H 7000 5450 50  0001 C CNN
	1    7000 5450
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 61464770
P 7000 5650
F 0 "H2" H 7100 5696 50  0000 L CNN
F 1 "MountingHole" H 7100 5605 50  0000 L CNN
F 2 "MountingHole:MountingHole_5.3mm_M5" H 7000 5650 50  0001 C CNN
F 3 "~" H 7000 5650 50  0001 C CNN
	1    7000 5650
	1    0    0    -1  
$EndComp
Text Notes 3000 5350 0    50   ~ 0
Power via wemos board
$EndSCHEMATC
