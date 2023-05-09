from django.db import models

# Create your models here.

class Wanted(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    url = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('company', 'position')

class Jobkorea(models.Model):
    company = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    url = models.TextField()
    exp = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('company', 'position')
        
class Saramin(models.Model):
    company = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    url = models.TextField()
    exp = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('company', 'position')

