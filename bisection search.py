print "Please think of a number between 0 and 100!"
mins=0
maxs=100
guess=(mins+maxs)/2

while True:    
    print"Is your secret number "+str(guess)+"?"
    print"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
    response=raw_input('Give me your response,h,l,c?')
    if response=='c':
        break
    elif response=='h':
        maxs=guess
        guess=(mins+maxs)/2
        print"Is your secret number "+str(guess)+"?"
    elif response=='l':
        mins=guess
        guess=(mins+maxs)/2
        print"Is your secret number "+str(guess)+"?"
    else:
        print "your answer cannot be understanded"
print "Game over. Your secret number was:"+str(guess)
    