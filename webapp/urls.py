from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "register/",
        views.register_view,
        name="register",
    ),

    path(
        "login/",
        views.login_view,
        name="login",
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout",
    ),

    path(
        "tasks/",
        views.task_list,
        name="task_list",
    ),

    path(
        "tasks/create/",
        views.task_create,
        name="task_create",
    ),

    path(
        "tasks/<int:task_id>/update/",
        views.task_update,
        name="task_update",
    ),

    path(
        "tasks/<int:task_id>/toggle/",
        views.task_toggle,
        name="task_toggle",
    ),

    path(
        "tasks/<int:task_id>/delete/",
        views.task_delete,
        name="task_delete",
    ),

    path(
        "health/",
        views.health_check,
        name="health_check",
    ),
]