from app import db

class OrderDetails(db.Model):
	order_details_id = db.Column(db.Integer, primary_key=True)
	order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
	coffee_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
	quantity = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f'<OrderDetails {self.order_details_id}>'