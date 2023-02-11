from django.urls import path 

from . import views

urlpatterns = [
    path('',views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name='project'),
    path('create-project/',views.createproject,name='create_project'),
    path('update-project/<str:pk>/',views.updateproject,name='update_project'),
     path('delete-project/<str:pk>/',views.deleteproject,name='delete_project'),
]
