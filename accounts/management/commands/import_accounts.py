import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from accounts.models import Account
import os
from django.conf import settings

from fund_transfer.settings import BASE_DIR

class Command(BaseCommand):
    help = 'Import accounts from a CSV file'

    def handle(self, *args, **kwargs):
        # Correctly resolve the path to the accounts.csv file located in the project root
        print(settings.BASE_DIR)
        csv_file_path = os.path.join(BASE_DIR, 'accounts.csv')

        # Ensure the path is absolute and points to the file
        csv_file_path = os.path.abspath(csv_file_path)

        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Account.objects.create(
                        name=row['Name'],
                        balance=row['Balance']
                    )

            self.stdout.write(self.style.SUCCESS('Successfully imported accounts'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {csv_file_path}'))
