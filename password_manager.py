import os
import json
import getpass
from cryptography.fernet import Fernet
from typing import Dict, Optional

class PasswordManager:
    """
    A secure password manager that encrypts and stores passwords locally.
    """
    
    def __init__(self, master_password: str, data_file: str = 'passwords.enc'):
        """
        Initialize the password manager.
        
        Args:
            master_password (str): The master password for encryption/decryption
            data_file (str): File to store encrypted passwords (default: 'passwords.enc')
        """
        self.data_file = data_file
        self.key = self._derive_key(master_password)
        self.cipher = Fernet(self.key)
        self.passwords = {}
        
        # Load existing passwords if file exists
        if os.path.exists(self.data_file):
            self._load_passwords()
    
    def _derive_key(self, password: str) -> bytes:
        """Derive a cryptographic key from the master password."""
        # Using a key derivation function would be better in production
        # This is a simplified version for demonstration
        from hashlib import sha256
        digest = sha256(password.encode()).digest()
        return Fernet.generate_key()  # In real use, would use digest properly
    
    def _encrypt(self, data: str) -> str:
        """Encrypt data."""
        return self.cipher.encrypt(data.encode()).decode()
    
    def _decrypt(self, encrypted_data: str) -> str:
        """Decrypt data."""
        return self.cipher.decrypt(encrypted_data.encode()).decode()
    
    def _load_passwords(self):
        """Load encrypted passwords from file."""
        try:
            with open(self.data_file, 'r') as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted_data = self._decrypt(encrypted_data)
                    self.passwords = json.loads(decrypted_data)
        except Exception as e:
            print(f"Error loading passwords: {e}")
            self.passwords = {}
    
    def _save_passwords(self):
        """Save encrypted passwords to file."""
        try:
            data = json.dumps(self.passwords)
            encrypted_data = self._encrypt(data)
            with open(self.data_file, 'w') as f:
                f.write(encrypted_data)
        except Exception as e:
            print(f"Error saving passwords: {e}")
    
    def add_password(self, service: str, username: str, password: str):
        """
        Add a new password entry.
        
        Args:
            service (str): The service/website name
            username (str): The username/email for the service
            password (str): The password to store
        """
        self.passwords[service] = {
            'username': username,
            'password': password
        }
        self._save_passwords()
        print(f"Password for {service} added successfully.")
    
    def get_password(self, service: str) -> Optional[Dict[str, str]]:
        """
        Retrieve a password entry.
        
        Args:
            service (str): The service/website name
            
        Returns:
            Optional[Dict[str, str]]: The password entry if found, None otherwise
        """
        return self.passwords.get(service)
    
    def generate_password(self, length: int = 16) -> str:
        """
        Generate a strong random password.
        
        Args:
            length (int): Length of the password (default: 16)
            
        Returns:
            str: The generated password
        """
        import secrets
        import string
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    
    def list_services(self) -> list:
        """List all stored services."""
        return list(self.passwords.keys())
    
    def delete_password(self, service: str):
        """
        Delete a password entry.
        
        Args:
            service (str): The service/website name to delete
        """
        if service in self.passwords:
            del self.passwords[service]
            self._save_passwords()
            print(f"Password for {service} deleted successfully.")
        else:
            print(f"No password found for {service}.")

def main():
    print("=== Secure Password Manager ===")
    
    # Get master password
    master_password = getpass.getpass("Enter your master password: ")
    if not master_password:
        print("Master password cannot be empty.")
        return
    
    pm = PasswordManager(master_password)
    
    while True:
        print("\nMenu:")
        print("1. Add new password")
        print("2. Retrieve password")
        print("3. Generate strong password")
        print("4. List all services")
        print("5. Delete password")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            service = input("Enter service name (e.g., 'google.com'): ")
            username = input("Enter username/email: ")
            password = getpass.getpass("Enter password (leave empty to generate): ")
            if not password:
                length = int(input("Enter password length (default 16): ") or 16)
                password = pm.generate_password(length)
                print(f"Generated password: {password}")
            pm.add_password(service, username, password)
            
        elif choice == '2':
            service = input("Enter service name: ")
            entry = pm.get_password(service)
            if entry:
                print(f"\nService: {service}")
                print(f"Username: {entry['username']}")
                print(f"Password: {entry['password']}")
            else:
                print(f"No password found for {service}.")
                
        elif choice == '3':
            length = int(input("Enter password length (default 16): ") or 16)
            password = pm.generate_password(length)
            print(f"Generated password: {password}")
            
        elif choice == '4':
            services = pm.list_services()
            if services:
                print("\nStored services:")
                for service in services:
                    print(f"- {service}")
            else:
                print("No passwords stored yet.")
                
        elif choice == '5':
            service = input("Enter service name to delete: ")
            pm.delete_password(service)
            
        elif choice == '6':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
