import pandas as pd

fee = {
    "kids": 200,
    "adults": 300
}
discount: float = 0.20

def get_customer(ctype: str):
    while True:
        try:
            count = int(input(f"Enter number of {ctype}: "))
            if count < 1:
                return 0, 0

            if ctype == "kids":
                pwd = int(input("How many are PWD: "))
            else:
                pwd = int(input("How many are PWD/Senior Citizen: "))
                
            if pwd > count:
                raise ValueError
            
            break

        except ValueError:
            print("Invalid input")

    return count - pwd, pwd

def get_total_fee(ctype: str, count: int, pwd: int):
    total_fee = (count + pwd) * fee[ctype]
    pwd_discount = pwd * fee[ctype] * discount

    return float(total_fee), float(pwd_discount)

def get_group_discount(total: int, kids: int, adults: int):
    if total > 10:
        percent = 0.08
    elif total > 5:
        percent = 0.06
    elif total > 2:
        percent = 0.04
    elif total > 1:
        percent = 0.02
    else:
        percent = 0

    discount = ((kids * 200) * percent) + ((adults * 300) * percent)

    return discount, int(percent * 100)

def main():
    kids_count, pwd_kids_count = get_customer("kids")
    adults_count, pwd_adults_count = get_customer("adults")
    group_count = kids_count + pwd_kids_count + adults_count + pwd_adults_count

    kids_total_fee, kids_pwd_discount = get_total_fee("kids", kids_count, pwd_kids_count)
    adults_total_fee, adults_pwd_discount = get_total_fee("adults", adults_count, pwd_adults_count)
    group_discount, percent = get_group_discount(group_count, kids_count + pwd_kids_count, adults_count + pwd_adults_count)

    initial = kids_total_fee + adults_total_fee
    total = initial - (kids_pwd_discount + adults_pwd_discount + group_discount)

    initial_fee_data = {
        "": ["Kids", "Adults", f"{"-"*15}", ""],
        "Count": [kids_count + pwd_kids_count, adults_count + pwd_adults_count, f"{"-"*10}", "Fee"],
        "Total": [kids_total_fee, adults_total_fee, f"{"-"*8}", initial],
    }

    discount_df = {
        "": ["Group", "PWD/Senior", f"{"-"*15}", ""],
        "Discount": [f"{percent}%", "20%", f"{"-"*10}", "Total Fee:"],
        "Total": [group_discount, kids_pwd_discount + adults_pwd_discount, f"{"-"*8}", total],
    }

    initial_fee_df = pd.DataFrame(initial_fee_data)
    discount_df = pd.DataFrame(discount_df)
    print(initial_fee_df.to_string(index=False), end="\n\n")
    print(discount_df.to_string(index=False), end="\n\n")
    
    
if __name__ == "__main__":
    main()
