from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    filter_option = request.GET.get('filter', 'all')

    if filter_option == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_option == 'not_completed':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')

    return render(request, 'todo/task_list.html', {'tasks': tasks})


    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})
from django.shortcuts import get_object_or_404

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')
def delete_all_tasks(request):
    Task.objects.all().delete()
    return redirect('/')
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        task.title = new_title
        task.save()
        return redirect('/')
    
    return render(request, 'todo/edit_task.html', {'task': task})



