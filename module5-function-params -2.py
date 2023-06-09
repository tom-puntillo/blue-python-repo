def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
        
print_letter_count('hocus-pocus', 's')

print_letter_count('e', 'welcome')

print_letter_count(text = 'Welcome', letter = 'e')

print_letter_count(letter = 'e', text = 'Welcome')