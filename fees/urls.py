from django.urls import path
from . import views

urlpatterns = [
    path('fees/',views.fees,name='fees'),
    path('record/',views.showRecord,name='showRecord'),
    path('deleterecord/<int:id>/',views.deleteRecord,name='deleteRecord'),
    path('editrecord/<int:id>/',views.editRecord,name='editRecord')
]
