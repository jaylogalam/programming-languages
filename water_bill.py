consumption: int = 0
bill: int = 0

try:
    consumption = int(input("Enter the water consumption: "))
except ValueError as err:
    print(err)

# 101 to 200 = 2
# 201 to 400 = 5
# 400 to 700 = 10

if consumption > 300:
    amount = consumption - 300
    bill += amount * 10
    consumption -= amount

if consumption > 200:
    amount = consumption - 200
    bill += amount * 5
    consumption -= amount

if consumption > 100:
    amount = consumption - 100
    bill += amount * 2
    consumption -= amount

print(f"Bill: P {float(bill)}")