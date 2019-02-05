import random

num = random.randint(1,100); 
print ("I thought of a number between 1 and 100! Try to guess it.");
guess = 0;
while (guess != num):
    guess = int( input ("Your guess: "));
    if (guess > num):
            print("Wrong! My number is smaller.")
    elif (guess < num):
            print("Wrong! My number is greater.")
    elif (guess == num):
            print ("Congrats! You guessed my number.")
