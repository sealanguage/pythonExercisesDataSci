# 3 ways to use substitution in format() function in python3


"{} is a {} company".format("CareerDevs", "technology")
#  result is    'CareerDevs is a technology company'

#  use indexing to substitute
"{1} is a {0} company".format("CareerDevs", "technology")
#  result is       'technology is a CareerDevs company'

#  use a keyword to select the substitution text
"{company_name} is a {type} company".format(
    type="technology", company_name="CareerDevs"
)
#  result is     "CareerDevs is a technology company"

