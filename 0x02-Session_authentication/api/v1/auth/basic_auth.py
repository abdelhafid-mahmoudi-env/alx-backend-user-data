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
        """Extracts the Base64-encoded token"""
        if isinstance(authorization_header, str):
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Decodes a Base64-encoded authorization."""
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
        """Extracts user credentials from"""
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
        """Retrieves a User object based"""
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            pass
