from django.core.management.base import BaseCommand
from django.utils import timezone
from base.models import CustomUser

class Command(BaseCommand):
    help = 'Check and delete accounts marked for deletion.'

    def handle(self, *args, **options):
        now = timezone.now()
        users_to_delete = CustomUser.objects.filter(deletion_date__lte=now)
        for user in users_to_delete:
            if user.is_staff:
                print("Estudiante")
            else:
                print("Profesor")
            print(user.deletion_date)

            user.delete()
            self.stdout.write(self.style.SUCCESS(f"Deleted user: {user.username}"))
        print("do you wish to reactivate this account?")
            