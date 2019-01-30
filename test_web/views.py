from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import  HttpResponse
# 将请求定位到index.html文件中
user_list = []


def index(request):
    # 业务逻辑对应着不同的业务逻辑，这里转到一个页面。
    if request.method == "POST ":
        print("看这里")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        temp = {'user': username, 'pwd': password}
        user_list.append(temp)
    return render(request,'index.html',{'data': user_list})


def index2(request):
    return render(request,'index2.html')
