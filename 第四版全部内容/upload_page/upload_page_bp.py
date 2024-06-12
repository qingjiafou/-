# 导入蓝图
import os
from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from 第四版全部内容.Config import Config

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

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}


# 检查文件扩展名是否符合要求
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 用蓝图注册路由
# 跳转到这个界面
@upload_page_blueprint.route("/file_upload")
def file_upload_page():
    return render_template('file_upload.html')


@upload_page_blueprint.route("/file_upload/load", methods=['POST', 'GET'])
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
        # 在这里处理文件，例如保存到服务器等
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
        flash({'success': '文件上传成功'})
        return redirect(url_for('upload_page.upload_file'))
