def get_consumption() -> int:
    try:
        consumption = int(input("Enter the water consumption: "))
        return consumption
    except ValueError as err:
        print(err)
        
def calculate_bill(consumption: int) -> float:
    bill: float = 0
    
    if consumption <= 100:
        bill = consumption * 0
        
    elif consumption <= 200:
        bill = consumption * 2
        
    elif consumption <= 300:
        bill = consumption * 5
        
    else:
        bill = consumption * 10
        
    return bill

def show_bill(bill: float) -> None:
    print(f"Bill: P {bill}")
        
def main() -> None:
    consumption = get_consumption()
    bill = calculate_bill(consumption)
    show_bill(bill)
    
if __name__ == "__main__":
    main()