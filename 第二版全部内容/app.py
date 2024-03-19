from flask import Flask, render_template, request, redirect, url_for
import pymysql
import mysql.connector

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






if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

