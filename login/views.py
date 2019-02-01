from django.shortcuts import render
from login import models  # 导入models文件


# Create your views here.
user_list = []

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存到数据库
        # models.UserInfo.objects.create(user=username, pwd=password)
        # print("存入数据完成")
    # 从数据库中读取所有数据，注意缩进
    # user_list = models.UserInfo.objects.all()

        temp = {'user': username, 'pwd': password}
        user_list.append(temp)

    return render(request, 'index.html', {'data': user_list})
