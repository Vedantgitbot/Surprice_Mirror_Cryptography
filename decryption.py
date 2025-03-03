import random

def surprise_mirror_encrypt(password):
    mapping_digits = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', 
                      '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
    
    special_chars = ['.', ',', ';', "'", '"', ':', '[', ']', '{', '}', '\\', '|']
    
    def reverse_letter(char):
        if char.isalpha():
            if char.isupper():
                return chr(187 - ord(char)) 
            elif char.islower():
                return chr(219 - ord(char))  
        return char

    if len(password) < 8:
        return "Error: Password must be at least 8 characters long."

    encrypted_password = ''.join(mapping_digits[char] if char in mapping_digits else reverse_letter(char) for char in password)
    
   
    encrypted_password += random.choice(special_chars)
    
    return encrypted_password


def surprise_mirror_decrypt(encrypted_password):
    mapping_digits_reverse = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', 
                              '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
    
    special_chars = ['.', ',', ';', "'", '"', ':', '[', ']', '{', '}', '\\', '|']
    
    def reverse_letter_decrypt(char):
        if char.isalpha():
            if 'a' <= char <= 'z':  
                return chr(187 - ord(char))  
            elif 'A' <= char <= 'Z':  
                return chr(219 - ord(char))  
        return char

    if len(encrypted_password) < 2:
        return "Error: Encrypted password is too short."

  
    encrypted_password = encrypted_password[:-1]

    decrypted_password = ''.join(mapping_digits_reverse[char] if char in mapping_digits_reverse else reverse_letter_decrypt(char) for char in encrypted_password)

    decrypted_password += random.choice(special_chars)
    
    return decrypted_password



password = input("Enter your password to encrypt (minimum 8 characters): ")
encrypted = surprise_mirror_encrypt(password)
print(f"Encrypted: {encrypted}")

decrypted = surprise_mirror_decrypt(encrypted)
print(f"Decrypted (with new random special character): {decrypted}")
