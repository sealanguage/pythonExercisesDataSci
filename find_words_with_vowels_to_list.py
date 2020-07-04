#   applying the sorted function creates a list of the keys

words = input("Type a sentence:  ")

vowels = ["a", "e", "i", "o", "u"]  #  this is a list of vowels
vowels_list = {}  #  creating a new dictionary


for word in words:
    for letter in word:
        if letter in vowels:
            if vowels_list.get(letter) == None:
                vowels_list[letter] = [word]
            else:
                vowels_list.get(letter).append(word)
print(vowels_list)



