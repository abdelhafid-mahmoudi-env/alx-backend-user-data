# Personal Data Management

## Overview

This project involves handling personal data securely and efficiently. It includes logging sensitive information with obfuscation, connecting to a secure database, and encrypting user passwords. The primary goal is to ensure the privacy and security of Personally Identifiable Information (PII) while maintaining data accessibility for authorized use.

## Features

1. **Regex-ing**: Function to obfuscate specific fields in log messages.
2. **Log Formatter**: Custom log formatter to filter and obfuscate sensitive information in logs.
3. **Logger Configuration**: Configured logger that handles and formats sensitive user data logs.
4. **Secure Database Connection**: Function to securely connect to a MySQL database using environment variables.
5. **Data Retrieval and Logging**: Main function to retrieve user data from the database and log it securely.
6. **Password Encryption**: Function to hash passwords using bcrypt.
7. **Password Validation**: Function to validate passwords against hashed passwords.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/alx-backend-user-data.git
    cd alx-backend-user-data/0x00-personal_data
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    ```sh
    export PERSONAL_DATA_DB_USERNAME='your_db_username'
    export PERSONAL_DATA_DB_PASSWORD='your_db_password'
    export PERSONAL_DATA_DB_HOST='your_db_host'
    export PERSONAL_DATA_DB_NAME='your_db_name'
    ```

## Usage

1. **Filter Datum Function**:
    ```sh
    ./main.py
    ```

2. **Log Formatter**:
    ```sh
    ./main.py
    ```

3. **Logger Configuration**:
    ```sh
    ./main.py
    ```

4. **Secure Database Connection**:
    ```sh
    ./main.py
    ```

5. **Data Retrieval and Logging**:
    ```sh
    ./filtered_logger.py
    ```

6. **Password Encryption and Validation**:
    ```sh
    ./main.py
    ```

## Learning Objectives

At the end of this project, you should be able to:
- Identify examples of Personally Identifiable Information (PII).
- Implement a log filter that obfuscates PII fields.
- Encrypt a password and check the validity of an input password.
- Authenticate to a database using environment variables.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- `pycodestyle` 2.5
- `mysql-connector-python`
- `bcrypt`

## Contributors

- **Abdelhafid Mahmoudi** - [Abdelhafid Mahmoudi](https://github.com/abdelhafid-mahmoudi-env.git)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
