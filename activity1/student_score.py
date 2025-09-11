def student_score():
    try:
        score = int(input("Enter score: "))
    except ValueError:
        print("Invalid input")
        return

    if score < 60:
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

def main():
    student_score()

if __name__ == "__main__":
    main()