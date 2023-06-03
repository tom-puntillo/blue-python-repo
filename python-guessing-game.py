while True:
    user_answer = int(input('When was Python 1.0 released? '))
    if (user_answer > 1994):
        print('It was earlier than that!')
        
    elif (user_answer < 1994):
        print('It was later than that!')
        
    else:
        print('Correct!')
        break