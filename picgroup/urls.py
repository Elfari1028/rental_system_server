from django.urls import path
from . import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('picgroup/', include([
        path('obtain/', views.obtainPics, name='obtain'),
        path('upload/', views.upload, name='upload'),
        path('remove/', views.remove, name='remove'),
        path('delete/', views.delete, name='delete'),
        path('append/', views.append, name='append'),
    ]))
]
