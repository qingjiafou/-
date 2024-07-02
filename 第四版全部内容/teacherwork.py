from sqlalchemy import create_engine
from models import Base  # 你的模型文件

user = 'root'
password = 'Mapanwei0116'
database = 'test'
# MySQL数据库连接信息
DATABASE_URL = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)

# 创建引擎
engine = create_engine(DATABASE_URL)

# 创建所有表
Base.metadata.create_all(engine)

print("数据库和表结构已成功创建。")