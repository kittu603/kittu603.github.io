from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Job(models.Model):

    job_title = models.CharField(max_length=200,blank=False)
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200,blank=True)
    employer = models.CharField(max_length=200,blank=False,default="HP")
    skills = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.job_title


class Post(models.Model):
    pass








