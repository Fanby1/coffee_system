import os
from flask import Blueprint, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from global_var import db
from entity.Order import Order
from entity.Product import Product
from util.jwt import verify_identify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/coffee'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

management_bp = Blueprint('management', __name__)

@management_bp.route('/get-all-orders', methods=['GET'])
@jwt_required()
def get_all_orders():
	verify_identify("管理员")
	orders = Order.query.all()
	res = [{"id": order.order_id, "customer_id": order.customer_id, "price": str(order.price), "status": order.status} for order in orders]
	return {
		"orders": res
	}
 
def change_order_status(order_id, status):
	order = Order.query.filter(Order.order_id == order_id).first()
	if order is None:
		return False
	order.status = status
	db.session.commit()
	return True

def change_product_quantity(product_id, quantity):
	product = Product.query.filter(Product.product_id == product_id).first()
	if product is None:
		return False
	product.quantity = quantity
	db.session.commit()
	return True

def delete_product(product_id):
	product = Product.query.filter(Product.product_id == product_id).first()
	if product is None:
		return False
	db.session.delete(product)
	db.session.commit()
	return True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def add_product(name, price, description, quantity, image):
	if image and allowed_file(image.filename):
		filename = secure_filename(image.filename)
		image.save(os.path.join(UPLOAD_FOLDER, filename))
	else:
		return False
	product = Product(name=name, price=price, description=description, quantity=quantity, image=image)
	db.session.add(product)
	db.session.commit()
	return True

@management_bp.route('/change-orders-statas', methods=['POST'])
@jwt_required()
@verify_identify("管理员")
def change_orders_status():
	
	order_ids = request.json['order_ids']
	status = request.json['status']
	result = []
	for order_id in order_ids:
		if not change_order_status(order_id, status):
			result.append(order_id)
	return {"error" : result}

@management_bp.route('/change-products-quantity', methods=['POST'])
@jwt_required()
@verify_identify("管理员")
def change_products_quantity():
	product_ids = request.json['product_ids']
	quantity = request.json['quantity']
	result = []
	for product_id in product_ids:
		if not change_product_quantity(product_id, quantity):
			result.append(product_id)
	return {"error" : result}

@management_bp.route('/delete-products', methods=['POST'])
@jwt_required()
@verify_identify("管理员")
def delete_products():
	product_ids = request.json['product_ids']
	result = []
	for product_id in product_ids:
		if not delete_product(product_id):
			result.append(product_id)
	return {"error" : result}

@management_bp.route('/add-products', methods=['POST'])
@jwt_required()
@verify_identify("管理员")
def add_products():
	name = request.json['name']
	price = request.json['price']
	description = request.json['description']
	quantity = request.json['quantity']
	image = request.json['image']
 
	message = []
 
	if not add_product(name, price, description, quantity, image):
		message.append(name)
	return {"error" : message}

	
 
 