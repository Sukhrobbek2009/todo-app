from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    
    return render(request, 'todoApp/todo_list.html' , {'todos': todos})

def pending_todos(request):
    todos = todo.objects.filter(is_completed=False)
    response = ""

    for todo in todos:
        response += f"{todos.title}\n{todo.priority}\n{todo.due_date}"
    
    return HttpResponse(response)

def completed_todos(request):
    todos = Todo.objects.filter(is_completed = True)
    response = ""

    for todo in todos:
        response += f"{todo.title}\n"

    return HttpResponse(response)
    

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todoApp/todo_form.html', {'form': form})
