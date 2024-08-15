#!/usr/bin/env python3
"""Module for simple end-to-end tests of the user."""
import requests
from app import AUTH


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """Sends a POST request to register a new user."""
    path = "{}/users".format(BASE_URL)
    content = {
        "email": email,
        "password": password
    }
    platform = requests.post(path, data=content)
    assert platform.status_code == 200
    assert platform.json() == {"email": email, "message": "user created"}
    platform = requests.post(path, data=content)
    assert platform.status_code == 400
    assert platform.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Sends a POST request to attempt login."""
    path = "{}/sessions".format(BASE_URL)
    content = {
        "email": email,
        "password": password
    }
    platform = requests.post(path, data=content)
    assert platform.status_code == 401


def profile_unlogged() -> None:
    """Sends a GET request to retrieve profile information."""
    path = "{}/profile".format(BASE_URL)
    platform = requests.get(path)
    assert platform.status_code == 403


def profile_logged(session_id: str) -> None:
    """Sends a GET request with a valid session ID to retrieve."""
    path = "{}/profile".format(BASE_URL)
    cookies = {
        "session_id": session_id
    }
    platform = requests.get(path, cookies=cookies)
    assert platform.status_code == 200
    payload = platform.json()
    assert "email" in payload
    user = AUTH.get_user_from_session_id(session_id)
    assert user.email == payload["email"]


def log_out(session_id: str) -> None:
    """Sends a DELETE request with a valid session ID to log out."""
    path = "{}/sessions".format(BASE_URL)
    headers = {
        "Content-Type": "application/json"
    }
    content = {
        "session_id": session_id
    }
    platform = requests.delete(path, headers=headers, cookies=content)
    assert platform.status_code == 200


def reset_password_token(email: str) -> str:
    """Sends a POST request a password reset token."""
    path = "{}/reset_password".format(BASE_URL)
    content = {
        "email": email
    }
    platform = requests.post(path, data=content)
    assert platform.status_code == 200
    assert "email" in platform.json()
    assert platform.json()["email"] == email
    reset_token = platform.json()["reset_token"]
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Sends a PUT request with the email, reset token, and new password."""
    path = "{}/reset_password".format(BASE_URL)
    content = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    platform = requests.put(path, data=content)
    assert platform.status_code == 200
    assert platform.json()["message"] == "Password updated"
    assert platform.json()["email"] == email


def log_in(email: str, password: str) -> str:
    """Sends a POST request with the user's email and password to log in."""
    path = "{}/sessions".format(BASE_URL)
    content = {
        "email": email,
        "password": password
    }
    platform = requests.post(path, data=content)
    if platform.status_code == 401:
        return "Invalid credentials"
    assert platform.status_code == 200
    platform_json = platform.json()
    assert "email" in platform_json
    assert "message" in platform_json
    assert platform_json["email"] == email
    return platform.cookies.get("session_id")


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    sess_id = log_in(EMAIL, PASSWD)
    profile_logged(sess_id)
    log_out(sess_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
