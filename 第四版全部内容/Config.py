class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    user = 'root'
    password = 'Mapanwei0116'
    database = 'teacher_work'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
    # 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
    #上传文件
    UPLOAD_FOLDER = 'uploads'
    # Flask 用来保护会话数据的关键配置
    SECRET_KEY = 'ccnu'