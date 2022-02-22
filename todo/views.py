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
    
class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

