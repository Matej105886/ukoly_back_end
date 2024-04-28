from django.db import models

class Goal(models.Model):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=256)
    complete = models.BooleanField(default=False)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="tasks")
    def __str__(self):
        return self.title
