from typing import Any
from My_app.models import category_table
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="inserting the category data into the table"
    
    def handle(self, *args, **options):

        #this line delets the existing data in the table
        category_table.objects.all().delete()

        category_names=['manager','admin','employee','client']
        
        for category in category_names:
            category_table.objects.create(c_name=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting categories .")) 
        