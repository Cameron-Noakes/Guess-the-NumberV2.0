# --Guess The Number Game V2.0--
# Create a attempt variable and change the chosen,
# number every 5 incorrect guesses
# use try and except blocks to catch errors
# Each incorrect guess makes guess_counter increment by 1.

import random

print ("""Welcome to Guess-The-Number\nInformation:
1.) Each successful guess is +1 point
2.) 5 wrong guesses and number changes
3.) Continuous gameplay
""")



number = random.randint(1,101)
attempts = 5
points = 0
guess_counter = 1
guess = ""

try:
    while guess != number:
        guess = int(input("Guess a number: "))
        guess_counter + 1
        attempts -= 1

        if attempts == 0:
            if guess == number:
                points +=1
                print "Guess correct! Done in:",guess_counter,"guesses - points:",points
                guess = ""
                guess_counter = 1
            
            print ("Choosing another number...")
            number = random.randint(1,101)
            guess_counter +=1
            attempts = 5
    

        elif guess < number:
            print ("Guess too low.")
            guess_counter += 1
            

        elif guess > number:
            print ("Guess too high.")
            guess_counter += 1
            
        
        else:
            print "Guess correct! Done in:",guess_counter,"guesses - points:",points
            print "New Game... Changing Number."
            guess = ""
            points +=1
            guess_counter = 1
except:
    print ("Error caught. Make sure guess is an integer and under 100.")
    guess = ""
