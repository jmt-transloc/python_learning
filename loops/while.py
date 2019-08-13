number = 42
running = True

while running:
    guess = int(input('Enter a number : '))
    
    if guess == number:
        print('You guessed the number!')
        running = False
    elif guess < number:
        print('No, the number is a bit higher')
    else:
        print('No, the number is a bit lower')
else:
    print('The while loop has ended')

print('Done')
