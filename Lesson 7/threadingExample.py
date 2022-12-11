import threading

def showLetters(number, word):
    for letter in word:
        print ("Thread #" + str(number) + ":" + letter)

def manager(lines):
    threads = []
    for line in lines:
        threads.append(threading.Thread(target=showLetters, args=(lines.index(line), line, )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

lines = [
    "Hello world",
    "This is an example line, which will be shown letter by letter",
    "Well, this is awkward, but I perfer python for desktop applications",
    "I hope, that chromium will be stable in future"
]

manager(lines)