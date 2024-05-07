from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymysql
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from model import CompetitionAward, DepartmentInternship,  \
    EducationalResearchProject, FirstClassCourse, PublicService, StudentResearch, TeachingAchievementAward, \
    UndergraduateMentorshipSystem, UndergraduateThesi, UndergraduateWorkloadCourseRanking
from database import db

app = Flask(__name__)


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


# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db.init_app(app)


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

    if allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'File uploaded successfully'

    return 'Invalid file format'


@app.route('/file_upload')
def file_upload_page():
    return render_template('file_upload.html')


@app.route('/modify_page', methods=['POST', 'GET'])
def modify_page():
    worksheet = request.form.get('worksheet')
    # 获取用户输入的教工号和教师名称
    teacher_id = request.form.get('teacher_id')
    teacher_name = request.form.get('teacher_name')
    table_name = None

    if worksheet == "NULL":
        return render_template('modify_page.html')
    elif worksheet == "undergraduate_workload_course_ranking":
        table_name = "本科工作量课程排序表"
        result = UndergraduateWorkloadCourseRanking.query.filter_by(teacher_id=teacher_id,
                                                                       teacher_name=teacher_name).all()
        columns = ["学年", "学期", "自然年", "上下半年", "课程号", "教学班", "课程名称", "教工号", "教师名称",
                   "研讨学时", "授课学时", "实验学时", "选课人数", "学生数量权重系数B", "课程类型系数A",
                   "理论课总学时P1", "实验分组数", "实验课系数", "实验课总学时P2", "课程拆分占比（工程中心用）",
                   "本科课程总学时", "课程总学时"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_thesis":
        table_name = "毕业论文"
        result = UndergraduateThesi.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["学生姓名", "学生学号", "学院", "专业", "专业号", "年级", "毕业论文题目", "毕业论文成绩",
                   "毕业论文指导老师", "毕业论文指导老师工号"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "department_internship":
        table_name = "本科实习"
        result = DepartmentInternship.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["学生姓名", "学生学号", "专业", "年级", "学部内实习指导教师", "学部内实习指导教师工号"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "competition_awards":
        table_name = "学生竞赛"
        result = CompetitionAward.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量",
                   "获奖年份"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "student_research":
        table_name = "学生科研"
        result = StudentResearch.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果",
                   "工作量"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_mentorship_system":
        table_name = "本科生导师制"
        result = UndergraduateMentorshipSystem.query.filter_by(teacher_id=teacher_id,
                                                                    teacher_name=teacher_name).all()
        columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "educational_research_project":
        table_name = "教研项目"
        result = EducationalResearchProject.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["序号，主键", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
                   "教师姓名", "工号", "教研项目工作量"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "first_class_courses":
        table_name = "一流课程"
        result = FirstClassCourse.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "teaching_achievement_awards":
        table_name = "教学成果奖"
        result = TeachingAchievementAward.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
                   "工号", "教学成果工作量"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    elif worksheet == "public_services":
        table_name = "公共服务"
        result = PublicService.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号"]
        return render_template('modify_page.html', table_name=table_name, columns=columns)
    return render_template('modify_page.html')


@app.route('/modify_page/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        # 获取前端发送的 JSON 数据
        json_data = request.get_json()

        if json_data:
            table_name = json_data["表名"]
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
                    json_data["教学班"]
                )
                # db_exec(sql)
                return redirect(url_for('modify_page'))
            elif table_name == "毕业论文":
                sql = "update undergraduate_thesis SET student_name = '{0}',college = '{1}',major = '{2}',major_id = '{3}',grade = '{4}',thesis_topic = '{5}', thesis_grade = '{6}',teacher_name = '{7}',teacher_id = '{8}'WHERE student_id = '{9}';".format(
                    json_data["学生姓名"],
                    json_data["学院"],
                    json_data["专业"],
                    json_data["专业号"],
                    json_data["年级"],
                    json_data["毕业论文题目"],
                    json_data["毕业论文成绩"],
                    json_data["毕业论文指导老师"],
                    json_data["毕业论文指导老师工号"],
                    json_data["学生学号"]
                )
                #   db_exec(sql)
                return redirect(url_for('modify_page'))
        else:
            print("NO DATA")
        # 在这里处理接收到的 JSON 数据
        # 返回响应，这里返回一个简单的字符串
        return render_template('modify_page.html')


@app.route('/analyse_page', methods=['POST', 'GET'])
def analyse_page():
    if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        teacher_name = request.form['teacher_name']
        sql = "select * from `undergraduate_workload_teacher_ranking` where teacher_id='{0}' and teacher_name='{1}'".format(
            teacher_id, teacher_name)
        #  result = db_query(sql)
        return render_template('analyse_page.html', **locals())
    else:
        return render_template('analyse_page.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
