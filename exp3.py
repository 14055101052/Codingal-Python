valid = True

while True : 
    try : 
        n = int(input("Enter a number :  "))
        while n % 2 == 0 :
            print("bye")
            valid = False
            break

    except ValueError : 
        print("Invalid")