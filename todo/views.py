from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Task, Group
from .serializers import GroupSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['title', 'due_date', 'priority', 'user']
    filterset_fields = ['task_group']
    
    # http://127.0.0.1:8000/tasks/?task_group=24&ordering=-due_date
    
    def get(self, request, *args, **kwargs):
        group_id = Group.objects.all()
        print(group_id)
        # print(self)
        # groupName = Group.objects.filter()
        # task = Task.objects.all()
        # print(task)
        # serializer = GroupSerializer(groupName, many=True)
        # return Response(serializer.data)
    
class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

