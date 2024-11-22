from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'phone_number','role', 'is_staff')
    fieldsets = (
        ('Personal info', {'fields': ('username', 'phone_number', 'password', 'role', 'is_staff')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
