import serial
import serial.tools.list_ports
import time

def search():
    device = ""
    while device == "":
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in str(port.product):
                device = str(port.device)
        time.sleep(1)
        print ("waiting...")
    return device

def reader():
    device = search()
    print ("FOUND: " + device)
    try:
        with serial.Serial(device, 115200, timeout=1) as ser:
            while True:
                line = ser.readline()
                if len(line) != 0:
                    print (str(line))
    except Exception as disconnectedException:
        print(str(disconnectedException))


def main():
    while True:
        reader()

main()