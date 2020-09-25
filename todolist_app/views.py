from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import tasklist
from todolist_app.form import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
        if request.method=="POST":
                form=taskform(request.POST or None)
                if form.is_valid():
                       instance=form.save(commit=False)
                       instance.manager=request.user
                       instance.save()
                messages.success(request,('New Task added!'))       
                return redirect("todolist")  
        else:             
                all_tasks=tasklist.objects.filter(manager=request.user)
                paginator=Paginator(all_tasks,3)
                page=request.GET.get("pg")
                all_tasks=paginator.get_page(page)


                return render(request,'todolist.html',{'all_tasks':all_tasks})

@login_required                
def delete_task(request,task_id):
      task=tasklist.objects.get(pk=task_id)  
      if task.manager==request.user:        
        
        task.delete( )
      else: 
        messages.error(request,('You Are Not Allowed'))       

      return redirect("todolist")   


@login_required
def edit_task(request,task_id):
         task=tasklist.objects.get(pk=task_id)
         if request.method=="POST":
                
                form=taskform(request.POST or None,instance=task)
                if form.is_valid():
                       form.save()
                messages.success(request,('Task Edited!'))       
                return redirect("todolist")  
         else:             
                task_obj=tasklist.objects.get(pk=task_id)
                return render(request,'edit.html',{'task_obj':task_obj})
@login_required
def about(request):
        context={'about_us':'welcome to about us page'}
        return render(request,'about.html',context)
@login_required        
def contact(request):
        context={'contact_us':'welcome to contact us'}
        return render(request,'contact.html',context)  
@login_required                      
def complete_task(request,task_id):  
  if task.manager==request.user:     
        task=tasklist.objects.get(pk=task_id)
        task.done=True
        task.save()
  else: 
         messages.error(request,('You Are Not Allowed'))         
  return redirect("todolist")
@login_required        
def pending_task(request,task_id):
      task=tasklist.objects.get(pk=task_id)  
      if task.manager==request.user:           
        
        task.done=False
        task.save()
      else: 
        messages.error(request,('You Are Not Allowed'))    
      return redirect("todolist")    
def index(request):
        context={"index_text":"welcome to my home page"}            
        return render(request,'index.html',context)