#problem 1.3 
##gather user input##
s = input("This program outputs the LONGEST alphabetical portion of an input string\nPlease input a string:\n")

s_len = len(s) 
alpha = s[0] 
##checks from each character of string##
for n in range(s_len): #z = 1
     
    if not (n==0): #if not start 
        test = s[n-1] #test equals last character 
        for c in range ((s_len-n)):#for c in remaining code
            index = c+n #gives true index
            if s[index] >= s[(index) - 1]: #if index is greater than last index
                    test += s[index] #append index 
                    #tests to see if test needs to replace alpha 
                    if len(test) > len(alpha): 
                        alpha = test
            else:
                break
             
##output##       
print(alpha)

       