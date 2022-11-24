from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import TaskSerializers, UserSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


class TaskViewset(viewsets.ModelViewSet):
    Permission_class =(IsAuthenticated)
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers
class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializers

class CreateuserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializers