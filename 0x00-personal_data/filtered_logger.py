#!/usr/bin/env python3

""" Filtered logger """


import logging
import os
import re
from typing import List, Any, Union
import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor
from mysql.connector.cursor import MySQLCursor


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Replacing """

    for f in fields:
        message = re.sub(
            rf"{f}=(.*?)\{separator}",
            f'{f}={redaction}{separator}',
            message)
    return message


class RedactingFormatter(logging.Formatter):
    """ RedactingFormatter class. """

    REDACTION: str = "***"
    FORMAT: str = "[HOLBERTON] %(name)s %(levelname)s %\
(asctime)-15s: %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]) -> None:
        """ Initialization of class """

        self.fields: List[str] = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Formating method """

        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ A method that implements a logger """

    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger


def get_db() -> MySQLConnection:
    """ A method that implements db conectivity """

    psw: str = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    username: str = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    host: str = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name: str | None = os.environ.get('PERSONAL_DATA_DB_NAME')
    connection: MySQLConnection = mysql.connector.connect(
        host=host,
        database=db_name,
        user=username,
        password=psw)
    return connection


def main() -> None:
    """ A method that implements a main function """

    db: PooledMySQLConnection | MySQLConnection | CMySQLConnection = get_db()
    cursor: Any | MySQLCursor | CMySQLCursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = f"name={row[0]!r}; email={row[1]!r}; phone={row[2]!r}; " +\
            f"ssn={row[3]!r}; password={row[4]!r};ip={row[5]!r}; " +\
            f"last_login={row[6]!r}; user_agent={row[7]!r};"
        print(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
