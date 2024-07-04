# 导入蓝图
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from version_four.models import UndergraduateWorkloadTeacherRanking

"""
实例化蓝图对象
第一个参数：蓝图名称
第二个参数：导入蓝图的名称
第三个参数：蓝图前缀，该蓝图下的路由规则前缀都需要加上这个
"""
analyse_page_blueprint = Blueprint('analyse_page', __name__,template_folder='templates')

@analyse_page_blueprint.route('/analyse_page', methods=['POST', 'GET'])
@login_required
def analyse_page():
    if request.method == 'POST':
        teacher_id = request.form.get('teacher_id')
        teacher_name = request.form.get('teacher_name')
        results = UndergraduateWorkloadTeacherRanking.query.filter_by(teacher_id=teacher_id,
                                                                      teacher_name=teacher_name).all()
        print("***********************")
        print(results)
        print("***********************")
        result = [record.UndergraduateWorkloadTeacherRanking_list(results) for record in results]
        columns = ["教工号", "教师名称", "本科课程总学时", "毕业论文学生人数", "毕业论文P",
                   "指导教学实习人数", "指导教学实习周数", "指导教学实习P",
                   "负责实习点建设与管理P", "指导本科生竞赛P", "指导本科生科研P", "本科生导师制", "教研教改P",
                   "一流课程", "教学成果奖", "公共服务"]
        return render_template('analyse_page.html', result=result[0], columns=columns)
    else:
        return render_template('analyse_page.html')