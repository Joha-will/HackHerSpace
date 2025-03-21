from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    is_mentor = models.BooleanField(default=False)  # Differentiate between mentor & mentee

    # Add unique related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Unique related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Unique related_name
        blank=True,
    )

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    experience_level = models.CharField(
        choices=[("Junior", "Junior"), ("Mid", "Mid"), ("Senior", "Senior")], max_length=10
    )
    tech_stack = models.CharField(max_length=255, blank=True)
    mentorship_focus = models.CharField(max_length=255, blank=True)
    availability = models.CharField(max_length=50, blank=True)
    contact_preference = models.CharField(
        choices=[("Email", "Email"), ("Discord", "Discord"), ("LinkedIn", "LinkedIn")],
        max_length=20,
        blank=True,
    )
    certificate = models.FileField(upload_to="certificates/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
