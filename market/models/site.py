from django.db import models

from market.constants.constants import SITE_TYPE


class SiteModel(models.Model):
    id = models.UUIDField(primary_key=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    street_name = models.CharField(max_length=1000)
    village = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    district = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    location_coordinates = models.CharField(
        max_length=1000, blank=True, null=True
    )
    type = models.CharField(
        max_length=30,
        choices=SITE_TYPE,
        blank=True
    )
    price = models.FloatField(null=True, blank=True)
    availability = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner} has {self.type} at {self.village}"