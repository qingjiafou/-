# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from database import db
from sqlalchemy import event, func
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TeacherInformation(Base, UserMixin):
    __tablename__ = 'teacher_information'

    teacher_id = db.Column(db.String(255), primary_key=True, info={'description': '教工号'})
    teacher_name = db.Column(db.String(255), info={'description': '教师姓名'})
    password_hash = db.Column(db.String(255), info={'description': 'hash密码'})

    @property
    def password(self):
        raise ArithmeticError("password是不可读字段")

    # 设置密码，加密，比如,xxx.password=xxxx
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.teacher_id  # 使用 teacher_id 作为用户 ID

    @classmethod
    def add_teacher_info(cls, teacher_id, teacher_name, password):
        new_teacher_info = cls(
        )
        new_teacher_info.teacher_id = teacher_id
        new_teacher_info.teacher_name = teacher_name
        new_teacher_info.password = password  # 使用 setter 进行密码哈希
        db.session.add(new_teacher_info)
        db.session.commit()


class CompetitionAward(Base):
    __tablename__ = 'competition_awards'
    id = db.Column(db.Integer, primary_key=True, info={'description': '序号'})
    event_name = db.Column(db.String(24), info={'description': '赛事名称'})
    work_name = db.Column(db.String(24), info={'description': '作品名称'})
    award_category = db.Column(db.String(24), info={'description': '获奖类别'})
    award_level = db.Column(db.String(24), info={'description': '获奖等级'})
    teacher_name = db.Column(db.String(24), info={'description': '指导教师'})
    teacher_id = db.Column(db.String(24), db.ForeignKey('teacher_information.teacher_id'), index=True,
                           info={'description': '指导教师工号'})
    total_workload = db.Column(db.Float(precision=6, asdecimal=True), info={'description': '总工作量'})
    award_year = db.Column(db.String(24), info={'description': '获奖年份'})

    teacher = db.relationship('TeacherInformation', backref='competition_awards')

    @classmethod
    def CompetitionAward_list(cls):
        return cls.query.all()

    @staticmethod
    def add_competition_award(json_data):
        new_award = CompetitionAward(
            id=json_data["序号"],
            event_name=json_data["赛事名称"],
            work_name=json_data["作品名称"],
            award_category=json_data["获奖类别"],
            award_level=json_data["获奖等级"],
            teacher_name=json_data["指导教师"],
            teacher_id=json_data["指导教师工号"],
            total_workload=json_data["总工作量"],
            award_year=json_data["获奖年份"]
        )
        db.session.add(new_award)
        db.session.commit()

    @staticmethod
    def update_CompetitionAward(json_data):
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


class DepartmentInternship(Base):
    __tablename__ = 'department_internship'

    student_name = db.Column(db.String(24), info={'description': '学生姓名'})
    student_id = db.Column(db.String(24), primary_key=True, info={'description': '学生学号'})
    major = db.Column(db.String(24), info={'description': '专业'})
    grade = db.Column(db.String(24), info={'description': '年级'})
    teacher_name = db.Column(db.String(24), info={'description': '学部内实习指导教师'})
    teacher_id = db.Column(db.String(24), db.ForeignKey('teacher_information.teacher_id'),
                           index=True, info={'description': '学部内实习指导教师工号'})
    week = db.Column(db.String(24), info={'description': '实习周数'})
    teacher = db.relationship('TeacherInformation',
                              primaryjoin='DepartmentInternship.teacher_id == TeacherInformation.teacher_id',
                              backref='department_internships')

    @classmethod
    def DepartmentInternship_list(self):
        return [self.student_name, self.student_id, self.major, self.grade, self.teacher_name, self.teacher_id]

    @staticmethod
    def add_internship_record(json_data):
        new_internship = DepartmentInternship(
            student_name=json_data["学生姓名"],
            student_id=json_data["学生学号"],
            major=json_data["专业"],
            grade=json_data["年级"],
            teacher_name=json_data["学部内实习指导教师"],
            teacher_id=json_data["学部内实习指导教师工号"],
            week=json_data["实习周数"]
        )
        db.session.add(new_internship)
        db.session.commit()

    @staticmethod
    def update_DepartmentInternship(json_data):
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


