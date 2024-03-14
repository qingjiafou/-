from flask import Flask, render_template, request, redirect, url_for
import pymysql
import mysql.connector

db_host = 'localhost'
db_user = 'root'
db_password = 'Mapanwei0116'
db_name = 'teacher'


def db_query(sql):
    db = pymysql.connect(host=db_host,
                        user=db_user,
                        password=db_password,
                        database=db_name)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute(sql)
    # 使用 fetchone() 方法获取所有数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return data


def db_exec(sql):
    db = pymysql.connect(host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()    #用于提交数据库中的更改
    db.close()


def db_fun():
    db = pymysql.connect(host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name)
    cursor = db.cursor()
    cursor.callproc('recompute_workload')
    db.commit()
    db.close()


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
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

# 查看各个表的内容
@app.route('/teacher_class')
def teacher_clas():
    sql = "select * from 本科工作量课程排序表"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'学年': row[0], '学期': row[1], '自然年': row[2],'上下半年': row[3], '课程号': row[4],'课程名称': row[5], '教工号':row[6],'教师名称': row[7],'研讨学时': row[8],'授课学时': row[9],'实验学时': row[10],'选课人数': row[11], '学生数量权重系数B': row[12], '课程类型系数A': row[13],'理论课总学时P1': row[14], '实验分组数': row[15],'实验课系数': row[16],'实验课总学时P2': row[17],'课程拆分占比': row[18],'本科课程总学时': row[19],'课程总学时': row[20]})
    return render_template('teacher_class.html', loaders=loaders)

@app.route('/thesis_18')
def thesis_18():
    sql = "select * from 毕业论文"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'姓名': row[0], '学号': row[1], '学院': row[2],'专业': row[3], '专业号': row[4],'年级': row[5],'毕业论文题目': row[6],'毕业论文成绩': row[7],'毕业论文指导老师': row[8]})
    return render_template('thesis_18.html', loaders=loaders)


@app.route('/internship_19')
def internship_19():
    sql = "select * from 本科实习"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'姓名': row[0], '学号': row[1], '专业': row[2],'年级': row[3], '学部内实习指导教师': row[4]})
    return render_template('internship_19.html', loaders=loaders)

@app.route('/student_competition')
def student_competition():
    sql = "select * from 学生竞赛"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'赛事名称': row[0], '作品名称': row[1], '获奖类别': row[2],'获奖等级': row[3], '获奖学生': row[4],'指导教师': row[5],'总工作量': row[6],'获奖年份': row[7]})
    return render_template('student_competition.html', loaders=loaders)

@app.route('/student_research')
def student_research():
    sql = "select * from 学生科研"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'序号': row[0], '项目名称': row[1], '级别': row[2],'负责人': row[3], '学号':row[4],'项目组总人数': row[5],'指导老师':row[6],'验收结论':row[7],'总工作量':row[8]})
    return render_template('student_research.html', loaders=loaders)

@app.route('/undergraduate_mentorship')
def undergraduate_mentorship():
    sql = "select * from 本科生导师制"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'导师姓名': row[0], '教工号': row[1], '学生姓名': row[2],'年级': row[3], '学号': row[4], '说明': row[5]})
    return render_template('undergraduate_mentorship.html', loaders=loaders)

@app.route('/teaching_research_project')
def teaching_research_project():
    sql = "select * from 教研项目"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'项目名称': row[0], '项目负责人': row[1], '项目成员': row[2],'级别': row[3], '立项时间': row[4],'结项时间': row[5],'验收结论': row[6]})
    return render_template('teaching_research_project.html', loaders=loaders)

@app.route('/first_class_courses')
def first_class_courses():
    sql = "select * from 一流课程"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'课程性质': row[0], '内容': row[1], '负责人': row[2],'工作量分配': row[3]})
    return render_template('first_class_courses.html', loaders=loaders)

@app.route('/teaching_achievement_award')
def teaching_achievement_award():
    sql = "select * from 教学成果奖"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'届': row[0], '时间': row[1], '推荐成果名称': row[2],'成果主要完成人姓名': row[3],'获奖类别': row[4],'获奖等级': row[5],'备注': row[6],'工作总量': row[7]})
    return render_template('teaching_achievement_award.html', loaders=loaders)

@app.route('/public_service')
def public_service():
    sql = "select * from 公共服务"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'日期': row[0], '内容': row[1], '姓名': row[2],'工作时长': row[3],'课时': row[4]})
    return render_template('public_service.html', loaders=loaders)


