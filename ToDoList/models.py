from django.db import models

# Create your models here.
class todoList (models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    ACTION_CHOICES = [
        ("D", "Done"),
        ("UN", "Active"),
    ]
    action = models.CharField(choices=ACTION_CHOICES, max_length=2)
