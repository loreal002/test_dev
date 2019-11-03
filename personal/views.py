from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def say_hello(request):
    input_name = request.GET.get("name",'')
    if input_name == '':
        return HttpResponse("请输入姓名")
    return render(request,'index.html',{"name":input_name})

def index(request):
    
    """
    登录功能
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')

        if username == '' or password == '':
            return render(request, 'index.html', {"error": "用户名或密码不能为空"})

        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, 'index.html', {"error": "用户名或密码错误"})
        else:
            auth.login(request,user) #记录认证通过的用户
            return HttpResponseRedirect("/project/")

@login_required
def project_manage(request):
    return render(request, 'project.html')


@login_required
def module_manage(request):
    return render(request, 'module.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')









# def login_action(request):
#     """
#     处理登陆
#     :param request:
#     :return:
#     """
#     username = request.POST.get("username",'')
#     password = request.POST.get("password",'')
#
#     if username == 'admin' and password == 'admin123':
#         return HttpResponse('登陆成功')
#     elif username == '' or password == '':
#         return render(request,'index.html',{"error":"用户名或密码不能为空"})
#         # return HttpResponse("用户名或密码不能为空")
#     else:
#         return render(request, 'index.html', {"error": "用户名或密码错误"})

