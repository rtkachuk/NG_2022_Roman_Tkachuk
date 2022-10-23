dct = {
    "CPU": "Ryzen-i910500K",
    "Motherboard": "ASUS-Huanan",
    "RAM": "16MB",
    "HDD": "Seagate200TB",
    "Volumes": [ "C:", "D:", "F:" ]
}

print (str(dct))
print (str(dct.get("CPU")))
print (str(dct.keys()))
print (str(dct.values()))

dct["CPU"] = "Zeon 5500G"
print (str(dct))

dct["Price"] = "1$"
print (str(dct))

del dct["RAM"]
print (str(dct))

print ("====================")

for key in dct.keys():
    print (str(key) + ": " + str(dct[key]))