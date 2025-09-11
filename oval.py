current: int = 0
distance: int = 0
counter: int = 0

while counter < 5:
    while True:
        try:
            distance = int(input("Please enter the distance in meters: "))
            break
        except ValueError:
            print("Invalid input")

    current += distance

    if current % 1000 <= 100:
        print("Asphalt")

    elif current % 1000 <= 300:
        print("Muddy")

    elif current % 1000 <= 600:
        print("Rocky")

    else:
        print("Concrete")

    counter += 1