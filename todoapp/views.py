from django.shortcuts import render, HttpResponse, redirect
from todoapp.models import Task
# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)

        instance = Task(taskTitle=title, taskDesc=desc)
        instance.save()
    return render(request, 'home.html')

def tasks(request):
    alltask = Task.objects.all()
    context = {'tasks': alltask}
    return render(request, 'tasks.html', context)

def delete_data(request, id):
    if request.method == "POST":
        dele = Task.objects.get(pk=id)
        dele.delete()
        return redirect('/tasks')