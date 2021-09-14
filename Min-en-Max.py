#Chrisstella b
#min en max

a = input("geef een getal: ")
b = input('geef nog een getal: ')
if a > b:
    Max = a
    Min = b
    print("a is het grootste getal: " + str(Max))
    print("b is het kleinste getal: " + str(Min))
    print("Het maximum is: " + str(Max))
    print("Het minimum is: " + str(Min))
elif a < b:
    Max = b
    Min = a
    print("b is het grootste getal: " + str(Max))
    print("a is het kleinste getal: " + str(Min))
    print("Het maximum is: " + str(Max))
    print("Het minimum is: " + str(Min))
else:
    print("a en b zijn even groot: " + str(a))
    print("Het minimum en het maximum zijn gelijk")
