from django.contrib.auth import logout
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('<str:users_id>/',views.func,name="home"),
    path('addposts/<str:users_id>/',views.ren,name="addpost"),
    path('logut',views.lgout,name="logout"),
    path('abot/<str:users_id>/',views.abt,name="about"),
    path('spost/<str:posts_id>/',views.spost,name="posts"),
    path('manage/<str:users_id>/',views.manage,name="manage"),
    path('update/<str:posts_id>/',views.update,name="update"),
    path('delete/<str:posts_id>/',views.delete,name="delete"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
