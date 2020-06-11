from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('support/', include([
        path('create/', views.createRequest, name='create request'),
    ])),
]
