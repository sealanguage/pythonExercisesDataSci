if __name__ == '__main__':
    n = int(input().strip())

    if n in range(101) :
        if n %2 != 0 :
            print("1 Weird")

    if(n in range(2, 6) ) :  
        if n %2 == 0 :
            print("2 Not Weird")
     
    if(n in range(5, 21)) :
        if n %2 == 0 :
            print("3 Weird")

    if(n in range(21, 101)) :
        if n %2 == 0 :
            print("4 Not Weird")