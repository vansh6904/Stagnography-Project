import cv2
import os
import string
import numpy as np
import hashlib

def encrypt_message():
    # Read the image
    image_path = input("Enter the image path (jpg/png): ")
    img = cv2.imread(image_path)
    
    # Get message and password
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    # Create simple hash of password (using first 8 bytes only)
    password_hash = hashlib.md5(password.encode()).digest()[:8]
    
    # Create ASCII mapping
    d = {chr(i): i for i in range(255)}
    
    # Save message length and password for decryption
    msg_length = len(msg)
    
    # Embed message
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    # Store password hash in the next 8 pixels after message
    for i in range(8):
        img[n, m, z] = password_hash[i]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    # Save length in the last pixel
    height = img.shape[0] - 1
    img[height, 0, 0] = msg_length
    
    # Always save as PNG to preserve exact pixel values
    output_path = "encrypted_image.png"
    cv2.imwrite(output_path, img)
    print(f"Encrypted image saved as: {output_path}")
    print(f"Password for decryption: {password}")
    print("Note: Encrypted image is saved as PNG to preserve data integrity.")

    os.system(f"open {output_path}")

if __name__ == "__main__":
    encrypt_message()
