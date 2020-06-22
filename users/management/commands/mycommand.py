from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Ai nevoie de ajutor?"

    def add_arguments(self, parser):
        parser.add_argument(
           'first_name',
            type=str,
            help='This is the first name argument'
        )

        parser.add_argument(
            'last_name',
            type=str,
            help='This is the last name argument'
        )

        parser.add_argument(
            'email',
            type=str,
            help='This is the email argument'
        )
        parser.add_argument(
            '--age',
            type=int,
            default=30,
            help='This is the age optional argument'
        )

    def handle(self, *args, **options):
        first_name = options['first_name']
        last_name = options['last_name']
        email = options['email']
        age = options['age']

        print('This is my custom command', first_name)
        print('This is my custom command', last_name)
        print('This is my custom command', email)
        print('This is my custom command', age)


print("Hello world! " * 7)

