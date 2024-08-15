# 教师工作量采集与分析系统文件

# ***<u>重要提醒</u>***！！

请基于此框架代码进行更新代码的人员务必先对此文件进行阅读！

需要修改[Config.py](#config.py)文件夹内的有关内容！

需要配置本工程文件环境！

# 工程说明

本项目是基于python开发的flask网站工程，主要采用了sqlalchemy扩展以实现ORM技术

# 工程环境配置

所有的开发环境可以根据![image-20240815142622678](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815142622678.png)

进行下载

# 网页展示

![image-20240815152724744](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152724744.png)

![image-20240815152738766](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152738766.png)

![image-20240815152746174](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152746174.png)

![image-20240815152751409](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152751409.png)

# 文件框架

所有的工程文件位于version_four文件夹中

![image-20240815142329292](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815142329292.png)

以下为version_four文件夹下全部内容，下对各个文件进行说明

![image-20240815142340524](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815142340524.png)

### **.idea**文件夹与 ** __pycache__**文件夹

配置文件夹，不用进行修改，用pycharm或者vscode编辑器打开整个文件夹时会在本地进行自动修改

### app.py文件

整个工程文件的主要启动文件，通过运行app.py文件来进行开发，下对该文件内容代码做出解释

**导入必要的库**

![image-20240815143238304](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815143238304.png)

**读取配置**，此处的具体配置文件可访问[Config.py](#config.py)

![image-20240815143259627](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815143259627.png)

**使登陆的页面为login.html**

![image-20240815144058374](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144058374.png)

**初始化对象**

![image-20240815144137149](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144137149.png)

**对数据库进行备份处理，利用flask-migrate**

![image-20240815144156399](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144156399.png)

**这里实现了三个功能即登陆、注册、登出**三个功能

![image-20240815144304885](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144304885.png)

**对登陆的基本逻辑进行说明**![image-20240815144412699](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144412699.png)

获取网页前端的账号和密码，通过账号在数据库中进行查找对应的加密密码，再对比密码，正确即可通过。

**对注册的基本逻辑进行说明**

![image-20240815144642490](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144642490.png)

获取教工号、教师姓名、密码，重复密码，同时满足***密码与重复密码需要相同，教工号没有重复***即可注册

**登陆后进入index.html**![image-20240815144803134](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144803134.png)

**注册蓝图 ** **analyse_page** 、**modify_page**、**upload_page**三个蓝图

![image-20240815144814040](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815144814040.png)

### **analyse_page** 、**modify_page**、**upload_page**三个文件夹

#### **analyse_page文件夹**

![image-20240815143013023](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815143013023.png)

主要文件为 **analyse_page_bp.py**文件，__pycache__文件夹同所有类似的文件夹一样为pycharm开发环境，不用进行手动修改

此处注册蓝图，指向渲染的网页文件夹**templates**

![image-20240815145124320](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145124320.png)

![image-20240815145212876](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145212876.png)

基本逻辑

@login_required注释器意为需要登陆后才能访问的网站

获取前端网页的教工号和教师姓名，查询数据库中存有的有关数据，将数据与标题行一同传给前端进行渲染

#### modify_page

同样只需要关注![image-20240815145454188](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145454188.png)

注册蓝图![image-20240815145512911](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145512911.png)

该蓝图有两个功能![image-20240815145524642](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145524642.png)

第一个函数是为了获取所有的要修改的数据库的数据，第二个函数是应用修改后的数据库的数据

![image-20240815145634509](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145634509.png)

**第一个函数的具体说明**以该数据库为例，其基本逻辑为根据表名以及教工号，教师姓名在数据库中进行查找然后返回前端进行渲染

![image-20240815145800175](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145800175.png)

**第二个函数的具体说明**以该数据库为例，将json_data数据重新写到对应的数据库中去

#### upload_page

同样仅需关注![image-20240815145919893](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815145919893.png)

四个主要的功能函数

![image-20240815150007043](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815150007043.png)

分别为重定向到该网页、批量上传数据、展示要提交数据的表单模板、手动提交表单进行修改

其中 **重定向**与 **展示**要提交数据的表单模板 与 **手动提交表单进行修改**的基本逻辑同上方的类似函数基本相同，不过多赘述

**批量上传数据**函数![image-20240815150212127](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815150212127.png)

逻辑为 1、获取上传的文件 2、对文件的格式进行**确认**（此处有函数进行处理，但逻辑非常简单不多做赘述） 3、对文件进行处理 4、将数据上传到对应的数据库中

其中**处理**的函数![image-20240815150340778](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815150340778.png)

为这个，基本逻辑是对excel表格中的每一行数据转变成json类型的数据，然后依次上传

### <span id="jump1">Config.py</span>

![image-20240815150524310](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815150524310.png)

**配置的基本文件，其中请开发人员在本地进行开发的时候，请务必修改掉user、password与database，改成自己的数据库内容以确保链接成功**

### migrations

该文件夹主要储存数据库的各个版本，一般来说不用修改，同git非常像，具体使用办法可以进行百度，主要用于数据库的版本管理以及同步

![image-20240815151013779](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815151013779.png)



### static

![image-20240815151136917](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815151136917.png)

渲染网页用的格式css文件等均放在此处，不多赘述

### templates

![image-20240815151216180](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815151216180.png)

前端网页界面，不多赘述

### uploads

![image-20240815151337289](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815151337289.png)

上传的文件临时存放的位置，不用手动修改

### database.py

![image-20240815151433801](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815151433801.png)

为了导入db，主要是为了解决**循环导入**的问题，不用进行修改

### models.py

![image-20240815151512908](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815151512908.png)

该文件为本工程文件**最为重要**的文件之一！！！

![image-20240815151608317](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815151608317.png)

本工程文件采用了sqlalchemy的格式，如果开发人员并不熟悉这一块内容请访问sqlalchemy的官方说明文档！！！

上面的内容（三个函数之前的内容）为对应的数据库内的表的字段，如果开发人员对这一块内容进行修改，请务必使用migration进行记录

下面的三个函数的作用分别是将查询出来的结果转变成列表，添加数据，更新数据，使用方法同官方用法，不多赘述

其中有**两个比较特殊**

一个是![image-20240815152056202](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152056202.png)

这个表主要用于存储信息记录，它下面的函数主要是对密码进行加密、确认

另一个是![image-20240815152137983](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152137983.png)

这个数据表主要负责储存一些参数方便计算教师工作量

![image-20240815152205879](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152205879.png)

![image-20240815152211307](C:\Users\13190\AppData\Roaming\Typora\typora-user-images\image-20240815152211307.png)

这些内容是触发器的书写以及触发器的应用，为了同步最终教师工作量的计算

### teacher_work.sql

这个文件夹是将数据库的表再次导出成sql文件，时效性无法保证，如果无法根据models.py进行建表的时候请使用该文件

### teacherwork.py

~~该文件是根据models.py文件内的格式在本地进行建表，请同样修改有关数据库的设置~~

请还是使用migration进行建表

### test.py

无意义，开发过程中为了检测错误和测试使用的文件

### 数据库设计.docx

文字形式的数据库设计，可能同最新的设计有所出入，仅供参考



# 当前的不足之处

在文件批量导入处没有限制条件，即如果上传的文件内容不对应可能会导致一些问题。

网页的UI设计仍然需要更新