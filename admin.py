from django.contrib import admin
from .models import UserName

@admin.register(UserName)
class UserNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)