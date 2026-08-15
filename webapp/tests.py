from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

    def test_task_creation(self):
        task = Task.objects.create(
            user=self.user,
            title="Learn Django",
            description="Build a production application",
            priority=Task.Priority.HIGH,
        )

        self.assertEqual(task.title, "Learn Django")
        self.assertEqual(task.priority, Task.Priority.HIGH)
        self.assertFalse(task.completed)

    def test_task_string(self):
        task = Task.objects.create(
            user=self.user,
            title="Learn Docker",
        )

        self.assertEqual(str(task), "Learn Docker")


class AuthenticationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

    def test_login(self):
        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "TestPassword123!",
            },
        )

        self.assertRedirects(
            response,
            reverse("task_list"),
        )


class TaskViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

    def test_task_list(self):
        response = self.client.get(
            reverse("task_list")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_task_create(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "title": "Learn Kubernetes",
                "description": "Deploy Django",
                "priority": "HIGH",
            },
        )

        self.assertRedirects(
            response,
            reverse("task_list"),
        )

        self.assertTrue(
            Task.objects.filter(
                user=self.user,
                title="Learn Kubernetes",
            ).exists()
        )

    def test_health_check(self):
        response = self.client.get(
            reverse("health_check")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertEqual(
            response.json()["status"],
            "healthy",
        )

    def test_unauthenticated_user_redirect(self):
        self.client.logout()

        response = self.client.get(
            reverse("task_list")
        )

        self.assertEqual(
            response.status_code,
            302,
        )