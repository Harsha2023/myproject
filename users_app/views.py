from django.shortcuts import render,redirect
from .forms import customerregister_form
from django.contrib import messages

def register(request):
    if request.method=="POST":
        register_form=customerregister_form(request.POST)
        if  register_form.is_valid():
            register_form.save()
            messages.success(request,("New user created,login to get started"))
            return redirect("register")
    else:
         register_form=customerregister_form()        
    return   render(request,'register.html',{"register_form":register_form})
