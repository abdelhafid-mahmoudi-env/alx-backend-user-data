#!/usr/bin/env python3
"""Filtered Logger Module"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        x = f'{field}=[^{separator}]*'
        y = f'{field}={redaction}'
        message = re.sub(x, y, message)
    return message
