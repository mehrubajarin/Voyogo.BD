from django.core.management.base import BaseCommand
from accounts.models import CustomUser

class Command(BaseCommand):
    help = 'Create sample users for testing'

    def handle(self, *args, **options):
        # Create a Travel Agent
        travel_agent, created = CustomUser.objects.get_or_create(
            username='travel_agent',
            defaults={
                'first_name': 'John',
                'last_name': 'TravelAgent',
                'email': 'travel_agent@example.com',
                'user_type': 'travel_agent',
                'phone_number': '+1234567890',
                'address': '123 Travel Street, Tourism City',
                'is_staff': True,
            }
        )
        if created:
            travel_agent.set_password('travel123')
            travel_agent.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully created Travel Agent user')
            )
        else:
            self.stdout.write('Travel Agent user already exists')

        # Create a Tourist
        tourist, created = CustomUser.objects.get_or_create(
            username='tourist',
            defaults={
                'first_name': 'Jane',
                'last_name': 'Tourist',
                'email': 'tourist@example.com',
                'user_type': 'tourist',
                'phone_number': '+0987654321',
                'address': '456 Tourist Avenue, Vacation Town',
            }
        )
        if created:
            tourist.set_password('tourist123')
            tourist.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully created Tourist user')
            )
        else:
            self.stdout.write('Tourist user already exists')

        # Create an Admin (if not superuser)
        admin_user, created = CustomUser.objects.get_or_create(
            username='admin_user',
            defaults={
                'first_name': 'Admin',
                'last_name': 'User',
                'email': 'admin_user@example.com',
                'user_type': 'admin',
                'phone_number': '+1122334455',
                'address': '789 Admin Boulevard, Management City',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully created Admin user')
            )
        else:
            self.stdout.write('Admin user already exists')

        self.stdout.write(
            self.style.SUCCESS('Sample users created successfully!')
        )
        self.stdout.write('Login credentials:')
        self.stdout.write('Travel Agent: username=travel_agent, password=travel123')
        self.stdout.write('Tourist: username=tourist, password=tourist123')
        self.stdout.write('Admin: username=admin_user, password=admin123') 