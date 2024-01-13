from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from shop.models import Client, for_phone_number_validation


class Command(BaseCommand):
    help = "Create one fake client"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name fake client')
        parser.add_argument('email', type=str, help='Email fake client')
        parser.add_argument('phone_number', type=str, help='Phone number fake client')
        parser.add_argument('address', type=str, help='Address fake client')

    def handle(self, *args, **kwargs):

        name = kwargs.get('name')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')
        address = kwargs.get('address')

        try:
            for_phone_number_validation(phone_number)
        except ValidationError as error:
            self.stderr.write(str(error))
            return

        one_client = \
            Client(name=name,
                   email=email,
                   phone_number=phone_number,
                   address=address)

        self.stdout.write(str(one_client))

        one_client.save()