class EducationalResearchProject(Base):
    __tablename__ = 'educational_research_project'

    id = db.Column(db.Integer, primary_key=True, info={'description': '序号，主键'})
    project_name = db.Column(db.String(24), info={'description': '项目名称'})
    project_leader = db.Column(db.String(24), info={'description': '项目负责人'})
    project_members = db.Column(db.String(24), info={'description': '项目成员'})
    project_level = db.Column(db.String(24), info={'description': '级别'})
    start_date = db.Column(db.Date, info={'description': '立项时间'})
    end_date = db.Column(db.Date, info={'description': '结项时间'})
    acceptance_result = db.Column(db.String(24), info={'description': '验收结论'})
    teacher_name = db.Column(db.String(24), info={'description': '教师姓名'})
    teacher_id = db.Column(db.String(24), db.ForeignKey('teacher_information.teacher_id'),
                           index=True, info={'description': '工号'})
    research_project_workload = db.Column(db.Float(precision=6, asdecimal=True),
                                          info={'description': '教研项目工作量'})

    teacher = db.relationship('TeacherInformation',
                              primaryjoin='EducationalResearchProject.teacher_id == TeacherInformation.teacher_id',
                              backref='educational_research_projects')

    @classmethod
    def EducationalResearchProject_list(self):
        return [
            self.id,
            self.project_name, self.project_leader, self.project_members, self.project_level, self.start_date,
            self.end_date, self.acceptance_result, self.teacher_name, self.teacher_id, self.research_project_workload
        ]

    @staticmethod
    def add_research_project(json_data):
        new_project = EducationalResearchProject(
            id=json_data["序号"],
            project_name=json_data["项目名称"],
            project_leader=json_data["项目负责人"],
            project_members=json_data["项目成员"],
            project_level=json_data["级别"],
            start_date=json_data["立项时间"],
            end_date=json_data["结项时间"],
            acceptance_result=json_data["验收结论"],
            teacher_name=json_data["教师姓名"],
            teacher_id=json_data["工号"],
            research_project_workload=json_data["教研项目工作量"]
        )
        db.session.add(new_project)
        db.session.commit()

    @staticmethod
    def update_EducationalResearchProject(json_data):
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


class FirstClassCourse(Base):
    __tablename__ = 'first_class_courses'

    id = db.Column(db.Integer, primary_key=True, info={'description': '序号'})
    course_type = db.Column(db.String(24), info={'description': '课程性质'})
    content = db.Column(db.String(24), info={'description': '内容'})
    leader = db.Column(db.String(24), info={'description': '负责人'})
    remark = db.Column(db.String(24), info={'description': '备注，工作量分配'})
    teacher_name = db.Column(db.String(24), info={'description': '教师姓名，一位老师一个记录'})
    teacher_id = db.Column(db.String(24), db.ForeignKey('teacher_information.teacher_id'),
                           index=True, info={'description': '工号，外键'})
    first_class_course_workload = db.Column(db.Float(precision=6, asdecimal=True),
                                            info={'description': '一流课程工作量'})

    teacher = db.relationship('TeacherInformation',
                              primaryjoin='FirstClassCourse.teacher_id == TeacherInformation.teacher_id',
                              backref='first_class_courses')

    @classmethod
    def FirstClassCourse_list(self):
        return [
            self.id,
            self.course_type,
            self.content,
            self.leader,
            self.remark,
            self.teacher_name,
            self.teacher_id,
            self.first_class_course_workload,
        ]

    @staticmethod
    def add_first_class_course(json_data):
        new_course = FirstClassCourse(
            id=json_data["序号"],
            course_type=json_data["课程性质"],
            content=json_data["内容"],
            leader=json_data["负责人"],
            remark=json_data["备注"],
            teacher_name=json_data["教师姓名"],
            teacher_id=json_data["工号"],
            first_class_course_workload=json_data["一流课程工作量"]
        )
        db.session.add(new_course)
        db.session.commit()

    @staticmethod
    def update_FirstClassCourse(json_data):
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


