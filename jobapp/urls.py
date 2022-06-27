from django.urls import path
from .import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
   
    path('insertlocation',views.insertlocation,name='insertlocation'),
    path('insertjob',views.insertjob,name='insertjob'),
    path('insertmoves',views.insertmoves,name='insertmoves'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('team',views.team,name='team'),
    path('movies',views.movies,name='movies'),
    path('privasyofk',views.privasyofk,name='privasyofk'),
    path('delet',views.delet,name='delet'),
    path('mdelet',views.mdelet,name='mdelet'),
    path('danger',views.danger,name='danger'),
 
    
    
    
]