firstNumberForSum = int(input("Enter first number: "))
secondNumberForSum = int(input("Enter second number: "))
print ("======================")
print ("Sum: " + str(firstNumberForSum + secondNumberForSum))

# 1 step: firstNumberForSum + secondNumberForSum => 5 + 3 = 8 (because it's most deeper brackets)
# 2 step: str(8) -> "8" (just turn 8 to string)
# 3 step: "Sum:" + "8" -> "Sum: 8"
# 4 step: print ("Sum: 8")