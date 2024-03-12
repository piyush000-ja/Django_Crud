from django.shortcuts import render,redirect
from .models import Course

def fees(request):
    if request.method == 'POST':
        name = request.POST['nm']
        course = request.POST['course']
        duration = request.POST['duration']
        fees = request.POST['fees']
        # print('name :', name)
        # print('course :', course)
        # print('duration :', duration)
        # print('fees :', fees)
        data = Course(Name=name,Course=course,Duration=duration,Fees=fees)
        data.save()
        return redirect('/')
    
    else:
        pass
    return render(request,'fees/fees.html')


def showRecord(request):
    records = Course.objects.all()
    return render(request, 'fees/showRecord.html',{'records':records})


def deleteRecord(request,id):
    record = Course.objects.get(id=id)
    record.delete()
    return redirect('showRecord')

def editRecord(request,id):
    record = Course.objects.get(id=id)
    print(record)
    return render(request,'fees/edit.html',{'record':record})




