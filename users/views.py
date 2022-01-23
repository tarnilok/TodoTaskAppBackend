from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.response import Response

class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"User successfully created."
        })
