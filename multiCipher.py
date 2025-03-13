import random
input = ""
outputList = []
letters = list(input)
pi = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9,3,9,9,3,7,5,1]
e = [2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5,2,3,5,3,6,0,2,8,7,4,7,1,3,5,2,6,6,2,4,9,7,7,5,7,2,4,7,0,9,3,6,9,9,9,5]
phi = [1,6,1,8,0,3,3,9,8,8,7,4,9,8,9,4,8,4,8,2,0,4,5,8,6,8,3,4,3,6,5,6,3,8,1,1,7,7,2,0,3,0,9,1,7,9,8,0,5,7,6,2,8,6]

def shift_letter(letter, shift, typeCipher):
    # Check for lowercase letters
    
    if 'a' <= letter <= 'z':
        pi.pop(0)
        e.pop(0)
        phi.pop(0)
        shiftedLetter = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        return str(f"{typeCipher, shiftedLetter}")
    # Check for uppercase letters
    elif 'A' <= letter <= 'Z':
        pi.pop(0)
        e.pop(0)
        phi.pop(0)
        shiftedLetter = chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        return str(f"{typeCipher, shiftedLetter}")
    # Return the character as-is if it's not a letter
    elif ' ':
        return str(f"//")
    else:
        return letter


for letter in letters:
    cipherType = random.randint(0,2)
    if cipherType == 0:
        outputList.append(shift_letter(letter,pi[0],"P"))
    elif cipherType == 1:
        outputList.append(shift_letter(letter,e[0], "E"))
    else: 
        outputList.append(shift_letter(letter,phi[0], "Ph"))

print(''.join(outputList))


