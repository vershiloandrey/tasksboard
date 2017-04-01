from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Login(models.Model):

    login = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    rate = models.BigIntegerField(default=0)

    def __str__(self):
        return self.login


class Task(models.Model):
    id = models.BigIntegerField(default=0, unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    employee = models.ForeignKey('userprofile.UserProfile')
    published_date = models.DateTimeField(blank=True, null=True)

    # image = models.ImageField(upload_to='images/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    comment_task = models.ForeignKey('Task')
    comment_user = models.ForeignKey('userprofile.UserProfile')

    def __str__(self):
        return self.comment
