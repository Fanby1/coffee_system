from global_var import db
from sqlalchemy import Column, Integer, String, Float

class Product(db.Model):
	product_id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	price = Column(Float, nullable=False)
	image = Column(String(80), nullable=False)
	description = Column(String(255), nullable=False)
	stock = Column(Integer, nullable=False)

	def __repr__(self):
		return f'<Product {self.product_id} | name {self.name} >'