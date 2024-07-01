/*
 Navicat Premium Data Transfer

 Source Server         : mapanwei
 Source Server Type    : MySQL
 Source Server Version : 80034
 Source Host           : localhost:3306
 Source Schema         : teacher_work

 Target Server Type    : MySQL
 Target Server Version : 80034
 File Encoding         : 65001

 Date: 01/07/2024 19:58:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------

-- ----------------------------
-- Table structure for competition_awards
-- ----------------------------
DROP TABLE IF EXISTS `competition_awards`;
CREATE TABLE `competition_awards`  (
  `id` int NOT NULL COMMENT '序号',
  `event_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '赛事名称',
  `work_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '作品名称',
  `award_category` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '获奖类别',
  `award_level` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '获奖等级',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '指导教师',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '指导教师工号',
  `total_workload` double(6, 2) NULL DEFAULT NULL COMMENT '总工作量',
  `award_year` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '获奖年份',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `competition_awards_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `competition_awards_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of competition_awards
-- ----------------------------

-- ----------------------------
-- Table structure for department_internship
-- ----------------------------
DROP TABLE IF EXISTS `department_internship`;
CREATE TABLE `department_internship`  (
  `student_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `student_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学生学号',
  `major` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '专业',
  `grade` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '年级',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学部内实习指导教师',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学部内实习指导教师工号',
  `week` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '实习周数',
  PRIMARY KEY (`student_id`) USING BTREE,
  INDEX `department_internship_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `department_internship_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department_internship
-- ----------------------------

-- ----------------------------
-- Table structure for educational_research_project
-- ----------------------------
DROP TABLE IF EXISTS `educational_research_project`;
CREATE TABLE `educational_research_project`  (
  `id` int NOT NULL COMMENT '序号，主键',
  `project_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目名称',
  `project_leader` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目负责人',
  `project_members` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目成员100',
  `project_level` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '级别',
  `start_date` date NULL DEFAULT NULL COMMENT '立项时间',
  `end_date` date NULL DEFAULT NULL COMMENT '结项时间',
  `acceptance_result` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '验收结论',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师姓名',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '工号',
  `research_project_workload` double(6, 2) NULL DEFAULT NULL COMMENT '教研项目工作量',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `educational_research_project_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `educational_research_project_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of educational_research_project
-- ----------------------------

-- ----------------------------
-- Table structure for first_class_courses
-- ----------------------------
DROP TABLE IF EXISTS `first_class_courses`;
CREATE TABLE `first_class_courses`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '序号',
  `course_type` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程性质',
  `content` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '内容',
  `leader` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '负责人',
  `remark` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注，工作量分配',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师姓名，一位老师一个记录',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '工号，外键',
  `first_class_course_workload` double(6, 2) NULL DEFAULT NULL COMMENT '一流课程工作量',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `first_class_courses_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `first_class_courses_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of first_class_courses
-- ----------------------------

-- ----------------------------
-- Table structure for public_services
-- ----------------------------
DROP TABLE IF EXISTS `public_services`;
CREATE TABLE `public_services`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '序号，主键，自增，无意义',
  `serve_date` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '日期',
  `content` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '内容',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '姓名',
  `work_duration` double(6, 2) NULL DEFAULT NULL COMMENT '工作时长',
  `class_hours` double(6, 2) NULL DEFAULT NULL COMMENT '课时',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师工号，外键',
  `workload` float NULL DEFAULT NULL COMMENT '工作量',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `public_services_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `public_services_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of public_services
-- ----------------------------

-- ----------------------------
-- Table structure for student_research
-- ----------------------------
DROP TABLE IF EXISTS `student_research`;
CREATE TABLE `student_research`  (
  `id` int NOT NULL COMMENT '序号',
  `project_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目名称',
  `project_level` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '级别',
  `leader` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '负责人',
  `student_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学号',
  `total_members` int NULL DEFAULT NULL COMMENT '项目组总人数',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '指导老师',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '指导老师工号',
  `acceptance_result` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '验收结果',
  `workload` double(6, 2) NULL DEFAULT NULL COMMENT '工作量',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `student_research_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `student_research_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_research
-- ----------------------------

-- ----------------------------
-- Table structure for teacher_information
-- ----------------------------
DROP TABLE IF EXISTS `teacher_information`;
CREATE TABLE `teacher_information`  (
  `teacher_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师姓名',
  `teacher_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '教工号',
  `password_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT 'hash密码',
  PRIMARY KEY (`teacher_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher_information
-- ----------------------------
INSERT INTO `teacher_information` VALUES ('测试员', '2021214168', 'pbkdf2:sha256:600000$ZiCHPb3ozxK0uBRA$4bc771e3810bd38d08919890e1a7b6685ea09ec02534ee5c1a38bba5e072c044');
INSERT INTO `teacher_information` VALUES ('马攀威', '2021214169', 'pbkdf2:sha256:600000$8ozVSYBKrA9YFj0t$861ca426a0bb0ef25491869ace2a94b8b0293e366ce93ecade4010c1302a7b7d');

-- ----------------------------
-- Table structure for teaching_achievement_awards
-- ----------------------------
DROP TABLE IF EXISTS `teaching_achievement_awards`;
CREATE TABLE `teaching_achievement_awards`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '序号，主键，自增，无意义',
  `student_session` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '届',
  `student_date` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '时间',
  `recommended_achievement_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '推荐成果名称',
  `main_completion_person_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '成果主要完成人名称',
  `award_category` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '获奖类别',
  `award_level` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '获奖等级',
  `remark` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '工号，外键',
  `teaching_achievement_workload` double(6, 2) NULL DEFAULT NULL COMMENT '教学成果工作量',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `teaching_achievement_awards_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `teaching_achievement_awards_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teaching_achievement_awards
-- ----------------------------

-- ----------------------------
-- Table structure for undergraduate_mentorship_system
-- ----------------------------
DROP TABLE IF EXISTS `undergraduate_mentorship_system`;
CREATE TABLE `undergraduate_mentorship_system`  (
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '导师姓名',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教工号',
  `student_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `grade` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '年级',
  `student_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学号',
  `teacher_workload` double(6, 2) NULL DEFAULT NULL COMMENT '教师工作量',
  PRIMARY KEY (`student_id`) USING BTREE,
  INDEX `undergraduate_mentorship_system_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `undergraduate_mentorship_system_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of undergraduate_mentorship_system
-- ----------------------------

-- ----------------------------
-- Table structure for undergraduate_thesis
-- ----------------------------
DROP TABLE IF EXISTS `undergraduate_thesis`;
CREATE TABLE `undergraduate_thesis`  (
  `student_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `student_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学生学号',
  `college` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学院',
  `major` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '专业',
  `major_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '专业号',
  `grade` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '年级',
  `thesis_topic` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '毕业论文题目',
  `thesis_grade` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '毕业论文成绩',
  `teacher_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '毕业论文指导老师',
  `teacher_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '毕业论文指导老师工号',
  PRIMARY KEY (`student_id`) USING BTREE,
  INDEX `undergraduate_thesis_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `undergraduate_thesis_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of undergraduate_thesis
-- ----------------------------

-- ----------------------------
-- Table structure for undergraduate_workload_course_ranking
-- ----------------------------
DROP TABLE IF EXISTS `undergraduate_workload_course_ranking`;
CREATE TABLE `undergraduate_workload_course_ranking`  (
  `academic_year` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学年',
  `semester` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '学期',
  `calendar_year` int NULL DEFAULT NULL COMMENT '自然年',
  `half_year` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '上下半年',
  `course_code` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '课程号',
  `teaching_class` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '教学班',
  `course_name` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程名称',
  `teacher_id` varchar(56) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教工号',
  `teacher_name` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师名称',
  `seminar_hours` double(6, 2) NULL DEFAULT NULL COMMENT '研讨学时',
  `lecture_hours` double(6, 2) NULL DEFAULT NULL COMMENT '授课学时',
  `lab_hours` double(6, 2) NULL DEFAULT NULL COMMENT '实验学时',
  `enrolled_students` int NULL DEFAULT NULL COMMENT '选课人数',
  `student_weight_coefficient_b` double(6, 2) NULL DEFAULT NULL COMMENT '学生数量权重系数B',
  `course_type_coefficient_a` double(6, 2) NULL DEFAULT NULL COMMENT '课程类型系数A',
  `total_lecture_hours_p1` double(6, 2) NULL DEFAULT NULL COMMENT '理论课总学时P1',
  `lab_group_count` int NULL DEFAULT NULL COMMENT '实验分组数',
  `lab_coefficient` double(6, 2) NULL DEFAULT NULL COMMENT '实验课系数',
  `total_lab_hours_p2` double(6, 2) NULL DEFAULT NULL COMMENT '实验课总学时P2',
  `course_split_ratio_for_engineering_center` double(6, 2) NULL DEFAULT NULL COMMENT '课程拆分占比（工程中心用）',
  `total_course_hours` double(6, 2) NULL DEFAULT NULL COMMENT '课程总学时',
  PRIMARY KEY (`course_code`, `teaching_class`) USING BTREE,
  INDEX `undergraduate_workload_course_ranking_ibfk_1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `undergraduate_workload_course_ranking_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of undergraduate_workload_course_ranking
-- ----------------------------

-- ----------------------------
-- Table structure for undergraduate_workload_teacher_ranking
-- ----------------------------
DROP TABLE IF EXISTS `undergraduate_workload_teacher_ranking`;
CREATE TABLE `undergraduate_workload_teacher_ranking`  (
  `id` int NOT NULL COMMENT '序号，自增',
  `teacher_id` varchar(56) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '教工号',
  `teacher_name` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '教师名称',
  `undergraduate_course_total_hours` double(6, 2) NULL DEFAULT NULL COMMENT '本科课程总学时',
  `graduation_thesis_student_count` int NULL DEFAULT NULL COMMENT '毕业论文学生人数',
  `graduation_thesis_p` double(6, 2) NULL DEFAULT NULL COMMENT '毕业论文P',
  `teaching_internship_student_count` int NULL DEFAULT NULL COMMENT '指导教学实习人数',
  `teaching_internship_weeks` int NULL DEFAULT NULL COMMENT '指导教学实习周数',
  `teaching_internship_p` double(6, 2) NULL DEFAULT NULL COMMENT '指导教学实习P',
  `responsible_internship_construction_management_p` double(6, 2) NULL DEFAULT NULL COMMENT '负责实习点建设与管理P',
  `guiding_undergraduate_competition_p` double(6, 2) NULL DEFAULT NULL COMMENT '指导本科生竞赛P',
  `guiding_undergraduate_research_p` double(6, 2) NULL DEFAULT NULL COMMENT '指导本科生科研P',
  `undergraduate_tutor_system` double(6, 2) NULL DEFAULT NULL COMMENT '本科生导师制',
  `teaching_research_and_reform_p` double(6, 2) NULL DEFAULT NULL COMMENT '教研教改P',
  `first_class_course` double(6, 2) NULL DEFAULT NULL COMMENT '一流课程',
  `teaching_achievement_award` double(6, 2) NULL DEFAULT NULL COMMENT '教学成果奖',
  `public_service` double(6, 2) NULL DEFAULT NULL COMMENT '公共服务',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `1`(`teacher_id` ASC) USING BTREE,
  CONSTRAINT `1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_information` (`teacher_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of undergraduate_workload_teacher_ranking
-- ----------------------------

-- ----------------------------
-- Table structure for workload_parameter
-- ----------------------------
DROP TABLE IF EXISTS `workload_parameter`;
CREATE TABLE `workload_parameter`  (
  `id` int NOT NULL COMMENT '序号',
  `graduation_thesis_p_count` float NOT NULL COMMENT '毕业论文参数',
  `intership_count` float NOT NULL COMMENT '指导实习参数',
  `intership_js` float NOT NULL COMMENT '实习点建设',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of workload_parameter
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
