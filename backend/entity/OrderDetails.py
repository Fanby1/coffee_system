from global_var import db
from sqlalchemy import Column, Integer, ForeignKey

class OrderDetails(db.Model):
	order_details_id = Column(Integer, primary_key=True)
	order_id = Column(Integer, ForeignKey('order.order_id'), nullable=False)
	coffee_id = Column(Integer, ForeignKey('product.product_id'), nullable=False)
	quantity = Column(Integer, nullable=False)

	def __repr__(self):
		return f'<OrderDetails {self.order_details_id}>'