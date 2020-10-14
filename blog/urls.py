from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.aboutUs, name="about_us"),

    path('register/',views.register, name='register'),

    
    path('profile/', views.profile, name="profile"),
    path('dashboard/', views.dashboard, name="dashboard"),

    path('create_blog/', views.createBlog, name="create_blog"),
    path('blog/<slug:slug>/', views.blog, name="blog"),
    
    path('my-blogs/', views.myBlogs, name="my_blogs"),
]
