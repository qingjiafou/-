from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
import pymysql
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
from model import CompetitionAward, DepartmentInternship, \
    EducationalResearchProject, FirstClassCourse, PublicService, StudentResearch, TeachingAchievementAward, \
    UndergraduateMentorshipSystem, UndergraduateThesi, UndergraduateWorkloadCourseRanking, \
    UndergraduateWorkloadTeacherRanking, TeacherInformation
from database import db

app = Flask(__name__)
Migrate(app, db)


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


# 校验密码


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
        results = UndergraduateWorkloadCourseRanking.query.filter_by(teacher_id=teacher_id,
                                                                     teacher_name=teacher_name).all()
        result = [record.UndergraduateWorkloadCourseRanking_list() for record in results]
        columns = ["学年", "学期", "自然年", "上下半年", "课程号", "教学班", "课程名称", "教工号", "教师名称",
                   "研讨学时", "授课学时", "实验学时", "选课人数", "学生数量权重系数B", "课程类型系数A",
                   "理论课总学时P1", "实验分组数", "实验课系数", "实验课总学时P2", "课程拆分占比（工程中心用）",
                   "课程总学时"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_thesis":
        table_name = "毕业论文"
        results = UndergraduateThesi.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.UndergraduateThesi_list() for record in results]
        columns = ["学生姓名", "学生学号", "学院", "专业", "专业号", "年级", "毕业论文题目", "毕业论文成绩",
                   "毕业论文指导老师", "毕业论文指导老师工号"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "department_internship":
        table_name = "本科实习"
        results = DepartmentInternship.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.DepartmentInternship_list() for record in results]
        columns = ["学生姓名", "学生学号", "专业", "年级", "学部内实习指导教师", "学部内实习指导教师工号", "实习周数"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "competition_awards":
        table_name = "学生竞赛"
        results = CompetitionAward.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.CompetitionAward_list() for record in results]
        columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量",
                   "获奖年份"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "student_research":
        table_name = "学生科研"
        results = StudentResearch.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.StudentResearch_list() for record in results]
        columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果",
                   "工作量"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_mentorship_system":
        table_name = "本科生导师制"
        results = UndergraduateMentorshipSystem.query.filter_by(teacher_id=teacher_id,
                                                                teacher_name=teacher_name).all()
        result = [record.UndergraduateMentorshipSystem_list() for record in results]
        columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "educational_research_project":
        table_name = "教研项目"
        results = EducationalResearchProject.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.EducationalResearchProject_list() for record in results]
        columns = ["序号", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
                   "教师姓名", "工号", "教研项目工作量"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "first_class_courses":
        table_name = "一流课程"
        results = FirstClassCourse.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.FirstClassCourse_list() for record in results]
        columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "teaching_achievement_awards":
        table_name = "教学成果奖"
        results = TeachingAchievementAward.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.TeachingAchievementAward_list() for record in results]
        columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
                   "工号", "教学成果工作量"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    elif worksheet == "public_services":
        table_name = "公共服务"
        results = PublicService.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.PublicService_list() for record in results]
        columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号", "工作量"]
        return render_template('modify_page.html', result=result, table_name=table_name, columns=columns)
    return render_template('modify_page.html')


