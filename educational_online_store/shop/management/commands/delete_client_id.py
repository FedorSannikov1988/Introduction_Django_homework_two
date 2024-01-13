from shop.models import Client
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete сlient by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')
        client = \
            Client.objects.filter(pk=pk).first()
        if client:
            client.delete()
        self.stdout.write(f'{client}')
