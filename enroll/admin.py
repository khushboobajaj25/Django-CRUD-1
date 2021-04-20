from django.contrib import admin
from .models import *


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ('id', 'name', 'message')
