weight = int(input("weight: "))
unit = input('(L)bs or (K)g: ' )
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kg")
else:
    converted = weight /0.45
    print(f"you are {converted} lbs")