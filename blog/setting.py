"""
 Created by qujl on 2018-05-25
"""
__author__ = 'qujl'
# 调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFCATIONS = False
# session必须要设置key
SECRET_KEY = 'zx1efSNdO0yV9LGp'

# mysql数据库连接信息，这里改成自己的账号
SQLALCHEMY_DATABASE_URL = 'mysql://root:root@localhost/3306/blog'
