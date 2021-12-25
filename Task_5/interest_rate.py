def compute_interest_rate(amount, percentege_rate, duretion_days):
    return amount * (1+percentege_rate/100) * duretion_days


def main():
    amount = float(input('amount: '))
    percentege_rate = int(input('percentege_rate: '))
    duretion_days = float(input('duretion_days: '))

    interest_rate = compute_interest_rate(amount, percentege_rate, duretion_days)
    print(interest_rate)
    

if __name__ == "__main__":
    main()
