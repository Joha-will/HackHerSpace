from django.urls import path
from .views import ProfileList

urlpatterns = [
    path("users/", ProfileList.as_view(), name="profile-list"),
]