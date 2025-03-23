from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

#adding dynamic data from the databse
from .models import User_database

def index(request):
    u_data=User_database.objects.all()
    print(u_data)
    return render(request,'index.html',{'database':u_data})

def details_to_base(request):
    return redirect(reverse('Notes:base_page'))



#post_detail
def detail(request,slug):
    #for static data
    """
    posts=[
        {'id':1,'title':'aaaa'},
        {'id':2,'title':'bbbb'},
        {'id':3,'title':'cccc'},
        {'id':4,'title':'dddd'},
        {'id':5,'title':'eeee'},
    ]
    next((i for i in posts if i['id']==id))
    """
    #for dynamic data
    user_data=User_database.objects.get(slug=slug)
    return render(request,'details.html',{'user_dat':user_data})
    


# Create your views here.
def Http_response(request):
    name="Broskies"
    return render(request,'welcome_page.html',{"name":name})



def login_response(request):
    #return HttpResponse("Hello, world!")
    return render(request, 'login.html')

def signup_response(request):
    return render(request,'signup.html')




# ? Redirection
def old_url(request):
    #return redirect("new_url")
    return redirect(reverse('Notes:redirected_page'))
    
def new_url_page(request):
    return HttpResponse("this is an New URL")

