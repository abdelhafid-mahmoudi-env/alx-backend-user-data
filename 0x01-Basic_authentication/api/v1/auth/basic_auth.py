#!/usr/bin/env python3
"""Module for basic authentication in the API.
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Class for handling basic authentication.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extracts the Base64-encoded token from the Authorization header.
        
        Args:
            authorization_header (str): The Authorization header value.
        
        Returns:
            str: The Base64 token, or None if the header is invalid.
        """
        if isinstance(authorization_header, str):
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Decodes a Base64-encoded authorization header into a UTF-8 string.
        
        Args:
            base64_authorization_header (str): The Base64-encoded authorization header.
        
        Returns:
            str: The decoded string, or None if decoding fails.
        """
        if isinstance(base64_authorization_header, str):
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extracts user credentials from a Base64-decoded authorization header.
        
        Args:
            decoded_base64_authorization_header (str): The decoded authorization header.
        
        Returns:
            Tuple[str, str]: A tuple containing the username and password, or (None, None) if extraction fails.
        """
        if isinstance(decoded_base64_authorization_header, str):
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            field_match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
            )
            if field_match is not None:
                user = field_match.group('user')
                password = field_match.group('password')
                return user, password
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Retrieves a User object based on the provided credentials.
        
        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.
        
        Returns:
            User: The corresponding User object, or None if no user is found.
        """
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            # The implementation of this method depends on the specifics of your User model and database access.
            # For example:
            # return User.query.filter_by(email=user_email, password=user_pwd).first()
            pass
