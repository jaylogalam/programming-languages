try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even")

    if num % 2 == 1:
        print("Odd")
        
except ValueError:
    print("Invalid input")