from django.urls import path, include
from rest_framework import routers
from .views import GroupView, TaskView, UserView

router = routers.DefaultRouter()
router.register('groups', GroupView)
router.register('tasks', TaskView)

urlpatterns = [
    path('', include(router.urls)),
    path('usernames/', UserView.as_view())
]