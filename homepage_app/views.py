from django.shortcuts import render
from .forms import ContactForm
from .models import Skills
# Create your views here.

def index(request):

    skills_list = Skills.objects.all()
    if len(skills_list)%2==0:
        half = int(len(skills_list)/2)
    else:
        half = int(len(skills_list)/2)+1

    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form=ContactForm()
        return render(request, 'index.html', context={'form':form, 'skills1': skills_list[:half], 'skills2': skills_list[half:]})


def skills_page_view(request):
    return render(request, 'skills.html')

def projects_view(request):
    return render(request, 'projects.html')
