# ADMS-7-converter
## CHIRP -> ADMS-7

### Purpose

The purpose of this Python script was to make it possible to import CHIRP
list from [przemienniki.net](https://przemienniki.net/) into Yaesu FTM-400XD. 
This code is dirty and made in a rush. There are things I still don't 
understand but with the following limitations it seems to work:
* only FM repeaters are supported (DV are skipped)
* no DCS support
* only CTCSS Tone or carrier wave is supported

### Usage:
```
$ python3 converter.py lista_sr6.csv
1,438.95000,431.35000,7.600000,-RPT,FM,SR6ACZ,TONE SQL,103.5 Hz,023,1500 Hz,HIGH,OFF,12.5KHz,0,Wroclaw,0
2,145.76250,145.16250,0.600000,-RPT,FM,SR6B,TONE SQL,77.0 Hz,023,1500 Hz,HIGH,OFF,12.5KHz,0,Dzialoszyn - stacja meteo,0
3,439.25000,431.65000,7.600000,-RPT,FM,SR6C,OFF,88.5 Hz,023,1500 Hz,HIGH,OFF,12.5KHz,0,Boleslawiec,0
4,431.75000,424.15000,7.600000,+RPT,FM,SR6DA,OFF,88.5 Hz,023,1500 Hz,HIGH,OFF,12.5KHz,0,Dalachow,0
5,144.97500,144.97500,0.000000,+RPT,FM,SR6DL,OFF,88.5 Hz,023,1500 Hz,HIGH,OFF,12.5KHz,0,Dalachow,0
6,438.62500,431.02500,7.600000,-RPT,FM,SR6DMO,TONE SQL,94.8 Hz,023,1500 Hz,HIGH,OFF,12.5KHz,0,Olawa,0
7,145.68750,145.08750,0.600000,-RPT,FM,SR6DST,TONE SQL,123.0 Hz,023,1500 Hz,HIGH,OFF,12.5KHz,0,Strzelin,0
[...]
497,,,,,,,,,,,,,,0,,0
498,,,,,,,,,,,,,,0,,0
499,,,,,,,,,,,,,,0,,0
500,,,,,,,,,,,,,,0,,0
```
Where the input was like:
```
$ head -10 lista_sr6.csv
247,SR6A,145.575000,-,0.600000,,88.5,88.5,DV,12.5,Brzeg
249,SR6ACZ,438.950000,-,7.600000,Tone,103.5,103.5,FM,12.5,Wrocław
250,SR6B,145.762500,-,0.600000,Tone,77.0,77.0,FM,12.5,Działoszyn - stacja meteo
251,SR6C,439.250000,-,7.600000,,88.5,88.5,FM,12.5,Bolesławiec
252,SR6DA,431.750000,+,7.600000,,88.5,88.5,FM,12.5,Dalachów
253,SR6DKB,438.262500,-,7.600000,,88.5,88.5,DV,12.5,Krapkowice
254,SR6DL,144.975000,+,0.000000,,88.5,88.5,FM,12.5,Dalachów
255,SR6DMO,438.625000,-,7.600000,Tone,94.8,94.8,FM,12.5,Oława
257,SR6DST,145.687500,-,0.600000,Tone,123.0,123.0,FM,12.5,Strzelin, Wieża Ciśnień
258,SR6DWS,438.462500,-,7.600000,,88.5,88.5,DV,12.5,Wielka Sowa
```

In order to get proper ADMS-7 file just redirect output to import.csv.
```
$ python3 converter.py lista_sr6.csv > import.csv
```

### Things I learned:
* There must be 500 entries per VFO (no more , no less)
* ADMS-7 supports only Japan fonts in comments , lol
* Don't know what "User Tone" is. XD

