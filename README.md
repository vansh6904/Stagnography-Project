Image Steganography System
A secure Python-based steganography system for hiding secret messages in images with password protection.
Overview
This system allows users to:

Hide text messages within images
Protect hidden messages with passwords
Extract hidden messages using the correct password
Support both PNG and JPG input images

Requirements

Python 3.x
OpenCV (cv2)
NumPy
hashlib (included in Python standard library)

Installation

Install required packages:

bashCopypip install opencv-python numpy
File 
encrypt.py: Script for hiding messages in images
decrypt.py: Script for extracting hidden messages
README.md: This documentation file

Usage
Encryption

Run the encryption script:

bashCopypython encrypt.py

Follow the prompts:

Enter the path to your image file (JPG or PNG)
Type your secret message
Enter a password for protection


The script will create an encrypted image named encrypted_image.png

Decryption

Run the decryption script:

bashCopypython decrypt.py

Follow the prompts:

Enter the path to the encrypted image (must be PNG)
Enter the password


If the password is correct, the hidden message will be displayed

Important Notes

Always use PNG format for encrypted images to prevent data loss
The input image must be large enough to store your message
Keep your password secure - it cannot be recovered if lost
The encrypted image will look identical to the original
Don't compress or edit the encrypted image as it will corrupt the hidden message

Example
pythonCopy# Example usage for encryption
Enter the image path (jpg/png): my_image.jpg
Enter secret message: This is a secret message
Enter a passcode: mypassword123

# Example usage for decryption
Enter the encrypted image path (must be PNG): encrypted_image.png
Enter passcode for decryption: mypassword123
Decrypted message: This is a secret message
