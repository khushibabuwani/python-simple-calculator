def Calculator():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    a=input("Enter your Choice: add,sub,mul,div")
    if a=="sub":
        print(num1-num2)
    elif a=="mul":
        print(num1*num2)
    elif a=="div":
        if num2==0:
            print("Error: Division by zero is not allowed.")
        else:
            print(num1/num2)
    elif a=="add":
        print(num1+num2)
    else:
        print("Invalid choice. Please select add, sub, mul, or div.")
Calculator()