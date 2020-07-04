count = 0

sentence = input("enter a sentence: ")
sentence = list(sentence)
vowels = ["a", "e", "i", "o", "u"]

for letter in list(sentence) :
   if letter in vowels :
      count = count + 1