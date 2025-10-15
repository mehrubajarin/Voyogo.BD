from django.contrib import admin
from .models import Destination, TourPackage

# Register your models here.

admin.site.register(Destination)


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "place", "price", "transport", "created_by", "created_at")
    list_filter = ("transport", "created_at", "created_by__user_type")
    search_fields = ("title", "place", "created_by__username", "created_by__first_name")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)

    fieldsets = (
        (
            "Package Information",
            {"fields": ("title", "image", "place", "time_slot", "price", "transport")},
        ),
        ("User Information", {"fields": ("created_by",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    def save_model(self, request, obj, form, change):
        if not change:  # Only set created_by when creating new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
