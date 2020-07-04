name = input("enter string - ")
length = len(name)

reversed_name = ""

while( length > 0 ) :
    reversed_name = reversed_name + name[length-1]
    length = length-1