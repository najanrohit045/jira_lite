from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from flask import jsonify

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            print("🔍 Checking JWT...")
            verify_jwt_in_request()

            user = get_jwt_identity()
            print("✅ USER ID:", user)

            return f(*args, **kwargs)

        except Exception as e:
            print("❌ ERROR:", e)   # 👈 THIS IS KEY
            return jsonify({"message": "Unauthorized"}), 401

    return wrapper