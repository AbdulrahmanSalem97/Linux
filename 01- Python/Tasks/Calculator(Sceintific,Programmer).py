print("***********************************************************************")
print("********************* Welcome to our Calculator ***********************")
print("***********************************************************************")

while True:
    mode_select = input("Select mode: 1. Scientific, 2. Programming, q. Quit\n")

    if mode_select == "1":
        result = 0
        while True:
            print("Select operation: 1. Addition, 2. Subtraction, 3. Division, 4. Multiplication, 5. Modulus, 6. Exponentiation,q. Quit")
            operation = input()

            if operation == "q":
                break
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                #Addition
                if operation == "1":
                    result = num1 + num2
                    print("Result = ", result)
                    print("***********************************************************************")
                #Subtraction    
                elif operation == "2":
                    result = num1 - num2
                    print("Result = ", result)
                    print("***********************************************************************")
                #Division    
                elif operation == "3":
                    result = num1 / num2
                    print("Result = ", result)
                    print("***********************************************************************")
                #Multiplication    
                elif operation == "4":
                    result = num1 * num2
                    print("Result = ", result)
                    print("***********************************************************************")
                #Modulus    
                elif operation == "5":
                    result = num1 % num2
                    print("Result = ", result)
                    print("***********************************************************************")
                #Exponentiation
                elif operation == "6":
                    result = num1 ** num2
                    print("Result = ", result)
                    print("***********************************************************************")
                else:
                    print("Invalid operation")

    elif mode_select == "2":
        #using builtin functions bin(), hex()
        while True:
            print("Select conversion: 1. Decimal to Binary, 2. Decimal to Hexadecimal,q. Quit")
            conversion = input()
            #decimal -> Binary
            if conversion == "1":
                decimal_num = int(input("Enter decimal number: "))
                print("Binary: ", bin(decimal_num))
                print("***********************************************************************")
            #decimal -> Hexadicemal    
            elif conversion == "2":
                decimal_num = int(input("Enter decimal number: "))
                print("Hexadecimal: ", hex(decimal_num))
                print("***********************************************************************")
            elif conversion == "q":
                break
            else:
                print("Please A correct choise")

    elif mode_select == "q":
        break

    else:
        print("Select A correct Mode pls!")
        print("***********************************************************************")