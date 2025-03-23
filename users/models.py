from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError



class UserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, email, password=None):
        if not username:
            raise ValidationError('Username is required.')
        if not email:
            raise ValidationError('Email is required.')
    
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, first_name, last_name, email, password):
        user = self.create_user(

            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser):

    MENTOR = 1
    STUDENT= 2

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.PositiveSmallIntegerField(choices=(
        (MENTOR, 'Mentor'),
        (STUDENT, 'Student'),
    ), default=STUDENT)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    def get_role(self):
        if self.role == 1:
            user_role = 'Mentor'
        elif self.role == 2:
            user_role = 'Student'
        return user_role


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