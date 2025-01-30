numbers = [5,2,6,7,9,]
numbers.append(20)
numbers.insert(0,40)
numbers.remove(5) #You enter the number which you want to remove
numbers.clear #Remove all the items in a list
numbers.pop() #Removes the last number in the list
numbers.index(2)#Checking the existence of a number in a list and print the index of the number in the list
numbers2 = numbers.copy()
numbers.append(90)
print(numbers2)
print(50 in numbers)
print(numbers)