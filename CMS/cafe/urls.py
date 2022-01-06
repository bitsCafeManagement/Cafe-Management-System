from django.urls import path
from . import views

urlpatterns = [
    path('cafehome/', views.homecafe, name = 'homecafe'),
    path('profile/', views.profile, name='profile'),
    path('cafemenu', views.menu, name='menucafe'),
    path('cafecommunity', views.community, name='communitycafe'),
]