# 导入蓝图
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from version_four.models import CompetitionAward, DepartmentInternship, \
    EducationalResearchProject, FirstClassCourse, PublicService, StudentResearch, TeachingAchievementAward, \
    UndergraduateMentorshipSystem, UndergraduateThesi, UndergraduateWorkloadCourseRanking

"""
实例化蓝图对象
第一个参数：蓝图名称
第二个参数：导入蓝图的名称
第三个参数：蓝图前缀，该蓝图下的路由规则前缀都需要加上这个
"""
modify_page_blueprint = Blueprint('modify_page', __name__,template_folder='templates')


# 用蓝图注册路由
@modify_page_blueprint.route("/modify_page/all", methods=['POST', 'GET'])
@login_required
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
        result = [record.UndergraduateWorkloadCourseRanking_list(results) for record in results]
        columns = ["学年", "学期", "自然年", "上下半年", "课程号", "教学班", "课程名称", "教工号", "教师名称",
                   "研讨学时", "授课学时", "实验学时", "选课人数", "学生数量权重系数B", "课程类型系数A",
                   "理论课总学时P1", "实验分组数", "实验课系数", "实验课总学时P2", "课程拆分占比（工程中心用）",
                   "课程总学时"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_thesis":
        table_name = "毕业论文"
        results = UndergraduateThesi.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.UndergraduateThesi_list(results) for record in results]
        columns = ["学生姓名", "学生学号", "学院", "专业", "专业号", "年级", "毕业论文题目", "毕业论文成绩",
                   "毕业论文指导老师", "毕业论文指导老师工号"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "department_internship":
        table_name = "本科实习"
        results = DepartmentInternship.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.DepartmentInternship_list(results) for record in results]
        columns = ["学生姓名", "学生学号", "专业", "年级", "学部内实习指导教师", "学部内实习指导教师工号", "实习周数"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "competition_awards":
        table_name = "学生竞赛"
        results = CompetitionAward.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.CompetitionAward_list(results) for record in results]
        columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量",
                   "获奖年份"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "student_research":
        table_name = "学生科研"
        results = StudentResearch.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.StudentResearch_list(results) for record in results]
        columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果",
                   "工作量"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "undergraduate_mentorship_system":
        table_name = "本科生导师制"
        results = UndergraduateMentorshipSystem.query.filter_by(teacher_id=teacher_id,
                                                                teacher_name=teacher_name).all()
        result = [record.UndergraduateMentorshipSystem_list(results) for record in results]
        columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "educational_research_project":
        table_name = "教研项目"
        results = EducationalResearchProject.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.EducationalResearchProject_list(results) for record in results]
        columns = ["序号", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
                   "教师姓名", "工号", "教研项目工作量"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "first_class_courses":
        table_name = "一流课程"
        results = FirstClassCourse.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.FirstClassCourse_list(results) for record in results]
        columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "teaching_achievement_awards":
        table_name = "教学成果奖"
        results = TeachingAchievementAward.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.TeachingAchievementAward_list(results) for record in results]
        columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
                   "工号", "教学成果工作量"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    elif worksheet == "public_services":
        table_name = "公共服务"
        results = PublicService.query.filter_by(teacher_id=teacher_id, teacher_name=teacher_name).all()
        result = [record.PublicService_list(results) for record in results]
        columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号", "工作量"]
        return render_template('modify_page.html', result=result[0], table_name=table_name, columns=columns)
    return render_template('modify_page.html')


@modify_page_blueprint.route("/modify_page/update", methods=['POST', 'GET'])
@login_required
def update():
    if request.method == 'POST':
        # 获取前端发送的 JSON 数据
        json_data = request.get_json()
        if json_data:
            table_name = json_data["表名"]
            if table_name == "本科工作量课程排序表":
                UndergraduateWorkloadCourseRanking.update_UndergraduateWorkloadCourseRanking_list(json_data)
                return render_template('modify_page.html')
            elif table_name == "毕业论文":
                UndergraduateThesi.update_UndergraduateThesi(json_data)
                return render_template('modify_page.html')
            elif table_name == "本科实习":
                DepartmentInternship.update_DepartmentInternship(json_data)
                return render_template('modify_page.html')
            elif table_name == "学生竞赛":
                # columns = ["序号", "赛事名称", "作品名称", "获奖类别", "获奖等级", "指导教师", "指导教师工号", "总工作量","获奖年份"]
                CompetitionAward.update_CompetitionAward(json_data)
                return render_template('modify_page.html')
            elif table_name == "学生科研":
                # columns = ["序号", "项目名称", "级别", "负责人", "学号", "项目组总人数", "指导老师", "指导老师工号", "验收结果","工作量"]
                StudentResearch.update_StudentResearch(json_data)
                return render_template('modify_page.html')
            elif table_name == "本科生导师制":
                # columns = ["导师姓名", "教工号", "学生姓名", "年级", "学号", "教师工作量"]
                UndergraduateMentorshipSystem.update_UndergraduateMentorshipSystem(json_data)
                return render_template('modify_page.html')
            elif table_name == "教研项目":
                # columns = ["序号", "项目名称", "项目负责人", "项目成员", "级别", "立项时间", "结项时间", "验收结论",
                #                    "教师姓名", "工号", "教研项目工作量"]
                EducationalResearchProject.update_EducationalResearchProject(json_data)
                return render_template('modify_page.html')
            elif table_name == "一流课程":
                # columns = ["序号", "课程性质", "内容", "负责人", "备注", "教师姓名", "工号", "一流课程工作量"]
                FirstClassCourse.update_FirstClassCourse(json_data)
                return render_template('modify_page.html')
            elif table_name == "教学成果奖":
                # columns = ["序号", "届", "时间", "推荐成果名称", "成果主要完成人名称", "获奖类别", "获奖等级", "备注", "教师",
                #   "工号", "教学成果工作量"]
                TeachingAchievementAward.update_TeachingAchievementAward(json_data)
                return render_template('modify_page.html')
            elif table_name == "公共服务":
                # columns = ["序号", "日期", "内容", "姓名", "工作时长", "课时", "教师工号"]
                PublicService.update_PublicService(json_data)
                return render_template('modify_page.html')
        else:
            print("NO DATA")
        # 在这里处理接收到的 JSON 数据
        # 返回响应，这里返回一个简单的字符串
        return render_template('modify_page.html')