class PublicService(Base):
    __tablename__ = 'public_services'

    id = db.Column(db.Integer, primary_key=True, info={'description': '序号，主键，自增，无意义'})
    serve_date = db.Column(db.String(24), info={'description': '日期'})
    content = db.Column(db.String(24), info={'description': '内容'})
    teacher_name = db.Column(db.String(24), info={'description': '姓名'})
    work_duration = db.Column(db.Float(precision=6, asdecimal=True), info={'description': '工作时长'})
    class_hours = db.Column(db.Float(precision=6, asdecimal=True), info={'description': '课时'})
    teacher_id = db.Column(db.String(24), db.ForeignKey('teacher_information.teacher_id'),
                           index=True, info={'description': '教师工号，外键'})
    workload = db.Column(db.Float, info={'description': '工作量'})
    teacher = db.relationship('TeacherInformation',
                              primaryjoin='PublicService.teacher_id == TeacherInformation.teacher_id',
                              backref='public_services')

    @classmethod
    def PublicService_list(self):
        return [
            self.id,
            self.serve_date,
            self.content,
            self.teacher_name,
            self.work_duration,
            self.class_hours,
            self.teacher_id
        ]

    @staticmethod
    def add_public_service_record(json_data):
        new_record = PublicService(
            id=json_data["序号"],
            serve_date=json_data["日期"],
            content=json_data["内容"],
            teacher_name=json_data["姓名"],
            work_duration=json_data["工作时长"],
            class_hours=json_data["课时"],
            teacher_id=json_data["教师工号"],
            workload=json_data["工作量"]
        )
        db.session.add(new_record)
        db.session.commit()

    @staticmethod
    def update_PublicService(json_data):
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


class StudentResearch(Base):
    __tablename__ = 'student_research'

    id = db.Column(db.Integer, primary_key=True, info={'description': '序号'})
    project_name = db.Column(db.String(24), info={'description': '项目名称'})
    project_level = db.Column(db.String(24), info={'description': '级别'})
    leader = db.Column(db.String(24), info={'description': '负责人'})
    student_id = db.Column(db.String(24), info={'description': '学号'})
    total_members = db.Column(db.Integer, info={'description': '项目组总人数'})
    teacher_name = db.Column(db.String(24), info={'description': '指导老师'})
    teacher_id = db.Column(db.ForeignKey('teacher_information.teacher_id'), index=True,
                           info={'description': '指导老师工号'})
    acceptance_result = db.Column(db.String(24), info={'description': '验收结果'})
    workload = db.Column(db.Float(precision=6, asdecimal=True), info={'description': '工作量'})

    teacher = db.relationship('TeacherInformation',
                              primaryjoin='StudentResearch.teacher_id == TeacherInformation.teacher_id',
                              backref='student_researches')

    @classmethod
    def StudentResearch_list(self):
        return [
            self.id, self.project_name, self.project_level,
            self.leader, self.student_id, self.total_members,
            self.teacher_name, self.teacher_id, self.acceptance_result,
            self.workload
        ]

    @staticmethod
    def add_student_research_record(json_data):
        new_record = StudentResearch(
            id=json_data["序号"],
            project_name=json_data["项目名称"],
            project_level=json_data["级别"],
            leader=json_data["负责人"],
            student_id=json_data["学号"],
            total_members=json_data["项目组总人数"],
            teacher_name=json_data["指导老师"],
            teacher_id=json_data["指导老师工号"],
            acceptance_result=json_data["验收结果"],
            workload=json_data["工作量"]
        )
        db.session.add(new_record)
        db.session.commit()

    @staticmethod
    def update_StudentResearch(json_data):
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


