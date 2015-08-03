# -*- coding: utf-8 -*-
# Register your models here.
from django.contrib import admin
from .models import LocationHistory


class LocationHisAdmin(admin.ModelAdmin):
    list_display = ('conta', 'latitude', 'longitude', 'origem',  'turno', 'modificador', )


admin.site.register(LocationHistory, LocationHisAdmin)