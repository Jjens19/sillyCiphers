input = "Did you crack the cipher?"
outputList = []
letters = list(input)
pi = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9,3,9,9,3,7,5,1]

def shift_letter(letter, shift):
    # Check for lowercase letters
    
    if 'a' <= letter <= 'z':
        pi.pop(0)
        return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
    # Check for uppercase letters
    elif 'A' <= letter <= 'Z':
        pi.pop(0)
        return chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    # Return the character as-is if it's not a letter
    else:
        return letter


for letter in letters:
    outputList.append(shift_letter(letter,pi[0]))

print(''.join(outputList))


