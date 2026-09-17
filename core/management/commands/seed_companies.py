from django.core.management.base import BaseCommand
from core.models import Company


class Command(BaseCommand):
    help = "Seed default companies"

    def handle(self, *args, **kwargs):
        companies = [
            "Google",
            "Microsoft",
            "Amazon",
            "IBM",
            "Infosys",
            "TCS",
            "Wipro",
            "Accenture",
        ]

        for company in companies:
            Company.objects.get_or_create(name=company)

        self.stdout.write(
            self.style.SUCCESS("Companies added successfully!")
        )