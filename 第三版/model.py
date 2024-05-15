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

    def CompetitionAward_list(self):
        return [self.id, self.event_name, self.work_name, self.award_category, self.award_level, self.teacher_name,
                self.teacher_id, self.total_workload, self.award_year]

    def add_competition_award(self, event_name, work_name, award_category, award_level, teacher_name, teacher_id,
                              total_workload, award_year):
        new_award = CompetitionAward(
            event_name=event_name,
            work_name=work_name,
            award_category=award_category,
            award_level=award_level,
            teacher_name=teacher_name,
            teacher_id=teacher_id,
            total_workload=total_workload,
            award_year=award_year
        )
        db.session.add(new_award)
        db.session.commit()


class DepartmentInternship(db.Model):
    __tablename__ = 'department_internship'

    student_name = db.Column(db.String(24), info='学生姓名')
    student_id = db.Column(db.String(24), primary_key=True, info='学生学号')
    major = db.Column(db.String(24), info='专业')
    grade = db.Column(db.String(24), info='年级')
    teacher_name = db.Column(db.String(24), info='学部内实习指导教师')
    teacher_id = db.Column(db.String(24), db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'),
                           index=True,
                           info='学部内实习指导教师工号')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='DepartmentInternship.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='department_internships')

    def DepartmentInternship_list(self):
        return [self.student_name, self.student_id, self.major, self.grade, self.teacher_name, self.teacher_id]

    def add_internship_record(self, student_name, student_id, major, grade, teacher_name, teacher_id):
        new_internship = DepartmentInternship(
            student_name=student_name,
            student_id=student_id,
            major=major,
            grade=grade,
            teacher_name=teacher_name,
            teacher_id=teacher_id
        )
        db.session.add(new_internship)
        db.session.commit()


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
    teacher_id = db.Column(db.String(24), db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'),
                           index=True, info='工号')
    research_project_workload = db.Column(db.Float(precision=6, asdecimal=True), info='教研项目工作量')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='EducationalResearchProject.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='educational_research_projects')

    def EducationalResearchProject_list(self):
        return [
            self.id,
            self.project_name, self.project_leader, self.project_members, self.project_level, self.start_date,
            self.end_date, self.acceptance_result, self.teacher_name, self.teacher_id, self.research_project_workload
        ]

    def add_research_project(self, project_name, project_leader, project_members, project_level, start_date, end_date,
                             acceptance_result, teacher_name, teacher_id, research_project_workload):
        new_project = EducationalResearchProject(
            project_name=project_name,
            project_leader=project_leader,
            project_members=project_members,
            project_level=project_level,
            start_date=start_date,
            end_date=end_date,
            acceptance_result=acceptance_result,
            teacher_name=teacher_name,
            teacher_id=teacher_id,
            research_project_workload=research_project_workload
        )
        db.session.add(new_project)
        db.session.commit()


class FirstClassCourse(db.Model):
    __tablename__ = 'first_class_courses'

    id = db.Column(db.Integer, primary_key=True, info='序号')
    course_type = db.Column(db.String(24), info='课程性质')
    content = db.Column(db.String(24), info='内容')
    leader = db.Column(db.String(24), info='负责人')
    remark = db.Column(db.String(24), info='备注，工作量分配')
    teacher_name = db.Column(db.String(24), info='教师姓名，一位老师一个记录')
    teacher_id = db.Column(db.String(24), db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'),
                           index=True,
                           info='工号，外键')
    first_class_course_workload = db.Column(db.Float(precision=6, asdecimal=True), info='一流课程工作量')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='FirstClassCourse.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='first_class_courses')

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

    def add_first_class_course(self, course_type, content, leader, remark, teacher_name, teacher_id,
                               first_class_course_workload):
        new_course = FirstClassCourse(
            course_type=course_type,
            content=content,
            leader=leader,
            remark=remark,
            teacher_name=teacher_name,
            teacher_id=teacher_id,
            first_class_course_workload=first_class_course_workload
        )
        db.session.add(new_course)
        db.session.commit()


