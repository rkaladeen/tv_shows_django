from django.shortcuts import render, redirect
from .models import Show
from time import strftime 

def index(request):
  return redirect("/shows/")

def shows(request):
  context = { "all_shows" : Show.objects.all() }
  return render(request, "tv_shows_app/all_shows.html", context)

  # add_show.html RENDER
def new(request):
  return render(request, "tv_shows_app/add_show.html")
  
  # add_show.html PROCESS
def add_show(request):
  # Add CREATE functions here
  Show.objects.create(
                      title=request.POST['title'], 
                      network=request.POST['network'], 
                      release=request.POST['rdate'], 
                      desc=request.POST['desc']
                      )

  last_show_added = Show.objects.last()
  sh_id = last_show_added.id
  return redirect(f"/shows/{sh_id}/") # Redirects to show_details.html

  # edit_show.html RENDER
def edit(request, sh_id):
  context = { "edit_detail" : Show.objects.get(id=sh_id) }
  return render(request, "tv_shows_app/edit_show.html", context)

  # edit_show.html PROCESS
def edit_show(request, sh_id):
  # Add UPDATE functions here
  show_to_edit = Show.objects.get(id=sh_id)

  show_to_edit.title = request.POST['title'] 
  show_to_edit.network = request.POST['network']
  show_to_edit.release = request.POST['rdate'] 
  show_to_edit.desc = request.POST['desc']
  

  show_to_edit.save()

  return redirect(f"/shows/{sh_id}")

def show(request, sh_id):
  context = { "show" : Show.objects.get(id=sh_id) }
  return render(request, "tv_shows_app/show_details.html", context)


def delete(request, sh_id):
  show_to_delete = Show.objects.get(id=sh_id)
  show_to_delete.delete()
  return redirect("/shows")