class TeachingAchievementAward(Base):
    __tablename__ = 'teaching_achievement_awards'

    id = db.Column(db.Integer, primary_key=True, info={'description': '序号，主键，自增，无意义'})
    student_session = db.Column(db.String(24), info={'description': '届'})
    student_date = db.Column(db.String(24), info={'description': '时间'})
    recommended_achievement_name = db.Column(db.String(24), info={'description': '推荐成果名称'})
    main_completion_person_name = db.Column(db.String(24), info={'description': '成果主要完成人名称'})
    award_category = db.Column(db.String(24), info={'description': '获奖类别'})
    award_level = db.Column(db.String(24), info={'description': '获奖等级'})
    remark = db.Column(db.String(24), info={'description': '备注'})
    teacher_name = db.Column(db.String(24), info={'description': '教师'})
    teacher_id = db.Column(db.ForeignKey('teacher_information.teacher_id'), index=True,
                           info={'description': '工号，外键'})
    teaching_achievement_workload = db.Column(db.Float(precision=6, asdecimal=True),
                                              info={'description': '教学成果工作量'})

    teacher = db.relationship('TeacherInformation',
                              primaryjoin='TeachingAchievementAward.teacher_id == TeacherInformation.teacher_id',
                              backref='teaching_achievement_awards')

    @classmethod
    def TeachingAchievementAward_list(self):
        return [
            self.id, self.student_session, self.student_date,
            self.recommended_achievement_name, self.main_completion_person_name,
            self.award_category, self.award_level, self.remark,
            self.teacher_name, self.teacher_id, self.teaching_achievement_workload
        ]

    @staticmethod
    def add_teaching_achievement_record(json_data):
        new_record = TeachingAchievementAward(
            id=json_data["序号"],
            student_session=json_data["届"],
            student_date=json_data["时间"],
            recommended_achievement_name=json_data["推荐成果名称"],
            main_completion_person_name=json_data["成果主要完成人名称"],
            award_category=json_data["获奖类别"],
            award_level=json_data["获奖等级"],
            remark=json_data["备注"],
            teacher_name=json_data["教师"],
            teacher_id=json_data["工号"],
            teaching_achievement_workload=json_data["教学成果工作量"]
        )
        db.session.add(new_record)
        db.session.commit()

    @staticmethod
    def update_TeachingAchievementAward(json_data):
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


class UndergraduateMentorshipSystem(Base):
    __tablename__ = 'undergraduate_mentorship_system'

    teacher_name = db.Column(db.String(24), info={'description': '导师姓名'})
    teacher_id = db.Column(db.ForeignKey('teacher_information.teacher_id'), index=True,
                           info={'description': '教工号'})
    student_name = db.Column(db.String(24), info={'description': '学生姓名'})
    grade = db.Column(db.String(24), info={'description': '年级'})
    student_id = db.Column(db.String(24), primary_key=True, info={'description': '学号'})
    teacher_workload = db.Column(db.Float(precision=6, asdecimal=True), info={'description': '教师工作量'})

    teacher = db.relationship('TeacherInformation',
                              primaryjoin='UndergraduateMentorshipSystem.teacher_id == TeacherInformation.teacher_id',
                              backref='undergraduate_mentorship_systems')

    @classmethod
    def UndergraduateMentorshipSystem_list(self):
        return [
            self.teacher_name, self.teacher_id, self.student_name,
            self.grade, self.student_id, self.teacher_workload
        ]

    @staticmethod
    def add_mentorship_record(json_data):
        new_record = UndergraduateMentorshipSystem(
            teacher_name=json_data["导师姓名"],
            teacher_id=json_data["教工号"],
            student_name=json_data["学生姓名"],
            grade=json_data["年级"],
            student_id=json_data["学号"],
            teacher_workload=json_data["教师工作量"]
        )
        db.session.add(new_record)
        db.session.commit()

    @staticmethod
    def update_UndergraduateMentorshipSystem(json_data):
        new_UndergraduateMentorshipSystem = UndergraduateMentorshipSystem.query.filter_by(
            student_id=json_data["学号"]).first()
        new_UndergraduateMentorshipSystem.teacher_name = json_data["导师姓名"]
        new_UndergraduateMentorshipSystem.teacher_id = json_data["教工号"]
        new_UndergraduateMentorshipSystem.student_name = json_data["学生姓名"]
        new_UndergraduateMentorshipSystem.grade = json_data["年级"]
        new_UndergraduateMentorshipSystem.teacher_workload = json_data["教师工作量"]
        db.session.add(new_UndergraduateMentorshipSystem)
        db.session.commit()


