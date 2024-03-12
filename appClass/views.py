from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class myView(View):
    def get(self,request):
        # return HttpResponse('<h1>hii i am class based viwq </h1?')
        return render(request, 'appclass/app.html')
    

class ContactView(TemplateView):
    template_name = 'appclass/contact.html'

