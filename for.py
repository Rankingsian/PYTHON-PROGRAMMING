list = ["Java","Python","C","C+"]
for items in list:
    print(items)
    
#FInding average of list of numbers
list_num = [20,30,40,50]
sum = 0
for i in list_num:
    sum = sum+i
print("sum =",sum)
print("average =",sum/len(list_num))

#for loop in tuples
num = (30,45,60,50,70)
sum = 0
for items in num:
    sum = sum + items
print(sum)
    
    
#range function
for i in range(1,10):
    sum = 0
    sum = sum + i
print(sum)

for items in range (0,10,2):
    print("Dispaly values with a step size of 2:", items)
    
#program to print table of a given number
# n = int(input("Enter a number: "))
# for i in range (1,11):
#     mul = n * i
#     print(n,"*",i,"=",mul)
    
list2 = ["C++","Java","Python"]
for item in range(len(list2)):
    print("Hello",list2[item])
    
#Nested for loops
companies = ["Google","Apple","Uber","PWC"]
for items in companies:
    print("We will display each letter of" +items)
    for letter in items:
        print(letter)
        
        #for loop with else clause
for i in  range(0,10,3):
    print(i)
else:
    print("No items in list")