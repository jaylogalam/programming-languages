def even_odd():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return

    if num % 2 == 0:
        print("Even")

    if num % 2 == 1:
        print("Odd")

def main():
    even_odd()

if "__main__" == __name__:
    main()