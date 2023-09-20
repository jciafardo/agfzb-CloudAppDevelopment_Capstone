from django.db import models
from django.utils.timezone import now


# Create your models here.

class carMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    def __str__(self):
         return self.name

class CarModel(models.Model):
    carMake = models.ForeignKey(carMake, on_delete=models.CASCADE)
    dealerId = models.IntegerField()
    name = models.CharField(max_length=100)
    Type = models.CharField(max_length=100, choices=(
            ("Car", "Car"),
            ("SUV", "SUV"),
            ("Sedan", "Sedan"),
            ("Pickup", "Pickup"),
            
        )
    )
    year = models.DateField()

    def __str__(self):
        return self.name

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
