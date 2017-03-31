from django import forms
from .models import Task
from .models import Comment


class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ('title', 'text', 'publish_date',)

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['comment']
