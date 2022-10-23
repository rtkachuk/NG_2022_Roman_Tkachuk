tpl = ("Manjaro", "Debian", "Gentoo", "Arch", "SLS")
print (str(tpl))

print (tpl[1])

# Lifehack to edit tuples
lst = list(tpl)
lst[-1] = "RedHat"
tpl = tuple(lst)
print ("LOL changed tuple: " + str(tpl))

# Unpack tuple!

(ungly_one, stable_one, useful_one, crappy_one, old_one) = tpl
print (useful_one)