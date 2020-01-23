from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import Show

# Create your views here.

def shows(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, "shows.html", context)


def new_show(request):
    return render(request, "add_show.html")

def show_detail(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id)
    }
    return render(request, "show_detail.html", context)

def create(request):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        show_title = request.POST["title"]
        show_network = request.POST["network"]
        show_release_date = request.POST["selected_date"]
        show_desc = request.POST["desc"]
        
        new_show = Show.objects.create(title = show_title, network = show_network, release_date = show_release_date, desc = show_desc)
        return redirect(f"/shows/{new_show.id}")


def edit(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id)
    }
    return render(request, "edit_show.html", context)

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    else:
        update = Show.objects.get(id = show_id)
        update.title = request.POST["title"]
        update.network = request.POST["network"]
        update.release_date = request.POST["selected_date"]
        update.desc = request.POST["desc"]
        update.save()
        messages.success(request, "Show successfully updated")

        return redirect(f"/shows/{show_id}")

def destroy(request, show_id):
    delete = Show.objects.get(id=show_id)
    delete.delete()
    return redirect("/shows")