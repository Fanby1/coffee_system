from app import db

class Payment(db.Model):
	payment_id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
	order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
	payment_time = db.Column(db.DateTime, nullable=False)
	payment_method = db.Column(db.String(80), nullable=False)
	status = db.Column(db.String(80), nullable=False)

	def __repr__(self):
		return f'<Payment {self.payment_id}>'