def log(type, message):
    print ("[" + str(type) + "]: " + str(message))

def warning(message):
    log("WARN", message)

def error(message):
    log ("ERR", message)

def info(message):
    log ("INFO", message)