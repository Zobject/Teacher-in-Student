from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


import pymongo
try:
    conn=pymongo.MongoClient()
except:
    print 'fail'

def create(request):
    if request.method=='GET':
        print 'x'
    return render(request,'register.html')

def index(request):
    if request.method=='GET':
        return render(request,'index.html')


def createuser(request):
    db=conn['Teacher']
    collecton=db.User
    if request.method=='GET':
        user=request.GET['user']
        email=request.GET['email']
        password=request.GET['password']
        doc={'password':password,'user':user,'email':email}
        collecton.insert(doc)
        return HttpResponse('succerss1111')

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
        doc={'username':profile_names,'name':profile_name,'studentid':profile_id,'phone':profile_phone,'xi':profile_faculty,'email':profile_email,'ziwo':profile_bio,'kecheng':[]}
        print doc
        collecton.insert(doc)
        return HttpResponse('succerss')

def jion(request):
    if request.method=='GET':
        return render(request,'login.html')



def show(request):
    db=conn['Teacher']
    collecton=db.Teacher
    if request.method=='GET':
        data=list(collecton.find())
        return render(request,'show.html',{'data':data})


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
            return render(request,'login_home.html')
         else:
             return HttpResponse("error")

def createteacher(request):
        if request.method == 'GET':
            print 'x'
        return render(request, 'profile.html')



def kemu(request):
    if request.method=='GET':
        return render(request,'addsubject.html')


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
        return HttpResponse('success')


# def tianjiakemu(request):
#     if request.method=='GET':
#      return HttpResponse('ssss')