class UndergraduateThesi(Base):
    __tablename__ = 'undergraduate_thesis'

    student_name = db.Column(db.String(24), info={'description': '学生姓名'})
    student_id = db.Column(db.String(24), primary_key=True, info={'description': '学生学号'})
    college = db.Column(db.String(24), info={'description': '学院'})
    major = db.Column(db.String(24), info={'description': '专业'})
    major_id = db.Column(db.String(24), info={'description': '专业号'})
    grade = db.Column(db.String(24), info={'description': '年级'})
    thesis_topic = db.Column(db.String(24), info={'description': '毕业论文题目'})
    thesis_grade = db.Column(db.String(24), info={'description': '毕业论文成绩'})
    teacher_name = db.Column(db.String(24), info={'description': '毕业论文指导老师'})
    teacher_id = db.Column(db.ForeignKey('teacher_information.teacher_id'), index=True,
                           info={'description': '毕业论文指导老师工号'})

    teacher = db.relationship('TeacherInformation',
                              primaryjoin='UndergraduateThesi.teacher_id == TeacherInformation.teacher_id',
                              backref='undergraduate_thesis')

    @classmethod
    def UndergraduateThesi_list(self):
        return [
            self.student_name, self.student_id, self.college, self.major, self.major_id,
            self.grade, self.thesis_topic, self.thesis_grade, self.teacher_name, self.teacher_id
        ]

    @staticmethod
    def add_thesis_record(json_data):
        new_record = UndergraduateThesi(
            student_name=json_data["学生姓名"],
            student_id=json_data["学生学号"],
            college=json_data["学院"],
            major=json_data["专业"],
            major_id=json_data["专业号"],
            grade=json_data["年级"],
            thesis_topic=json_data["毕业论文题目"],
            thesis_grade=json_data["毕业论文成绩"],
            teacher_name=json_data["毕业论文指导老师"],
            teacher_id=json_data["毕业论文指导老师工号"]
        )
        db.session.add(new_record)
        db.session.commit()

    @staticmethod
    def update_UndergraduateThesi(json_data):
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


