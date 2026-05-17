from django.shortcuts import render, redirect
from .models import Task

def home(request):

    if request.method == "POST":

        title = request.POST.get("title")

        description = request.POST.get("description")

        Task.objects.create(
            title=title,
            description=description
        )

        return redirect('/')

    tasks = Task.objects.all()

    context = {
        "title": "AWS Multi-Tier Task Manager",
        "tasks": tasks
    }

    return render(request, "index.html", context)