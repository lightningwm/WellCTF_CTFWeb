from django.urls import path
from . import views


urlpatterns = [
    path(r'contests/<int:page>/', views.contests, name='contests'),
    path(r'problems/', views.get_problems, name='problems'),
    path(r'problems/<int:type>/<int:page>/', views.get_problems, name='problems'),
    path(r'flagPost/', views.flagPost, name='flagPost'),
    path(r'contest_detail/<int:contest_id>/', views.contest_detail, name='contest_detail'),
    path(r'contest_detail/board/<int:contest_id>/', views.board, name='board'),
]
