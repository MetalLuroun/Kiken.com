from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 载入配置文件
app.config.from_object(Config)
# 初始化数据库
# db.init_app(app)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/Work')
def work():
    return '数据库图片'


@app.route('/Personal')
def personal():
    return '数据库图片'


if __name__ == '__main__':
    app.run()
