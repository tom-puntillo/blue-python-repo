sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    word = input('Enter a word in English or EXIT: ')
    
    if word == 'EXIT':
        print('Bye!')
        break
    
    if word not in sample_dict:
        print('No match!')
        
    if word in sample_dict:
       print('Translation:', sample_dict[word])