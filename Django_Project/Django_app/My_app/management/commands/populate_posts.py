from typing import Any
from My_app.models import User_database, category_table
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help="inserting the data into the table"
    
    def handle(self, *args, **options):
        #this line delets the existing data in the table
        User_database.objects.all().delete()
        
        #inserting the data into the table
        usernames = [
            "john_doe",
            "jane_smith",
            "bob_johnson",
            "alice_williams",
            "mike_davis",
            "emily_chen",
            "david_lee",
            "sarah_taylor",
            "kevin_white",
            "olivia_martin"
        ]
        emails=[
            "john_doe@example.com",
            "jane_smith@gmail.com",
            "bob_johnson@yahoo.com",
            "alice_williams@hotmail.com",
            "mike_davis@aol.com",
            "emily_chen@outlook.com",
            "david_lee@protonmail.com",
            "sarah_taylor@icloud.com",
            "kevin_white@zoho.com",
            "olivia_martin@yandex.com"
        ]
        passwords = [
            "P@ssw0rd123",
            "Giraffe#LemonTree88",
            "Tr0ub4d3!K1ng",
            "PineapplePizzaLover22",
            "SunnyDay123!",
            "BaseballFan42!",
            "ILoveDogs!",
            "CoffeeLover88",
            "Bookworm2000",
            "MusicIsLife123"
        ]
        img_urls=[
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
        ]
        
        categories=category_table.objects.all()

        for username,email,passw,img_url in zip(usernames,emails,passwords,img_urls):
            category=random.choice(categories)
            User_database.objects.create(username=username,email=email,password=passw,img_url=img_url,category_id=category)
     
        self.stdout.write(self.style.SUCCESS("Completed inserting .")) 
        