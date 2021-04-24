from django.db import models

# Create your models here.
class crud(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=False)
    email = models.CharField(max_length=80,null=True)
    phone = models.IntegerField(null=True)
    branch = models.CharField(max_length=30,default="",null=True)

    def __str__(self):
        return self.name
