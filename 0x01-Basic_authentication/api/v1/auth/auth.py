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
        if path is None:
            return True
        if excluded_paths is None || not excluded_paths:
            return True
        if path is in excluded_paths:
            return False
        """n_path = path.rstrip('/')
        n_excluded_path = [ex_p.rstrip('/') for ex_p in excluded_paths]

        if n_path in n_excluded_path:
            return False"""
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
