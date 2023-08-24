from django.shortcuts import render,redirect
from home.forms import TaskForm,TaskModel
# Create your views here.
def home(request):
    return render(request,'home.html')
def show_task(request):
    return render(request,'show_task.html')
def complete_task(request):
    return render(request,'complete_task.html')

def edit_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm()
    return render(request,'edit_task.html',{'form':form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form':form})

def show_task(request):
    task = TaskModel.objects.all()
    return render(request,'show_task.html',{'task':task})

def modify_task(request,id):
    obj = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = obj)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm(instance=obj)
    return render(request,'edit_task.html',{'form':form})

def delete_task(request,id):
    form = TaskModel.objects.get(pk = id).delete()
    return redirect('show_task')

def completed_task(request,id):
    
    form = TaskModel.objects.get(pk = id).delete()
    return redirect('completed_task')