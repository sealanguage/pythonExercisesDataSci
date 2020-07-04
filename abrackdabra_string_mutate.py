def mutate_string(string, position, character):
    # print(i, c)  # i is position, c is replacement letter
    #  put the replacement character c into position i in string s
    #  s[i]
    s = string
    # print(s[5])
    # string.split()
    string.replace(s[5], "k")
    # print(string)

    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    