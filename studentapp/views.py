from django.shortcuts import render,redirect
from adminapp.models import course,batch
import datetime
from . import models
from educationproject.models import mstuser
from django.http import HttpResponse

def sessioncheckstudent_middleware(get_response):
 def middleware(request):
    if request.path=='/studenthome/' or request.path=='/studenthome/admission/' or request.path=='/studenthome/batchlist2/' or request.path=='/studenthome/courselist2/' or request.path=='/studenthome/success/' or request.path=='/studenthome/updateprofile/':
      if "emailid" not in request.session:  
            response=redirect('/login/')
      else:
            response=get_response(request)
    else:
        response=get_response(request)
    return response
 return middleware 

# Create your views here.
def studenthome(request):
    #for fetch session-------------------------------------
    emailid=request.session.get("emailid")
    role=request.session.get("role")
    #------------------------------------------------------
    return render(request,"studenthome.html",
        {"emailid":emailid,"role":role})


def courselist2(request):
    result=course.objects.all()
    return render(request,"courselist2.html",{"result":result})

def batchlist2(request):
    result=batch.objects.filter(batchstatus=1)
    return render (request,"batchlist2.html",
                   {"result":result})

def admission(request):
    if request.method=="GET":
        batchid=request.GET.get("batchid")
        #print("batchid -",batchid)
        res=batch.object.filter(batchid=batchid)
        return render(request,"admission.html",{"res":res})
    else:
        batchid=request.POST.get("batchid")
        emailid=request.session.get("emailid")
        x=datetime.datetime.now()
        admissiondate=x.strftime("%Y-%m-%d")
        print("admission date-",admissiondate)
        res=models.admission(batchid=batchid,emailid=emailid,
                             admissiondate=admissiondate,)
        res.save()
        return redirect("/studenthome/success/")
    

def success(request):
    return render(request,"success.html")

def updateprofile(request):
 if request.method=="GET":
   emailid=request.session.get("emailid")
   res=mstuser.objects.filter(emailid=emailid)
   return render(request,"updateprofile.html",{"res":res})
 else:
   name=request.POST.get("name")
   mobile=request.POST.get("mobile")
   address=request.POST.get("address")
   pwd=request.POST.get("pwd")
   emailid=request.POST.get("emailid")
   obj=mstuser.objects.filter(emailid=emailid).update(name=name,mobile=mobile,address=address,pwd=pwd)
  
   return redirect("/studenthome/")  
 
