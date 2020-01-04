
def silly_encrypt(string, shift):
    encrypted_letter = []
    letters = []
    string = [char for char in string]
    for y in range(len(string)):
        encrypted_letter.append(ord(string[y]))
        encrypted_letter[y] = encrypted_letter[y] + shift
        letters.append(chr(encrypted_letter[y]))

    letters = "".join(letters)
    return letters

def silly_decrypt(encrypted_string, shift):
    decrypted_letter = []
    letters = []
    encrypted_letter = []
    encrypted_string = [char for char in encrypted_string]
    for y in range(len(encrypted_string)):
        encrypted_letter.append(ord(encrypted_string[y]))
        decrypted_letter.append(encrypted_letter[y] - shift)
        letters.append(chr(decrypted_letter[y]))
    
    letters = "".join(letters)
    return letters
    
