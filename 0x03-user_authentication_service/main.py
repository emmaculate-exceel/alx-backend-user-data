#!/usr/bin/env python3
"""11;rgb:0707/0000/0000
Main module
"""

import requests


EMAIL = "guillaume@holberton.io"
PASSWD = 'b4l0u'
NEW_PASSWD = 't4rt1fl3tt3'


def register_user(email: str, password: str) -> None:
    """register users function
    """
    response = request.post("http://myserver.com/register",
                            data={'email': email, 'password': password})
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """logging in the wrong way
    """
    response = request.post

if __name__ == '__main__':
        register_user(EMAIL, PASSWD)
        log_in_wrong_password(EMAIL, NEW_PASSWD)
        profile_unlogged()
        session_id = log_in(EMAIL, NEW_PASSWD)
        profile_logged(session_id)
        log_out(session_id)
        reset_token = reset_password_token(EMAIL)
        update_password(EMAIL, reset_token, NEW_PASSWD)
        log_in(EMAIL, NEW_PASSWD)
