# PasswordSecure

This repository is designed to help you check whether your passwords have been hacked or leaked on the web. It uses various security-related APIs and databases to determine whether a password has been exposed in any data breaches. The process involves sending the password through a secure connection and checking hashes against previously compromised ones stored in the database.

## Motivation

The Password Checker Repository is developed to help enhance the security of passwords by notifying users if any of their passwords have ever been compromised. As passwords are widely used for accessing various services and personal information, it is critical to have secure passwords that are resistant to hacking. By using an open-source password checker, users can identify and fix vulnerable passwords before any data breaches occur.

## Features

The Password Checker repository has the following features:

- Checks whether your password is vulnerable to a dictionary attack
- It scans for weak passwords to provide an accurate estimation of your passwords' strength
- It checks your password against a vast database of compromised passwords to suggest better alternatives.
- Contributes towards safer password management habits by promoting the usage of unique and secure passwords.
- Easy plug and play functionality in any web application.

## Installation

1. Clone or fork this repository to your local environment.
2. Install the required dependencies in your system using pip: pip install -r requirements.txt
3. Import the checker module in your Python project and create an instance of the PasswordChecker class.
4. Set up the API keys, if applicable, and configure the settings in the config.py and .env files
5. Use the is_secure() function to check whether the password is secure, and use the get_all_data() function to retrieve all data related to password security.

## Usage

To use the Password Checker, follow these steps:

1. First, define the password that you want to check.
2. Create an instance of the PasswordChecker class.
3. Use the is_secure() function to check whether the password is secure.
4. Use the get_all_data() function to retrieve all data related to password security.
