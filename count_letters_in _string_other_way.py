name = input("enter string: ")
char = input("entr character to search: ")

counter = 0
length = len(name)

for i in range(0, length) :
    if name[i].upper() == char.upper() :
        counter = counter + 1
        
print(counter)  