from flask import Blueprint, request, current_app
from sqlalchemy import or_
from global_var import db
from entity.Customer import Customer
from entity.Manager import Manager
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetails import OrderDetails
from flask_jwt_extended import jwt_required, get_jwt_identity

payment_bp = Blueprint('payment', __name__)

def check_quantity(cart):
	for item in cart:
		product = Product.query.filter(Product.product_id==item['id']).first()
		if product is None:
			return False
		if product.stock < item['quantity']:
			return False
	return True

def create_order_details(order_id, cart):
	for item in cart:
		order_details = OrderDetails(order_id=order_id, coffee_id=item['id'], quantity=item['quantity'])
		db.session.add(order_details)

def create_order(cart, customer, price):
	for item in cart:
		if not check_quantity(cart):
			return False
	order = Order(customer_id=customer.customer_id, price=price, status="processing")
	db.session.add(order)
	for item in cart:
		product = Product.query.filter(Product.product_id==item['id']).first()
		product.stock -= item['quantity']
		db.session.add(product)
	create_order_details(order.order_id, cart)
	db.session.commit()
    

@payment_bp.route('/pay', methods=['POST'])
@jwt_required()
def pay():
	current_user = Customer.query.filter(Customer.customer_id==get_jwt_identity()).first()
	data = request.get_json()
	print(data)
	create_order(data['detail'], current_user, data['amount'])
	return {
		"user": current_user.to_json(),
	}