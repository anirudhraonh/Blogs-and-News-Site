from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.all_blogs,name="BlogsPage"),
    path('<int:user_id>/',views.user_blogs,name="UserBlogs"),
    path('CreateBlogPost/',views.create_blog,name="CreateBlog"),
    path('blog/<str:title>/',views.blog_post,name="BlogPost"),
    path('<str:title>/delete',views.delete_blog,name="delete"),

]
