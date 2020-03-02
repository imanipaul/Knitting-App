from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Needle, Note, Pattern, Yarn, Project


#Serializers define the API representation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class NeedleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needle
        fields = ('id', 'size', 'length', 'in_use', 'circular')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'content')

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = ('id', 'url', 'image')

class YarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yarn
        fields = ('id', 'weight', 'skeins')

class ProjectSerializer(serializers.ModelSerializer):
    pattern = PatternSerializer(read_only=True)
    yarn = YarnSerializer(many=True, read_only=True)
    note = NoteSerializer(read_only=True)


    class Meta:
        model = Project
        fields = ('id', 'name', 'row', 'repeat', 'pattern', 'yarn', 'note')
        extra_kwargs = {
            'pattern': {'required': False},
            'yarn': {'required': False},
            'note': {'required': False}
            }
