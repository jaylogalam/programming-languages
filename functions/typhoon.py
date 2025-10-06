def get_speed() -> int:
    while True:
        try:
            speed = int(input("Enter the wind speed (kph): "))
            return speed
        except ValueError:
            print("Invalid input")

# w/o return_value w/ params
def show_signal(speed) -> None:
    if speed <= 61:
        print("TD - Signal no. 1")

    elif speed <= 88:
        print("TS - Signal no. 2")

    elif speed <= 117:
        print("STS - Signal no. 3")

    elif speed <= 184:
        print("TY - Signal no. 4")

    else:
        print("STY - Signal no. 5")

# w/o return_value w/o params
def main():
    speed = get_speed()
    show_signal(speed)

if __name__ == '__main__':
    main()