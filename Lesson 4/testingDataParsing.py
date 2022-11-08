def multiplyByTwoStrElement(element):
    return str(int(element) * 2)


lst = [ 0, 2, 4, 6, 8, 10 ]
print (list(map(lambda x: x * 2, lst)))

stringExample = "0,1,2,3,4,5"
print (list(map(lambda x: str(int(x) * 2), stringExample.split(','))))
print (list(map(lambda x: multiplyByTwoStrElement(x), stringExample.split(','))))
