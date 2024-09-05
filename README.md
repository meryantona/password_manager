# Password Manager

This Streamlit app allows you to manage passwords with encryption. You can add, retrieve, and remove passwords securely.

`[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)`

## Installation

1. Clone the repository

   ```bash
   git clone https://github.com/meryantona/password_manager.git
   cd password-manager
   ```

2. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Creating the Encryption Key

Before running the app, you need to create an encryption key file. This key is used to encrypt and decrypt your passwords.

2. **Run the generate_encryption_key.py script** using the following command:

```bash
python generate_encryption_key.py
```

This will create a new file named `encryption_key.txt` in your project directory. 

2. **Verify that the encryption key file has been created**. You should see a new file named `encryption_key.txt` in your project directory.

```bash
echo "your-generated-key-here" > encryption_key.txt`
```

3. **Keep this file safe and secure**. 

Anyone who has access to this file can decrypt your passwords. Make sure to back it up and store it securely. 

Once you have created the encryption key file, you can run your password manager app using Streamlit. 

**Important:** This step is **mandatory** for running the password manager app.Generate encryption key before running the app. Without the key, the app will not function.

## Usage

1. Run the Streamlit app:
 
```bash
streamlit run password_manager.py`
```

2. Open your web browser and go to `http://localhost:8501`. 
3. Use the interface to add, retrieve, or remove passwords.

## Features

- **Add Password**: Save a website name and password.
- **Retrieve Password**: Retrieve and decrypt a saved password.
- **Remove Password**: Delete a saved password from the database.

## Security Recommendations

- **Encryption Key**: Store your encryption key securely. Do not hard-code it in your script.
- **Secure Storage**: Use encrypted storage for the credentials file.
- **Environment**: Run this application in a secure environment and restrict access.

## Explanation

This app demonstrates the basics of password management and encryption using Python and Streamlit. It uses the `cryptography` library to encrypt and decrypt passwords securely. Passwords are stored in a CSV file in encrypted form.

The main functionalities are:

- **Encryption**: Passwords are encrypted before being saved.
- **Decryption**: Encrypted passwords are decrypted when retrieved.
- **Storage**: Passwords are stored in a CSV file with encryption.
- **User Interface**: The app uses Streamlit for a user-friendly web interface.

## Notes

- **Development and Testing**: This script is intended for educational purposes. For production use, consider more robust and secure storage solutions.
- **Backup**: Always backup your encryption key and credentials file securely.
- **Updates**: Regularly update dependencies to the latest versions to ensure security patches are applied.

## Adding .gitignore

To ensure sensitive files like your encryption key and credentials are not committed to your repository, create a `.gitignore` file in the root of your project directory with the following content:

### .gitignore

`encryption_key.txt credentials.csv`

This will prevent Git from tracking and committing these files.