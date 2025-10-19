from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("travel_agent", "Travel Agent"),
        ("tourist", "Tourist"),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default="tourist")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"


    def is_travel_agent(self):
        return self.user_type == "travel_agent"

    def is_tourist(self):
        return self.user_type == "tourist"
