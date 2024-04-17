
-- ----------------------------
-- 1、本科工作量教师排序表
-- ----------------------------
DROP TABLE IF exists undergraduate_workload_teacher_ranking;
CREATE TABLE undergraduate_workload_teacher_ranking (
  teacher_id VARCHAR(56) PRIMARY KEY COMMENT '教工号',
  teacher_name VARCHAR(12) COMMENT '教师名称',
  undergraduate_course_total_hours DOUBLE(6,2) COMMENT '本科课程总学时',
  total_course_hours DOUBLE(6,2) COMMENT '课程总学时',
  graduation_thesis_student_count INT COMMENT '毕业论文学生人数',
  graduation_thesis_p DOUBLE(6,2) COMMENT '毕业论文P',
  teaching_internship_student_count INT COMMENT '指导教学实习人数',
  teaching_internship_weeks INT COMMENT '指导教学实习周数',
  teaching_internship_p DOUBLE(6,2) COMMENT '指导教学实习P',
  responsible_internship_construction_management_p DOUBLE(6,2) COMMENT '负责实习点建设与管理P',
  guiding_undergraduate_competition_p DOUBLE(6,2) COMMENT '指导本科生竞赛P',
  guiding_undergraduate_research_p DOUBLE(6,2) COMMENT '指导本科生科研P',
  undergraduate_tutor_system DOUBLE(6,2) COMMENT '本科生导师制',
  teaching_research_and_reform_p DOUBLE(6,2) COMMENT '教研教改P',
  first_class_course DOUBLE(6,2) COMMENT '一流课程',
  teaching_achievement_award DOUBLE(6,2) COMMENT '教学成果奖',
  public_service DOUBLE(6,2) COMMENT '公共服务'
);
-- ----------------------------
-- 2、本科工作量课程排序表
-- ----------------------------
DROP TABLE IF exists undergraduate_workload_course_ranking;
CREATE TABLE undergraduate_workload_course_ranking (
  academic_year VARCHAR(10) COMMENT '学年',
  semester VARCHAR(10) COMMENT '学期',
  calendar_year INT COMMENT '自然年',
  half_year VARCHAR(20) COMMENT '上下半年',
  course_code VARCHAR(24) COMMENT '课程号',
  teaching_class VARCHAR(24) COMMENT '教学班',
  course_name VARCHAR(24) COMMENT '课程名称',
  teacher_id VARCHAR(56) COMMENT '教工号',
  teacher_name VARCHAR(12) COMMENT '教师名称',
  seminar_hours DOUBLE(6,2) COMMENT '研讨学时',
  lecture_hours DOUBLE(6,2) COMMENT '授课学时',
  lab_hours DOUBLE(6,2) COMMENT '实验学时',
  enrolled_students INT COMMENT '选课人数',
  student_weight_coefficient_b DOUBLE(6,2) COMMENT '学生数量权重系数B',
  course_type_coefficient_a DOUBLE(6,2) COMMENT '课程类型系数A',
  total_lecture_hours_p1 DOUBLE(6,2) COMMENT '理论课总学时P1',
  lab_group_count INT COMMENT '实验分组数',
  lab_coefficient DOUBLE(6,2) COMMENT '实验课系数',
  total_lab_hours_p2 DOUBLE(6,2) COMMENT '实验课总学时P2',
  course_split_ratio_for_engineering_center DOUBLE(6,2) COMMENT '课程拆分占比（工程中心用）',
  total_undergraduate_course_hours DOUBLE(6,2) COMMENT '本科课程总学时',
  total_course_hours DOUBLE(6,2) COMMENT '课程总学时',
  PRIMARY KEY (course_code, teaching_class),
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking (teacher_id)
);

-- ----------------------------
-- 3、毕业论文
-- ----------------------------
DROP TABLE IF exists undergraduate_thesis;
CREATE TABLE undergraduate_thesis (
  student_name VARCHAR(24) COMMENT '学生姓名',
  student_id VARCHAR(24) PRIMARY KEY COMMENT '学生学号',
  college VARCHAR(24) COMMENT '学院',
  major VARCHAR(24) COMMENT '专业',
  major_id VARCHAR(24) COMMENT '专业号',
  grade VARCHAR(24) COMMENT '年级',
  thesis_topic VARCHAR(24) COMMENT '毕业论文题目',
  thesis_grade VARCHAR(24) COMMENT '毕业论文成绩',
  teacher_name VARCHAR(24) COMMENT '毕业论文指导老师',
  teacher_id VARCHAR(24) COMMENT '毕业论文指导老师工号',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);
-- ----------------------------
-- 4、本科实习
-- ----------------------------
DROP TABLE IF exists department_internship;
CREATE TABLE department_internship (
  student_name VARCHAR(24) COMMENT '学生姓名',
  student_id VARCHAR(24) PRIMARY KEY COMMENT '学生学号',
  major VARCHAR(24) COMMENT '专业',
  grade VARCHAR(24) COMMENT '年级',
  teacher_name VARCHAR(24) COMMENT '学部内实习指导教师',
  teacher_id VARCHAR(24) COMMENT '学部内实习指导教师工号',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);
