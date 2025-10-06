def get_distance() -> int:
    while True:
        try:
            distance = int(input("Please enter the distance in meters: "))
            return distance
        except ValueError:
            print("Invalid input")

def show_location(current_distance) -> None:
    if current_distance % 1000 <= 100:
        print("Asphalt")

    elif current_distance % 1000 <= 300:
        print("Muddy")

    elif current_distance % 1000 <= 600:
        print("Rocky")

    else:
        print("Concrete")

def main():
    current: int = 0
    counter: int = 0

    while counter < 5:
        distance = get_distance()
        current += distance
        show_location(current)
        counter += 1

if __name__ == "__main__":
    main()