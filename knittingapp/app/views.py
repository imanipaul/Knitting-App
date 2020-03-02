from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from django.contrib.auth.models import User
from .serializer import UserSerializer, NoteSerializer, PatternSerializer, YarnSerializer, ProjectSerializer
from .models import Yarn, Note, Pattern, Project, Needle
from rest_framework import filters

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class YarnViewSet(viewsets.ModelViewSet):
    """
    List all yarns, or create a new yarn
    """
    queryset = Yarn.objects.all()
    serializer_class = YarnSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class NoteViewSet(viewsets.ModelViewSet):
    """
    List all notes, or create a new yarn
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class PatternViewSet(viewsets.ModelViewSet):
    """
    List all patterns, or create a new yarn
    """
    queryset = Pattern.objects.all()
    serializer_class = PatternSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class ProjectViewSet(viewsets.ModelViewSet):
    """
    List all projects, or create a new yarn
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class NeedleViewSet(viewsets.ModelViewSet):
    """
    List all needles, or create a new yarn
    """
    queryset = Needle.objects.all()
    serializer_class = NeedleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'


