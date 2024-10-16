from flask import Blueprint
from global_var import config
from global_var import db
from entity.Product import Product

show_coffee_bp = Blueprint('show_coffee', __name__)

STATIC_DIR = config['server']['static_dir']

def get_all_coffees():
    # 查询所有咖啡的名称
    coffees = db.session.query(Product).all()
    res = [{"image": "/" + STATIC_DIR + "/coffee/" + coffee.image,
            "name": coffee.name, "price":  str(coffee.price), 
            "discribe": coffee.description} for coffee in coffees]
    return res

@show_coffee_bp.route('/coffees', methods=['GET'])
def all_coffees():
	return {
		"coffees": get_all_coffees()
	}