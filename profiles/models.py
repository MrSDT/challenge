from django.contrib.auth.models import models

class UpdateInfo(models.Model):
    realname = models.CharField(max_length=100)
    age = models.CharField(max_length=1000)
    desc = models.TextField()