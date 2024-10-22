from global_var import db

class Manager(db.Model):
	manager_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	password = db.Column(db.String(60), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	phone = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return f'<Manager {self.manager_id}>'

	def get_id(self):
		return self.manager_id