class UndergraduateWorkloadCourseRanking(Base):
    __tablename__ = 'undergraduate_workload_course_ranking'

    academic_year = db.Column(db.String(10), info={'description': '学年'})
    semester = db.Column(db.String(10), info={'description': '学期'})
    calendar_year = db.Column(db.Integer, info={'description': '自然年'})
    half_year = db.Column(db.String(20), info={'description': '上下半年'})
    course_code = db.Column(db.String(24), primary_key=True, nullable=False, info={'description': '课程号'})
    teaching_class = db.Column(db.String(24), primary_key=True, nullable=False, info={'description': '教学班'})
    course_name = db.Column(db.String(100), info={'description': '课程名称'})  # 调整长度
    teacher_id = db.Column(db.String(30), db.ForeignKey('teacher_information.teacher_id'),
                           index=True, info={'description': '教工号'})  # 调整长度
    teacher_name = db.Column(db.String(50), info={'description': '教师名称'})  # 调整长度
    seminar_hours = db.Column(db.Float, info={'description': '研讨学时'})  # 调整类型为Float
    lecture_hours = db.Column(db.Float, info={'description': '授课学时'})  # 调整类型为Float
    lab_hours = db.Column(db.Float, info={'description': '实验学时'})  # 调整类型为Float
    enrolled_students = db.Column(db.Integer, info={'description': '选课人数'})
    student_weight_coefficient_b = db.Column(db.Float, info={'description': '学生数量权重系数B'})  # 调整类型为Float
    course_type_coefficient_a = db.Column(db.Float, info={'description': '课程类型系数A'})  # 调整类型为Float
    total_lecture_hours_p1 = db.Column(db.Float, info={'description': '理论课总学时P1'})  # 调整类型为Float
    lab_group_count = db.Column(db.Integer, info={'description': '实验分组数'})
    lab_coefficient = db.Column(db.Float, info={'description': '实验课系数'})  # 调整类型为Float
    total_lab_hours_p2 = db.Column(db.Float, info={'description': '实验课总学时P2'})  # 调整类型为Float
    course_split_ratio_for_engineering_center = db.Column(db.Float, info={
        'description': '课程拆分占比（工程中心用）'})  # 调整类型为Float
    total_course_hours = db.Column(db.Float, info={'description': '课程总学时'})  # 调整类型为Float

    # 修改外键关系设置
    teacher = db.relationship('TeacherInformation',
                              primaryjoin='UndergraduateWorkloadCourseRanking.teacher_id == TeacherInformation.teacher_id',
                              backref='undergraduate_workload_course_rankings')

    @classmethod
    def UndergraduateWorkloadCourseRanking_list(self):
        return [
            self.academic_year, self.semester, self.calendar_year, self.half_year, self.course_code,
            self.teaching_class, self.course_name, self.teacher_id, self.teacher_name, self.seminar_hours,
            self.lecture_hours, self.lab_hours, self.enrolled_students, self.student_weight_coefficient_b,
            self.course_type_coefficient_a, self.total_lecture_hours_p1, self.lab_group_count, self.lab_coefficient,
            self.total_lab_hours_p2, self.course_split_ratio_for_engineering_center,
            self.total_course_hours
        ]

    @staticmethod
    def add_UndergraduateWorkloadCourseRanking(json_data):
        new_course_ranking = UndergraduateWorkloadCourseRanking(
            academic_year=json_data["学年"],
            semester=json_data["学期"],
            calendar_year=json_data["自然年"],
            half_year=json_data["上下半年"],
            course_code=json_data["课程号"],
            teaching_class=json_data["教学班"],
            course_name=json_data["课程名称"],
            teacher_id=json_data["教工号"],
            teacher_name=json_data["教师名称"],
            seminar_hours=json_data["研讨学时"],
            lecture_hours=json_data["授课学时"],
            lab_hours=json_data["实验学时"],
            enrolled_students=json_data["选课人数"],
            student_weight_coefficient_b=json_data["学生数量权重系数B"],
            course_type_coefficient_a=json_data["课程类型系数A"],
            total_lecture_hours_p1=json_data["理论课总学时P1"],
            lab_group_count=json_data["实验分组数"],
            lab_coefficient=json_data["实验课系数"],
            total_lab_hours_p2=json_data["实验课总学时P2"],
            course_split_ratio_for_engineering_center=json_data["课程拆分占比（工程中心用）"],
            total_course_hours=json_data["课程总学时"]
        )
        db.session.add(new_course_ranking)
        db.session.commit()

    @staticmethod
    def update_UndergraduateWorkloadCourseRanking_list(json_data):
        new_workload_course_ranking = UndergraduateWorkloadCourseRanking.query.filter_by(
            course_code=json_data["课程号"],
            teaching_class=json_data["教学班"]
        ).first()

        if not new_workload_course_ranking:
            new_workload_course_ranking = UndergraduateWorkloadCourseRanking(
                course_code=json_data["课程号"],
                teaching_class=json_data["教学班"]
            )

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
        new_workload_course_ranking.course_split_ratio_for_engineering_center = json_data["课程拆分占比（工程中心用）"]
        new_workload_course_ranking.total_course_hours = json_data["课程总学时"]
        new_workload_course_ranking.teacher_id = json_data["教工号"]
        new_workload_course_ranking.teacher_name = json_data["教师名称"]

        db.session.add(new_workload_course_ranking)
        db.session.commit()


