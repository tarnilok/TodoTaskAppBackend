from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Task, Group
from .serializers import GroupSerializer, TaskSerializer

class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

