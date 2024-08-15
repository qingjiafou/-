# 导入蓝图
import os
import pandas as pd
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

# 允许上传的文件类型,表格类型
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}


# 检查文件扩展名是否符合要求
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 处理csv后缀名的导入文件
def analyse_worksheet(file_name, worksheet):
    _, file_extension = os.path.splitext(file_name)  # 获取文件的后缀名部分
    if file_extension.lower() == '.csv':
        df = pd.read_csv(file_name)  # 读取CSV文件为DataFrame
    elif file_extension.lower() == '.xlsx':
        df = pd.read_excel(file_name)  # 读取Excel文件的指定工作表为DataFrame
    if worksheet == "competition_awards":
        json_data_list = []
        for index, row in df.iterrows():
            json_data = {
                "序号": row["序号"],
                "赛事名称": row["赛事名称"],
                "作品名称": row["作品名称"],
                "获奖类别": row["获奖类别"],
                "获奖等级": row["获奖等级"],
                "指导教师": row["指导教师"],
                "指导教师工号": row["指导教师工号"],
                "总工作量": row["总工作量"],
                "获奖年份": row["获奖年份"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "department_internships":
        json_data_list = []
        for index, row in df.iterrows():
            json_data = {
                "学生姓名": row["学生姓名"],
                "学生学号": row["学生学号"],
                "专业": row["专业"],
                "年级": row["年级"],
                "学部内实习指导教师": row["学部内实习指导教师"],
                "学部内实习指导教师工号": row["学部内实习指导教师工号"],
                "实习周数": row["实习周数"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "educational_research_projects":
        json_data_list = []
        for index, row in df.iterrows():
            json_data = {
                "项目名称": row["项目名称"],
                "项目负责人": row["项目负责人"],
                "项目成员": row["项目成员"],
                "级别": row["级别"],
                "立项时间": row["立项时间"],
                "结项时间": row["结项时间"],
                "验收结论": row["验收结论"],
                "教师姓名": row["教师姓名"],
                "工号": row["工号"],
                "教研项目工作量": row["教研项目工作量"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "first_class_courses":
        json_data_list = []
        for index, row in df.iterrows():
            json_data = {
                "序号": row["序号"],
                "课程性质": row["课程性质"],
                "内容": row["内容"],
                "负责人": row["负责人"],
                "备注": row["备注"],
                "教师姓名": row["教师姓名"],
                "工号": row["工号"],
                "一流课程工作量": row["一流课程工作量"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "public_service":
        json_data_list = []
        for index, row in df.iterrows():
            json_data = {
                "课程名称": row["课程名称"],
                "课程代码": row["课程代码"],
                "授课教师": row["授课教师"],
                "上课时间": row["上课时间"],
                "上课地点": row["上课地点"],
                "课程类型": row["课程类型"],
                "学分": row["学分"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "student_research":
        json_data_list = []
        for index, row in df.iterrows():
            # 创建一个项目的JSON数据字典
            json_data = {
                "序号": row["序号"],
                "项目名称": row["项目名称"],
                "级别": row["级别"],
                "负责人": row["负责人"],
                "学号": row["学号"],
                "项目组总人数": row["项目组总人数"],
                "指导老师": row["指导老师"],
                "指导老师工号": row["指导老师工号"],
                "验收结果": row["验收结果"],
                "工作量": row["工作量"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "teaching_achievement":
        json_data_list = []
        for index, row in df.iterrows():
            # 创建一个项目的JSON数据字典
            json_data = {
                "序号": row["序号"],
                "届": row["届"],
                "时间": row["时间"],
                "推荐成果名称": row["推荐成果名称"],
                "成果主要完成人名称": row["成果主要完成人名称"],
                "获奖类别": row["获奖类别"],
                "获奖等级": row["获奖等级"],
                "备注": row["备注"],
                "教师": row["教师"],
                "工号": row["工号"],
                "教学成果工作量": row["教学成果工作量"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "undergraduate_mentorship_system":
        json_data_list = []
        for index, row in df.iterrows():
            # 创建一个项目的JSON数据字典
            json_data = {
                "导师姓名": row["导师姓名"],
                "教工号": row["教工号"],
                "学生姓名": row["学生姓名"],
                "年级": row["年级"],
                "学号": row["学号"],
                "教师工作量": row["教师工作量"]
            }
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "undergraduate_thesis":
        json_data_list = []
        # 遍历数据框的每一行
        for index, row in df.iterrows():
            # 创建一个项目的JSON数据字典
            json_data = {
                "学生姓名": row["学生姓名"],
                "学生学号": row["学生学号"],
                "学院": row["学院"],
                "专业": row["专业"],
                "专业号": row["专业号"],
                "年级": row["年级"],
                "毕业论文题目": row["毕业论文题目"],
                "毕业论文成绩": row["毕业论文成绩"],
                "毕业论文指导老师": row["毕业论文指导老师"],
                "毕业论文指导老师工号": row["毕业论文指导老师工号"]
            }
            # 将该项目的JSON数据字典添加到json_data_list中
            json_data_list.append(json_data)
        return json_data_list
    elif worksheet == "undergraduate_workload_course_ranking":
        json_data_list = []

        # 遍历数据框的每一行
        for index, row in df.iterrows():
            # 创建一个项目的JSON数据字典
            json_data = {
                "学生姓名": row["学生姓名"],
                "学生学号": row["学生学号"],
                "学院": row["学院"],
                "专业": row["专业"],
                "专业号": row["专业号"],
                "年级": row["年级"],
                "毕业论文题目": row["毕业论文题目"],
                "毕业论文成绩": row["毕业论文成绩"],
                "毕业论文指导老师": row["毕业论文指导老师"],
                "毕业论文指导老师工号": row["毕业论文指导老师工号"]
            }
            # 将该项目的JSON数据字典添加到json_data_list中
            json_data_list.append(json_data)
            return json_data_list


# 处理好数据后直接导入
def process_work(worksheet, json_data_list):
    # 在这里对DataFrame进行操作，
    if worksheet == "undergraduate_workload_course_ranking":
        for json_data in json_data_list:
            UndergraduateWorkloadCourseRanking.add_UndergraduateWorkloadCourseRanking(json_data)
    elif worksheet == "undergraduate_thesis":
        for json_data in json_data_list:
            UndergraduateThesi.add_thesis_record(json_data)
    elif worksheet == "department_internship":
        for json_data in json_data_list:
            DepartmentInternship.add_internship_record(json_data)
    elif worksheet == "competition_awards":
        for json_data in json_data_list:
            # columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量","获奖年份"]
            CompetitionAward.add_competition_award(json_data)
    elif worksheet == "student_research":
        for json_data in json_data_list:
            # columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果","工作量"]
            StudentResearch.add_student_research_record(json_data)
    elif worksheet == "undergraduate_mentorship_system":
        for json_data in json_data_list:
            # columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
            UndergraduateMentorshipSystem.add_mentorship_record(json_data)
    elif worksheet == "educational_research_project":
        for json_data in json_data_list:
            # columns = ["序号", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
            #                    "教师姓名", "工号", "教研项目工作量"]
            EducationalResearchProject.add_research_project(json_data)
    elif worksheet == "first_class_courses":
        for json_data in json_data_list:
            # columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
            FirstClassCourse.add_first_class_course(json_data)
    elif worksheet == "teaching_achievement_awards":
        for json_data in json_data_list:
            # columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
            #   "工号", "教学成果工作量"]
            TeachingAchievementAward.add_teaching_achievement_record(json_data)
    elif worksheet == "public_services":
        for json_data in json_data_list:
            # columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号"]
            PublicService.add_public_service_record(json_data)


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

        # 在这里处理文件
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
        # 获取选定的表单名
        worksheet = request.form.get('selectedWorksheet')

        # 解析上传的文件变成json_data_list
        json_data_list = analyse_worksheet(file.filename, worksheet)
        # 处理文件
        process_work(worksheet, json_data_list)
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
        return render_template('file_upload.html')
