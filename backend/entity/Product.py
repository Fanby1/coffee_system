from global_var import db

class Product(db.Model):
	product_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	price = db.Column(db.Float, nullable=False)
	image = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(255), nullable=False)
	stock = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f'<Product {self.product_id} | name {self.name} >'