-- ----------------------------
-- 5、学生竞赛
-- ----------------------------
DROP TABLE IF exists competition_awards;
CREATE TABLE competition_awards (
  id INT PRIMARY KEY COMMENT '序号',
  event_name VARCHAR(24) COMMENT '赛事名称',
  work_name VARCHAR(24) COMMENT '作品名称',
  award_category VARCHAR(24) COMMENT '获奖类别',
  award_level VARCHAR(24) COMMENT '获奖等级',
  teacher_name VARCHAR(24) COMMENT '指导教师',
  teacher_id VARCHAR(24) COMMENT '指导教师工号',
  total_workload DOUBLE(6,2) COMMENT '总工作量',
  award_year VARCHAR(24) COMMENT '获奖年份',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);
-- ----------------------------
-- 6、学生科研
-- ----------------------------
DROP TABLE IF exists student_research;
CREATE TABLE student_research (
  id INT PRIMARY KEY COMMENT '序号',
  project_name VARCHAR(24) COMMENT '项目名称',
  project_level VARCHAR(24) COMMENT '级别',
  leader VARCHAR(24) COMMENT '负责人',
  student_id VARCHAR(24) COMMENT '学号',
  total_members INT COMMENT '项目组总人数',
  teacher_name VARCHAR(24) COMMENT '指导老师',
  teacher_id VARCHAR(24) COMMENT '指导老师工号',
  acceptance_result VARCHAR(24) COMMENT '验收结果',
  workload DOUBLE(6,2) COMMENT '工作量',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);
-- ----------------------------
-- 7、本科生导师制
-- ----------------------------
DROP TABLE IF exists undergraduate_mentorship_system;
CREATE TABLE undergraduate_mentorship_system (
  teacher_name VARCHAR(24) COMMENT '导师姓名',
  teacher_id VARCHAR(24) COMMENT '教工号',
  student_name VARCHAR(24) COMMENT '学生姓名',
  grade VARCHAR(24) COMMENT '年级',
  student_id VARCHAR(24) PRIMARY KEY COMMENT '学号',
  teacher_workload DOUBLE(6,2) COMMENT '教师工作量',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
  );
  -- ----------------------------
-- 8、教研项目
-- ----------------------------
DROP TABLE IF exists educational_research_project;
CREATE TABLE educational_research_project (
id INT PRIMARY KEY COMMENT '序号，主键',
project_name VARCHAR(24) COMMENT '项目名称',
project_leader VARCHAR(24) COMMENT '项目负责人',
project_members VARCHAR(24) COMMENT '项目成员100',
project_level VARCHAR(24) COMMENT '级别',
start_date DATE COMMENT '立项时间',
end_date DATE COMMENT '结项时间',
acceptance_result VARCHAR(24) COMMENT '验收结论',
teacher_name VARCHAR(24) COMMENT '教师姓名',
teacher_id VARCHAR(24) COMMENT '工号',
research_project_workload DOUBLE(6,2) COMMENT '教研项目工作量',
FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);
-- ----------------------------
-- 9、一流课程
-- ----------------------------
DROP TABLE IF exists first_class_courses;
CREATE TABLE first_class_courses (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '序号',
  course_type VARCHAR(24) COMMENT '课程性质',
  content VARCHAR(24) COMMENT '内容',
  leader VARCHAR(24) COMMENT '负责人',
  remark VARCHAR(24) COMMENT '备注，工作量分配',
  teacher_name VARCHAR(24) COMMENT '教师姓名，一位老师一个记录',
  teacher_id VARCHAR(24) COMMENT '工号，外键',
  first_class_course_workload DOUBLE(6,2) COMMENT '一流课程工作量',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);
-- ----------------------------
-- 10、教学成果奖
-- ----------------------------
DROP TABLE IF exists teaching_achievement_awards;
CREATE TABLE teaching_achievement_awards (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '序号，主键，自增，无意义',
  student_session VARCHAR(24) COMMENT '届',
  student_date VARCHAR(24) COMMENT '时间',
  recommended_achievement_name VARCHAR(24) COMMENT '推荐成果名称',
  main_completion_person_name VARCHAR(24) COMMENT '成果主要完成人名称',
  award_category VARCHAR(24) COMMENT '获奖类别',
  award_level VARCHAR(24) COMMENT '获奖等级',
  remark VARCHAR(24) COMMENT '备注',
  teacher_name VARCHAR(24) COMMENT '教师',
  teacher_id VARCHAR(24) COMMENT '工号，外键',
  teaching_achievement_workload DOUBLE(6,2) COMMENT '教学成果工作量',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);
-- ----------------------------
-- 11、公共服务
-- ----------------------------
DROP TABLE IF exists public_services;
CREATE TABLE public_services (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '序号，主键，自增，无意义',
  serve_date VARCHAR(24) COMMENT '日期',
  content VARCHAR(24) COMMENT '内容',
  teacher_name VARCHAR(24) COMMENT '姓名',
  work_duration DOUBLE(6,2) COMMENT '工作时长',
  class_hours DOUBLE(6,2) COMMENT '课时',
  teacher_id VARCHAR(24) COMMENT '教师工号，外键',
  FOREIGN KEY (teacher_id) REFERENCES undergraduate_workload_teacher_ranking(teacher_id) 
);