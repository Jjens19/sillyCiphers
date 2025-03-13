import random
import string

input = "I once slept over at a buddhist temple"
outputList = []
letters = list(input)

def shift_letter(letter, shift):
    # Check for lowercase letters
    
    if 'a' <= letter <= 'z':
        return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
    # Check for uppercase letters
    elif 'A' <= letter <= 'Z':
        return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    # Return the character as-is if it's not a letter
    else:
        return letter


for letter in letters:
    if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z': 
        cipherRand = random.randint(0, 6)
        outputList.append(str(cipherRand))  
    outputList.append(shift_letter(letter, 3))
    if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z': 
        for noise in range(cipherRand):
            outputList.append(random.choice(string.ascii_lowercase))



print(''.join(outputList))


