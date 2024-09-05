#!/usr/bin/env python3

import streamlit as st
import csv
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import os

# Function to read the encryption key from a file
def load_encryption_key():
    try:
        with open('encryption_key.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        st.error("Encryption key file not found!")
        return None

# Load the encryption key
CUSTOM_ENCRYPTION_KEY = load_encryption_key()
if CUSTOM_ENCRYPTION_KEY is None:
    st.stop()

# Function to encrypt password
def encrypt_password(password):
    cipher_suite = Fernet(CUSTOM_ENCRYPTION_KEY)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Function to decrypt password
def decrypt_password(encrypted_password):
    if isinstance(encrypted_password, bytes):
        try:
            cipher_suite = Fernet(CUSTOM_ENCRYPTION_KEY)
            decrypted_password = cipher_suite.decrypt(encrypted_password)
            return decrypted_password.decode()
        except InvalidToken:
            return "Invalid Token"
    else:
        return None

# Function to save website name and password to CSV file
def save_credentials(website_name, password):
    encrypted_password = encrypt_password(password)
    with open('credentials.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([website_name, encrypted_password.decode()])  # Ensure storing string representation

# Function to retrieve password from CSV file
def retrieve_password(website_name):
    with open('credentials.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == website_name:
                encrypted_password = row[1].encode()
                return encrypted_password
    return None

# Streamlit UI
st.title("Password Manager")

# Input fields for website name and password
website_name = st.text_input("Enter website name:")
password = st.text_input("Enter password:", type="password")

# Save button to save website name and password
if st.button("Save"):
    if website_name and password:
        save_credentials(website_name, password)
        st.success("Website name and password saved successfully.")
    else:
        st.error("Please fill in all fields.")

# Retrieve button to retrieve password
if st.checkbox("Retrieve Password"):
    if not os.path.exists('credentials.csv'):
        st.warning("Credentials file not created yet. Please add a password first.")
    else:
        website_name = st.selectbox("Select website name:", options=[""] + [row[0] for row in csv.reader(open('credentials.csv', 'r'))])
        key = st.text_input("Enter Your Encryption Key:", type="password")
        if st.button("Retrieve Password"):
            if key == CUSTOM_ENCRYPTION_KEY:
                if website_name:
                    encrypted_password = retrieve_password(website_name)
                    if encrypted_password:
                        decrypted_password = decrypt_password(encrypted_password)
                        st.success(f"Password for **{website_name}** -> **{decrypted_password}**")
                    else:
                        st.error("Password not found in database.")
            elif key == "":
                pass 
            else:
                st.error("Invalid Encryption Key!!!")

# Remove button to delete a website name and password
if st.checkbox("Remove Password"):
    if not os.path.exists('credentials.csv'):
        st.warning("Credentials file not created yet. Please add a password first.")
    else:
        website_name = st.selectbox("Select website name to remove:", options=[""] + [row[0] for row in csv.reader(open('credentials.csv', 'r'))])
        key = st.text_input("Enter Your Encryption Key for removal:", type="password")
        if st.button("Remove Password"):
            if key == CUSTOM_ENCRYPTION_KEY:
                if website_name:
                    # Read all rows except the one to be deleted
                    rows = []
                    with open('credentials.csv', 'r') as csvfile:
                        reader = csv.reader(csvfile)
                        for row in reader:
                            if row[0] != website_name:
                                rows.append(row)
                    
                    # Write the remaining rows back to the file
                    with open('credentials.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(rows)
                    
                    st.success(f"Password for **{website_name}** has been removed.")
                else:
                    st.error("Please select a website name to remove.")
            elif key == "":
                pass
            else:
                st.error("Invalid Encryption Key!!!")
