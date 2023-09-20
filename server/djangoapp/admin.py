from django.contrib import admin
from .models import CarModel, carMake





# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here



class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to display for adding new CarModel objects

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

admin.site.register(CarModel)
admin.site.register(carMake)