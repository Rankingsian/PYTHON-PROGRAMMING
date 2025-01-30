numbers = [2,3,4,5,3,2,1,23]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)