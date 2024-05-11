from django.shortcuts import render, redirect
from .models import appTask
from .forms import TaskForm

# Create your views here.

def listTask(request):
    tasks = appTask.objects.all()
    return render(request, 'app/list_task.html', {'tasks': tasks})

def createTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/create_task.html', {'form': form})

def updateTask(request, pk):
    task = appTask.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'app/update_task.html', {'form': form})

def deleteTask(request, pk):
    task = appTask.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'app/delete_task.html', {'task': task})

