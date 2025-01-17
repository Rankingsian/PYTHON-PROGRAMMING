# help
# start - To statr the car
# stop - tp stop the car
# quit -  to exit the 

command = ""
while command != "quit:":
    command = input (">").lower
    if command == "start":
        print("car started..")
    elif command == "stop":
        print("car stopped.")
    elif command == "help":
        print(""" 
              start - to statr the car
              stop - to stop thr car
              quit - to quit
              
              """)
    else:
        print("I don't understsnd that!")