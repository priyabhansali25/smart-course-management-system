from django.shortcuts import redirect, render

# to connect models to view
from . import models
from adminapp.models import course,batch

#for display image
from django.conf import settings
media_url=settings.MEDIA_URL

#for email sending
from . import emailAPI
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        # print(emailid,pwd)
        res = models.mstuser.objects.filter(emailid=emailid,pwd = pwd) #for search record in table

        if(len(res)>0):
            role = res[0].role
            #print(role)
            #for create session---------------------------------------
            request.session["emailid"]=emailid
            request.session["role"]=role
            
            #-----------------------------------------------------------

            if(role=="admin"):
                print("Welcome admin")
                return redirect("/adminhome/")
            elif(role=="student"):
                print("welcome student")
                return redirect("/studenthome/")
            # else:
            #     print("welcome student")

            # print("role -",role)
            # name = res[0].name
            # print("name - ",name)
            print("login success")
        else:
            print("Invalid emailid or pwd")
        return render(request,"login.html")


def register(request):
    if(request.method=="GET"):
        return render(request,"register.html")
    else:
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        city = request.POST.get("city")
        emailid = request.POST.get("emailid")
        pwd = request.POST.get("pwd")
        role = "student"
        obj = models.mstuser(name=name,gender=gender,mobile=mobile,address=address,city=city,emailid=emailid,pwd=pwd,role=role)
        obj.save()
        #to send verification email to registered email id
        emailAPI.sendMail(emailid, pwd)
        #----------------------------------------------------------------------
        return render(request,"register.html")
    
def emailtesting(request):
    from . import emailAPItesting
    email = "ritishatiwari31@gmail.com"
    password = "ritisha31_12"
    res = emailAPItesting.sendMail(email, password)
    return HttpResponse(res)
    

def courselist3(request):
    result=course.objects.all()
    return render(request,"courselist3.html",
                  {"result":result,'media_url':media_url})

def batchlist3(request):
    result=batch.objects.filter(batchstatus=1)
    return render (request,"batchlist3.html",
                   {"result":result})




