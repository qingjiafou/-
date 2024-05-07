# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from database import db


class CompetitionAward(db.Model):
    __tablename__ = 'competition_awards'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    event_name = db.Column(db.String(24), info='赛事名称')
    work_name = db.Column(db.String(24), info='作品名称')
    award_category = db.Column(db.String(24), info='获奖类别')
    award_level = db.Column(db.String(24), info='获奖等级')
    teacher_name = db.Column(db.String(24), info='指导教师')
    teacher_id = db.Column(db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='指导教师工号')
    total_workload = db.Column(db.Float(precision=6, asdecimal=True), info='总工作量')
    award_year = db.Column(db.String(24), info='获奖年份')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='CompetitionAward.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='competition_awards')


class DepartmentInternship(db.Model):
    __tablename__ = 'department_internship'

    student_name = db.Column(db.String(24), info='学生姓名')
    student_id = db.Column(db.String(24), primary_key=True, info='学生学号')
    major = db.Column(db.String(24), info='专业')
    grade = db.Column(db.String(24), info='年级')
    teacher_name = db.Column(db.String(24), info='学部内实习指导教师')
    teacher_id = db.Column(db.String(24),db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='学部内实习指导教师工号')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='DepartmentInternship.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='department_internships')


class EducationalResearchProject(db.Model):
    __tablename__ = 'educational_research_project'

    id = db.Column(db.Integer, primary_key=True, info='序号，主键')
    project_name = db.Column(db.String(24), info='项目名称')
    project_leader = db.Column(db.String(24), info='项目负责人')
    project_members = db.Column(db.String(24), info='项目成员')
    project_level = db.Column(db.String(24), info='级别')
    start_date = db.Column(db.Date, info='立项时间')
    end_date = db.Column(db.Date, info='结项时间')
    acceptance_result = db.Column(db.String(24), info='验收结论')
    teacher_name = db.Column(db.String(24), info='教师姓名')
    teacher_id = db.Column(db.String(24),db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True, info='工号')
    research_project_workload = db.Column(db.Float(precision=6, asdecimal=True), info='教研项目工作量')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='EducationalResearchProject.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='educational_research_projects')


class FirstClassCourse(db.Model):
    __tablename__ = 'first_class_courses'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    course_type = db.Column(db.String(24), info='课程性质')
    content = db.Column(db.String(24), info='内容')
    leader = db.Column(db.String(24), info='负责人')
    remark = db.Column(db.String(24), info='备注，工作量分配')
    teacher_name = db.Column(db.String(24), info='教师姓名，一位老师一个记录')
    teacher_id = db.Column(db.String(24),db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='工号，外键')
    first_class_course_workload = db.Column(db.Float(precision=6, asdecimal=True), info='一流课程工作量')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='FirstClassCourse.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='first_class_courses')


class PublicService(db.Model):
    __tablename__ = 'public_services'

    id = db.Column(db.Integer, primary_key=True, info='序号，主键，自增，无意义')
    serve_date = db.Column(db.String(24), info='日期')
    content = db.Column(db.String(24), info='内容')
    teacher_name = db.Column(db.String(24), info='姓名')
    work_duration = db.Column(db.Float(precision=6, asdecimal=True), info='工作时长')
    class_hours = db.Column(db.Float(precision=6, asdecimal=True), info='课时')
    teacher_id = db.Column(db.String(24),db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='教师工号，外键')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='PublicService.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='public_services')


class StudentResearch(db.Model):
    __tablename__ = 'student_research'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    project_name = db.Column(db.String(24), info='项目名称')
    project_level = db.Column(db.String(24), info='级别')
    leader = db.Column(db.String(24), info='负责人')
    student_id = db.Column(db.String(24), info='学号')
    total_members = db.Column(db.Integer, info='项目组总人数')
    teacher_name = db.Column(db.String(24), info='指导老师')
    teacher_id = db.Column(db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='指导老师工号')
    acceptance_result = db.Column(db.String(24), info='验收结果')
    workload = db.Column(db.Float(precision=6, asdecimal=True), info='工作量')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='StudentResearch.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='student_researches')


class TeachingAchievementAward(db.Model):
    __tablename__ = 'teaching_achievement_awards'

    id = db.Column(db.Integer, primary_key=True, info='序号，主键，自增，无意义')
    student_session = db.Column(db.String(24), info='届')
    student_date = db.Column(db.String(24), info='时间')
    recommended_achievement_name = db.Column(db.String(24), info='推荐成果名称')
    main_completion_person_name = db.Column(db.String(24), info='成果主要完成人名称')
    award_category = db.Column(db.String(24), info='获奖类别')
    award_level = db.Column(db.String(24), info='获奖等级')
    remark = db.Column(db.String(24), info='备注')
    teacher_name = db.Column(db.String(24), info='教师')
    teacher_id = db.Column(db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='工号，外键')
    teaching_achievement_workload = db.Column(db.Float(precision=6, asdecimal=True), info='教学成果工作量')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='TeachingAchievementAward.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='teaching_achievement_awards')


