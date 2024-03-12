from django.shortcuts import render,redirect ,HttpResponse
from .models import  Courses,Signup                 #reference from models.py se
from .forms import studentForm                      #reference forms py se




# Create your views here.

def home(request):
        # info = Courses.objects.all()
#         context = {                           #we can use multiple times variable like context
#              'info':info
#         }

#         # name = 'piyush kumar'
#         # city = 'delhi'
#         # email = 'piyush@gmail.com'
#         # context ={
#         #     'name':name,
#         #     'city':city,
#         #     'email':email      
        
        return render(request,'index.html')

# def login(request):
#     signup = studentForms()
#     return render(request,'login.html',{'form':signup})
#     # return HttpResponse('<h1>This is course page...<h1>')


# def signup(request):
#     if request.method == 'POST':
#          fm = RegistrationForm(request.POST)
#          if fm.is_valid():
#             firstName = fm.cleaned_data['firstname']            #['add from form data']forms.py
#             LastName = fm.cleaned_data['lastname']
#             email = fm.cleaned_data['email']
#             pwd = fm.cleaned_data['password']
#             cpwd = fm.cleaned_data['password1']
#             # print('firstname :',firstName)
#             # print('lastname :',LastName)
#             # print('email :',email)
#             # print('pwd :',pwd)
#             # print('cpwd :',cpwd)
#             data =  Signup(firstname=firstName,lastname=LastName,email=email,password=pwd,password1=cpwd)
#             data.save()
#             return redirect('/alldata')

#          else:
#             signupForm = RegistrationForm()


#     signupForm = RegistrationForm()
#     context = {
#          'signupForm':signupForm
#     }
#     return render(request,'signup.html',context)


# def alldata(request):
#     records = Signup.objects.all()
#     context={
#         'records':records
#     }
#     return render(request,'alldata.html',context)





def create(request):
    if request.method=='POST':
        fm = studentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm = studentForm()
        return render(request,'signup.html',{'signupForm':fm})
    


def read(request):
        data = Signup.objects.all()
        return render(request,'alldata.html',{'records':data})
    


#edit
def edit(request,id):
    dataget = Signup.objects.get(id=id)
    fm = studentForm(instance=dataget)
    if request.method == 'POST':
        fm = studentForm(request.POST,instance=dataget)
        if fm.is_valid():
            fm.save()
            return redirect('create')
    return render(request,'edit.html',{'editform':fm})


def delete(request,id):
     dataget = Signup.objects.get(id=id)
     dataget.delete()
     return redirect('read')



def login(request):
    if request.method == 'POST':
         email = request.POST['email']
         password = request.POST['password']
         userobj = Signup.objects.filter(email=email)
         print(userobj)
         if userobj:
             password =  Signup.objects.filter(password=password)
             if password:
                  return HttpResponse('dashboard')
             else:
                  return redirect('login')
            
         else:
              return redirect('login')
    else:
         pass
    return render(request,'login.html', )



# cookie set and get
def about(request):
    res = HttpResponse('<h1>cookie set</h1>')
    res.set_cookie('name','pooja',max_age=None)              #for set cookie
    val = request.COOKIES.get('name')                        # for get cookie
    print(val)
    context = {
         'cookie':val
    }
    if res:
        #  return res
         return render(request,'about.html',context)
    else:
         print('cookie not set')
    return render(request,'about.html')










def dtl(request):
     name = 'DEEPAK'
     city = 'delhi'
     email = 'deepak@gmail.com'
     message = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
     fees = ''
     context = {
          'name':name,
          'message':message,
          'city':city,
          'email':email,
          'fees' : fees
     }
     return render(request, 'course/dtl.html',context)