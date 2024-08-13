#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, request, jsonify, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()

@app.route('/', methods=['GET'])
def index():
    """Home route"""
    return jsonify(message="Bienvenue")


@app.route('/sessions', methods=['POST'])
def login():
    """Log in a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(400, description="Missing email or password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify(email=email, message="logged in")
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['POST'])
def login():
    """Log in a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(400, description="Missing email or password")
    
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify(email=email, message="logged in")
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)

@app.route('/sessions', methods=['DELETE'])
def logout():
    """Log out a user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        response = jsonify(message="logout successful")
        response.delete_cookie("session_id")
        return response
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """Get user profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify(email=user.email)
    else:
        abort(403)


@app.route('/users', methods=['POST'])
def register_user():
    """Register a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(400, description="Missing email or password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify(email=user.email, message="user created")
    except ValueError as e:
        return jsonify(message=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
