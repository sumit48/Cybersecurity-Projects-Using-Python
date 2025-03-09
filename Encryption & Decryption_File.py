import os
from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'.")

# Function to load the saved key
def load_key():
    if not os.path.exists("secret.key"):
        print("No key found! Generating a new key...")
        generate_key()
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Function to encrypt a message
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# Main function
def main():
    key = load_key()  # Load or generate key

    while True:
        print("\n1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter message to encrypt: ")
            encrypted_msg = encrypt_message(message, key)
            print(f"Encrypted Message: {encrypted_msg.decode()}")

        elif choice == "2":
            encrypted_msg = input("Enter encrypted message: ").encode()
            try:
                decrypted_msg = decrypt_message(encrypted_msg, key)
                print(f"Decrypted Message: {decrypted_msg}")
            except:
                print("Invalid decryption key or message!")

        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please choose again.")

# Run the program
if __name__ == "__main__":
    main()
