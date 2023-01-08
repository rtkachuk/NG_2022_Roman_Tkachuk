import serial
import serial.tools.list_ports
import time
import os

def processKey(key, ser):
    match key:
        case "ASK":
            data = input("Enter key: ").encode("UTF-8")
            ser.write(data)
        case "firefox": 
            os.popen("firefox-bin")
        case _:
            print (key)

def search():
    device = ""
    while device == "":
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in str(port.product):
                device = str(port.device)
        time.sleep(1)
    return device

def reader():
    print ("Device wait...")
    device = search()
    print ("FOUND: " + device)
    try:
        with serial.Serial(device, 115200, timeout=1) as ser:
            while True:
                line = ser.readline()
                if len(line) != 0:
                    processKey(line.decode('UTF-8').rstrip(), ser)
    except Exception as disconnectedException:
        print(str(disconnectedException))


def main():
    while True:
        reader()

main()
