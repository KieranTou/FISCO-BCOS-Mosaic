# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'createCard'

urlpatterns = [
    # 目前还没有urls
    path('createCard_set/', views.createCard_set, name='createCard_set'),
]
