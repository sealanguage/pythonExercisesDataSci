def swap_case(s):
    news = 0
    for i in s :
        news = s.swapcase()
    
    return news

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)