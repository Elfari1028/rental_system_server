from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('support/', include([
        path('create/', views.createRequest, name='create request'),
        path('all/', views.getallRqs, name='get all rqs'),
        path('conversation/',views.getConverstation,name='get convo'),
        path('reply/',views.replyToRequest,name='reply'),
        path('dispatch/',views.appointFix,name='dispatch'),
        path('pickup/',views.appointRes,name='pickup'),
        path('close/',views.closeRq,name='close'),
        path('rate/',views.rate,name='close')
    ])),
]
