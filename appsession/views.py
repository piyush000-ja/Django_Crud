from django.shortcuts import render,HttpResponse

# Create your views here.

#set session
def setsession(request):
    request.session['Name'] = 'ajay kumar'
    request.session['city'] = 'delhi'
    request.session['age'] = 32
    return HttpResponse ('<h1>session set </h1>')

 
#  get session
def getsession(request):
    item = request.session['Name']
    # keys = request.session.keys()                          #get key() method
    # print('keys :',keys)

    value = request.session.items()                          #get values of key method
    print('values', value)

    context = {
        'name':item
    }
    return render(request,'getsession.html',context)


#delete session
def deletesession(request):
    request.session.flush()
    return HttpResponse('<h1>Session deleted</h1>')