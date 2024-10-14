from app import db
from app import app
from entity.Customer import Customer
from entity.Payment import Payment
from entity.Product import Product
from entity.Order import Order
from entity.OrderDetails import OrderDetails
from entity.ShoppingCart import ShoppingCart
from entity.Manager import Manager

with app.app_context():
	db.create_all()

print("数据库初始化完成")