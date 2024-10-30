from global_var import config
from flask_jwt_extended import get_jwt

# 定义密钥和算法
SECRET_KEY = config["jwt"]["secret_key"]
ALGORITHM = 'HS256'


def verify_identify(type):
    claims = get_jwt()
    user_type = claims.get('user_type')

    if user_type != type:
        return False
    return True
