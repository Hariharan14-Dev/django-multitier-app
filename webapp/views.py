from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, TaskForm
from .models import Task


def home(request):
    return render(request, "webapp/home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("task_list")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Account created successfully.",
            )

            return redirect("task_list")
    else:
        form = RegisterForm()

    return render(
        request,
        "webapp/register.html",
        {"form": form},
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("task_list")

    if request.method == "POST":
        form = AuthenticationForm(
            request,
            data=request.POST,
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(
                request,
                "Login successful.",
            )

            return redirect("task_list")

        messages.error(
            request,
            "Invalid username or password.",
        )
    else:
        form = AuthenticationForm()

    return render(
        request,
        "webapp/login.html",
        {"form": form},
    )


@login_required
def logout_view(request):
    logout(request)

    messages.success(
        request,
        "You have been logged out.",
    )

    return redirect("home")


@login_required
def task_list(request):
    tasks = Task.objects.filter(
        user=request.user
    )

    return render(
        request,
        "webapp/task_list.html",
        {"tasks": tasks},
    )


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            messages.success(
                request,
                "Task created successfully.",
            )

            return redirect("task_list")
    else:
        form = TaskForm()

    return render(
        request,
        "webapp/task_form.html",
        {
            "form": form,
            "title": "Create Task",
            "button_text": "Create Task",
        },
    )


@login_required
def task_update(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user,
    )

    if request.method == "POST":
        form = TaskForm(
            request.POST,
            instance=task,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Task updated successfully.",
            )

            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "webapp/task_form.html",
        {
            "form": form,
            "title": "Update Task",
            "button_text": "Update Task",
        },
    )


@login_required
def task_toggle(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user,
    )

    if request.method == "POST":
        task.completed = not task.completed
        task.save(
            update_fields=[
                "completed",
                "updated_at",
            ]
        )

    return redirect("task_list")


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user,
    )

    if request.method == "POST":
        task.delete()

        messages.success(
            request,
            "Task deleted successfully.",
        )

        return redirect("task_list")

    return render(
        request,
        "webapp/task_confirm_delete.html",
        {"task": task},
    )


def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return JsonResponse(
            {
                "status": "healthy",
                "database": "connected",
            },
            status=200,
        )

    except Exception:
        return JsonResponse(
            {
                "status": "unhealthy",
                "database": "disconnected",
            },
            status=503,
        )