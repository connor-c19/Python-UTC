#problem 1.1
##gather info from user##
s = input("How many vowels in(lowercase):\n")
vowel = 0
##iterates through user input## 
for x in s: 
    if x in "AEIOUaeiou":
        vowel += 1

##output##
print('Number of vowels: ' + str(vowel))