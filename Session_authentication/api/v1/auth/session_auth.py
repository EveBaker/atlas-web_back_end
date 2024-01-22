#!/usr/bin/env python3
""" sesion auth views
"""
from api.v1.auth.auth import Auth
from flask import abort, jsonify, request
import os


class SessionAuth(Auth):
    """sessionAuth"""
    pass