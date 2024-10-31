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
	db.session.add(order)
	db.session.commit()
	return True

def change_product(product_id, data):
	product = Product.query.filter(Product.product_id == product_id).first()
	if product is None:
		return False
	product.quantity = data.quantity
	product.name = data.name
	product.price = data.price
	product.description = data.description
	product.image = data.image
	product.stock = data.stock
	db.session.add(product)
	db.session.commit()
	return True

def delete_product(product_id):
	product = Product.query.filter(Product.product_id == product_id).first()
	if product is None:
		return False
	os.remove(os.path.join(UPLOAD_FOLDER, product.image))
	db.session.delete(product)
	db.session.commit()
	return True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def add_product(data):
	try:
		name = data['name']
		price = data['price']
		description = data['description']
		quantity = data['quantity']
		image = data['image']
		if image and allowed_file(image.filename):
			filename = secure_filename(image.filename)
			image.save(os.path.join(UPLOAD_FOLDER, filename))
		else:
			return False
		product = Product(name=name, price=price, description=description, quantity=quantity, image=image)
		db.session.add(product)
		db.session.commit()
	except Exception as e:
		current_app.logger.error('Add product error: %s', e)
		db.session.rollback()
		return False
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

@management_bp.route('/change-products', methods=['POST'])
@jwt_required()
@verify_identify("管理员")
def change_products_quantity():
	product_ids = request.json['product_ids']
	datas = request.json['datas']
	result = []
	for product_id, data in product_ids, datas:
		if not change_product(product_id, data):
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
	return {"error" : result}, 200

@management_bp.route('/add-products', methods=['POST'])
@jwt_required()
@verify_identify("管理员")
def add_products():
	current_app.logger.info('Add product request: %s', request.json)
	message = []
	for data in request.json:
		if not add_product(data):
			message.append(data["name"])
	return {"error" : message}

@management_bp.route('/add-product', methods=['POST'])
@jwt_required()
@verify_identify("管理员")
def add_product():
    try:
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        quantity = request.form['quantity']
        image = request.files['image']

        if image and allowed_file(image.filename):
            current_app.logger.info('Image file: %s', image.filename)
            filename = image.filename
            current_app.logger.info('Image filename: %s', filename)
            image.save(os.path.join(UPLOAD_FOLDER, filename))
        else:
            return {"error": "Invalid image file"}, 400

        product = Product(name=name, price=price, description=description, stock=quantity, image=filename)
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        current_app.logger.error('Add product error: %s', e)
        db.session.rollback()
        return {"error": "Add product failed"}, 500
    return {"message": "Product added successfully"}, 200
	
 
 