#!/usr/bin/env python3
# an authication code the sessions

from flask import request


class Auth:
    """
    an authentication object
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ required authentication
        """
        pass


    def authorization_header(self, request=None) -> str:
        """ authorized header
        """
        pass


    def current_user(self, request=None) -> str:
        """ user authentication
        """
        pass
