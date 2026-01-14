# def ADD(a,b):
#     return a+b

# def Sub(a,b):
#     return a-b

# def devision(a,b):
#     if b == 0:
#         return "Error! Division by zero."
#     return a/b

# def multi(a,b):
#     return a*b

# print("Simple Calculator")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = int(input("Enter your choice (1-4): "))

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == 1:
#     print("sum  " , ADD(num1,num2) )
    
# if choice == 2:
#     print("sub  : " 
#           , Sub(num1,num2))


while True:
    print("\n--- Calculator ---")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("q  Quit")

    choice = input("Enter operation: ")

    if choice == "q":
        print("Calculator closed")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    match choice:
        
        case "+":
            print("Result:", a + b)

        case "-":
            print("Result:", a - b)

        case "*":
            print("Result:", a * b)

        case "/":
            if b == 0:
                print("Error: Division by zero")
            else:
                print("Result:", a / b)

        case _:
            print("Invalid operation")
            break
