from global_var import db
from sqlalchemy import Column, Integer, String

class Customer( db.Model):
	customer_id = Column(Integer, primary_key=True)
	name = Column(String(20), unique=False, nullable=False)
	password = Column(String(60), unique=False, nullable=False)
	email = Column(String(100), unique=False, nullable=False)
	phone = Column(String(20), unique=False, nullable=False)

	def __repr__(self):
		return f'<Customer {self.name}>'

	def get_id(self):
		return self.customer_id
	def to_json(self):
		return {
			"id": self.customer_id,
			"name": self.name,
			"email": self.email,
			"phone": self.phone
		}