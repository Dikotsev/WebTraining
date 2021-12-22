from django.contrib import admin

# Register your models here.
from WebTraining.properties.models import Properties


@admin.register(Properties)
class PropertyAdmin(admin.ModelAdmin):
    pass