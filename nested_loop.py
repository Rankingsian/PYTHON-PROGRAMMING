for x in range (4):
    for y in range (3):
        print(f'{x} , {y}')
        
        
numbers = [5,2,5,2,2]
for x_count in numbers:
    print("x" * x_count)
    
    
    
numbers = [4,5,6,7,3,9]
for x_count in numbers:
    output = ''
    for count in range (x_count):
        output +='x'
    print(output)