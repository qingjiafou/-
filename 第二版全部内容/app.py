from flask import Flask, render_template, request, redirect, url_for
import pymysql
import mysql.connector
from werkzeug.utils import secure_filename
import os

db_host = 'localhost'
db_user = 'root'
db_password = 'Mapanwei0116'
db_name = 'teacher'


def db_query(sql):
    db = pymysql.connect(host=db_host,
                        user=db_user,
                        password=db_password,
                        database=db_name)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute(sql)
    # 使用 fetchone() 方法获取所有数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return data


def db_exec(sql):
    db = pymysql.connect(host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()    #用于提交数据库中的更改
    db.close()


def db_fun():
    db = pymysql.connect(host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name)
    cursor = db.cursor()
    cursor.callproc('recompute_workload')
    db.commit()
    db.close()


app = Flask(__name__)

# 定义上传文件的保存目录
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# 检查文件扩展名是否符合要求
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return render_template('index.html')
        else:
            return render_template('login.html', error=True)
    else:
        return render_template('login.html', error=False)



@app.route('/logout')
def logout():
    # 重定向到登录页面
    return render_template('login.html')


@app.route('/toindex')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'

    return 'Invalid file format'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

