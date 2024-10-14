from app import db
from sqlalchemy.dialects.postgresql import JSON

class ShoppingCart(db.Model):
    shopping_cart_id = db.Column(db.Integer, db.ForeignKey("customer.customer_id"), primary_key=True)
    coffee_list = db.Column(JSON, nullable=False)