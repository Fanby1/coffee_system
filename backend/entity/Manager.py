from global_var import db
from sqlalchemy import Column, Integer, String
class Manager(db.Model):
	manager_id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	password = Column(String(60), nullable=False)
	email = Column(String(100), nullable=False)
	phone = Column(String(20), nullable=False)

	def __repr__(self):
		return f'<Manager {self.manager_id}>'

	def get_id(self):
		return self.manager_id