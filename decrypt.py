import cv2
import os
import string
import numpy as np
import hashlib

def decrypt_message():
    # Read the encrypted image
    image_path = input("Enter the encrypted image path (must be PNG): ")
        
    img = cv2.imread(image_path)

    # Create ASCII mapping
    c = {i: chr(i) for i in range(255)}
    
    # Get password and create hash
    password = input("Enter passcode for decryption: ")
    input_password_hash = hashlib.md5(password.encode()).digest()[:8]
    
    # Read message length from the image
    height = img.shape[0] - 1
    msg_length = img[height, 0, 0]
    
    try:
        # First extract the stored password hash
        n = msg_length
        m = msg_length
        z = msg_length % 3
        stored_password_hash = bytearray()
        
        for i in range(8):
            stored_password_hash.append(img[n, m, z])
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        
        # Verify password
        if stored_password_hash != input_password_hash:
            print("Error: Incorrect password!")
            return
        
        # If password is correct, extract message
        message = ""
        n, m, z = 0, 0, 0
        
        for i in range(msg_length):
            message += c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
            
        print("Decrypted message:", message)
        
    except Exception as e:
        print("Error: Failed to decrypt. The image might be corrupted or not properly encrypted.")
        print("Make sure you're using the PNG file created by the encryption process.")

if __name__ == "__main__":
    decrypt_message()
