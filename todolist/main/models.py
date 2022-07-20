from django.db import models

class Task(models.Model):
    task_title = models.CharField("Назва", max_length=50)
    task_desc = models.TextField("Опис Завдання")
    def __str__(self):
        return self.title
