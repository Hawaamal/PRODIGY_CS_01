def encrypt_text(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(text, shift):
    return encrypt_text(text, -shift)

def main():
    # Custom ASCII Art for POTTA header
    print(r"""
      ██████╗  ██████╗ ████████╗████████╗ █████╗  
      ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔══██╗
      ██████╔╝██║   ██║   ██║      ██║   ███████║  
      ██╔═══╝ ██║   ██║   ██║      ██║   ██╔══██║     
      ██║     ╚██████╔╝   ██║      ██║   ██║  ██║
      ╚═╝      ╚═════╝    ╚═╝      ╚═╝   ╚═╝  ╚═╝  
      
                     Caesar Cipher Encryption Tool
    """)

    print("Welcome to POTTA - Caesar Cipher Encryption & Decryption Tool")
    print("=" * 60)
    
    choice = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice! Please select 'e' for encryption or 'd' for decryption.")
        return
    
    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return
    
    print("=" * 60)
    
    if choice == 'e':
        encrypted_message = encrypt_text(message, shift)
        print(f"\n🔒 Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt_text(message, shift)
        print(f"\n🔓 Decrypted Message: {decrypted_message}")
    
    print("=" * 60)
    print("Thank you for using POTTA!")

if __name__ == "__main__":
    main()
