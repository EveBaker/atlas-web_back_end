#!/usr/bin/env python3
""" sesion auth views
"""
from api.v1.auth.auth import Auth
from flask import abort, jsonify, request
import uuid


class SessionAuth(Auth):
    """sessionAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        "creats a session"
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """retrieve the user ID associated with a given session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
