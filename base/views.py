from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home.html")

def addStudent(request):
    if request.method=="POST":
        sid = request.POST["sid"]
        obj = Student.objects.filter(sid=sid)
        if len(obj)>0:
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Student Already exist')
        else:
            name = request.POST["name"]
            branch = request.POST["branch"]
            semester = request.POST["semester"]
            Student.objects.create(sid=sid,name=name,branch=branch,semester=semester)
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Student Details Added Successfully')
    return render(request,"addStudent.html")

def listStudent(request):
    obj = Student.objects.all()
    return render(request,'viewStudent.html',{'obj':obj})

def updateStudent(request,sid):
    if request.method=="POST":
        myid=request.POST["sid"]
        obj = Student.objects.filter(sid=myid)
        if len(obj)==0:
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,"Student with entered sid doesn't exist")
            return redirect('/')
        name = request.POST["name"]
        branch = request.POST["branch"]
        semester = request.POST["semester"]    
        Student.objects.filter(sid=myid).update(name=name,branch=branch,semester=semester)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,"Student details Updated Successfully")
        return redirect('/')
    else:
        obj = Student.objects.filter(sid=sid)
        if len(obj)==0:
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,"Student with entered sid doesn't exist")
            return redirect('/')
        else:
            return render(request,"addStudent.html",{'obj':obj[0],'updated':True})
def deleteStudent(request,sid):
    Student.objects.filter(sid=sid).delete()
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,"Student Details Deleted")
    return redirect('/')
    