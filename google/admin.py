from django.contrib import admin
from import_export import resources
from .models import LocationHistory
# Register your models here.
class Location(resources.ModelResource):
    
    class Meta:
        model = LocationHistory