from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
import pymysql
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
import modify_page
from 第四版全部内容.models import UndergraduateWorkloadTeacherRanking, TeacherInformation
from database import db
from Config import Config
from modify_page.modify_page_bp import modify_page_blueprint
from 第四版全部内容.upload_page.upload_page_bp import upload_page_blueprint

app = Flask(__name__, template_folder='templates')
Migrate(app, db)

# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = TeacherInformation.query.filter_by(teacher_id=username).first()
        if user.verify_password(password):
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



app.register_blueprint(modify_page_blueprint)
app.register_blueprint(upload_page_blueprint)

@app.route('/analyse_page', methods=['POST', 'GET'])
def analyse_page():
    if request.method == 'POST':
        teacher_id = request.form.get('teacher_id')
        teacher_name = request.form.get('teacher_name')
        results = UndergraduateWorkloadTeacherRanking.query.filter_by(teacher_id=teacher_id,
                                                                      teacher_name=teacher_name).all()
        result = [record.UndergraduateWorkloadTeacherRanking_list() for record in results]
        columns = ["教工号", "教师名称", "本科课程总学时", "毕业论文学生人数", "毕业论文P",
                   "指导教学实习人数", "指导教学实习周数", "指导教学实习P",
                   "负责实习点建设与管理P", "指导本科生竞赛P", "指导本科生科研P", "本科生导师制", "教研教改P",
                   "一流课程", "教学成果奖", "公共服务"]
        return render_template('analyse_page.html', result=result, columns=columns)
    else:
        return render_template('analyse_page.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
