
from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^user/token', views.home,name='token'),
    url(r'^user/testApi', views.test),
    url(r'^user/regist', views.recv_regist),
    url(r'^user/login', views.recv_login),
    url(r'^user/logout', views.recv_loginOut),
    url(r'^user/getInfomation', views.recv_infomation),
    
    
]