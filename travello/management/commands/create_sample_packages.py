from django.core.management.base import BaseCommand
from travello.models import TourPackage
from accounts.models import CustomUser


class Command(BaseCommand):
    help = "Create sample tour packages for testing"

    def handle(self, *args, **options):
        # Get or create a travel agent user
        travel_agent, created = CustomUser.objects.get_or_create(
            username="travel_agent",
            defaults={
                "first_name": "John",
                "last_name": "TravelAgent",
                "email": "travel_agent@example.com",
                "user_type": "travel_agent",
                "is_staff": True,
            },
        )
        if created:
            travel_agent.set_password("travel123")
            travel_agent.save()
            self.stdout.write("Created travel agent user")

        # Create sample packages
        packages_data = [
            {
                "title": "Bali Paradise Adventure",
                "place": "Bali, Indonesia",
                "time_slot": "7 Days 6 Nights",
                "price": 1299.99,
                "transport": "plane",
            },
            {
                "title": "European City Explorer",
                "place": "Paris, France",
                "time_slot": "5 Days 4 Nights",
                "price": 899.99,
                "transport": "plane",
            },
            {
                "title": "Mountain Trekking Experience",
                "place": "Swiss Alps",
                "time_slot": "4 Days 3 Nights",
                "price": 699.99,
                "transport": "train",
            },
            {
                "title": "Coastal Road Trip",
                "place": "California Coast",
                "time_slot": "6 Days 5 Nights",
                "price": 799.99,
                "transport": "bus",
            },
            {
                "title": "Tokyo Urban Adventure",
                "place": "Tokyo, Japan",
                "time_slot": "8 Days 7 Nights",
                "price": 1499.99,
                "transport": "plane",
            },
        ]

        for package_data in packages_data:
            package, created = TourPackage.objects.get_or_create(
                title=package_data["title"],
                defaults={
                    "place": package_data["place"],
                    "time_slot": package_data["time_slot"],
                    "price": package_data["price"],
                    "transport": package_data["transport"],
                    "created_by": travel_agent,
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created package: {package.title}"))
            else:
                self.stdout.write(f"Package already exists: {package.title}")

        self.stdout.write(self.style.SUCCESS("Sample tour packages created successfully!"))
        self.stdout.write("You can now test the tour package functionality.")
