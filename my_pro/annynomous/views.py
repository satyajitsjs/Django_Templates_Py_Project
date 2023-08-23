from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import user_master
# Create your views here.


# def index(request):
#     return HttpResponse("<h1> Welcom to sereee </h1>")

def register(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        ob = user_master.objects.create(name=name,email=email,mobile=mobile,password=password)
        ob.save()
        return render(request,'register.html',{ 'output' : 'Register Success' }) 
    return render(request,"register.html")

def index(request):
    return render(request,"index.html")


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            ob = user_master.objects.get(email=email,password=password)
            request.session['email'] = ob.email
            return render (request,'index.html',{ 'output':"valid" })
        except Exception as e:
            return render (request,'index.html' ,{ "output" : 'invalid'+str(e) })
    return render(request,"index.html")


def viewdata(request):
    if request.method == "POST":
        btn = request.POST['btn']
        if btn == "View":
            try:
                ob = user_master.objects.all()
                return render (request,"viewdata.html",{'users':ob})
            except Exception as e:
                ob = user_master.objects.all()
                return render(request,"viewdata.html",{"output":'invalid '+str(e)})
            

        if btn == "Edit":
            email = request.POST['email']
            try:
                ob = user_master.objects.filter(email=email)
                return render(request,"edit.html",{'users':ob})
            except Exception as e:
                return render(request,"viewdata.html",{'users':"invalid "+str(e)})

        
        if btn == "Delete":
            email = request.POST['email']
            try:
                ob = user_master.objects.filter(email=email).delete()
                ob = user_master.objects.all()
                return render (request,'viewdata.html' ,{'users':ob})
            except Exception as e:
                return render(request,"viewdata.html",{"users":"invalid "+str(e)})
            

    return render (request,'viewdata.html')


def update(request):
    if request.method == "POST":
        # btn = request.POST['btn']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        # if btn == "update":
        try:
            user_master.objects.filter(email=email).update(name=name,password=password,mobile=mobile)
            ob = user_master.objects.all()
            return render(request,"viewdata.html",{'users':ob})
        except Exception as e :
            return render(request,"viewdata.html",{'users':"invalid "+str(e)})

    return render(request,"viewdata.html")




def about(request):
    return render(request,"about.html")


from .models import contact_master,feedback_master
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        ob = contact_master.objects.create(name=name,email=email,mobile=mobile,message=message)
        ob.save();
        return render(request,'contact.html' , { 'output': ' Thank you We will contact you Soon' })
    return render(request,"contact.html")


def feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        ob = feedback_master.objects.create(name=name,email=email,mobile=mobile,message=message)
        ob.save();
        return render(request,'feedback.html' , { 'output': ' Thank you for your feedback ' })
    return render(request,"feedback.html")


def viewc(request):
    ob=contact_master.objects.all()
    return render(request,'viewcontact.html', {'contact' : ob} )

def viewf(request):
    ob=feedback_master.objects.all()
    return render(request,'viewfeedback.html', {'feedback' : ob} )


def gallery(request):
    return render(request,"gallery.html")