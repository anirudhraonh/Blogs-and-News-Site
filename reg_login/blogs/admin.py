from django.contrib import admin
from .models import BlogPost,CommentModel
# Register your models here.
admin.site.register(BlogPost) 
admin.site.register(CommentModel) 