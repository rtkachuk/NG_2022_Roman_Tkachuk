def askForNumber():
    value = int(input("Enter value: "))
    return value

def powerNumber(number):
    return number * number

def processAndShowPowerNumber():
    print ("Result: " + str(powerNumber(askForNumber())))

processAndShowPowerNumber()