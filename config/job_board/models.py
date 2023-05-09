from django.db import models

class Wanted(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    url = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('company', 'position')

# Create your models here.

