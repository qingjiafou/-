from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from version_four.Config import Config
from version_four.database import db
from version_four.modify_page.modify_page_bp import modify_page_blueprint
from version_four.analyse_page.analyse_page_bp  import analyse_page_blueprint
from version_four.upload_page.upload_page_bp import upload_page_blueprint
from version_four.models import UndergraduateWorkloadTeacherRanking, TeacherInformation

app = Flask(__name__, template_folder='templates')

# 读取配置
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = 'login'  # 设置登录视图名称


# 创建数据库sqlalchemy工具对象
db.init_app(app)

Migrate(app, db)


@login_manager.user_loader
def load_user(teacher_id):
    return TeacherInformation.query.get(teacher_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form['action']
        if action == 'login':
            # 处理登录操作
            user = TeacherInformation.query.filter_by(teacher_id=username).first()
            if user and user.verify_password(password):
                login_user(user)  # 登入用户
                return redirect(url_for('index'))  # 重定向到主页
            else:
                # 登录失败处理
                flash('Invalid username or password')
                return redirect(url_for('login'))  # 渲染登录页面
        else:
            return redirect(url_for('register'))
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        teacher_name = request.form['teacher_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        #教工号、教师姓名、密码
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('register'))

        existing_user = TeacherInformation.query.filter_by(teacher_id=username).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        TeacherInformation.add_teacher_info(username, teacher_name, password)

        flash('Registration successful, please login')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')  # 登出
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html',teacher_id=current_user.teacher_id)


app.register_blueprint(upload_page_blueprint)
app.register_blueprint(modify_page_blueprint)
app.register_blueprint(analyse_page_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
