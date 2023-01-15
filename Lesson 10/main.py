from C_component import *

cpu = Component("Ryzen 5900X", 3529.50)
mem = Component("CORSAIR DD4 16 GB 2666Mhz", 1600.70)

cpu.setPrice(0)

print (cpu.getDiscountPrice())
#del cpu # delete cpu
print (cpu)
print (mem)