#删除与修改数据数据
@app.route('/delete1/<xz>/<content>/<fzr>/<gzl>')
def delete1(xz,content,fzr,gzl):
    sql = "delete from 一流课程 where 课程性质='{0}' and 内容='{1}' and 负责人='{2}' and 工作量分配='{3}'".format(xz, content, fzr, gzl)
    db_exec(sql)
    return redirect(url_for('first_class_courses'))

@app.route('/edit1/<xz>/<content>/<fzr>/<gzl>', methods=['GET', 'POST'])
def edit(xz,content,fzr,gzl):
    if request.method == 'GET':
        sql = "select * from 一流课程 where 课程性质='{0}' and 内容='{1}' and 负责人='{2}' and 工作量分配='{3}'".format(xz,content,fzr,gzl)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'课程性质': row[0], '内容': row[1], '负责人': row[2],'工作量分配': row[3]})
        return render_template('edit1.html', loader=loaders)
    else:
        # POST
        new_xz = request.form.get('课程性质')
        new_content = request.form.get('内容')
        new_fzr = request.form.get('负责人')
        new_gzl = request.form.get('工作量分配')
        sql = "update 一流课程 set 课程性质='{0}', 内容='{1}', 负责人='{2}', 工作量分配='{3}' where 课程性质='{4}' and 内容='{5}' and 负责人='{6}' and 工作量分配='{7}'".format(
        new_xz, new_content, new_fzr, new_gzl, xz, content, fzr, gzl
        )
        db_exec(sql)
        return redirect(url_for('first_class_courses'))

@app.route('/delete2/<xm>/<snum>/<zy>/<nj>/<xb>', methods=['GET', 'POST'])
def delete2(xm,snum,zy,nj,xb):
    sql = "delete from 本科实习 where 姓名='{0}' and 学号 = '{1}' and 专业= '{2}' and 年级 = '{3}' and 学部内实习指导教师 = '{4}'".format(xm,snum,zy,nj,xb)
    db_exec(sql)
    return redirect(url_for('internship_19'))

@app.route('/edit2/<xm>/<snum>/<zy>/<nj>/<xb>', methods=['GET', 'POST'])
def edit2(xm,snum,zy,nj,xb):
    if request.method == 'GET':
        sql = "select * from 本科实习 where 姓名='{0}' and 学号 = '{1}' and 专业= '{2}' and 年级 = '{3}' and 学部内实习指导教师 = '{4}'".format(xm,snum,zy,nj,xb)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'姓名': row[0], '学号': row[1], '专业': row[2],'年级': row[3], '学部内实习指导教师': row[4]})
        return render_template('edit2.html', loader=loaders)
    else:
        # POST
        new_xm=request.form.get('姓名')
        new_snum=request.form.get('学号')
        new_zy=request.form.get('专业')
        new_nj=request.form.get('年级')
        new_xb=request.form.get('学部内实习指导教师')
        sql = "update 本科实习 set 姓名='{0}', 学号='{1}', 专业='{2}', 年级='{3}',学部内实习指导教师='{4}' where 姓名='{5}' and 学号 = '{6}' and 专业= '{7}' and 年级 = '{8}' and 学部内实习指导教师 = '{9}'".format(
            new_xm,new_snum,new_zy,new_nj,new_xb,xm,snum,zy,nj,xb
        )
        db_exec(sql)
        return redirect(url_for('internship_19'))

@app.route('/delete3/<date>/<nr>/<xm>/<gz>/<ks>')
def delete3(date,nr,xm,gz,ks):
    sql = "delete from 公共服务 where 日期 = '{0}' and 内容 = '{1}' and 姓名 = '{2}' and 工作时长 = '{3}' and 课时 = '{4}'".format(date,nr,xm,gz,ks)
    db_exec(sql)
    return redirect(url_for('public_service'))

@app.route('/edit3/<date>/<nr>/<xm>/<gz>/<ks>',methods=['GET', 'POST'])
def edit3(date,nr,xm,gz,ks):
    if request.method == 'GET':
        sql = "select * from 公共服务 where 日期 = '{0}' and 内容 = '{1}' and 姓名 = '{2}' and 工作时长 = '{3}' and 课时 = '{4}'".format(date,nr,xm,gz,ks)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'日期': row[0], '内容': row[1], '姓名': row[2],'工作时长': row[3], '课时': row[4]})
        return render_template('edit3.html', loader=loaders)
    else:
        # POST
        new_date=request.form.get('日期')
        new_nr=request.form.get('内容')
        new_xm=request.form.get('姓名')
        new_gz=request.form.get('工作时长')
        new_ks=request.form.get('课时')
        sql = "update 公共服务 set 日期='{0}', 内容='{1}', 姓名='{2}', 工作时长='{3}',课时='{4}' where 日期 = '{5}' and 内容 = '{6}' and 姓名 = '{7}' and 工作时长 = '{8}' and 课时 = '{9}'".format(
            new_date,new_nr,new_xm,new_gz,new_ks,date,nr,xm,gz,ks
        )
        db_exec(sql)
        return redirect(url_for('public_service'))

