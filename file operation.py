import os
# file = open("file_name","mode")
# print(file.read())


file = open("mydata.txt","r")
print(file.readlines())  # read the entire file

#WRITE A NEW FILE 
# new_file = open("filename","mode")
# new_file.write("We add the content of that file")

# newfile = open("filename.txt","w")
# newfile.write("We add the content of that file")


 #How to remove file from
os.remove("filename.txt")