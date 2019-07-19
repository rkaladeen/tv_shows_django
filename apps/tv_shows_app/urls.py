from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('shows/', views.shows), # RENDER
  path('shows/new/', views.new), # RENDER
  path('shows/new/add-show/', views.add_show), # REDIRECT
  path('shows/<int:sh_id>/edit/update/', views.edit_show), # REDIRECT
  path('shows/<int:sh_id>/edit/', views.edit), # RENDER
  path('shows/<int:sh_id>/', views.show), # RENDER
  path('shows/<int:sh_id>/delete/', views.delete), # REDIRECT
]