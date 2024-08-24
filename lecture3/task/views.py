from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="new_task")
    # priority = forms.IntegerField(label = "priority", min_value = 1, max_value = 10)

def index(request):
    if "task" not in request.session:
        request.session["task"]=[]
    return render(request,"task/index.html",{
        "task":request.session["task"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            added_task = form.cleaned_data["task"]
            request.session["task"] += [added_task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"task/add.html"),{
                "form": form
            }
    return render(request,"task/add.html",{
        "form": NewTaskForm()
    })