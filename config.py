import os


class Config(object):
    # 格式为mysql+pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字?数据库格式
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/kiken'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
