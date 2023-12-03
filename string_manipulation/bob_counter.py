#problem 1.2

##gather user input##
n = input("This program counts the amount of 'bob's in a string\nPlease input a string:\n")
x = len(n)
result = 0
##bob-checker##
for z in range(x):
    if x - z == 2:
        break
    if n[z] == "b":
        if n[z+1] == "o":
            if n[z+2] == "b":
                result += 1
##output##
print(result)