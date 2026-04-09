from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from . import models
from educationproject.models import mstuser
from django.contrib.auth import logout
from django.http import HttpResponse
   

def sessioncheckadmin_middleware(get_response): 
 def middleware(request):
    if request.path=='/adminhome/' or request.path=='/adminhome/courselist/' or request.path=='/adminhome/courseentry/' or  request.path=='/adminhome/batchentry/'  or  request.path=='/adminhome/batchlist1/' or  request.path=='/adminhome/courselist/'or request.path=='/adminhome/editcourse/' or request.path=='/adminhome/studentlist/' :
      if "emailid" not in request.session:  
            response=redirect('/login/')
      else:
            response=get_response(request)
    else:
        response=get_response(request)
    return response
 return middleware  


# Create your views here.
def adminhome(request):
    #for fetch session-------------------------------------
    emailid=request.session.get("emailid")
    role=request.session.get("role")
    #------------------------------------------------------
    return render(request,'adminhome.html',
                  {"emailid":emailid,"role":role})

def courseentry(request):
    if request.method=="GET":
     return render(request,"courseentry.html",{"msg":""})
    else:
     coursename=request.POST.get("coursename")
     duration=request.POST.get("duration")
     fees=request.POST.get("fees")
     coursedetails=request.POST.get("coursedetails")
     #for file uploading .................................
     courseicon=request.FILES["courseicon"]
     fs=FileSystemStorage()
     courseimg=fs.save(courseicon.name,courseicon)  
     #.................................................... 
     #for save record in course table ---------------------
     obj=models.course(coursename=coursename,duration=duration,
                      fees=fees,coursedetails=coursedetails,
                       courseicon=courseicon )
     obj.save()
     #-----------------------------------------------------
     return render(request,"courseentry.html",{"msg":"Record Saved"}) 
    
def courselist(request):
   result=models.course.objects.all()
   return render(request,"courselist.html",{"result":result})

def studentlist(request):
   result=mstuser.objects.filter(role='student')
   return render(request,"studentlist.html",{"result":result})

def adminlogout(request):
   logout(request)
   return redirect("http://localhost:8000")

def batchentry(request):
   if request.method=="GET":
      return render(request,"batchentry.html",{"msg":""})
   else:
      batchtitle=request.POST.get("batchtitle")
      batchtime=request.POST.get("batchtime")
      startdate=request.POST.get("startdate")
      facultyname=request.POST.get("facultyname")
      batchstatus=1
      obj=models.batch(batchtitle=batchtitle,
                       batchtime=batchtime,
                       startdate=startdate,
                       facultyname=facultyname,
                       batchstatus=batchstatus)
      obj.save()
      return render(request,"batchentry.html",
                    {"msg":"Record Saved"})
   

def batchlist1(request):
   res=models.batch.objects.filter(batchstatus=1)
   return render(request,"batchlist1.html",{"res":res})

def editcourse(request):
   if request.method=="GET":
      #for fetch data from query string
      courseid=request.GET.get("courseid")
      print("course id -",courseid)
      res=models.course.objects.filter(courseid=courseid)
      return render(request,"editcourse.html",{"res":res})
   else:
      courseid=request.POST.get("courseid")
      coursename=request.POST.get("coursename")
      duration=request.POST.get("duration")
      fees=request.POST.get("fees")
      coursedetails=request.POST.get("coursedetails")
      res=models.course.objects.filter(courseid=courseid).update(duration=duration,fees=fees,coursedetails=coursedetails)
      return redirect("/adminhome/courselist/")
   
      
   




   

