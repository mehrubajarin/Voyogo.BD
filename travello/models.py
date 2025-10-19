from django.db import models
from django.conf import settings

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
    )
    package = models.ForeignKey("TourPackage", on_delete=models.CASCADE, related_name="purchases")
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bought {self.package.title} on {self.purchased_at.strftime('%Y-%m-%d')}"


class TourPackage(models.Model):
    TRANSPORT_CHOICES = [
        ("bus", "Bus"),
        ("train", "Train"),
        ("plane", "Plane"),
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="tour_packages/", blank=True, null=True)
    place = models.CharField(max_length=200)
    time_slot = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transport = models.CharField(max_length=100, choices=TRANSPORT_CHOICES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.place}"
