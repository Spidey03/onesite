from django.urls import path

from market import views

urlpatterns = [
    path('get_user/<str:id>', views.get_user, name="Get User"),
    path('get_site_details/<str:site_id>', views.get_site_details, name="Get Site Details"),
    path('get_sites', views.get_sites_bulk, name="Get List of Sites"),
    path('add_site', views.add_site_details, name="Add Site Details")
]