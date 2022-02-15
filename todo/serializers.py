from rest_framework import serializers
from .models import Task, Group
from django.contrib.auth.models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
    
        
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    task_group = serializers.StringRelatedField()
    task_group_id = serializers.IntegerField()
    class Meta:
        model = Task
        fields = ('id', 'user', 'user_id', 'task_group', 'task_group_id', 'title', 'description', 'created_date', 'due_date', 'priority', 'is_completed')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
