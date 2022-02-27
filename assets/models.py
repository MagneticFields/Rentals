from django.db import models


class FuelTypes(models.TextChoices):
    # Fuel Types
    GASOLINE = 'Gasoline'
    DIESEL = 'Diesel',
    ELECTRIC = 'Electric'
    HYBRID = 'Hybrid'
    OTHER = 'Other'


class VehicleTypes(models.TextChoices):
    # Vehicle Types
    A_CLASS_CAR = 'A Class Car'
    B_CLASS_CAR = 'B Class Car'
    C_CLASS_CAR = 'C Class Car'
    S_CLASS_CAR = 'S Class Car'
    SUV = 'SUV'
    VAN = 'Van'
    TRUCK = 'Truck'
    MOTORCYCLE = 'Motorcycle'
    OTHER = 'Other'


class BaseAsset(models.Model):
    """
    Base model for all assets
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=255, blank=True)
    model_year = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    fuel_type = models.CharField(max_length=10, choices=FuelTypes.choices, default=FuelTypes.GASOLINE)

    class Meta:
        abstract = True


class Vehicles(BaseAsset):
    fuel_type = models.CharField(max_length=10, choices=FuelTypes.choices, default=FuelTypes.GASOLINE)
    vehicle_type = models.CharField(max_length=20, choices=VehicleTypes.choices, default=VehicleTypes.C_CLASS_CAR)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

