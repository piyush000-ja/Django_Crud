from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    # path('signup/',views.signup,name='signup'),
    # path('alldata/',views.alldata,name='alldata'),
    # path('edit/',views.editform,name='editform'),


    path('create/',views.create,name='create'),
    path('read/',views.read,name='read'),
    path('update/<int:id>/',views.edit,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('dtl/',views.dtl,name='dtl')



]
