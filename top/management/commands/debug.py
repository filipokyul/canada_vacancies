from django.core.management.base import BaseCommand, CommandError
from top.models import Cities

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cities = ['Toronto', 'Calgary', 'Edmonton', 'Vancouver', 'Winnipeg',
                  'Ottawa', 'Saskatoon', 'Halifax', 'Hamilton', 'Victoria']
        for city in cities:
            b = Cities(name=city)
            b.save()


