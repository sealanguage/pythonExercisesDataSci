#   using default values in function. can return values from default or override 

def calculate_interest_curr(balance = 1000, interest = 4, days = 100) :
    """
    1. Balance: Amount on which balance needs to be calculated
    2. Interest: annual interest in percentage
    3. Days: numver of days since the beginning of the year
    """

    interest_amount = balance * (interest / 100) * (days/365)
    return interest_amount