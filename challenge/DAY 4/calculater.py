# Basic calculater 🐍🐍


while True:
    operation = input(
        "Enter the operation you want performed ( + , - , * , / ) :  "
    ).strip()
    num1 = float(input("Enter the first number  : "))
    num2 = float(input("Enter the second number  : "))

    if operation == "+":
        result = num1 + num2
        print(f"Sum of the number is :{result}")
    elif operation == "-":
        result = num1 - num2
        print(f"subtraction of the number is  : {result}")

    elif operation == "*":
        result = num1 * num2
        print(f"multiplication of the number is :{result:.3f}")

    # print (multiplication of the number is :{round(result ,3)})

    elif operation == "/":

        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"Division of the number is :{result:.3f}")

    else:
        print(f" {operation} is invalid please try again ! ")


    choice = input("\nDo you want to perform another calculation? (yes/no): ")

    if choice.lower() != "yes":
        print("Calculator closed. Goodbye! 👋")
        break
