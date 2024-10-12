from flask import Flask, render_template

# 初始化 Flask 应用
app = Flask(__name__)

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

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