class UndergraduateMentorshipSystem(db.Model):
    __tablename__ = 'undergraduate_mentorship_system'

    teacher_name = db.Column(db.String(24), info='导师姓名')
    teacher_id = db.Column(db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='教工号')
    student_name = db.Column(db.String(24), info='学生姓名')
    grade = db.Column(db.String(24), info='年级')
    student_id = db.Column(db.String(24), primary_key=True, info='学号')
    teacher_workload = db.Column(db.Float(precision=6, asdecimal=True), info='教师工作量')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='UndergraduateMentorshipSystem.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='undergraduate_mentorship_systems')


class UndergraduateThesi(db.Model):
    __tablename__ = 'undergraduate_thesis'

    student_name = db.Column(db.String(24), info='学生姓名')
    student_id = db.Column(db.String(24), primary_key=True, info='学生学号')
    college = db.Column(db.String(24), info='学院')
    major = db.Column(db.String(24), info='专业')
    major_id = db.Column(db.String(24), info='专业号')
    grade = db.Column(db.String(24), info='年级')
    thesis_topic = db.Column(db.String(24), info='毕业论文题目')
    thesis_grade = db.Column(db.String(24), info='毕业论文成绩')
    teacher_name = db.Column(db.String(24), info='毕业论文指导老师')
    teacher_id = db.Column(db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True,
                           info='毕业论文指导老师工号')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='UndergraduateThesi.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='undergraduate_thesis')


class UndergraduateWorkloadCourseRanking(db.Model):
    __tablename__ = 'undergraduate_workload_course_ranking'

    # 修改字段类型和长度
    academic_year = db.Column(db.String(10), info='学年')
    semester = db.Column(db.String(10), info='学期')
    calendar_year = db.Column(db.Integer, info='自然年')
    half_year = db.Column(db.String(20), info='上下半年')
    course_code = db.Column(db.String(24), primary_key=True, nullable=False, info='课程号')
    teaching_class = db.Column(db.String(24), primary_key=True, nullable=False, info='教学班')
    course_name = db.Column(db.String(50), info='课程名称')  # 调整长度
    teacher_id = db.Column(db.String(20), db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'), index=True, info='教工号')  # 调整长度
    teacher_name = db.Column(db.String(30), info='教师名称')  # 调整长度
    seminar_hours = db.Column(db.Float, info='研讨学时')  # 调整类型为Float
    lecture_hours = db.Column(db.Float, info='授课学时')  # 调整类型为Float
    lab_hours = db.Column(db.Float, info='实验学时')  # 调整类型为Float
    enrolled_students = db.Column(db.Integer, info='选课人数')
    student_weight_coefficient_b = db.Column(db.Float, info='学生数量权重系数B')  # 调整类型为Float
    course_type_coefficient_a = db.Column(db.Float, info='课程类型系数A')  # 调整类型为Float
    total_lecture_hours_p1 = db.Column(db.Float, info='理论课总学时P1')  # 调整类型为Float
    lab_group_count = db.Column(db.Integer, info='实验分组数')
    lab_coefficient = db.Column(db.Float, info='实验课系数')  # 调整类型为Float
    total_lab_hours_p2 = db.Column(db.Float, info='实验课总学时P2')  # 调整类型为Float
    course_split_ratio_for_engineering_center = db.Column(db.Float, info='课程拆分占比（工程中心用）')  # 调整类型为Float
    total_undergraduate_course_hours = db.Column(db.Float, info='本科课程总学时')  # 调整类型为Float
    total_course_hours = db.Column(db.Float, info='课程总学时')  # 调整类型为Float

    # 修改外键关系设置
    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='UndergraduateWorkloadCourseRanking.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='undergraduate_workload_course_rankings')


class UndergraduateWorkloadTeacherRanking(db.Model):
    __tablename__ = 'undergraduate_workload_teacher_ranking'

    teacher_id = db.Column(db.String(56), primary_key=True, info='教工号')
    teacher_name = db.Column(db.String(12), info='教师名称')
    undergraduate_course_total_hours = db.Column(db.Double(6, True), info='本科课程总学时')
    total_course_hours = db.Column(db.Double(6, True), info='课程总学时')
    graduation_thesis_student_count = db.Column(db.Integer, info='毕业论文学生人数')
    graduation_thesis_p = db.Column(db.Double(6, True), info='毕业论文P')
    teaching_internship_student_count = db.Column(db.Integer, info='指导教学实习人数')
    teaching_internship_weeks = db.Column(db.Integer, info='指导教学实习周数')
    teaching_internship_p = db.Column(db.Double(6, True), info='指导教学实习P')
    responsible_internship_construction_management_p = db.Column(db.Double(6, True), info='负责实习点建设与管理P')
    guiding_undergraduate_competition_p = db.Column(db.Double(6, True), info='指导本科生竞赛P')
    guiding_undergraduate_research_p = db.Column(db.Double(6, True), info='指导本科生科研P')
    undergraduate_tutor_system = db.Column(db.Double(6, True), info='本科生导师制')
    teaching_research_and_reform_p = db.Column(db.Double(6, True), info='教研教改P')
    first_class_course = db.Column(db.Double(6, True), info='一流课程')
    teaching_achievement_award = db.Column(db.Double(6, True), info='教学成果奖')
    public_service = db.Column(db.Double(6, True), info='公共服务')
