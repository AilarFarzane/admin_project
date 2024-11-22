from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'sender', 'text', 'is_approved')



admin.site.register(Message, MessageAdmin)
