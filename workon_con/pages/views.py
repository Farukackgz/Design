from django.shortcuts import render ,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from . forms import ContactForm
from . models import Proje




def call(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'call.html', {'form': form})

def index(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    
    projects=Proje.objects.all()

    context = {
        
        'form' : form ,
        'projects' : projects
    }
    return render(request, 'index.html' ,context )
    


def about(request):
    return render(request,'about.html')



