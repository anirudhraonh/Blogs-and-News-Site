from django.urls import path
from .views import home,reg,logout_page,news
from django.contrib.auth import views as auth_views

app_name = 'main'
urlpatterns = [
    path('', home, name="Home"),
    path('news/', news, name="News"),
    path('reg/', reg, name="Reg"),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='Login'),
    path('logout/', logout_page, name="logout"),
]
