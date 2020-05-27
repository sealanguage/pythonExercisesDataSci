y = "1 w 2 r 3g"

# Complete the solve function below.
def solve(y):
    if s.isalpha() == False :
        s = s.title()
        print("s is ", s)
    return s



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
