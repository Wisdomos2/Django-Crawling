from django.db import models
from django.conf import settings

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=12, null=False)
    password = models.CharField(max_length=20, null=False)
    profile_Img = models.CharField(max_length=256, blank=True)
    access_Token = models.CharField(max_length=256, blank=True)
    refresh_Token = models.CharField(max_length=256, blank=True)
    regDate = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        db_table = "Account"
