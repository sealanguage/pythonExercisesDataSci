def birthdayCakeCandles(ar):
    count = 0
    highest = 0

    for i in ar :
        if i > highest :
            highest = i
            count = 1
        elif i == highest :
            count += 1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()