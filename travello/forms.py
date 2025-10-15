from django import forms
from .models import TourPackage


class TourPackageForm(forms.ModelForm):
    class Meta:
        model = TourPackage
        fields = ["title", "image", "place", "time_slot", "price", "transport"]
        # Make image optional
        required = ["title", "place", "time_slot", "price", "transport"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Package Title"}
            ),
            "place": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Destination Place"}
            ),
            "time_slot": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g., 3 Days 2 Nights"}
            ),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Price"}),
            "transport": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control-file"}),
        }
