from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

# 初始化 Flask 应用
app = Flask(__name__)
CORS(app)

# 定义路由和视图函数
@app.route('/')
def home():
    return "Welcome to my Coffee Ordering System!"

@app.route('/menu')
def menu():
    return "Here is the menu."

@app.route('/api/test')
def api_test():
	return {
		"message": "Hello, World!"
	}

# 配置静态文件存储目录
SERVER_IP = 'http://localhost:5000'
STATIC_DIR = 'static'

@app.route('/api/static/<path:filename>', methods=['GET'])
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route('/api/coffees', methods=['GET'])
def all_coffees():
	return {
		"coffees": [
			{
                "image": SERVER_IP + "/" + STATIC_DIR + "/coffee/拿铁.png",
				"name": "拿铁",
				"price": "2.5"
			}
		]
	}
# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
