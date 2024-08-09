#!/usr/bin/env python3
""" an authication code that checks sessions
    and authenticate users
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    an authentication object
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        required authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorized header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        user authentication
        """
        return None
