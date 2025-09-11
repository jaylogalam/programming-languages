def get_avg():
    while True:
        try:
            x: int = int(input("Enter score 1: "))
            y: int = int(input("Enter score 2: "))
            break
        except ValueError:
            print("Invalid input")

    result: float = (x + y) / 2
    return result

def get_remarks(avg: float):
    if avg <= 50:
        return "Poor"

    if avg <= 70:
        return "Good"

    if avg <= 90:
        return "Very good"

    return "Excellent"

if __name__ == "__main__":
    average: float = get_avg()
    remarks: str = get_remarks(average)

    print("Average:", average)
    print("Remarks: ", remarks)