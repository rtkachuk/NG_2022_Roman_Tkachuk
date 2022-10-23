randomVariable = "I'm here!"
list = [ "TEST", "Hello", "TEST", 2, -456.7, True, False, "LOL", randomVariable ]
print (list)
print ("Length: " + str(len(list)))
print ("On the first position is: " + str(list[0]))
print ("On the last position is: " + str(list[-1]))
print ("From third to fifth position: " + str(list[2:5]))
print ("List all elements up to fourth one: " + str(list[:4]))

if "TEST" in list:
    print ("YUP")

print ("=========================================")

# Change item on first position:
list[0] = "OH"
print ("Chagned first element: " + str(list))
list [1:6] = [ "Nothing", "left" ]
print ("Replaced items from second to sixth elements: " + str(list))
list.insert(1, "KEK")
print ("Inserted into second element: " + str(list))
list.append("ROFL")
print ("Appended to the end of the list: " + str(list))
list1 = [ "a", 5, False, "TEST" ]
list.extend(list1)
print ("Extended list: " + str(list))
list.remove(False)
print ("Removed False: " + str(list))
print ("=========================================")

print ("List elements via for loop: ")
for elem in list:
    print (elem)
print ("List elements via for loop but with indexes:")
for index in range(len(list)):
    print (str(index) + ": " + str(list[index]))
print ("Let's use simple while script at this time: ")
index = 0
while index < len(list):
    print (str(index) + ": " + str(list[index]))
    index = index + 1

print ("=========================================")
list.clear()
print ("Clear list: " + str(list))

list = [ 95, 0, 14, 5, 2, 66, 10 ]
list.sort()
print ("Sorted list: " + str(list))

print ("Example of working with copy: ")
list1 = [ "Hello", "my", "friend" ]
list2 = list1.copy()
list1[0] = "Goodbye"
print (str(list2))