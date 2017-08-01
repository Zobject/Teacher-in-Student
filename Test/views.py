from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from bson import objectid


import  xlrd

import pymongo
try:
    conn=pymongo.MongoClient()
except:
    print 'fail'

db=conn['Teacher']
# render home page
def index(request):
    if request.method=='GET':
        return render(request,'index.html')

# register user page
def create(request):
    if request.method=='GET':
        #print 'x'
     return render(request,'register.html')

# register user
def createuser(request):

    collecton=db.User
    if request.method=='GET':
        user=request.GET['user']
        email=request.GET['email']
        password=request.GET['password']
        doc={'password':password,'user':user,'email':email}
        collecton.insert(doc)
       # return HttpResponse('succerss1111')
        return  render(request,'login_home.html')

# setting profile page
def profile(request):
    if request.method=='GET':
        return render(request,'profile.html')

# update account page
def account(request):
    if request.method=='GET':
        return render(request,'account.html')

# update email page
def emails(request):
    if request.method=='GET':
        return render(request,'emails.html')

# application page
def application(request):
    if request.method=='GET':
        return render(request,'application.html')

# yuyue reservation page
def reservation(request):
    if request.method=='GET':
        return render(request,'reservation.html')

# Retrieve the password
def password_reset(request):
    if request.method=='GET':
        return render(request,'password_reset.html')


#  shen qing jia ru teacher
def acceptteacher(request):
    db=conn['Teacher']
    collecton=db.Teacher
    if request.method=='GET':
        profile_names= request.GET['profile_names']
        profile_name= request.GET['profile_name']
        profile_id = request.GET['profile_id']
        profile_faculty= request.GET['profile_faculty']
        profile_phone=request.GET['profile_phone']
        profile_email = request.GET['profile_email']
        profile_bio=request.GET['profile_bio']
        doc={'username':profile_names,'name':profile_name,'studentid':profile_id,'phone':profile_phone,'xi':profile_faculty,'email':profile_email,'ziwo':profile_bio,'kecheng':[],'time':[],'room':[]}
        print doc
        collecton.insert(doc)
        return HttpResponse('your application is submit,please wait shenhe!')

# login page
def jion(request):
    if request.method=='GET':
        return render(request,'login.html')

# teacher source list page
def show(request):
    db=conn['Teacher']
    collecton=db.Teacher
    if request.method=='GET':
        data=list(collecton.find())
        return render(request,'show.html',{'data':data})

# login panduan
@csrf_exempt
def login (request):
    db=conn['Teacher']
    collecton=db.User
    if request.method=='POST':
         name= request.POST['login']
         password=request.POST['password']
         data=collecton.find_one({'user':name})
         passw=data.get('password')
         if passw==password:
             request.session['username'] = name
             #提取 session中值
             username= request.session.get('username')
             # 将session放入到页面中 用{{username}}进行值的读取
             return render(request,'login_home.html',{'username':username})
         else:
             return HttpResponse("Your username and password didn't match!")

# application jion teacher page
def createteacher(request):
        if request.method == 'GET':
          print 'x'
        return render(request, 'profile.html',)

# add subject page
def kemu(request):
    if request.method=='GET':
        return render(request,'addsubject.html')

# add subject
def acceptkecheng(request):
    db=conn['Teacher']
    collecton=db.Teacher
    if request.method=='GET':
        print request
        kecheng=request.GET['course']
        miaoshu=request.GET['profile_bio']
        studentid=request.GET['studentid']
        doc={'kecheng':kecheng,'miaoshu':miaoshu}
        collecton.update({'studentid':studentid},{"$addToSet":{'kecheng':doc}})
        return HttpResponse('add subject success!')

# add tutors time
def accpetaddtime(request):
    if request.method=='GET':
        db = conn['Teacher']
        collecton = db.Teacher
        #print 'xxxxxxx'
        studentid=request.GET['user']
        time=request.GET['time']
        # print collecton.find_one({'studentid':1})
        collecton.update({'studentid':studentid},{'$addToSet':{'time':time}})
        print time
        return HttpResponse('add tutors time success!')

# this code has bug
def addtime(request):
         if request.method == 'GET':
             print request.GET
             if  request.GET.has_key('user') :
                 db = conn['Teacher']
                 collecton = db.Teacher
                 print 'xxxxxxx'
                 studentid = request.GET['user']
                 time = request.GET['time']
                 # print collecton.find_one({'studentid':1})
                 collecton.update({'studentid': studentid}, {'$addToSet': {'time': time}})
                 print time
                 return render(request, 'addtime.html')
             else:
                #print request
                return render(request,'addtime.html')



# dai you yuyue button de teacherlist
def teacherlist(request):
        db = conn['Teacher']
        collecton = db.Teacher
        if request.method == 'GET':
            data = list(collecton.find())
            return render(request, 'teacherlist.html', {'data': data})

def yue(request):
    if request.method=='GET':
        db = conn['Teacher']
        collecton = db.Teacher
        studentid=request.GET['id']
        data=collecton.find_one({'studentid':studentid})
        return render(request,'yue.html',{'data':data})

def addroom(request):
        if request.method == 'GET':
            print request.GET
            if request.GET.has_key('user'):
                db = conn['Teacher']
                collecton = db.Teacher
                print 'xxxxxxx'
                studentid = request.GET['user']
                time = request.GET['time']
                # print collecton.find_one({'studentid':1})
                collecton.update({'studentid': studentid}, {'$addToSet': {'room': time}})
                print time
                return render(request, 'addroom.html')
            else:
                # print request
                return render(request, 'addroom.html')


#添加新闻页面
def addnews(request):
    if request.method=='GET':
        return render(request,'addnews.html')

#获得页面信息
def acceptnews(request):
    if request.method=='GET':
        title=request.GET['title']
        content=request.GET['content']
        collecton=db.News
        collecton.insert({'title':title,'content':content})
    return HttpResponse('success')
#新闻展示列表
def delnews(request):
    if request.method=='GET':
        collection=db.News
        data=list(collection.find({}))
        return  render(request,'delnews.html',{'data':data})

#接受删除信息
def accpedelnews(request):
    if request.method=='GET':
        id=request.GET['id']
        collecton = db.News
        collecton.romove({'_id':objectid(id)})
        return  HttpResponse('success')




#
# def tianjiakemu(request):
#     if request.method=='GET':
#      return HttpResponse('ssss')
# db = conn['Teacher']
# collecton = db.Teacher
# print collecton.find_one({'studentid':'1'})