# simple CHIRP->ADMS-7 converter
# Bartlomiej Marcinkowski SP6XD
# Do whatever you want with this script.
import sys
import csv


if len(sys.argv) < 2:
    print("Usage: python3 convert.py CHRIP_list.csv")
    exit(1)


with open(sys.argv[1]) as lista:
    repeaters = csv.reader(lista)
    counter = 1
    for row in repeaters:
        row_no = str(counter)
        tx_freq = "{:.5f}".format(float(row[2]))
        rx_freq = "{:.5f}".format(float(row[2])-float(row[4]))
        offset = row[4]
        if row[8] == "FM":
        #only FM 
            mode = row[8]
        else:
            continue
        name = row[1]
        if row[5] == "Tone":
            tone_mode = "TONE SQL"
        elif row[5] == "":
            tone_mode = "OFF"
        else:
        #no dcs support for now
           continue

        #with a space 
        ctcss_tone = row[6] + " Hz"
        dcs_code = "023"

        #not sure what it is
        ctcss_user ="1500 Hz"

        #fk yeah, full power
        power = "HIGH"
        skip = "OFF"

        #yep, no space here because fuck you I guess
        step = row[9]+"KHz"

        clock_shift = "0"
        unknown = "0"

        # this is so retarted ... I have no words for that, only Japan is supported by ADMS-7
        remove_polish_utf = {ord('ą'):'a', ord('ę'):'e', ord('ś'):'s', ord('ł'):'l' , ord('ź'):'z' , ord('ż'):'z' , ord('ó'):'o' , ord('ń'):'n',
                             ord('Ą'):'A', ord('Ę'):'E', ord('Ś'):'S', ord('Ł'):'L' , ord('Ż'):'z' , ord('Ź'):'Z' , ord('Ó'):'O' , ord('Ń'):'N'}
        comment = str(row[10]).translate(remove_polish_utf)

        if row[3] == "-":
            off_dir = "-RPT"
        elif row[3] == "+":
            off_dir = "+RPT"
        elif row[3] == "split":
            rx_freq = "{:.5f}".format(float(row[4]))
            offset = "0.00000"
            off_dir = "-/+"
        elif row[3] == "":
            off_dir = "OFF"

        print (row_no +","+  tx_freq  +","+  rx_freq  +","+  offset  +","+  off_dir  +","+  mode  +","+  name  +","+  tone_mode  +","+  ctcss_tone  +","+  dcs_code  +","+  ctcss_user +","+  power  +","+  skip  +","+  step  +","+  clock_shift  +","+ comment  +","+  unknown)

        counter += 1
        if counter > 500:
           break;

# yep, there must be exactly 500 entires per VFO
if counter < 500:
    while counter <= 500:
        print(str(counter) + ",,,,,,,,,,,,,,0,,0")
        counter += 1
