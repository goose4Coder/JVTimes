from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help="Creates admin if none exist"

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            password=os.environ.get("SUPER_USER_PASSWORD","admin")
            admin = User.objects.create_superuser(username='SuperAdmin', password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print('Admin created succesfuly')
        else:
            print('Admin accounts can only be initialized if no Accounts exist')