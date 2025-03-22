from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError




"""
# User model with mentor-specific fields
class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Common fields for all users
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    # Mentor-specific fields (Optional at sign-up)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    # Roles
    is_mentor = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    # Explicit related_name for groups and permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='custom_user_groups', 
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='custom_user_permissions', 
        blank=True,
        help_text="Specific permissions for this user."
    )

    def save(self, *args, **kwargs):
        # Ensure that mentors must provide full_name, bio, skills, and photo before saving
        if self.is_mentor:
            if not self.full_name:
                raise ValidationError("Mentors must provide a full name.")
            if not self.bio or not self.photo or not self.skills:
                raise ValidationError("Mentors must have a bio, photo, and skills.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username"

"""