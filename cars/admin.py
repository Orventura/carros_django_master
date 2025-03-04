from django.contrib import admin
from cars.models import Car, Brand

class Caradmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo')
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, Caradmin)
admin.site.register(Brand, BrandAdmin)
