from django.shortcuts import render

# Create your views here.
from django.core import serializers  

from django.shortcuts import render, HttpResponse, Http404, get_object_or_404
import json
from django.contrib.auth import get_user_model
from django.contrib import auth

from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.template import RequestContext
from django.shortcuts import render_to_response
from dss.Serializer import serializer



User = get_user_model();

def home(request):
	print('tokennnnn______')
	return render(request, 'csrf_home.html')


# 查询电子病历的类型

def test(requese):
	print(requese.COOKIES)

	return HttpResponse('jsons', content_type="application/json")	

# 账号注册
@csrf_exempt
def recv_regist(request):
	print('注册——————');
	if request.method == 'POST':
		req = json.loads(request.body);
		telpNum = req.get('telpNum',None);
		password = req.get('pw',None);
		nickname = req.get('nickname',None);


		responseData = {};
		responseData['status'] = '-1';
		responseData['msg'] = '注册失败';
		if not telpNum:
			responseData['msg'] = '请输入手机号';

		if not nickname:
			responseData['msg'] = '请输入用户名';
			
		if not password:
			responseData['msg'] = '请输入密码';	


		if telpNum is not None and password is not None and nickname is not None:
			try:
				user=User.objects.create_user(telphone=telpNum,nickName=nickname,password=password)
				user.save
				responseData['status'] = '1';
				responseData['msg'] = '注册成功';
			except Exception as e:
				print(str(e));
				if str(e) == 'UNIQUE constraint failed: myUser_myuser.nickName':
					responseData['msg'] = '用户名已使用';
				elif str(e) == 'UNIQUE constraint failed: myUser_myuser.telphone':
					responseData['msg'] = '该手机已注册';

					

		jsons = json.dumps(responseData)
		return HttpResponse(jsons, content_type="application/json")
	else:
		jsons = json.dumps({'status':'-1','msg':'注册密码失败，请使用post'})		
		return HttpResponse(jsons, content_type="application/json")




@csrf_exempt
def recv_login(request):

	responseData = {};
	responseData['status'] = '-1';
	responseData['msg'] = '登录失败';

	if request.method == 'POST':
		req = json.loads(request.body);
		telpNum = req.get('telpNum',None);
		password = req.get('pw',None);

		if not telpNum:
			responseData['msg'] = '请输入手机号';
			
		if not password:
			responseData['msg'] = '请输入密码';

		if telpNum is not None and password is not None:
			myuser = auth.authenticate(telphone=telpNum,password=password)
			if myuser:
				auth.login(request, myuser)
				responseData['status'] = '1';
				responseData['msg'] = '登录成功';
	jsons = json.dumps(responseData)

	print('登录:'+jsons)
	
	return HttpResponse(jsons, content_type="application/json")	




def recv_loginOut(request):
	if request.method == 'POST':
		hh = request.user;
		print('退出——————');	
		print(hh)
		print('退出——————');

		print(request.COOKIES)


	
	
	auth.logout(request)
	jsons = json.dumps({'status':'1','msg':'退出登录'})
	return HttpResponse(jsons, content_type="application/json")	


@csrf_protect
def recv_infomation(request):

	responseData = {};
	responseData['status'] = '-1';
	responseData['msg'] = 'get information failed';

	if request.method == 'POST':
		myuser = request.user;
		
		if myuser.is_authenticated():
			responseData['status'] = '1';
			responseData['msg'] = serializer(request.user)
		else:
			print('非法用户')

	jsons = json.dumps(responseData)
	print('get user infomation :'+jsons)
	return HttpResponse(jsons, content_type="application/json")	