@app.route('/delete4/<a>/<work_name>/<b>/<c>/<d>/<e>/<f>/<g>')
def delete4(a,work_name,b,c,d,e,f,g):
    sql = "delete from 学生竞赛 where 赛事名称='{0}' and 作品名称='{1}' and 获奖类别='{2}' and 获奖等级='{3}' and 获奖学生='{4}' and 指导教师='{5}' and 总工作量='{6}' and 获奖年份='{7}'".format(a,work_name,b,c,d,e,f,g)
    db_exec(sql)
    return redirect(url_for('student_competition'))

@app.route('/edit4/<a>/<work_name>/<b>/<c>/<d>/<e>/<f>/<g>',methods=['GET', 'POST'])
def edit4(a,work_name,b,c,d,e,f,g):
    if request.method=='GET':
        sql="select * from 学生竞赛 where 赛事名称='{0}' and 作品名称='{1}' and 获奖类别='{2}' and 获奖等级='{3}' and 获奖学生='{4}' and 指导教师='{5}' and 总工作量='{6}' and 获奖年份='{7}'".format(a,work_name,b,c,d,e,f,g)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'赛事名称': row[0], '作品名称': row[1], '获奖类别': row[2],'获奖等级': row[3], '获奖学生': row[4],'指导教师': row[5],'总工作量': row[6],'获奖年份': row[7]})
        return render_template('edit4.html', loader=loaders)
    else:
        new_a=request.form.get('赛事名称')
        new_work_name=request.form.get('作品名称')
        new_b=request.form.get('获奖类别')
        new_c=request.form.get('获奖等级')
        new_d=request.form.get('获奖学生')
        new_e=request.form.get('指导教师')
        new_f=request.form.get('总工作量')
        new_g=request.form.get('获奖年份')
        sql="update 学生竞赛 set 赛事名称='{0}', 作品名称='{1}', 获奖类别='{2}', 获奖等级='{3}',获奖学生='{4}',指导教师='{5}',总工作量='{6}',获奖年份='{7}' where 赛事名称='{8}' and 作品名称='{9}' and 获奖类别='{10}' and 获奖等级='{11}' and 获奖学生='{12}' and 指导教师='{13}' and 总工作量='{14}' and 获奖年份='{15}'".format(
        new_a,new_work_name,new_b,new_c,new_d,new_e,new_f,new_g,a,work_name,b,c,d,e,f,g
        )
        db_exec(sql)
        return redirect(url_for('student_competition'))
    
@app.route('/delete5/<num>/<a>/<b>/<c>/<h>/<d>/<e>/<f>/<g>')
def delete5(num,a,b,c,h,d,e,f,g):
    sql = "delete from 学生科研 where 序号 = '{0}' and 项目名称='{1}' and 级别='{2}' and 负责人='{3}' and 学号='{4}' and 项目组总人数='{5}' and 指导老师='{6}' and 验收结论='{7}' and 总工作量='{8}'".format(num,a,b,c,h,d,e,f,g)
    db_exec(sql)
    return redirect(url_for('student_research'))

@app.route('/edit5/<num>/<a>/<b>/<c>/<h>/<d>/<e>/<f>/<g>',methods=['GET', 'POST'])
def edit5(num,a,b,c,h,d,e,f,g):
    if request.method=='GET':
        sql="select * from 学生科研 where 序号 = '{0}' and 项目名称='{1}' and 级别='{2}' and 负责人='{3}' and 学号='{4}' and 项目组总人数='{5}' and 指导老师='{6}' and 验收结论='{7}' and 总工作量='{8}'".format(num,a,b,c,h,d,e,f,g)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'序号': row[0], '项目名称': row[1], '级别': row[2],'负责人': row[3], '学号':row[4], '项目组总人数': row[5],'指导老师': row[6],'验收结论': row[7],'总工作量': row[8]})
        return render_template('edit5.html', loader=loaders)
    else:
        new_num=request.form.get('序号')
        new_a=request.form.get('项目名称')
        new_b=request.form.get('级别')
        new_c=request.form.get('负责人')
        new_h=request.form.get('学号')
        new_d=request.form.get('项目组总人数')
        new_e=request.form.get('指导老师')
        new_f=request.form.get('验收结论')
        new_g=request.form.get('总工作量')
        sql="update 学生科研 set 序号='{0}', 项目名称='{1}', 级别='{2}', 负责人='{3}',学号='{4}',项目组总人数='{5}',指导老师='{6}',验收结论='{7}',总工作量='{8}' where 序号 = '{9}' and 项目名称='{10}' and 级别='{11}' and 负责人='{12}' and 学号='{13}' 项目组总人数='{14}' and 指导老师='{15}' and 验收结论='{16}' and 总工作量='{17}'".format(
           new_num,new_a,new_b,new_c,new_h,new_d,new_e,new_f,new_g,num,a,b,c,h,d,e,f,g
        )
        db_exec(sql)
        return redirect(url_for('student_research'))
