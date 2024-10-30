import bcrypt
from flask import Blueprint, request, current_app
from sqlalchemy import or_
from global_var import db
from entity.Customer import Customer
from entity.Manager import Manager
from flask_jwt_extended import create_access_token

authentication_bp = Blueprint('authentication', __name__)

def hash_password(plain_password):
    # 生成盐值并将密码进行哈希
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def check_password(plain_password, hashed_password):
    # 如果 plain_password 是 str 类型，先转换为 bytes
    if isinstance(plain_password, str):
        plain_password = plain_password.encode('utf-8')

    # 如果 hashed_password 是 str 类型，转换为 bytes
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')

    # 使用 bcrypt 检查密码
    return bcrypt.checkpw(plain_password, hashed_password)


def is_exist(sheet, phone, email):
	res = sheet.query.filter(or_(sheet.phone == phone, sheet.email == email)).first()
	return res is not None

def authentication(sheet, username, password, phone, email):
	res = sheet.query.filter(sheet.name == username, sheet.phone == phone, sheet.email == email).first()
	if res is None:
		return None
	if not check_password(password, res.password):
		return None
	return res

def customer_register(username, password, phone, email):
	if is_exist(Customer, phone, email):
		return False
	customer = Customer(name=username, password=password, phone=phone, email=email)
	db.session.add(customer)
	db.session.commit()
	return True


@authentication_bp.route('/login', methods=['POST'])
def login():
	type = request.json['type']
	username = request.json['username']
	password = request.json['password']
	phone = request.json['phone']
	email = request.json['email']
 
	current_app.logger.info('Login request: %s', request.json)
	print(request.json)
 
	if type == '顾客':
		sheet = Customer
	elif type == '管理员':
		sheet = Manager
	user = authentication(sheet, username, password, phone, email)
	if user is not None:
		return {
			"message": "Login successfully",
   			"token": create_access_token(identity=user.get_id(),  additional_claims={"user_type": type}),
			"user" : {
				"username": user.name,
				"phone": user.phone,
				"email": user.email}
		}
	else:
		return {
			"message": "Login failed",
   			"token": "none"
		}
 
@authentication_bp.route('/register', methods=['POST'])
def register():
	username = request.json['username']
	password = hash_password(request.json['password'])
	phone = request.json['phone']
	email = request.json['email']

	if customer_register(username, password, phone, email):
		return {
			"message": "Register successfully"
		}
	else:
		return {
			"message": "Register failed"
		}