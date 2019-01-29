from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import  HttpResponse
# 将请求定位到index.html文件中
def index(request):
    return render(request,'index.html')
def index2(request):
    return render(request,'index2.html')