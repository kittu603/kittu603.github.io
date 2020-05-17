from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Job

# Create your views here.

def about_me(request):
    return render(request,'jobs/about.html')

def index(request):
    return render(request,"jobs/index.html")

def show_jobs(request):
    jobs = Job.objects
    return render(request,"jobs/job_data.html",{"jobs_data":jobs})

def contact(request):
    return render(request,"jobs/contact.html")

def my_gallery(request):
    return render(request,"jobs/gallery.html")

def job_detail(request,job_id):
    job = get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/job_detail.html',{'job': job})






