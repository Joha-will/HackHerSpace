from . import views
from django.urls import path

urlpatterns = [
    path("users/", views.ProfileList.as_view(), name="profile-list"),
]