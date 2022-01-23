from django.contrib import admin
from .models import Group, Task

admin.site.register(Group)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'task_group',
        'title',
        'due_date',
        'priority',
        'is_completed'
    ]
    list_filter = ('title', 'user', 'due_date', 'priority', 'is_completed', 'task_group')
    search_fields = ('title', 'content') 
    
admin.site.register(Task, TaskAdmin)
