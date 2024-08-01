# Personal Data Handling

This project demonstrates how to handle personal data securely in Python. It includes functionalities for filtering sensitive information in log messages, setting up secure logging, connecting to a database using environment variables, and encrypting passwords.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Description

The project includes several functionalities related to handling personal data securely:
- Filtering and obfuscating personally identifiable information (PII) in log messages.
- Setting up a logger with a custom formatter that filters PII.
- Connecting to a MySQL database using credentials stored in environment variables.
- Encrypting and validating passwords using bcrypt.

## Features

- **Filter PII in Logs:** Obfuscates specified fields in log messages to protect sensitive information.
- **Secure Logging:** Custom logger setup with a formatter that filters out PII.
- **Database Connection:** Securely connects to a MySQL database using environment variables.
- **Password Encryption:** Encrypts passwords and validates them securely using bcrypt.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/alx-backend-user-data.git
    cd alx-backend-user-data
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**
    ```bash
    export PERSONAL_DATA_DB_USERNAME='your_username'
    export PERSONAL_DATA_DB_PASSWORD='your_password'
    export PERSONAL_DATA_DB_HOST='your_host'
    export PERSONAL_DATA_DB_NAME='your_database'
    ```

## Usage

1. **Run the main script:**
    ```bash
    python3 filtered_logger.py
    ```

2. **Example for filtering logs:**
    ```python
    from filtered_logger import filter_datum

    fields = ["password", "email"]
    message = "name=John Doe; email=john@example.com; password=12345;"
    print(filter_datum(fields, "XXX", message, ";"))
    ```

3. **Example for setting up and using the logger:**
    ```python
    import logging
    from filtered_logger import get_logger

    logger = get_logger()
    logger.info("name=John Doe; email=john@example.com; password=12345;")
    ```

## File Structure
alx-backend-user-data/
│
├── filtered_logger.py # Main module with filtering and logging functionalities
├── encrypt_password.py # Module for password encryption and validation
├── main.py # Script for testing the functionalities
├── requirements.txt # Required packages
└── README.md # Project documentation


## Examples

### Filtering Log Messages

```python
from filtered_logger import filter_datum

fields = ["password", "email"]
message = "name=John Doe; email=john@example.com; password=12345;"
filtered_message = filter_datum(fields, "XXX", message, ";")
print(filtered_message)
