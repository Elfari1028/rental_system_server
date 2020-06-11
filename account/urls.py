from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    path('', views.ins, name='in'),
    path('account/', include([
        path('login/', views.login, name='login'),
        path('register/', views.register, name='register'),
        path('get/', views.getMyInfo, name='getMyInfo'),
        path('getall/', views.getAllUsers, name='getall'),
        path('update/', views.update, name='update'),
        path('avatar/',views.uploadAvatar, name='updateAvatar'),
    ])),
]
