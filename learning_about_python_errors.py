age = 21
try:
    age = age + "1"
    age = age / 0
except TypeError:
    print("cannot add integer to string")
except ZeroDivisionError:
    print("divide by zero error")
except KeyError:
    print("dictionary key error")
