import pandas as pd

def get_customer(ctype: str) -> tuple:
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

def calculate_fee(ctype: str, normal: int, pwd: int):
    fee: float = 0.00
    discount: float = 0.20

    if ctype == "kids":
        fee: float = 200
    else:
        fee: float = 300

    normal_fee = normal * fee
    pwd_fee = pwd * (fee - (fee * discount))

    return normal_fee, pwd_fee

def get_group_discount(count: int) -> float:
    if count > 10:
        return 0.08
    elif count > 5:
        return 0.06
    elif count > 2:
        return 0.04
    elif count > 1:
        return 0.02
    else:
        return 0

def main():
    kids, pwd_kids = get_customer("kids")
    adults, pwd_adults = get_customer("adults")

    kids_total_fee, pwd_kids_total_fee = calculate_fee("kids", kids, pwd_kids)
    adults_total_fee, pwd_adults_total_fee = calculate_fee("adults", adults, pwd_adults)

    normal_total_fee = kids_total_fee + adults_total_fee
    pwd_total_fee = pwd_kids_total_fee + pwd_adults_total_fee
    total_count = kids + adults + pwd_kids + pwd_adults
    group_discount = normal_total_fee * get_group_discount(total_count)
    normal_total_fee = normal_total_fee - group_discount

    final_fee = normal_total_fee + pwd_total_fee
    # print("Total fee: ", final_fee)

    data = {
        "": ["Kids", "Adults", "", "PWD Kids", "PWD Adults", "", "Total fee", "Group discount", "", ""],
        "Count": [kids, adults, "", pwd_kids, pwd_adults, "", "", f"{int(get_group_discount(total_count) * 100)}%", "", "Total:"],
        "Total": [kids_total_fee, adults_total_fee, "", pwd_kids_total_fee, pwd_adults_total_fee, "", normal_total_fee + pwd_total_fee, -group_discount, "", final_fee],
    }
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