@app.route('/delete6/<a>/<b>/<recommended_achievement>/<c>/<d>/<e>/<f>/<g>')
def delete6(a,b,recommended_achievement,c,d,e,f,g):
    sql = "delete from 教学成果奖 where 届='{0}' and 时间='{1}' and 推荐成果名称='{2}' and 成果主要完成人姓名='{3}' and 获奖类别='{4}' and 获奖等级='{5}' and 备注='{6}' and 工作总量='{7}'".format(a,b,recommended_achievement,c,d,e,f,g)
    db_exec(sql)
    return redirect(url_for('teaching_achievement_award'))

@app.route('/edit6/<a>/<b>/<recommended_achievement>/<c>/<d>/<e>/<f>/<g>>',methods=['GET', 'POST'])
def edit6(a,b,recommended_achievement,c,d,e,f,g):
    if request.method=='GET':
        sql="select * from 教学成果奖 where 届='{0}' and 时间='{1}' and 推荐成果名称='{2}' and 成果主要完成人姓名='{3}' and 获奖类别='{4}' and 获奖等级='{5}' and 备注='{6}' and 工作总量='{7}'".format(a,b,recommended_achievement,c,d,e,f,g)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'届': row[0], '时间': row[1], '推荐成果名称': row[2],'成果主要完成人姓名': row[3], '获奖类别': row[4],'获奖等级': row[5],'备注': row[6],'工作总量': row[7]})
        return render_template('edit6.html', loader=loaders)
    else:
        new_a=request.form.get('届')
        new_b=request.form.get('时间')
        new_recommended_achievement=request.form.get('推荐成果名称')
        new_c=request.form.get('成果主要完成人姓名')
        new_d=request.form.get('获奖类别')
        new_e=request.form.get('获奖等级')
        new_f=request.form.get('备注')
        new_g=request.form.get('工作总量')
        sql="update 教学成果奖 set 届='{0}', 时间='{1}', 推荐成果名称='{2}', 成果主要完成人姓名='{3}',获奖类别='{4}',获奖等级='{5}',备注='{6}',工作总量='{7}' where  届='{8}' and 时间='{9}' and 推荐成果名称='{10}' and 成果主要完成人姓名='{11}' and 获奖类别='{12}' and 获奖等级='{13}' and 备注='{14}' and 工作总量='{15}'".format(
        new_a,new_b,new_recommended_achievement,new_c,new_d,new_e,new_f,new_g,a,b,recommended_achievement,c,d,e,f,g
        )
        db_exec(sql)
        return redirect(url_for('teaching_achievement_award'))
    
@app.route('/delete7/<pname>/<a>/<b>/<c>/<d>/<e>/<f>')
def delete7(pname,a,b,c,d,e,f):
    sql = "delete from 教研项目 where 项目名称='{0}' and 项目负责人='{1}' and 项目成员='{2}' and 级别='{3}' and 立项时间='{4}' and 结项时间='{5}' and 验收结论='{6}'".format(pname,a,b,c,d,e,f)
    db_exec(sql)
    return redirect(url_for('teaching_research_project'))

