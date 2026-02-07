from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

@login_required
def todo_list(request):
    todos = Todo.objects.all()
    
    return render(request, 'todoApp/todo_list.html' , {'todos': todos})

@login_required
def pending_todos(request):
    todos = Todo.objects.filter(is_completed=False)
    return render(request, 'todoApp/pending_todos.html' , {'todos': todos})

@login_required
def completed_todos(request):
    todos = Todo.objects.filter(is_completed = True)
    return render(request, 'todoApp/completed_todos.html' , {'todos': todos})
    

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todoApp/todo_form.html', {'form': form})

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
        
    return render(request, 'todoApp/todo_form.html', {'form': form})
    
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    
    return render(request, 'todoApp/todo_delete.html', {'todo': todo})



