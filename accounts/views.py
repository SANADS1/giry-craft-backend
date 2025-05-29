from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

# accounts/views.py
from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Welcome to GiriCraft API!"})
