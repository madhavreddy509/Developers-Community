from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Project
from . forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from .utils import searchProjects, paginateProjects
def projects (request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    content ={'projects':projects,'search_query': search_query,'custom_range': custom_range}
    return render(request,'projects/projects.html',content)

def project (request,pk):
    projectobj = Project.objects.get(id=pk)
    tags=projectobj.tags.all()
    return render(request,'projects/project-single.html',{'project':projectobj,'tags':tags})
@login_required(login_url='login')
def createproject (request):
    profile =request.user.profile
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()

            return redirect('projects')
    content ={'form':form}
    return render (request,'projects/project_form.html',content)
@login_required(login_url='login')
def updateproject (request,pk):
    profile =request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    content ={'form':form}
    return render (request,'projects/project_form.html',content)
@login_required(login_url='login')
def deleteproject (request,pk):
    profile =request.user.profile
    project=profile.project_set.get(id=pk)
    if request.method=="POST":
        project.delete()
        return redirect('projects')
    content ={'object':project}
    return render (request,'projects/delete-template.html',content)