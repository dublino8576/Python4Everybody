print(ord("G"))
#gets ascii value of a character

#convert a list of numbers into a string with Unicode integers
a = [108, 105, 110, 101]
#maps through a list telling to run the method chr() for each element
#map gets wrapped into a string
b = ''.join(map(chr, a))
print(b)