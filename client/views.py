from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import SysInfo
# Create your views here.


def dispatcher(request):
    #通过request类型修改request.params
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST','PUT','DELETE']:
        request.params = json.loads(request.body)
    #通过method类型分派给不同的action来实现请求分发
    action = request.params['action']
    if action == 'listUserData':
        return listUserData(request)
    elif action == 'addUserData':
        return addUserData(request)
    elif action == 'deleteUserData':
        return deleteUserData(request)
    elif action == 'modifyUserData':
        return modifyUserData(request)
    else:
        return JsonResponse({'ret':1,'msg':'不支持该类型http请求'})

def listUserData(request):
    #turn query set structured data into json
    qs = SysInfo.objects.values()
    ret_list = list(qs)
    return JsonResponse({'ret':0, 'retlist':ret_list})

def addUserData(request):
    #从request.params获取数据
    info = request.params['data']
    #将转化成python object的data存入数据库
    record =  SysInfo.objects.create(os = info['os'],
                compiler = info['compiler'],
                cpu_architecture = info['cpu_architecture'])
    return JsonResponse({'ret':0,'id':record.id})

def deleteUserData(request):
    user_id = request.params['id']
    try:
        # 根据 id 从数据库中找到相应的记录
        user = SysInfo.objects.get(id=user_id)
    except SysInfo.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{user_id}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    SysInfo.delete()
    return JsonResponse({'ret': 0})

def modifyUserData(request):
    user_id = request.params['id']
    new_data = request.params['newdata']
    try:
        user = SysInfo.objects.get(id=user_id)
    except SysInfo.DoesNotExit:
        return{
            'ret':1,
            'msg':f'id为{user_id}的客户不存在'
        }
    if 'os' in new_data:
        SysInfo.os = new_data['os']
    if 'compiler' in new_data:
        SysInfo.compiler = new_data['compiler']
    if 'cpu_architecture' in new_data:
        SysInfo.cpu_architecture = new_data['cpu_architecture']
    SysInfo.save()
    return JsonResponse({'ret':0})