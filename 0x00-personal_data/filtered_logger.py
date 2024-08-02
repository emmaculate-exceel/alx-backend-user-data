#!/usr/bin/env python3
""" user logging details """
import logging
import re


def filter_datum(fields, redaction, message, separator):
    """ a function that returns logging info """
    fields =
    redaction =
    message =
    seperator = 
    return re.sub(


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname0s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"


    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
      
        
def main:
    return get_db
