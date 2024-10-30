from global_var import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func

class Payment(db.Model):
	payment_id = Column(Integer, primary_key=True)
	customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
	order_id = Column(Integer, ForeignKey('order.order_id'), nullable=False)
	payment_time = Column(DateTime, default=func.now())
	payment_method = Column(String(80), nullable=False)
	status = Column(String(80), nullable=False)

	def __repr__(self):
		return f'<Payment {self.payment_id}>'