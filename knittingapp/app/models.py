from django.db import models

# Create your models here.

class Yarn(models.Model): #one to one with project
    weight = models.CharField(max_length=100)
    skeins = models.IntegerField()

class Needle(models.Model): #one to one with project (project has one needle, needle belongs to one project)
    size = models.IntegerField()
    length = models.IntegerField()
    in_use = models.BooleanField(default=False)
    circular = models.BooleanField(default=False)

class Pattern(models.Model): #one to many with project (project has one pattern, but a pattern can have many projects)
    url = models.URLField()
    image = models.FileField(upload_to='uploads/', blank=True)

class Note(models.Model):
    content = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length = 200)
    row = models.IntegerField()
    repeat = models.IntegerField()
    pattern = models.ForeignKey('Pattern', on_delete=models.CASCADE, blank=True, null=True)
    yarn = models.OneToOneField('Yarn', on_delete=models.CASCADE, blank=True, null=True)
    note = models.OneToOneField('Note', on_delete=models.CASCADE, blank=True, null=True)