class PublicService(db.Model):
    __tablename__ = 'public_services'

    id = db.Column(db.Integer, primary_key=True, info='序号，主键，自增，无意义')
    serve_date = db.Column(db.String(24), info='日期')
    content = db.Column(db.String(24), info='内容')
    teacher_name = db.Column(db.String(24), info='姓名')
    work_duration = db.Column(db.Float(precision=6, asdecimal=True), info='工作时长')
    class_hours = db.Column(db.Float(precision=6, asdecimal=True), info='课时')
    teacher_id = db.Column(db.String(24), db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'),
                           index=True,
                           info='教师工号，外键')

    teacher = db.relationship('UndergraduateWorkloadTeacherRanking',
                              primaryjoin='PublicService.teacher_id == UndergraduateWorkloadTeacherRanking.teacher_id',
                              backref='public_services')

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

    def add_public_service_record(self, serve_date, content, teacher_name, work_duration, class_hours, teacher_id):
        new_record = PublicService(
            serve_date=serve_date,
            content=content,
            teacher_name=teacher_name,
            work_duration=work_duration,
            class_hours=class_hours,
            teacher_id=teacher_id
        )
        db.session.add(new_record)
        db.session.commit()


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

    def StudentResearch_list(self):
        return [
            self.id, self.project_name, self.project_level,
            self.leader, self.student_id, self.total_members,
            self.teacher_name, self.teacher_id, self.acceptance_result,
            self.workload
        ]

    def add_student_research_record(self, project_name, project_level, leader, student_id, total_members, teacher_name,
                                    teacher_id, acceptance_result, workload):
        new_record = StudentResearch(
            project_name=project_name,
            project_level=project_level,
            leader=leader,
            student_id=student_id,
            total_members=total_members,
            teacher_name=teacher_name,
            teacher_id=teacher_id,
            acceptance_result=acceptance_result,
            workload=workload
        )
        db.session.add(new_record)
        db.session.commit()


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

    def TeachingAchievementAward_list(self):
        return [
            self.id, self.student_session, self.student_date,
            self.recommended_achievement_name, self.main_completion_person_name,
            self.award_category, self.award_level, self.remark,
            self.teacher_name, self.teacher_id, self.teaching_achievement_workload
        ]

    def add_teaching_achievement_record(self, student_session, student_date, recommended_achievement_name,
                                        main_completion_person_name, award_category, award_level, remark, teacher_name,
                                        teacher_id, teaching_achievement_workload):
        new_record = TeachingAchievementAward(
            student_session=student_session,
            student_date=student_date,
            recommended_achievement_name=recommended_achievement_name,
            main_completion_person_name=main_completion_person_name,
            award_category=award_category,
            award_level=award_level,
            remark=remark,
            teacher_name=teacher_name,
            teacher_id=teacher_id,
            teaching_achievement_workload=teaching_achievement_workload
        )
        db.session.add(new_record)
        db.session.commit()


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

    def UndergraduateMentorshipSystem_list(self):
        return [
            self.teacher_name, self.teacher_id, self.student_name,
            self.grade, self.student_id, self.teacher_workload
        ]

    def add_mentorship_record(self, teacher_name, teacher_id, student_name, grade, student_id, teacher_workload):
        new_record = UndergraduateMentorshipSystem(
            teacher_name=teacher_name,
            teacher_id=teacher_id,
            student_name=student_name,
            grade=grade,
            student_id=student_id,
            teacher_workload=teacher_workload
        )
        db.session.add(new_record)
        db.session.commit()


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

    def UndergraduateThesi_list(self):
        return [
            self.student_name, self.student_id, self.college, self.major, self.major_id,
            self.grade, self.thesis_topic, self.thesis_grade, self.teacher_name, self.teacher_id
        ]

    def add_thesis_record(self, student_name, student_id, college, major, major_id, grade, thesis_topic, thesis_grade,
                          teacher_name, teacher_id):
        new_record = UndergraduateThesi(
            student_name=student_name,
            student_id=student_id,
            college=college,
            major=major,
            major_id=major_id,
            grade=grade,
            thesis_topic=thesis_topic,
            thesis_grade=thesis_grade,
            teacher_name=teacher_name,
            teacher_id=teacher_id
        )
        db.session.add(new_record)
        db.session.commit()


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
    teacher_id = db.Column(db.String(20), db.ForeignKey('undergraduate_workload_teacher_ranking.teacher_id'),
                           index=True, info='教工号')  # 调整长度
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

    def UndergraduateWorkloadCourseRanking_list(self):
        return [
            self.academic_year, self.semester, self.calendar_year, self.half_year, self.course_code,
            self.teaching_class, self.course_name, self.teacher_id, self.teacher_name, self.seminar_hours,
            self.lecture_hours, self.lab_hours, self.enrolled_students, self.student_weight_coefficient_b,
            self.course_type_coefficient_a, self.total_lecture_hours_p1, self.lab_group_count, self.lab_coefficient,
            self.total_lab_hours_p2, self.course_split_ratio_for_engineering_center,
            self.total_undergraduate_course_hours, self.total_course_hours
        ]

    def add_course_ranking(self, academic_year, semester, calendar_year, half_year, course_code, teaching_class,
                           course_name, teacher_id, teacher_name, seminar_hours, lecture_hours, lab_hours,
                           enrolled_students, student_weight_coefficient_b, course_type_coefficient_a,
                           total_lecture_hours_p1, lab_group_count, lab_coefficient, total_lab_hours_p2,
                           course_split_ratio_for_engineering_center, total_undergraduate_course_hours,
                           total_course_hours):
        new_course_ranking = UndergraduateWorkloadCourseRanking(
            academic_year=academic_year,
            semester=semester,
            calendar_year=calendar_year,
            half_year=half_year,
            course_code=course_code,
            teaching_class=teaching_class,
            course_name=course_name,
            teacher_id=teacher_id,
            teacher_name=teacher_name,
            seminar_hours=seminar_hours,
            lecture_hours=lecture_hours,
            lab_hours=lab_hours,
            enrolled_students=enrolled_students,
            student_weight_coefficient_b=student_weight_coefficient_b,
            course_type_coefficient_a=course_type_coefficient_a,
            total_lecture_hours_p1=total_lecture_hours_p1,
            lab_group_count=lab_group_count,
            lab_coefficient=lab_coefficient,
            total_lab_hours_p2=total_lab_hours_p2,
            course_split_ratio_for_engineering_center=course_split_ratio_for_engineering_center,
            total_undergraduate_course_hours=total_undergraduate_course_hours,
            total_course_hours=total_course_hours
        )
        db.session.add(new_course_ranking)
        db.session.commit()


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

    def UndergraduateWorkloadTeacherRanking_list(self):
        return [
            self.teacher_id, self.teacher_name,
            self.undergraduate_course_total_hours, self.total_course_hours,
            self.graduation_thesis_student_count, self.graduation_thesis_p,
            self.teaching_internship_student_count, self.teaching_internship_weeks,
            self.teaching_internship_p, self.responsible_internship_construction_management_p,
            self.guiding_undergraduate_competition_p, self.guiding_undergraduate_research_p,
            self.undergraduate_tutor_system, self.teaching_research_and_reform_p,
            self.first_class_course, self.teaching_achievement_award, self.public_service
        ]

    def add_teacher_ranking(self, teacher_id, teacher_name, undergraduate_course_total_hours, total_course_hours,
                            graduation_thesis_student_count, graduation_thesis_p, teaching_internship_student_count,
                            teaching_internship_weeks, teaching_internship_p,
                            responsible_internship_construction_management_p, guiding_undergraduate_competition_p,
                            guiding_undergraduate_research_p, undergraduate_tutor_system,
                            teaching_research_and_reform_p, first_class_course, teaching_achievement_award,
                            public_service):
        new_teacher_ranking = UndergraduateWorkloadTeacherRanking(
            teacher_id=teacher_id,
            teacher_name=teacher_name,
            undergraduate_course_total_hours=undergraduate_course_total_hours,
            total_course_hours=total_course_hours,
            graduation_thesis_student_count=graduation_thesis_student_count,
            graduation_thesis_p=graduation_thesis_p,
            teaching_internship_student_count=teaching_internship_student_count,
            teaching_internship_weeks=teaching_internship_weeks,
            teaching_internship_p=teaching_internship_p,
            responsible_internship_construction_management_p=responsible_internship_construction_management_p,
            guiding_undergraduate_competition_p=guiding_undergraduate_competition_p,
            guiding_undergraduate_research_p=guiding_undergraduate_research_p,
            undergraduate_tutor_system=undergraduate_tutor_system,
            teaching_research_and_reform_p=teaching_research_and_reform_p,
            first_class_course=first_class_course,
            teaching_achievement_award=teaching_achievement_award,
            public_service=public_service
        )
        db.session.add(new_teacher_ranking)
        db.session.commit()
