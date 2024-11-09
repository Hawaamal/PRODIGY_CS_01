# PRODIGY_CS_01
POTTA Tool: A Caesar Cipher Encryption & Decryption Tool
POTTA is a command-line tool designed to encrypt and decrypt messages using the Caesar Cipher algorithm. It allows users to securely transform their text by shifting the letters of the alphabet by a specified value. This tool is ideal for learning and experimenting with basic encryption techniques.

**Features:**
Encryption: Encrypts a message by shifting each letter of the text by a specified number of positions in the alphabet.
Decryption: Reverses the encryption process, retrieving the original message by shifting the letters back by the same amount.
Flexible Shift Values: Users can choose any integer as a shift value, allowing for a variety of encryption possibilities.
Support for Both Uppercase and Lowercase: The tool works with both uppercase and lowercase letters, maintaining case sensitivity.
Handles Non-Alphabetic Characters: Non-alphabetic characters like spaces, punctuation, and numbers are preserved during encryption and decryption.

........**How the Tool Works:**............
Encryption:
For each letter in the message, the tool shifts the letter forward by the specified number of positions (shift value). 
For example, with a shift of 3, the letter A becomes D, B becomes E, and so on.
If the letter is a lowercase or uppercase letter, the shift respects its case (uppercase stays uppercase, lowercase stays lowercase).
Non-alphabetic characters (spaces, punctuation, etc.) are not modified.
Decryption:
The decryption process is simply the reverse of encryption. It shifts the letters backward by the specified number of positions to retrieve the original text.

...........**How to Run POTTA:**..........

Step 1: Install Python
Ensure you have Python installed on your system. You can check if Python is installed by running the following command in your terminal:

python3 --version


Step 2: Save the Code
Save the provided POTTA code in a Python file, for example, POTTA.py.

Step 3: Open Terminal or Command Prompt
Navigate to the folder where you saved the file using the terminal or command prompt.

Step 4: Run the Tool
Execute the script by typing the following command in the terminal:

python3 POTTA.py
Once you run the command, the tool will display the header and prompt you for the necessary inputs.

Step 5: Use the Tool
Choose Encryption or Decryption: After running the program, you will be asked whether you want to encrypt or decrypt a message. You can type e for encryption or d for decryption.

Enter the Message: After choosing the encryption or decryption option, you'll be asked to input the message you want to encrypt or decrypt.

Enter the Shift Value: You will then be asked to provide a shift value (an integer). For example, if you choose 3, then each letter in your message will be shifted 3 positions forward (for encryption) or backward (for decryption).

View the Output: After providing the message and shift value, the program will display the encrypted or decrypted message.


................**Example Usage**................

Here’s an example of how to use the tool:

Encrypting a Message:
Do you want to encrypt or decrypt the message? (e/d): e
Enter the message: Hello, World!
Enter the shift value: 3
Encrypted Message: Khoor, Zruog!

Decrypting a Message:
Do you want to encrypt or decrypt the message? (e/d): d
Enter the message: Khoor, Zruog!
Enter the shift value: 3
Decrypted Message: Hello, World!
This TOOL is straightforward and user-friendly. 