@app.route('/edit7/<pname>/<a>/<b>/<c>/<d>/<e>/<f>',methods=['GET', 'POST'])
def edit7(pname,a,b,c,d,e,f):
    if request.method=='GET':
        sql="select * from 教研项目 where 项目名称='{0}' and 项目负责人='{1}' and 项目成员='{2}' and 级别='{3}' and 立项时间='{4}' and 结项时间='{5}' and 验收结论='{6}'".format(pname,a,b,c,d,e,f)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'项目名称': row[0], '项目负责人': row[1], '项目成员': row[2],'级别': row[3], '立项时间': row[4],'结项时间': row[5],'验收结论': row[6]})
        return render_template('edit7.html', loader=loaders)
    else:
        new_pname=request.form.get('项目名称')
        new_a=request.form.get('项目负责人')
        new_b=request.form.get('项目成员')
        new_c=request.form.get('级别')
        new_d=request.form.get('立项时间')
        new_e=request.form.get('结项时间')
        new_f=request.form.get('验收结论')
        sql="update 教研项目 set 项目名称='{0}', 项目负责人='{1}', 项目成员='{2}', 级别='{3}',立项时间='{4}',结项时间='{5}',验收结论='{6}' where  项目名称='{7}' and 项目负责人='{8}' and 项目成员='{9}' and 级别='{10}' and 立项时间='{11}' and 结项时间='{12}' and 验收结论='{13}'".format(
           new_pname,new_a,new_b,new_c,new_d,new_e,new_f,pname,a,b,c,d,e,f
        )
        db_exec(sql)
        return redirect(url_for('teaching_research_project'))

@app.route('/delete8/<a>/<b>/<c>/<d>/<class_num>/<e>/<f>/<g>/<h>/<i>/<j>/<k>/<l>/<m>/<n>/<o>/<p>/<q>/<r>/<s>/<t>')
def delete8(a,b,c,d,class_num,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t):
    sql = "delete from 本科工作量课程排序表 where 学年='{0}' and 学期='{1}' and 自然年='{2}' and 上下半年='{3}' and 课程号='{4}' and 课程名称='{5}' and 教工号='{6}' and 教师名称='{7}' and  研讨学时='{8}' and 授课学时='{9}' and 实验学时='{10}' and 选课人数='{11}' and 学生数量权重系数B='{12}' and 课程类型系数A='{13}' and 理论课总学时P1='{14}' and  实验分组数='{15}' and 实验课系数='{16}' and 实验课总学时P2='{17}' and 课程拆分占比='{18}' and 本科课程总学时='{19}' and 课程总学时='{20}'".format(a,b,c,d,class_num,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t)
    db_exec(sql)
    return redirect(url_for('teacher_clas'))

@app.route('/edit8/<a>/<b>/<c>/<d>/<class_num>/<e>/<f>/<g>/<h>/<i>/<j>/<k>/<l>/<m>/<n>/<o>/<p>/<q>/<r>/<s>/<t>',methods=['GET', 'POST'])
def edit8(a,b,c,d,class_num,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t):
    if request.method=='GET':
        sql="select * from 本科工作量课程排序表 where 学年='{0}' and 学期='{1}' and 自然年='{2}' and 上下半年='{3}' and 课程号='{4}' and 课程名称='{5}' and 教工号='{6}' and 教师名称='{7}' and  研讨学时='{8}' and 授课学时='{9}' and 实验学时='{10}' and 选课人数='{11}' and 学生数量权重系数B='{12}' and 课程类型系数A='{13}' and 理论课总学时P1='{14}' and  实验分组数='{15}' and 实验课系数='{16}' and 实验课总学时P2='{17}' and 课程拆分占比='{18}' and 本科课程总学时='{19}' and 课程总学时='{20}'".format(a,b,c,d,class_num,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'学年': row[0], '学期': row[1], '自然年': row[2],'上下半年': row[3], '课程号': row[4],'课程名称': row[5], '教工号':row[6],'教师名称': row[7],'研讨学时': row[8],'授课学时': row[9],'实验学时': row[10],'选课人数': row[11], '学生数量权重系数B': row[12], '课程类型系数A': row[13],'理论课总学时P1': row[14], '实验分组数': row[15],'实验课系数': row[16],'实验课总学时P2': row[17],'课程拆分占比': row[18],'本科课程总学时': row[19],'课程总学时': row[20]})
        return render_template('edit8.html', loader=loaders)

    else:
        new_a=request.form.get('学年')
        new_b=request.form.get('学期')
        new_c=request.form.get('自然年')
        new_d=request.form.get('上下半年')
        new_class_num=request.form.get('课程号')
        new_e=request.form.get('课程名称')
        new_f=request.form.get('教工号')
        new_g=request.form.get('教师名称')
        new_h=request.form.get('研讨学时')
        new_i=request.form.get('授课学时')
        new_j=request.form.get('实验学时')
        new_k=request.form.get('选课人数')
        new_l=request.form.get('学生数量权重系数B')
        new_m=request.form.get('课程类型系数A')
        new_n=request.form.get('理论课总学时P1')
        new_o=request.form.get('实验分组数')
        new_p=request.form.get('实验课系数')
        new_q=request.form.get('实验课总学时P2')
        new_r=request.form.get('课程拆分占比')
        new_s=request.form.get('本科课程总学时')
        new_t=request.form.get('课程总学时')
        sql="update 本科工作量课程排序表 set 学年='{0}', 学期='{1}', 自然年='{2}', 上下半年='{3}',课程号='{4}',课程名称='{5}',教工号='{6}',教师名称='{7}', 研讨学时='{8}',授课学时='{9}',实验学时='{10}',选课人数='{11}', 学生数量权重系数B='{12}', 课程类型系数A='{13}',理论课总学时P1='{14}', 实验分组数='{15}',实验课系数='{16}',实验课总学时P2='{17}',课程拆分占比='{18}',本科课程总学时='{19}',课程总学时='{20}' where 学年='{21}' and 学期='{22}' and 自然年='{23}' and 上下半年='{24}' and 课程号='{25}' and 课程名称='{26}' and 教工号='{27}' and 教师名称='{28}' and  研讨学时='{29}' and 授课学时='{30}' and 实验学时='{31}' and 选课人数='{32}' and 学生数量权重系数B='{33}' and 课程类型系数A='{34}' and 理论课总学时P1='{35}' and  实验分组数='{36}' and 实验课系数='{37}' and 实验课总学时P2='{38}' and 课程拆分占比='{39}' and 本科课程总学时='{40}' and 课程总学时='{41}'".format(
            new_a,new_b,new_c,new_d,new_class_num,new_e,new_f,new_g,new_h,new_i,new_j,new_k,new_l,new_m,new_n,new_o,new_p,new_q,new_r,new_s,new_t,a,b,c,d,class_num,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t
        )
        db_exec(sql)
    return redirect(url_for('teacher_clas'))

