while True:
    print("Vcalculator")
    print("Select an operation to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("E. Exit Program")

    operation= input()

    if operation == "1":
       num1 = input("Enter a number: ")
       num2 = input("Enter a second number: ")
       print("The sum is " + str(int(num1) + int(num2)))
    elif operation == "2":
      num1 = input("Enter a number: ")
      num2 = input("Enter a second number: ")
      print("The difference is " + str(int(num1) - int(num2)))
    elif operation == "3":
      num1 = input("Enter a number: ")
      num2 = input("Enter a second number: ")
      print("The product is " + str(int(num1) * int(num2)))
    elif operation == "4":
      num1 = input("Enter a number: ")
      num2 = input("Enter a second number: ")
      print("The result is " + str(int(num1) / int(num2)))
    elif operation == "E":
        print("Program has ended")
        quit()
    else:
     print("Invalid Entry")



