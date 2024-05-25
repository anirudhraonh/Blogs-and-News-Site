from django import forms
from .models import BlogPost,CommentModel,Query

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','summary','image_small',)

class commentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment',)


class searchForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('query',)