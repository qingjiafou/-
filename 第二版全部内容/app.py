from flask import Flask, render_template, request, redirect, url_for,jsonify
import pymysql
import mysql.connector
from werkzeug.utils import secure_filename
import os

db_host = 'localhost'
db_user = 'root'
db_password = 'Mapanwei0116'
db_name = 'teacher_work'


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

# 创建上传文件目录
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}

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

    if  allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File uploaded successfully'

    return 'Invalid file format'
@app.route('/file_upload')
def file_upload_page():
    return render_template('file_upload.html')


@app.route('/modify_page', methods=['POST','GET'])
def modify_page():
    worksheet = request.form.get('worksheet')
    # 获取用户输入的教工号和教师名称
    teacher_id = request.form.get('teacher_id')
    teacher_name = request.form.get('teacher_name')  
    table_name=None

    if worksheet=="NULL":
        return render_template('modify_page.html')
    elif worksheet=="undergraduate_workload_course_ranking":
        table_name = "本科工作量课程排序表"
        sql="select * from undergraduate_workload_course_ranking where teacher_id='{0}' and teacher_name='{1}'".format(teacher_id,teacher_name)
        sql_name="show full columns from undergraduate_workload_course_ranking;"
        result=db_query(sql)
        columns_all=db_query(sql_name)
        columns=[]
        for column in columns_all:
            column_comment = column[8]
            columns.append(column_comment)
        return render_template('modify_page.html',**locals())
    return render_template('modify_page.html')
@app.route('/modify_page/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        # 获取前端发送的 JSON 数据
        json_data = request.get_json()
        
        if json_data:
            table_name=json_data["表名"]
            if table_name == "本科工作量课程排序表":
                sql = "UPDATE undergraduate_workload_course_ranking SET academic_year = '{0}', semester = '{1}', calendar_year = '{2}', half_year = '{3}', course_name = '{4}', seminar_hours = '{5}', lecture_hours = '{6}', lab_hours = '{7}', enrolled_students = '{8}', student_weight_coefficient_b = '{9}', course_type_coefficient_a = '{10}', total_lecture_hours_p1 = '{11}', lab_group_count = '{12}', lab_coefficient = '{13}', total_lab_hours_p2 = '{14}', course_split_ratio_for_engineering_center = '{15}', total_undergraduate_course_hours = '{16}', total_course_hours = '{17}', teacher_id = '{18}', teacher_name = '{19}' WHERE course_code = '{20}' AND teaching_class = '{21}'".format(
                    json_data["学年"],
                    json_data["学期"],
                    json_data["自然年"],
                    json_data["上下半年"],
                    json_data["课程名称"],
                    json_data["研讨学时"],
                    json_data["授课学时"],
                    json_data["实验学时"],
                    json_data["选课人数"],
                    json_data["学生数量权重系数B"],
                    json_data["课程类型系数A"],
                    json_data["理论课总学时P1"],
                    json_data["实验分组数"],
                    json_data["实验课系数"],
                    json_data["实验课总学时P2"],
                    json_data["课程拆分占比（工程中心用）"],
                    json_data["本科课程总学时"],
                    json_data["课程总学时"],
                    json_data["教工号"],
                    json_data["教师名称"],
                    json_data["课程号"],
                    json_data["教学班"],
                )
                db_exec(sql)
                return redirect(url_for('modify_page'))
        else:
            print("NO DATA")
        # 在这里处理接收到的 JSON 数据
        # 返回响应，这里返回一个简单的字符串
        return render_template('modify_page.html')


@app.route('/analyse_page', methods=['POST','GET'])
def analyse_page():
     if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        teacher_name = request.form['teacher_name']
        sql="select * from `undergraduate_workload_teacher_ranking` where teacher_id='{0}' and teacher_name='{1}'".format(teacher_id,teacher_name)
        result=db_query(sql)
        return render_template('analyse_page.html',**locals())
     else:
        return render_template('analyse_page.html',**locals())
     


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

