urlpatterns = [
    path('', views.ins, name='in'),
    path('house/', include([
        path('recommend/', views.recommend, name='recommend'),
        path('create/', views.create, name='create'),
        path('getall/', views.getMyInfo, name='getall'),
        path('suspend/', views.getAllUsers, name='suspend'),
        path('update/', views.update, name='update'),
        path('search/', views.update, name='search'),
    ])),
]