@app.route('/delete9/<a>/<snum>/<b>/<c>/<d>/<e>/<f>/<g>/<h>')
def delete9(a,snum,b,c,d,e,f,g,h):
    sql = "delete from 毕业论文 where 姓名='{0}' and 学号='{1}' and 学院='{2}' and 专业='{3}' and 专业号='{4}' and 年级='{5}' and 毕业论文题目='{6}' and 毕业论文成绩='{7}' and 毕业论文指导老师='{8}'".format(a,snum,b,c,d,e,f,g,h)
    db_exec(sql)
    return redirect(url_for('thesis_18'))

@app.route('/edit9/<a>/<snum>/<b>/<c>/<d>/<e>/<f>/<g>/<h>',methods=['GET', 'POST'])
def edit9(a,snum,b,c,d,e,f,g,h):
    if request.method=='GET':
        sql="select * from  毕业论文 where 姓名='{0}' and 学号='{1}' and 学院='{2}' and 专业='{3}' and 专业号='{4}' and 年级='{5}' and 毕业论文题目='{6}' and 毕业论文成绩='{7}' and 毕业论文指导老师='{8}'".format(a,snum,b,c,d,e,f,g,h)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'姓名': row[0], '学号': row[1], '学院': row[2],'专业': row[3], '专业号': row[4],'年级': row[5],'毕业论文题目': row[6],'毕业论文成绩': row[7],'毕业论文指导老师': row[8]})
        return render_template('edit9.html', loader=loaders)
    else:
        new_a=request.form.get('姓名')
        new_snum=request.form.get('学号')
        new_b=request.form.get('学院')
        new_c=request.form.get('专业')
        new_d=request.form.get('专业号')
        new_e=request.form.get('年级')
        new_f=request.form.get('毕业论文题目')
        new_g=request.form.get('毕业论文成绩')
        new_h=request.form.get('毕业论文指导老师')
        sql="update 毕业论文 set 姓名='{0}', 学号='{1}', 学院='{2}', 专业='{3}',专业号='{4}',年级='{5}',毕业论文题目='{6}',毕业论文成绩='{7}',毕业论文指导老师='{8}' where 姓名='{9}' and 学号='{10}' and 学院='{11}' and 专业='{12}' and 专业号='{13}' and 年级='{14}' and 毕业论文题目='{15}' and 毕业论文成绩='{16}' and 毕业论文指导老师='{17}'".format(
            new_a,new_snum,new_b,new_c,new_d,new_e,new_f,new_g,new_h,a,snum,b,c,d,e,f,g,h
        )
        db_exec(sql)
        return redirect(url_for('thesis_18'))
