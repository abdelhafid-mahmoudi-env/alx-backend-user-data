#!/usr/bin/env python3
"""User authentication features."""
import logging
from flask import Flask, abort, jsonify, redirect, request
from auth import Auth

logging.disable(logging.WARNING)


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """containing a welcome message."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """containing various information."""
    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """form containing login info."""
    email, password = request.form.get("email"), request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    sess_id = AUTH.create_session(email)
    platform = jsonify({"email": email, "message": "logged in"})
    platform.set_cookie("session_id", sess_id)
    return platform


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """A redirect if successful"""
    sess_id = request.cookies.get("session_id")
    myuser = AUTH.get_user_from_session_id(sess_id)
    if myuser is None:
        abort(403)
    AUTH.destroy_session(myuser.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """containing the email if successful."""
    sess_id = request.cookies.get("session_id")
    myuser = AUTH.get_user_from_session_id(sess_id)
    if myuser is None:
        abort(403)
    return jsonify({"email": myuser.email})


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """the email & reset token if successful."""
    email = request.form.get("email")
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "reset_token": token})


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """The user's updated password."""
    email = request.form.get("email")
    token = request.form.get("reset_token")
    new_pass = request.form.get("new_password")
    try:
        AUTH.update_password(token, new_pass)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
