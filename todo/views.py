from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import SignUpForm


@login_required
def task_list(request):
    filter_param = request.GET.get('filter')
    search_query = request.GET.get('search')

    tasks = Task.objects.filter(user=request.user)

    if filter_param == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_param == 'pending':
        tasks = tasks.filter(completed=False)

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date') or None
        priority = request.POST.get('priority', 'M')  # Default to Medium

        if title:
            Task.objects.create(title=title, due_date=due_date, priority=priority, user=request.user)
            return redirect('/')

    return render(request, 'todo/task_list.html', {
        'tasks': tasks,
        'filter': filter_param,
        'search': search_query
    })


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('/')



@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    return redirect('/')



@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.due_date = request.POST.get('due_date') or None
        task.priority = request.POST.get('priority', 'M')
        task.save()
        return redirect('/')

    return render(request, 'todo/edit_task.html', {'task': task})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'todo/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/login/')
