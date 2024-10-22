import jwt
import datetime
from global_var import config

# 定义密钥和算法
SECRET_KEY = config["jwt"]["secret_key"]
ALGORITHM = 'HS256'

def create_jwt(user_id):
    # 设置过期时间
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    
    # 构建 payload
    payload = {
        'user_id': user_id,
        'exp': expiration  # 过期时间
    }
    
    # 生成 token
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return token

def verify_jwt(token):
    try:
        # 验证 token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # 成功，返回解码后的 payload
    except jwt.ExpiredSignatureError:
        # 处理 token 过期的情况
        return None
    except jwt.InvalidTokenError:
        # 处理无效 token 的情况
        return None
