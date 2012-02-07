from django.db import models

class foo(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    
