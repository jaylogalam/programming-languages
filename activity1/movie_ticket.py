import pandas as pd

def get_customer(ctype: str):
    while True:
        try:
            count = int(input(f"Enter number of {ctype}: "))
            if count < 1:
                return 0, 0
            pwd = int(input("How many are PWD: "))
            if pwd > count:
                raise ValueError
            break

        except ValueError:
            print("Invalid input")

    return count - pwd, pwd

def get_pwd_discount(ctype: str, normal: int, pwd: int):
    fee: float = 0.00
    discount: float = 0.20

    if ctype == "kids":
        fee: float = 200
    else:
        fee: float = 300

    normal_fee = (normal + pwd) * fee
    pwd_fee = pwd * fee * discount

    return float(normal_fee), float(pwd_fee)

def get_group_discount(count: int, kids: int, adults: int):
    if count > 10:
        percent = 0.08
    elif count > 5:
        percent = 0.06
    elif count > 2:
        percent = 0.04
    elif count > 1:
        percent = 0.02
    else:
        percent = 0

    discount = ((kids * 200) * percent) + ((adults * 300) * percent)

    return int(percent * 100), discount

def main():
    kids, pwd_kids = get_customer("kids")
    adults, pwd_adults = get_customer("adults")

    kids_total_fee, pwd_kids_discount = get_pwd_discount("kids", kids, pwd_kids)
    adults_total_fee, pwd_adults_discount = get_pwd_discount("adults", adults, pwd_adults)

    total_fee = float(kids_total_fee + adults_total_fee)
    total_count = kids + pwd_kids + adults + pwd_adults
    discount_percent, group_discount = get_group_discount(total_count, kids, adults)
    pwd_discount = pwd_kids_discount + pwd_adults_discount
    total = total_fee - pwd_discount - group_discount

    data = {
        "": ["Kids", "Adults", "", "Total Fee", "PWD Discount", "Group Discount", "", ""],
        "Count": [kids + pwd_kids, adults + pwd_adults, "", "", "", f"{discount_percent}%", "", "Total"],
        "Total": [kids_total_fee, adults_total_fee, "", total_fee, -pwd_discount, -group_discount, "", total],
    }
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
