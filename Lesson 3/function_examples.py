from function_log import *

def divizion(root, divider):
    try:
        return root / divider
    except ZeroDivisionError as e:
        error(e)
        return "Infinity"

def askNumber(message):
    try:
        return float(input(message))
    except ValueError as e:
        error(e)
        info ("Using 0")
        return 0.0

def main():
    info ("Program started")
    root = askNumber("Enter first value: ")
    divider = askNumber("Enter second value: ")
    info ("Variable initialized")
    info ("Result: " + str(divizion(root, divider)))

main()