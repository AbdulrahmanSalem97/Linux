while True:
        print("isdigit()"+"\nljust()"+"\nstartswith()"+"\npress any key to exit")
        key  = input("Please enter your choise to visualize and understand the function")
        if key == '1':
                data = "1750"
                x = data.isdigit()
                print(x)
                print(" isdigit(): Returns True if all characters in the string are digits.")
        elif key == '2' :
                data = "Abdulrahman Salem"
                x = data.ljust()
                print(x)
                print("ljust() : Returns a left justified version of the string")
        elif key =='3' :
                data = "Hola"
                x = data.rfind("H")
                print(x)
                print("startswith()	Returns true if the string starts with the specified value")   
        else :
               print("Thank You!")
               break
        

#isdigit()     Returns True if all characters in the string are digits
#ljust()	     Returns a left justified version of the string
#startswith()	Returns true if the string starts with the specified value
