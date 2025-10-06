def get_sales() -> tuple[int, int]:
    while True:
        try:
            sales1 = int(input("Enter 1st half sales: "))
            sales2 = int(input("Enter 2nd half sales: "))
            return sales1, sales2

        except ValueError:
            print("Invalid input")

def get_incentive(sales) -> int:
    if sales > 500000:
        return int(sales * 0.10)
    return int(sales * 0.05)

def main():
    sales1, sales2 = get_sales()
    incentive1 = get_incentive(sales1)
    incentive2 = get_incentive(sales2)

    total_sales = sales1 + sales2

    print(f"\nTotal sales: {total_sales}")
    print(f"Incentives:")
    print(f"\t1st half: {incentive1}")
    print(f"\t2nd half: {incentive2}")
    if total_sales >= 1200000:
        print("\tAdditional trip to Japan")

if __name__ == "__main__":
    main()
