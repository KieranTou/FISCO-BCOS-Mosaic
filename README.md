# FISCO-BCOS-Mosaic
毕业设计--基于区块链的征信数据名片的设计与实现

## 2023.02.26 - 2023.02.28

撰写开题报告 制作开题答辩PPT

> 准备换一下技术架构 Django+Vue3+UI框架？ 还是快速搞出来才是王道 重点在前端与合约部分

## 2023.03.09

### 配置Anaconda Django环境

`conda create --name mosaic python=3.9` 创建虚拟环境

`source activate mosaic` 激活环境

> 注意Django操作需在虚拟环境中进行

`conda remove --name xxx --all` 删除环境

`conda info -e` 查看所有环境

`pip list` 查看当前环境下安装了哪些包

> 注意 install用conda或pip uninstall也须相对应操作

`pip install django==3.1.3` 安装3.1.3版本的Django

`django-admin startproject project` 创建名为project的项目

`python manage.py runserver` 启动web服务器

> 一个app代表一个功能模块 方便代码复用

`python manage.py startapp createCard` CN（Credit Needed）创建数字卡片的功能模块

### 项目结构

project
- db.sqlite3 轻量级数据库文件 存储项目数据
- createCard 刚创建的app
- - migrations 存放数据迁移文件的目录
- - admin.py 后台管理文件
- - models.py 数据模型文件
- - views.py 视图文件
- project
- - settings.py 包含项目的配置参数
- - urls.py 根路由文件

### 配置createCard（注册app 路由基础配置）

到project/project/settings.py中找到`INSTALLED_APPS`添加即可

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 激活app
    'createCard',
]
```

配置url 到project/project/urls.py中进行修改

```python
# 导入include
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    # 配置app的url
    path('createCard/', include('createCard.urls', namespace='createCard')),
    # 参数article/分配了app的访问路径
    # include将路径分发给下一步处理
    # namespace
]
```

现在根路由为createCard的访问都会交给createCard这个app处理，但一个app也会有多个页面地址，所以app需要一路由分发，创建`createCard.urls`

需自己在createCard文件夹中创建`urls.py`

```python
# 引入path
from django.urls import path

# 正在部署的应用的名称
app_name = 'createCard'

urlpatterns = [
    # 目前还没有urls
]
```