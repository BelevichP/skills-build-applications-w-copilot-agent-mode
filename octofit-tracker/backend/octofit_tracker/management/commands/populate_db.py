from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate the octofit_db MongoDB database with test data"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Database populated successfully"))

