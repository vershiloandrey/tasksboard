from django.shortcuts import render, redirect
from .models import Task
from .models import Login
from .models import Comment
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import CommentForm


def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                auth.login(request, user)
                print("User is valid, active and authenticated")
                return redirect('task_list')
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
    return render(request, 'blog/page_login.html', {})


def logout(request):
    auth.logout(request)
    return redirect("/")


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'blog/task_list.html', {'tasks': tasks, 'username': auth.get_user(request).username})


def task_detail(request, task_id=1):
    return render(request, 'blog/task_detail.html',
                  {'task': Task.objects.get(id=task_id), 'comments': Comment.objects.filter(comment_task=task_id)})


def addComment(request, task_id=1):
    if request.POST:
        form = CommentForm(request.POST)
        if form.isvalid():
            comment = form.save(commit=False)
            comment.comment_task = Task.objects.get(id=task_id)
            form.save()
    return redirect('/task_detail/%s' % task_id)