@app.route('/delete10/<a>/<b>/<c>/<d>/<snum>/<e>')
def delete10(a,b,c,d,snum,e):
    sql = "delete from 本科生导师制 where 导师姓名='{0}' and 教工号='{1}' and 学生姓名='{2}' and  年级='{3}' and 学号='{4}' and 说明='{5}'".format(a,b,c,d,snum,e)
    db_exec(sql)
    return redirect(url_for('undergraduate_mentorship'))

@app.route('/edit10/<a>/<b>/<c>/<d>/<snum>/<e>', methods=['GET', 'POST'])
def edit10(a, b, c, d, snum, e):
    if request.method == 'GET':
        sql = "SELECT * FROM 本科生导师制 WHERE 导师姓名='{0}' AND 教工号='{1}' AND 学生姓名='{2}' AND 年级='{3}' AND 学号='{4}' AND 说明='{5}'".format(a, b, c, d, snum, e)
        data = db_query(sql)
        loaders = []
        for row in data:
            loaders.append({'导师姓名': row[0], '教工号': row[1], '学生姓名': row[2],'年级': row[3], '学号': row[4], '说明': row[5]})
        return render_template('edit10.html', loader=loaders)
    else:
        new_a = request.form.get('导师姓名')
        new_b = request.form.get('教工号')
        new_c = request.form.get('学生姓名')
        new_d = request.form.get('年级')
        new_snum = request.form.get('学号')
        new_e = request.form.get('说明')
        sql = "UPDATE 本科生导师制 SET 导师姓名='{0}', 教工号='{1}', 学生姓名='{2}', 年级='{3}', 学号='{4}', 说明='{5}' WHERE 导师姓名='{6}' AND 教工号='{7}' AND 学生姓名='{8}' AND 年级='{9}' AND 学号='{10}' AND 说明='{11}'".format(new_a, new_b, new_c, new_d, new_snum, new_e, a, b, c, d, snum, e)
        db_exec(sql)
        return redirect(url_for('undergraduate_mentorship'))


#增加数据
@app.route('/add1', methods=['GET', 'POST'])
def add1():
    if request.method == 'GET':
        return render_template('add1.html')
    else:
        # POST
        sql = "insert into 一流课程 values('{0}', '{1}', '{2}', '{3}')".format(
            request.form.get('课程性质'),
            request.form.get('内容'),
            request.form.get('负责人'),
            request.form.get('工作量分配'),
        )
        db_exec(sql)
        return redirect(url_for('first_class_courses'))

@app.route('/add2', methods=['GET', 'POST'])
def add2():
    if request.method == 'GET':
        return render_template('add2.html')
    else:
        # POST
        sql = "insert into 本科实习 values('{0}', '{1}', '{2}', '{3}', '{4}')".format(
            request.form.get('姓名'),
            request.form.get('学号'),
            request.form.get('专业'),
            request.form.get('年级'),
            request.form.get('学部内实习指导教师'),
        )
        db_exec(sql)
        return redirect(url_for('internship_19'))

@app.route('/add3', methods=['GET', 'POST'])
def add3():
    if request.method == 'GET':
        return render_template('add3.html')
    else:
        # POST
        sql = "insert into 公共服务 values('{0}', '{1}', '{2}', '{3}', '{4}')".format(
            request.form.get('日期'),
            request.form.get('内容'),
            request.form.get('姓名'),
            request.form.get('工作时长'),
            request.form.get('课时')
        )
        db_exec(sql)
        return redirect(url_for('public_service'))
@app.route('/add4', methods=['GET', 'POST'])
def add4():
    if request.method == 'GET':
        return render_template('add4.html')
    else:
        # POST
        sql = "insert into 学生竞赛 values('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}','{7}')".format(
            request.form.get('赛事名称'),
            request.form.get('作品名称'),
            request.form.get('获奖类别'),
            request.form.get('获奖等级'),
            request.form.get('获奖学生'),
            request.form.get('指导教师'),
            request.form.get('总工作量'),
            request.form.get('获奖年份'),
        )
        db_exec(sql)
        return redirect(url_for('student_competition'))
@app.route('/add5', methods=['GET', 'POST'])
def add5():
    if request.method == 'GET':
        return render_template('add5.html')
    else:
        # POST
        sql = "insert into 学生科研 values('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}','{7}','{8}')".format(
            request.form.get('序号'),
            request.form.get('项目名称'),
            request.form.get('级别'),
            request.form.get('负责人'),
            request.form.get('学号'),
            request.form.get('项目组总人数'),
            request.form.get('指导老师'),
            request.form.get('验收结论'),
            request.form.get('总工作量'),
        )
        db_exec(sql)
        return redirect(url_for('student_research'))