@app.route('/modify_page/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        # 获取前端发送的 JSON 数据
        json_data = request.get_json()
        if json_data:
            table_name = json_data["表名"]
            if table_name == "本科工作量课程排序表":
                new_workload_course_ranking = \
                    UndergraduateWorkloadCourseRanking.query.filter_by(course_code=json_data["课程号"],
                                                                       teaching_class=json_data["教学班"]).first()
                new_workload_course_ranking.academic_year = json_data["学年"]
                new_workload_course_ranking.semester = json_data["学期"]
                new_workload_course_ranking.calendar_year = json_data["自然年"]
                new_workload_course_ranking.half_year = json_data["上下半年"]
                new_workload_course_ranking.course_name = json_data["课程名称"]
                new_workload_course_ranking.seminar_hours = json_data["研讨学时"]
                new_workload_course_ranking.lecture_hours = json_data["授课学时"]
                new_workload_course_ranking.lab_hours = json_data["实验学时"]
                new_workload_course_ranking.enrolled_students = json_data["选课人数"]
                new_workload_course_ranking.student_weight_coefficient_b = json_data["学生数量权重系数B"]
                new_workload_course_ranking.course_type_coefficient_a = json_data["课程类型系数A"]
                new_workload_course_ranking.total_lecture_hours_p1 = json_data["理论课总学时P1"]
                new_workload_course_ranking.lab_group_count = json_data["实验分组数"]
                new_workload_course_ranking.lab_coefficient = json_data["实验课系数"]
                new_workload_course_ranking.total_lab_hours_p2 = json_data["实验课总学时P2"]
                new_workload_course_ranking.course_split_ratio_for_engineering_center = json_data[
                    "课程拆分占比（工程中心用）"]
                new_workload_course_ranking.total_course_hours = json_data["课程总学时"]
                new_workload_course_ranking.teacher_id = json_data["教工号"]
                new_workload_course_ranking.teacher_name = json_data["教师名称"]
                db.session.add(new_workload_course_ranking)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "毕业论文":
                new_undergraduate_thesis = UndergraduateThesi.query.filter_by(student_id=json_data["学生学号"]).first()
                new_undergraduate_thesis.student_name = json_data["学生姓名"]
                new_undergraduate_thesis.college = json_data["学院"]
                new_undergraduate_thesis.major = json_data["专业"]
                new_undergraduate_thesis.major_id = json_data["专业号"]
                new_undergraduate_thesis.grade = json_data["年级"]
                new_undergraduate_thesis.thesis_topic = json_data["毕业论文题目"]
                new_undergraduate_thesis.thesis_grade = json_data["毕业论文成绩"]
                new_undergraduate_thesis.teacher_name = json_data["毕业论文指导老师"]
                new_undergraduate_thesis.teacher_id = json_data["毕业论文指导老师工号"]
                db.session.add(new_undergraduate_thesis)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "本科实习":
                new_departmentInternship = DepartmentInternship.query.filter_by(
                    student_id=json_data["学生学号"]).first()
                new_departmentInternship.student_name = json_data["学生姓名"]
                new_departmentInternship.major = json_data["专业"]
                new_departmentInternship.grade = json_data["年级"]
                new_departmentInternship.teacher_name = json_data["学部内实习指导教师"]
                new_departmentInternship.teacher_id = json_data["学部内实习指导教师工号"]
                new_departmentInternship.week = json_data["实习周数"]
                db.session.add(new_departmentInternship)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "学生竞赛":
                # columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量","获奖年份"]
                new_competitionAward = CompetitionAward.query.filter_by(id=json_data["序号"]).first()
                new_competitionAward.event_name = json_data["赛事名称"]
                new_competitionAward.work_name = json_data["作品名称"]
                new_competitionAward.award_category = json_data["获奖类别"]
                new_competitionAward.award_level = json_data["获奖等级"]
                new_competitionAward.teacher_name = json_data["指导教师"]
                new_competitionAward.teacher_id = json_data["指导教师工号"]
                new_competitionAward.total_workload = json_data["总工作量"]
                new_competitionAward.award_year = json_data["获奖年份"]
                db.session.add(new_competitionAward)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "学生科研":
                # columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果","工作量"]
                new_StudentResearch = StudentResearch.query.filter_by(id=json_data["序号"]).first()
                new_StudentResearch.project_name = json_data["项目名称"]
                new_StudentResearch.project_level = json_data["级别"]
                new_StudentResearch.leader = json_data["负责人"]
                new_StudentResearch.student_id = json_data["学号"]
                new_StudentResearch.total_members = json_data["项目组总人数"]
                new_StudentResearch.teacher_name = json_data["指导老师"]
                new_StudentResearch.teacher_id = json_data["指导老师工号"]
                new_StudentResearch.acceptance_result = json_data["验收结果"]
                new_StudentResearch.workload = json_data["工作量"]
                db.session.add(new_StudentResearch)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "本科生导师制":
                # columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
                new_UndergraduateMentorshipSystem = UndergraduateMentorshipSystem.query.filter_by(
                    student_id=json_data["学号"]).first()
                new_UndergraduateMentorshipSystem.teacher_name = json_data["导师姓名"]
                new_UndergraduateMentorshipSystem.teacher_id = json_data["教工号"]
                new_UndergraduateMentorshipSystem.student_name = json_data["学生姓名"]
                new_UndergraduateMentorshipSystem.grade = json_data["年级"]
                new_UndergraduateMentorshipSystem.teacher_workload = json_data["教师工作量"]
                db.session.add(new_UndergraduateMentorshipSystem)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "教研项目":
                # columns = ["序号", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
                #                    "教师姓名", "工号", "教研项目工作量"]
                new_EducationalResearchProject = EducationalResearchProject.query.filter_by(
                    id=json_data["序号"]).first()
                new_EducationalResearchProject.project_name = json_data["项目名称"]
                new_EducationalResearchProject.project_leader = json_data["项目负责人"]
                new_EducationalResearchProject.project_members = json_data["项目成员"]
                new_EducationalResearchProject.project_level = json_data["级别"]
                new_EducationalResearchProject.start_date = json_data["立项时间"]
                new_EducationalResearchProject.end_date = json_data["结项时间"]
                new_EducationalResearchProject.acceptance_result = json_data["验收结论"]
                new_EducationalResearchProject.teacher_name = json_data["教师姓名"]
                new_EducationalResearchProject.teacher_id = json_data["工号"]
                new_EducationalResearchProject.research_project_workload = json_data["教研项目工作量"]
                db.session.add(new_EducationalResearchProject)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "一流课程":
                # columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
                new_FirstClassCourse = FirstClassCourse.query.filter_by(id=json_data["序号"]).first()
                new_FirstClassCourse.course_type = json_data["课程性质"]
                new_FirstClassCourse.content = json_data["内容"]
                new_FirstClassCourse.leader = json_data["负责人"]
                new_FirstClassCourse.remark = json_data["备注"]
                new_FirstClassCourse.teacher_name = json_data["教师姓名"]
                new_FirstClassCourse.teacher_id = json_data["工号"]
                new_FirstClassCourse.first_class_course_workload = json_data["一流课程工作量"]
                db.session.add(new_FirstClassCourse)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "教学成果奖":
                # columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
                #   "工号", "教学成果工作量"]
                new_TeachingAchievementAward = TeachingAchievementAward.query.filter_by(id=json_data["序号"])
                new_TeachingAchievementAward.student_session = json_data["届"]
                new_TeachingAchievementAward.student_date = json_data["时间"]
                new_TeachingAchievementAward.recommended_achievement_name = json_data["推荐成果名称"]
                new_TeachingAchievementAward.main_completion_person_name = json_data["成果主要完成人名称"]
                new_TeachingAchievementAward.award_category = json_data["获奖类别"]
                new_TeachingAchievementAward.award_level = json_data["获奖等级"]
                new_TeachingAchievementAward.remark = json_data["备注"]
                new_TeachingAchievementAward.teacher_name = json_data["教师"]
                new_TeachingAchievementAward.teacher_id = json_data["工号"]
                new_TeachingAchievementAward.teaching_achievement_workload = json_data["教学成果工作量"]
                db.session.add(new_TeachingAchievementAward)
                db.session.commit()
                return redirect(url_for('modify_page'))
            elif table_name == "公共服务":
                # columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号"]
                new_PublicService = PublicService.query.filter_by(id=json_data["序号"])
                new_PublicService.serve_date = json_data["日期"]
                new_PublicService.content = json_data["内容"]
                new_PublicService.teacher_name = json_data["姓名"]
                new_PublicService.work_duration = json_data["工作时长"]
                new_PublicService.class_hours = json_data["课时"]
                new_PublicService.teacher_id = json_data["教师工号"]
                new_PublicService.workload = json_data["工作量"]
                db.session.add(new_PublicService)
                db.session.add()
                return redirect(url_for('modify_page'))
        else:
            print("NO DATA")
        # 在这里处理接收到的 JSON 数据
        # 返回响应，这里返回一个简单的字符串
        return render_template('modify_page.html')


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
