#bisection search demo 
##initilaze/gather info from user##
print("Please think of a number between 0 and 99!")
z = input("press enter to continue")
high = 100
low = 0
x = 'a'
guess = round((high + low)/2, 0)

##bisection portion, program uses user input to decide which half of range to search##
while (x != 'c'):
    print("h = " + str(high) + "l = " + str(low))
    print ("Is your secret number " + str(guess) + " ?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if x == 'h':
        high = guess 
        
        
    else:
        low = guess

    guess = int((high+low)/2)

##output##
print("Your secret number is: " + str(guess))
    