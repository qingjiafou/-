# 导入蓝图
import os
from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from flask_login import login_required
from version_four.models import CompetitionAward, DepartmentInternship, \
    EducationalResearchProject, FirstClassCourse, PublicService, StudentResearch, TeachingAchievementAward, \
    UndergraduateMentorshipSystem, UndergraduateThesi, UndergraduateWorkloadCourseRanking
from version_four.Config import Config

"""
实例化蓝图对象
第一个参数：蓝图名称
"""
upload_page_blueprint = Blueprint('upload_page', __name__, template_folder='templates')

# 定义上传文件的保存目录
UPLOAD_FOLDER = Config.UPLOAD_FOLDER  # 使用新的配置

# 创建上传文件目录
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}


# 检查文件扩展名是否符合要求
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 用蓝图注册路由
# 跳转到这个界面
@upload_page_blueprint.route("/file_upload")
@login_required
def file_upload_page():
    return render_template('file_upload.html')


# 批量上传的按钮的路由
@upload_page_blueprint.route("/file_upload/load", methods=['POST', 'GET'])
@login_required
def upload_file():
    if request.method == 'GET':
        return render_template('file_upload.html')
    elif request.method == 'POST':
        if 'file' not in request.files:
            flash({'error': 'No file part'})
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash({'error': '没有选择的文件'})
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash({'error': '文件扩展名有问题'})
            return redirect(request.url)
        # 在这里处理文件，例如保存到服务器等
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
        flash({'success': '文件上传成功'})
        return redirect(url_for('upload_page.upload_file'))


# 展示要提交的内容表单
@upload_page_blueprint.route("/file_upload/add", methods=['POST', 'GET'])
@login_required
def upload_file_add():
    worksheet = request.form.get('worksheet')
    if worksheet == "NULL":
        return render_template('file_upload.html')
    elif worksheet == "undergraduate_workload_course_ranking":
        table_name = "本科工作量课程排序表"
        columns = ["学年", "学期", "自然年", "上下半年", "课程号", "教学班", "课程名称", "教工号", "教师名称",
                   "研讨学时", "授课学时", "实验学时", "选课人数", "学生数量权重系数B", "课程类型系数A",
                   "理论课总学时P1", "实验分组数", "实验课系数", "实验课总学时P2", "课程拆分占比（工程中心用）",
                   "课程总学时"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_thesis":
        table_name = "毕业论文"
        columns = ["学生姓名", "学生学号", "学院", "专业", "专业号", "年级", "毕业论文题目", "毕业论文成绩",
                   "毕业论文指导老师", "毕业论文指导老师工号"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "department_internship":
        table_name = "本科实习"
        columns = ["学生姓名", "学生学号", "专业", "年级", "学部内实习指导教师", "学部内实习指导教师工号", "实习周数"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "competition_awards":
        table_name = "学生竞赛"
        columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量",
                   "获奖年份"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "student_research":
        table_name = "学生科研"
        columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果",
                   "工作量"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_mentorship_system":
        table_name = "本科生导师制"
        columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "educational_research_project":
        table_name = "教研项目"
        columns = ["序号", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
                   "教师姓名", "工号", "教研项目工作量"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "first_class_courses":
        table_name = "一流课程"
        columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "teaching_achievement_awards":
        table_name = "教学成果奖"
        columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
                   "工号", "教学成果工作量"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    elif worksheet == "public_services":
        table_name = "公共服务"
        columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号", "工作量"]
        return render_template('file_upload.html', table_name=table_name, columns=columns)
    return render_template('file_upload.html')

# 提交的按钮的路由
@upload_page_blueprint.route("/file_upload/submit", methods=['POST', 'GET'])
@login_required
def upload_file_submit():
    if request.method == 'POST':
        # 获取前端发送的 JSON 数据
        json_data = request.get_json()
        if json_data:
            table_name = json_data["表名"]
            if table_name == "本科工作量课程排序表":
                UndergraduateWorkloadCourseRanking.add_UndergraduateWorkloadCourseRanking(json_data)
                return render_template('file_upload.html')
            elif table_name == "毕业论文":
                UndergraduateThesi.add_thesis_record(json_data)
                return render_template('file_upload.html')
            elif table_name == "本科实习":
                DepartmentInternship.add_internship_record(json_data)
                return render_template('file_upload.html')
            elif table_name == "学生竞赛":
                # columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量","获奖年份"]
                CompetitionAward.add_competition_award(json_data)
                return render_template('file_upload.html')
            elif table_name == "学生科研":
                # columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果","工作量"]
                StudentResearch.add_student_research_record(json_data)
                return render_template('file_upload.html')
            elif table_name == "本科生导师制":
                # columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
                UndergraduateMentorshipSystem.add_mentorship_record(json_data)
                return render_template('file_upload.html')
            elif table_name == "教研项目":
                # columns = ["序号", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
                #                    "教师姓名", "工号", "教研项目工作量"]
                EducationalResearchProject.add_research_project(json_data)
                return render_template('file_upload.html')
            elif table_name == "一流课程":
                # columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
                FirstClassCourse.add_first_class_course(json_data)
                return render_template('file_upload.html')
            elif table_name == "教学成果奖":
                # columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
                #   "工号", "教学成果工作量"]
                TeachingAchievementAward.add_teaching_achievement_record(json_data)
                return render_template('file_upload.html')
            elif table_name == "公共服务":
                # columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号"]
                PublicService.add_public_service_record(json_data)
                return render_template('file_upload.html')
        else:
            print("NO DATA")
    else:
        return  render_template('file_upload.html')