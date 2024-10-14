from app import db

class Customer(db.Model):
	customer_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	email = db.Column(db.String(120), unique=False, nullable=False)
	phone = db.Column(db.String(20), unique=False, nullable=False)

	def __repr__(self):
		return f'<Customer {self.name}>'