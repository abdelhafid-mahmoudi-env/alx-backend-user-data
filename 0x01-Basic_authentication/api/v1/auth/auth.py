#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

User = TypeVar('User')

class Auth:
    """ Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required for a given path.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request.
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """ Returns the current user based on the request.
        """
        return None
