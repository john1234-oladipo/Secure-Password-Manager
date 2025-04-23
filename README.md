# Secure Password Manager

![Security](https://img.shields.io/badge/security-encrypted-blue)
![Python](https://img.shields.io/badge/python-3.6%2B-green)

A simple yet secure password manager that stores and encrypts passwords locally, helping users maintain unique, strong passwords for each account.

## Features

- 🔒 AES-256 encryption for password storage
- 📝 Store usernames and passwords for multiple services
- 🛡️ Master password protection
- 🔄 Automatic encryption/decryption of stored data
- 🎲 Strong password generator
- 📋 List all stored services
- 🗑️ Delete password entries
- 💻 Command-line interface

## Why Use This?

- Never reuse passwords across sites again
- Generate and store strong, unique passwords
- Your data never leaves your computer
- Simple and easy to use
- No internet connection required

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/secure-password-manager.git
   cd secure-password-manager
   ```
2.  Install required dependencies:
    ```bash
     pip install cryptography
    ```
3.  Run the password manager:
    ```bash
     python password_manager.py
    ```

## Usage
When you run the program, you'll be prompted to enter a master password. This password will be used to encrypt all your stored passwords, so choose a strong one and don't forget it!

## Main Menu Options:
1.  Add new password
  Store a new password for a service. You can either enter your own password or have the manager generate a strong one for you.
2.  Retrieve password
  View a stored password by entering the service name.
3.  Generate strong password
  Generate a random, strong password without storing it.
4.  List all services
  View all services for which you have stored passwords.
5.  Delete password
  Remove a stored password.
6.  Exit
  Quit the password manager.

## Security Notes
- The master password is never stored anywhere. If you forget it, you won't be able to access your passwords.
- All passwords are encrypted before being saved to disk.
- For maximum security:
   - Choose a long, complex master password
   - Don't share your master password
   - Keep your computer secure
- The encrypted password file (passwords.enc) should be kept in a secure location.

## Limitations
- This is a local password manager with no cloud sync functionality
- No browser integration (you'll need to copy/paste passwords)
- For production use, consider more robust key derivation (like PBKDF2)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT

## Key Features
1. **Strong Encryption**: Uses AES-256 encryption via the `cryptography` library
2. **Master Password Protection**: All data is encrypted with a master password
3. **Password Generation**: Built-in strong password generator
4. **Local Storage**: Passwords are stored only on your local machine
5. **Simple Interface**: Easy-to-use command-line interface
6. **Complete Documentation**: Detailed README with usage instructions and security notes

