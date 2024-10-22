from global_var import db

class Customer(db.Model):
	customer_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	password = db.Column(db.String(60), unique=False, nullable=False)
	email = db.Column(db.String(100), unique=False, nullable=False)
	phone = db.Column(db.String(20), unique=False, nullable=False)

	def __repr__(self):
		return f'<Customer {self.name}>'

	def get_id(self):
		return self.customer_id