from django.shortcuts import render,get_object_or_404, redirect

from .models import Task
from .forms import TaskForm


# Create your views here.

def home(request):
    objecto = Task.objects.all()

    if request.method == 'GET':
        form = TaskForm()
        contexto = {'form':form, 'tarefas':objecto}
        return render(request, 'home.html', contexto)

    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()
            return redirect('home')
        print(form)
        print(request.POST)



def deleteall(request):
    objecto = Task.objects.all()
    objecto.delete()
    return redirect('home')


def delete(request, id):
    objecto = get_object_or_404(Task, id=id)
    print(f' o objecto tem o id {objecto}')
    objecto.delete()
    return redirect('home')






def update(request, id):
    obj = get_object_or_404(Task, id=id)
    form = TaskForm(instance=obj)
    contexto = {'form':form}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return  redirect('home')
    return render(request, 'update.html', contexto)

def about(request):
    return render(request, 'about.html')


            







