from functools import wraps
from global_var import config
from flask_jwt_extended import get_jwt
from flask import current_app, jsonify

# 定义密钥和算法
SECRET_KEY = config["jwt"]["secret_key"]
ALGORITHM = 'HS256'

def verify_identify(required_type):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            claims = get_jwt()
            user_type = claims.get('user_type')

            if user_type != required_type:
                current_app.logger.warning(f"Unauthorized access attempt by user type {user_type}. Required type: {required_type}.")
                return jsonify({"error": "Unauthorized access"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator