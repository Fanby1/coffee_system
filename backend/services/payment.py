from flask import Blueprint, request, current_app
from global_var import db
from entity.Customer import Customer
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetails import OrderDetails
from entity.Payment import Payment
from flask_jwt_extended import jwt_required, get_jwt_identity
from util.jwt import verify_identify

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
			raise Exception("库存不足")
	order = Order(customer_id=customer.customer_id, price=price, status="processing")
	db.session.add(order)
	for item in cart:
		product = Product.query.filter(Product.product_id==item['id']).first()
		product.stock -= item['quantity']
		db.session.add(product)
	create_order_details(order.order_id, cart)
	return order.order_id
 
def create_payment(customer_id, order_id, payment_method):
	payment = Payment()
	payment.customer_id = customer_id
	current_app.logger.info("order_id : %d",order_id)
	payment.order_id = order_id
	payment.payment_method = payment_method
	payment.status = "processing"
	db.session.add(payment)
	return payment.payment_id
    

@payment_bp.route('/pay', methods=['POST'])
@jwt_required()
@verify_identify("顾客")
def pay():
	current_user = Customer.query.filter(Customer.customer_id==get_jwt_identity()).first()
	data = request.get_json()
	try:
		order_id = create_order(data['detail'], current_user, data['amount'])
		payment_id = create_payment(current_user.customer_id, order_id, data['description'])
		db.session.commit()
		return {
			"result" : "success",
    	    "user": current_user.to_json(),
    	    "order_id": order_id,
    	    "payment_id": payment_id
    	}
	except Exception as e:
		current_app.logger.error(e)
		db.session.rollback()
		return {
			"result" : "error",
			"message" : str(e)
		}