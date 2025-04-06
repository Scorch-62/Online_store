from django.core.management.base import BaseCommand
from django.core.management import  call_command


class Command(BaseCommand):
    help= 'Load test data from Fixture'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'catalog.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
