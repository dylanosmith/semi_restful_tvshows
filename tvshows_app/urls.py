from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create),
    path('shows/<show_id>', views.show_detail),
    path('shows/<show_id>/edit', views.edit),
    path('shows/<show_id>/update', views.update),
    path('shows/<show_id>/destroy', views.destroy),
]