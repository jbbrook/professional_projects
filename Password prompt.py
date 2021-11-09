#password
password = input("What is your password?")

#password tries
num_tires = 3
#password
while num_tires <= 3:
    if password != ("james"):
        print("you have {} tires left".format(num_tries))
        num_tries -= 1
        if num_tries == 0:
            print("you have been locked out")
            break
        
