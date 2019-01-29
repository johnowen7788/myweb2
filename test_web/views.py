from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import  HttpResponse
# 将请求定位到index.html文件中
def index(request):
    #业务逻辑对应着不同的业务逻辑，这里转到一个页面。
    #if request.method == "POST ":
    #   username = request.POST.get("username",None)
    #   password = request.POST.get("username", None)
    #   print(username,password)
    return render(request,'index.html')
def index2(request):
    return render(request,'index2.html')