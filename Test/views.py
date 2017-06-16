from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def create(request):
    if request.method=='GET':
        print 'x'
    return render(request,'jion.html')

@csrf_exempt
def jion(request):
    if request.method=='get':
        print request.GET

    return render(request,'login.html')


def login (request):
    if request.method=='POST':
        name= request.GET['login']
        password=request.GET['password']
    return render(request,'loginin.html')