class UndergraduateWorkloadTeacherRanking(Base):
    __tablename__ = 'undergraduate_workload_teacher_ranking'

    id = db.Column(db.Integer, primary_key=True, info={'description': '序号，主键，自增，无意义'})
    teacher_id = db.Column(db.String(30), db.ForeignKey('teacher_information.teacher_id'),
                           info={'description': '教工号'})
    teacher_name = db.Column(db.String(50), info={'description': '教师名称'})  # 调整长度
    undergraduate_course_total_hours = db.Column(db.Float, info={'description': '本科课程总学时'})
    graduation_thesis_student_count = db.Column(db.Integer, info={'description': '毕业论文学生人数'})
    graduation_thesis_p = db.Column(db.Float, info={'description': '毕业论文P'})
    teaching_internship_student_count = db.Column(db.Integer, info={'description': '指导教学实习人数'})
    teaching_internship_weeks = db.Column(db.Integer, info={'description': '指导教学实习周数'})
    teaching_internship_p = db.Column(db.Float, info={'description': '指导教学实习P'})
    responsible_internship_construction_management_p = db.Column(db.Float,
                                                                 info={'description': '负责实习点建设与管理P'})
    guiding_undergraduate_competition_p = db.Column(db.Float, info={'description': '指导本科生竞赛P'})
    guiding_undergraduate_research_p = db.Column(db.Float, info={'description': '指导本科生科研P'})
    undergraduate_tutor_system = db.Column(db.Float, info={'description': '本科生导师制'})
    teaching_research_and_reform_p = db.Column(db.Float, info={'description': '教研教改P'})
    first_class_course = db.Column(db.Float, info={'description': '一流课程'})
    teaching_achievement_award = db.Column(db.Float, info={'description': '教学成果奖'})
    public_service = db.Column(db.Float, info={'description': '公共服务'})
    # 修改外键关系设置
    teacher = db.relationship('TeacherInformation',
                              primaryjoin='UndergraduateWorkloadTeacherRanking.teacher_id == TeacherInformation.teacher_id',
                              backref='undergraduate_workload_teacher_ranking')

    @classmethod
    def UndergraduateWorkloadTeacherRanking_list(self):
        return [
            self.teacher_id, self.teacher_name,
            self.undergraduate_course_total_hours,
            self.graduation_thesis_student_count, self.graduation_thesis_p,
            self.teaching_internship_student_count, self.teaching_internship_weeks,
            self.teaching_internship_p, self.responsible_internship_construction_management_p,
            self.guiding_undergraduate_competition_p, self.guiding_undergraduate_research_p,
            self.undergraduate_tutor_system, self.teaching_research_and_reform_p,
            self.first_class_course, self.teaching_achievement_award, self.public_service
        ]



class workload_parameter(Base):
    __tablename__ = 'workload_parameter'

    id = db.Column(db.Integer, primary_key=True, info={'description': '序号'})
    graduation_thesis_p_count = db.Column(db.Float, info={'description': '毕业论文参数'})
    intership_count = db.Column(db.Float, info={'description': '指导实习参数'})
    intership_js = db.Column(db.Float, info={'description': '实习点建设'})


# 触发器


def update_undergraduate_course_total_hours(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.total_course_hours)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


def update_graduation_thesis_info(mapper, connection, target):
    session = Session(bind=connection)
    teacher_id = target.teacher_id

    # 更新毕业论文学生数量
    graduation_thesis_student_count = (
        session.query(func.count(mapper.c.student_id))
        .filter(mapper.c.teacher_id == teacher_id)
        .scalar()
    )

    # 查询毕业论文工作量参数
    graduation_thesis_p_count = session.query(workload_parameter.graduation_thesis_p_count).scalar()

    # 计算毕业论文工作量
    graduation_thesis_p = graduation_thesis_p_count * graduation_thesis_student_count

    # 查询该教师的记录
    teacher = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=teacher_id).one()

    # 更新毕业论文学生数量字段
    teacher.graduation_thesis_student_count = graduation_thesis_student_count

    # 更新毕业论文工作量字段
    teacher.graduation_thesis_p = graduation_thesis_p

    session.commit()


