"""
 Created by qujl on 2018-05-25
 url : https://www.cnblogs.com/mysql-dba/p/6070258.html
"""
__author__ = 'qujl'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建项目对象
app = Flask(__name__)
# 加载配置文件内容
app.config.from_object('blog.setting')      # 模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASK_SETTINGS')    # 环境变量，只想配置文件setting的路径

# 创建数据库对象
db = SQLAlchemy(app)

# 只有在app对象之后声明，用于导入model否则无法创建表
from blog.model import User,Category

# 只有在app对象之后声明，用于导入view模块
from blog.controller import blog_message