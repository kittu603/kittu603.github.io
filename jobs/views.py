from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Job,Visitor
from .forms import VisitorForm

# Create your views here.

 # Grabbing no of visitors using len

def about_me(request):
    return render(request,'jobs/about.html')

def index(request):
    total_visitors = len(Visitor.objects.all())
    return render(request,"jobs/index.html",{"total_visitors": total_visitors })

def show_jobs(request):
    jobs = Job.objects
    return render(request,"jobs/job_data.html",{"jobs_data":jobs})

def contact(request):
    
    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            visitor_name = form.cleaned_data['name']
            total_visitors = len(Visitor.objects.all())
            return render(request, "jobs/thanks.html", {"visitor": visitor_name,"total_visitors": total_visitors})
        else:
            print("invalid form data")    
    else:
        form = VisitorForm()

    return render(request,"jobs/contact.html",{"form":form})

def my_gallery(request):
    return render(request,"jobs/gallery.html")

def job_detail(request,job_id):
    job = get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/job_detail.html',{'job': job})

def post_contact(request):
    return render(request, 'jobs/thanks.html')








