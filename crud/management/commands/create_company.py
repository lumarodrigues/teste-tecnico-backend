from django.core.management.base import BaseCommand
from crud.models import Company
import os


class Command(BaseCommand):
    help = 'Creates a Company with a name and API token from environment variables'

    def handle(self, *args, **kwargs):
        company_name = os.getenv('COMPANY_NAME')
        api_token = os.getenv('COMPANY_API_TOKEN')

        if not company_name or not api_token:
            self.stdout.write(self.style.ERROR('COMPANY_NAME or COMPANY_API_TOKEN not provided in environment variables.'))
            return

        existing_company = Company.objects.filter(api_token=api_token).first()
        if existing_company:
            self.stdout.write(self.style.WARNING(f'A company with the provided API Token already exists: {existing_company.name}'))
            return

        company = Company.objects.create(
            name=company_name,
            api_token=api_token
        )

        self.stdout.write(self.style.SUCCESS(f'Company "{company.name}" with API Token "{api_token}" created successfully.'))