@app.route('/add6', methods=['GET', 'POST'])
def add6():
    if request.method == 'GET':
        return render_template('add6.html')
    else:
        # POST
        sql = "insert into 教学成果奖 values('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}','{7}')".format(
            request.form.get('届'),
            request.form.get('时间'),
            request.form.get('推荐成果名称'),
            request.form.get('成果主要完成人姓名'),
            request.form.get('获奖类别'),
            request.form.get('获奖等级'),
            request.form.get('备注'),
            request.form.get('工作总量'),
        )
        db_exec(sql)
        return redirect(url_for('teaching_achievement_award'))
@app.route('/add7', methods=['GET', 'POST'])
def add7():
    if request.method == 'GET':
        return render_template('add7.html')
    else:
        # POST
        sql = "insert into 教研项目 values('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}')".format(
            request.form.get('项目名称'),
            request.form.get('项目负责人'),
            request.form.get('项目成员'),
            request.form.get('级别'),
            request.form.get('立项时间'),
            request.form.get('结项时间'),
            request.form.get('验收结论'),
        )
        db_exec(sql)
        return redirect(url_for('teaching_research_project'))
@app.route('/add8', methods=['GET', 'POST'])
def add8():
    if request.method=='GET':
        return  render_template('add8.html')
    else:
        sql = "insert into 本科工作量课程排序表 values('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}','{7}', '{8}', '{9}', '{10}', '{11}','{12}','{13}','{14}', '{15}', '{16}','{17}','{18}','{19}','{20}')".format(
            request.form.get('学年'),
            request.form.get('学期'),
            request.form.get('自然年'),
            request.form.get('上下半年'),
            request.form.get('课程号'),
            request.form.get('课程名称'),
            request.form.get('教工号'),
            request.form.get('教师名称'),
            request.form.get('研讨学时'),
            request.form.get('授课学时'),
            request.form.get('实验学时'),
            request.form.get('选课人数'),
            request.form.get('学生数量权重系数B'),
            request.form.get('课程类型系数A'),
            request.form.get('理论课总学时P1'),
            request.form.get('实验分组数'),
            request.form.get('实验课系数'),
            request.form.get('实验课总学时P2'),
            request.form.get('课程拆分占比'),
            request.form.get('本科课程总学时'),
            request.form.get('课程总学时')
        )
        db_exec(sql)
        return redirect(url_for('teacher_clas'))
@app.route('/add9', methods=['GET', 'POST'])
def add9():
    if request.method == 'GET':
        return render_template('add9.html')
    else:
        # POST
        sql = "insert into 毕业论文 values('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}','{7}','{8}')".format(
            request.form.get('姓名'),
            request.form.get('学号'),
            request.form.get('学院'),
            request.form.get('专业'),
            request.form.get('专业号'),
            request.form.get('年级'),
            request.form.get('毕业论文题目'),
            request.form.get('毕业论文成绩'),
            request.form.get('毕业论文指导老师'),
        )
        db_exec(sql)
        return redirect(url_for('thesis_18'))
@app.route('/add10', methods=['GET', 'POST'])
def add10():
    if request.method == 'GET':
        return render_template('add10.html')
    else:
        # POST
        sql = "insert into 本科生导师制 values('{0}', '{1}', '{2}', '{3}', '{4}','{5}')".format(
            request.form.get('导师姓名'),
            request.form.get('教工号'),
            request.form.get('学生姓名'),
            request.form.get('年级'),
            request.form.get('学号'),
            request.form.get('说明'),
        )
        db_exec(sql)
        return redirect(url_for('undergraduate_mentorship'))


@app.route('/data_query')
def data_query():
    sql = "select * from 本科工作量教师排序表"
    data = db_query(sql)
    loaders = []
    for row in data:
        loaders.append({'教工号': row[0], '教师名称': row[1], '本科课程总学时': row[2],'课程总学时': row[3], '毕业论文学生人数': row[4],'毕业论文P': row[5], '指导教学实习人数':row[6],'指导教学实习周数': row[7],'指导教学实习P': row[8],'负责实习点建设与管理P': row[9],'指导本科生竞赛P': row[10],'指导本科生科研P': row[11], '本科生导师制': row[12], '教研教改P': row[13],'一流课程': row[14], '教学成果奖': row[15],'公共服务': row[16]})
    return render_template('data_query.html', loaders=loaders)

@app.route('/fun')
def fun():
    db_fun()
    return redirect(url_for('data_query'))




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

