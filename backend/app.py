from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from global_var import config
from global_var import db
from global_var import jwt

# 访问配置项
host = config['mysql']['host']
user = config['mysql']['user']
password = config['mysql']['password']
database = config['mysql']['database']
jwt_secret_key = config['jwt']['secret_key']

print(f"Host: {host}, User: {user}, Database: {database}, JWT Secret: {jwt_secret_key}")

# 初始化 Flask 应用
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = jwt_secret_key
db.init_app(app)
jwt.init_app(app)


# 导入并注册蓝图
from services.show_coffee import show_coffee_bp
from services.authentication import authentication_bp
app.register_blueprint(show_coffee_bp)
app.register_blueprint(authentication_bp)

# 配置静态文件存储目录
SERVER_IP = config['server']['ip']
STATIC_DIR = config['server']['static_dir']

@app.route('/static/<path:filename>', methods=['GET'])
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

# 启动应用
if __name__ == "__main__":
    app.run(debug=True)
