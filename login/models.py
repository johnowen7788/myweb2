from django.db import models

# Create your models here.
# 要继承这个类，固定写法 两个字段，分别保存用户的名字和密码  这里就是MTV中的M


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

