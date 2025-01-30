#Exception handling
try:
    # Code that might raise an exception
    file = open("mydat.txt","r")
    print(file.read())
except FileNotFoundError:
    print("Sorry, the file does not exist.")
finally:
    print("Any statement")