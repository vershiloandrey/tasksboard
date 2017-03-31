from django.contrib import admin
from .models import Task
from .models import Login
from .models import Comment

admin.site.register(Task)
admin.site.register(Login)
admin.site.register(Comment)
