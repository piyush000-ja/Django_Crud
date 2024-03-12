from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('course.urls')),
    path('',include('fees.urls')),
    path('appsession/',include('appsession.urls')),
    path('appClass/',include('appClass.urls'))
]