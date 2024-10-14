from app import db

class Manager(db.Model):
	manager_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	password = db.Column(db.String(80), nullable=False)

	def __repr__(self):
		return f'<Manager {self.manager_id}>'