from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name=models.CharField(max_length=100, unique=True)
    order = models.CharField(max_length=15, default='due_date/asc')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Group'
        ordering = ['id']

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    task_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    URGENCY = [
        ('high priority', '3'),
        ('medium priority', '2'),
        ('low priority', '1'),
        ('no priority', '0'),
    ]
    priority = models.CharField(max_length=20, choices=URGENCY, default='0')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        ordering = ['priority']