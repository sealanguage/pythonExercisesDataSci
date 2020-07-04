
# Last Checkpoint: a minute ago
sentence = input( "Enter a sentence" )

vowels = ["a", "e", "i", "o", "u"]
vowel_count = {}

for i in list(sentence) :
    if i in vowels :
        if vowel_count.get(i) == None :
            vowel_count[i] = 1
        else :
            vowel_count[i] = vowel_count[i] +1

            print(vowel_count)