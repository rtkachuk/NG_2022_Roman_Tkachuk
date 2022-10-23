st = { "Apple", "Xiaomi", "ASUS", "HP", "Apple" }
print (str(st))

print ("Apple" in st)

st.add("Samsung")
print (str(st))

st1 = { "Lenovo", "Acer", "Blackberry" }
st.update(st1)


print (str(st))

print ("Remove vs discard: ")
st.remove("Apple") # Fail if key not found
st.discard("Apple") # Don't fail if key not found
print (st)