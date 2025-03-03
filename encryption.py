import random

def surprise_mirror_encrypt():
    password = input("Enter your password (minimum 8 characters): ")
    
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
        print("Error: Password must be at least 8 characters long.")
        return
    
    encrypted_password = ''.join(mapping_digits[char] if char in mapping_digits else reverse_letter(char) for char in password)
    
    
    encrypted_password += random.choice(special_chars)
    
    print(f"Surprise Mirror Encryption: {encrypted_password}")

surprise_mirror_encrypt()
