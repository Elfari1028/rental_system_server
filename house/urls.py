from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('house/', include([
        path('recommend/', views.recommend, name='recommend'),
        path('create/', views.create, name='create'),
        path('getall/', views.getAllHouses, name='getall'),
        # path('suspend/', views.suspend, name='suspend'),
        path('available/',views.getAvailHouses,name='get avail'),
        path('update/', views.update, name='update'),
        # path('search/', views.update, name='search'),
    ])),
     path('order/', include([
        path('create/', views.createOrder, name='createorder'),
        path('getall/', views.getAllOrder, name='getall'),
        path('get/', views.getUserOrder, name='getorder'),
        # path('suspend/', views.suspend, name='suspend'),
        path('update/', views.updateOrder, name='update'),
    ])),
]
