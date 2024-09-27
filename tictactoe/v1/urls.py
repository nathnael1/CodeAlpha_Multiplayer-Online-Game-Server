from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name= 'index'),
    path('game/<str:room_code>', views.game_view, name='game_view'),
]
