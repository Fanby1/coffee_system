from global_var import db
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Order(db.Model):
	order_id = Column(Integer, primary_key=True)
	customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
	price = Column(Float, nullable=False)
	status = Column(String(80), nullable=False)

	def __repr__(self):
		return f'<Order {self.id}>'