def update_teaching_internship_student_info(mapper, connection, target):
    session = Session(bind=connection)
    teacher_id = target.teacher_id
    # 更新指导教学实习的人数
    internship_student_count = session.query(
        func.count(mapper.c.student_id).filter(mapper.c.teacher_id == teacher_id).scalar())
    # 更新指导教学实习的周数
    internship_week_count = session.query(
        func.sum(mapper.c.week).filter(mapper.c.teacher_id == teacher_id).scalar())
    # 查询教学实习指导的参数
    internship_count = session.query(workload_parameter.internship_count).scalar()
    # 查询教学实习点的建设与管理P，这个直接查表得到
    internship_js = session.query(workload_parameter.internship_js).scalar()
    # 更新指导教学实习P
    teaching_internship_student_count = internship_student_count * internship_week_count * internship_count
    # 查询该教师的记录并更新
    teacher = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=teacher_id).one()
    teacher.teaching_internship_student_count = internship_student_count
    teacher.teaching_internship_weeks = internship_week_count
    teacher.teaching_internship_p = teaching_internship_student_count
    teacher.responsible_internship_construction_management_p = internship_js
    session.commit()


def update_guiding_undergraduate_competition_p(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.total_workload)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


def update_guiding_undergraduate_research_p(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.workload)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


def update_undergraduate_tutor_system(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.teacher_workload)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


def update_teaching_research_and_reform_p(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.research_project_workload)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


def update_first_class_course(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.first_class_course_workload)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


def update_teaching_achievement_award(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.teaching_achievement_workload)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


def update_public_service(mapper, connection, target):
    session = Session(bind=connection)
    course = session.query(UndergraduateWorkloadTeacherRanking).filter_by(teacher_id=target.teacher_id).one()
    course.undergraduate_course_total_hours = session.query(
        func.sum(mapper.c.workload)). \
        filter(mapper.c.teacher_id == target.teacher_id). \
        scalar()
    session.commit()


# 触发器监听
db.event.listen(UndergraduateWorkloadCourseRanking, 'after_insert', update_undergraduate_course_total_hours)
db.event.listen(UndergraduateWorkloadCourseRanking, 'after_update', update_undergraduate_course_total_hours)
# 有几个触发器需要传递几个可变参数来计算工作量，将参数全部放在一张表里面了
db.event.listen(UndergraduateThesi, 'after_insert', update_graduation_thesis_info)
db.event.listen(UndergraduateThesi, 'after_update', update_graduation_thesis_info)
db.event.listen(DepartmentInternship, 'after_insert', update_teaching_internship_student_info)
db.event.listen(DepartmentInternship, 'after_update', update_teaching_internship_student_info)
db.event.listen(CompetitionAward, 'after_insert', update_guiding_undergraduate_competition_p)
db.event.listen(CompetitionAward, 'after_update', update_guiding_undergraduate_competition_p)
db.event.listen(StudentResearch, 'after_insert', update_guiding_undergraduate_research_p)
db.event.listen(StudentResearch, 'after_update', update_guiding_undergraduate_research_p)
db.event.listen(UndergraduateMentorshipSystem, 'after_insert', update_undergraduate_tutor_system)
db.event.listen(UndergraduateMentorshipSystem, 'after_update', update_undergraduate_tutor_system)
db.event.listen(EducationalResearchProject, 'after_insert', update_teaching_research_and_reform_p)
db.event.listen(EducationalResearchProject, 'after_update', update_teaching_research_and_reform_p)
db.event.listen(FirstClassCourse, 'after_insert', update_first_class_course)
db.event.listen(FirstClassCourse, 'after_update', update_first_class_course)
db.event.listen(TeachingAchievementAward, 'after_insert', update_teaching_achievement_award)
db.event.listen(TeachingAchievementAward, 'after_update', update_teaching_achievement_award)
db.event.listen(PublicService, 'after_insert', update_public_service)
db.event.listen(PublicService, 'after_update', update_public_service)
