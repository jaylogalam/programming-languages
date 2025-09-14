try:
    score = int(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score")

    elif score < 60:
        print("F")

    elif score < 70:
        print("D")

    elif score < 80:
        print("C")

    elif score < 90:
        print("B")

    elif score <= 100:
        print("A")

    if score >= 60:
        print("Passed")
    else:
        print("Failed")
        
except ValueError:
    print("Invalid input")

