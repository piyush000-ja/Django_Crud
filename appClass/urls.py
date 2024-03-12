from django.urls import path
from .import views
from django.views.generic import TemplateView


urlpatterns = [
    path('cl/',views.myView.as_view(),name='cl'),
    path('about/',TemplateView.as_view(template_name= 'appclass/about.html')),
    path('contact/',views.ContactView.as_view(),name='contact')
]