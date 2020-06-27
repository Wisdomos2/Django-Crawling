from django.db import models

# Create your models here.


class loaCrawling(models.Model):
    title = models.CharField(max_length=16, null= False)
    cristal = models.IntegerField()
    reg_Date = models.DateTimeField(auto_created=True, auto_now=True)
