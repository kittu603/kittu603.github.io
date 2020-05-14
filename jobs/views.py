from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

# Create your views here.

def about_me(request):
    return HttpResponse("This is abt me")

def index(request):
    return render(request,"jobs/index.html")

def show_jobs(request):
    jobs = Job.objects
    return render(request,"jobs/job_data.html",{"jobs_data":jobs})


