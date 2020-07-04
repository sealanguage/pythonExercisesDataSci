# Pythonist 2  to  pYTHONIST 2\n",
#   HackerRank.com presents \ Pythonist 2 \
#   HackerRank.com presents "Pythonist 2".

s = input( "input a string: ")

for i in s :
        if i.islower() :
            print(i.upper(), end = '')
        if i.isupper() :
            print(i.lower(), end = '')
        if i.isnumeric() :
            print(i, end = '')
        if i.isspace() :
            print(i, end = '')
        if i.endswith(".) :
            print(i, end = '')