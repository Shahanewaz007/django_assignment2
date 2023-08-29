from django.shortcuts import render, redirect
from .models import ToDoModel
from .forms import ToDoForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'base.html')

def todo_store(request):
    if request.method == 'POST':
        todo = ToDoForm(request.POST)
        if todo.is_valid():
            todo.save()
            return redirect('show_todo')
    else:
        todo = ToDoForm()
    return render(request, 'todo_store.html', {'form':todo})


def show_todo(request):
    todo = ToDoModel.objects.all()
    return render(request, 'show_todo.html', {'data':todo})

def edit_todo(request, id):
    todo = ToDoModel.objects.get(pk = id)
    form = ToDoForm(instance=todo)
    if request.method == 'POST':
        form = ToDoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('show_todo')
    return render(request, 'todo_store.html', {'form':form})


def delete_todo(request, id):
    todo = ToDoModel.objects.get(pk = id).delete()
    return redirect('show_todo')

def complete_todo(request, id):
    todo1 = ToDoModel.objects.get(pk = id)
    todo1.is_complete = True
    todo1.save()
    return redirect('show_todo')

def complete_task_view(request):
    todo = ToDoModel.objects.all()
    return render(request, 'complete_todo.html', {'data':todo}) 

def complete_task_delete(request, id):
    todo = ToDoModel.objects.get(pk = id).delete()
    return redirect('complete_task_view')