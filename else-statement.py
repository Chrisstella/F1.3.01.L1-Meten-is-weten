#Chrisstella b
#else statement

a = input("geef een getal: ")
b = input('geef nog een getal: ')
if a > b:
    Max = a
    print("a is het grootste getal: " + str(Max))
elif a < b:
    Min = a
    print("a is het kleinste getal: " + str(Min))
else:
    print("a en b zijn even groot")

