from django.contrib import admin

# Register your models here.
from .models import MessageCategory
from .models import Message

admin.site.register(MessageCategory)
admin.site.register(Message)
