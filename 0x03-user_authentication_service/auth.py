#!/usr/bin/env python3
"""Authentication system management"""
import logging
from typing import Union
from uuid import uuid4
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User

logging.disable(logging.WARNING)


def _hash_password(password: str) -> bytes:
    """The hashed password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a new UUID as a string."""
    return str(uuid4())


class Auth:
    """This class handles user registration, login, session creation."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hash = _hash_password(password)
        myuser = self._db.add_user(email, hash)
        return myuser

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a user's login credentials."""
        try:
            myuser = self._db.find_user_by(email=email)
            if myuser is not None:
                passwordbytes = password.encode('utf-8')
                hash = myuser.hashed_password
                if bcrypt.checkpw(passwordbytes, hash):
                    return True
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """Creates a session and returns the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        if user is None:
            return None
        sess_id = _generate_uuid()
        self._db.update_user(user.id, session_id=sess_id)
        return sess_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Retrieve a User object from a session ID."""
        if session_id is None:
            return None
        try:
            myuser = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return myuser

    def destroy_session(self, user_id: int) -> None:
        """Method to destroy the session associated with a user"""
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generates a password reset token for a user."""
        try:
            myuser = self._db.find_user_by(email=email)
        except NoResultFound:
            myuser = None
        if myuser is None:
            raise ValueError()
        token = _generate_uuid()
        self._db.update_user(myuser.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates a user's password using a reset token."""
        try:
            myuser = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid reset token")
        new_hash = _hash_password(password)
        self._db.update_user(
            myuser.id,
            hashed_password=new_hash,
            reset_token=None,
        )
