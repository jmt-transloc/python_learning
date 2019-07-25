number = 42
guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratulations, you guessed the number!')
elif guess < number:
    print('No, the number is a bit higher than that.')
else: 
    print('No, the number is a bit lower than that.')

print('Done')