import threading
import time

lock = threading.Lock()
number = 0

def incrementNumber(threadNumber):
    global number
    while number < 100:
        with lock:
            if number < 100:
                number = number + 1
                print ("Thread #" + str(threadNumber) + ":" + str(number))
        time.sleep(0.1)

def manager():
    threads = []
    for threadNumber in range (0, 10):
        threads.append(threading.Thread(target=incrementNumber, args=(threadNumber, )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

manager()