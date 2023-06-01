user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old!')
    print('Sorry, you do not qualify.')
elif user_age == 30:
    print('You are exactly 30 yearls old!')
    print('You will need to meet additional conditions to qualify.')
else:
    print('You are younger than 30 years old!')
    print('Congratulations, you qualify!')