from django.db import models

class Comments(models.Model):
    name       = models.CharField(max_length = 50)
    contents   = models.TextField()
    created    = models.DateTimeField(auto_now_add = True)
    updated    = models.DateTimeField(auto_now = True)