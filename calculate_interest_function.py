def calculate_interest(balance, interest, days) :
    interest_amount = balance * (interest / 100) * (days/365)
    return interest_amount