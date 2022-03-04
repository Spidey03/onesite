from django.urls import path

from market import views

urlpatterns = [
    path('get_user/<str:id>', views.get_user, name="Get User")
]