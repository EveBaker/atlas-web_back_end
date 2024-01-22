#!/usr/bin/env python3
""" sesion auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login"""
    email = request.form.get('email')
    if not email:
       return make_response(jsonify({"error": "email missing"}), 400)
    password = request.form.get("password")
    if not password:
        return make_response(jsonify({"error": "password missing"}), 400)
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    session_id = auth.create_session(user.id)
    session_name = os.getenv('SESSION_NAME')
    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id)
    return response
