from flask import Blueprint
from global_var import config
from global_var import db
from entity.Product import Product
from flask_jwt_extended import jwt_required
from util.jwt import verify_identify

show_coffee_bp = Blueprint('show_coffee', __name__)

STATIC_DIR = config['server']['static_dir']

def get_all_coffees():
    # 查询所有咖啡的名称
    coffees = db.session.query(Product).all()
    res = [{"id": coffee.product_id, "image": "/" + STATIC_DIR + "/coffee/" + coffee.image,
            "name": coffee.name, "price":  str(coffee.price), 
            "describe": coffee.description} for coffee in coffees]
    return res

@show_coffee_bp.route('/coffees', methods=['GET'])
def all_coffees():
	return {
		"coffees": get_all_coffees()
	}
 
@show_coffee_bp.route('/coffees-manager', methods=['GET'])
@jwt_required()
@verify_identify("管理员")
def all_coffees_manager():
	coffees = db.session.query(Product).all()
	coffees = [{"id" : coffee.product_id,
                "product_name" : coffee.name,
                "describe" : coffee.description,
                "price" : coffee.price,
                "stock" : coffee.stock,
                "image" : coffee.image,
                } for coffee in coffees]
	return {
		"coffees": coffees
	}
 
@show_coffee_bp.route('/coffees-headers')
def all_coffees_heads():
	return [
			{
		"title" : '产品编号',
		"sortable" : False,
		"value": 'id',
		"type" : "number"
	},
	{ "title": '产品名', "value": 'product_name', "type": "string" },
	{ "title": '产品描述', "value": 'describe', "type" : "string" },
	{ "title": '价格', "value": 'price', "type": "number" },
	{ "title": '库存', "value": 'stock', "type": "number" },
	{ "title": '图片', "value": 'image', "type": "image" },
	{ "title": 'Actions', "value": 'actions', "sortable": False },
	] 