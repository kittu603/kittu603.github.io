from django.db import models
from phone_field import PhoneField
# Create your models here.

class Job(models.Model):

    job_title = models.CharField(max_length=200,blank=False)
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200,blank=True)
    employer = models.CharField(max_length=200,blank=False,default="HP")
    skills = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.job_title


class Visitor(models.Model):
    name = models.CharField(max_length=200,blank=False)
    email = models.EmailField(max_length=200)
    phone_no = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.name} @ {self.email}"










