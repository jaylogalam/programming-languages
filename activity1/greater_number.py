try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if number1 > number2:
        print(number1, "is greater")

    elif number1 < number2:
        print(number2, "is greater")

    else:
        print("Equal")

except ValueError:
    print("Invalid input")