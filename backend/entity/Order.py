from app import db

class Order(db.Model):
	order_id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
	coffee = db.Column(db.String(80), nullable=False)
	price = db.Column(db.Float, nullable=False)
	status = db.Column(db.String(80), nullable=False)

	def __repr__(self):
		return f'<Order {self.id}>'

