from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'service.html')    

def aboutus(request):
    return render(request,'about.html')        

def contactus(request):
    return render(request,'contact.html')            

def careers(request):
    return render(request,'careers.html')    

def quotes(request):
    return render(request,'getaquote.html')        

def servicedetail(request):
    return render(request,'servicedetails.html')    

def jobdetails(request):
    return render(request,'apply.html')    

def gallery(request):
    return render(request,'gallery.html')    