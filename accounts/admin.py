from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User, UserProfile, Mentor



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'role',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Mentor)