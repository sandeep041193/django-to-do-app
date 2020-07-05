from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    task = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'items': task, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    tasky = Task.objects.get(id=pk)
    form = TaskForm(instance=tasky)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasky)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'formy': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}

    return render(request, 'tasks/delete.html', context)
