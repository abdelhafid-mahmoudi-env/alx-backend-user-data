#!/usr/bin/env python3
"""
Main file for testing
"""

from filtered_logger import filter_datum, RedactingFormatter, get_logger, get_db
from encrypt_password import hash_password, is_valid

# Testing filter_datum
fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

# Testing RedactingFormatter
import logging

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))

# Testing get_logger
print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))

# Testing get_db
db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()

# Testing main function
main()

# Testing hash_password and is_valid
password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))
