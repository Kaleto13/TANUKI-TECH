from celery import shared_task
from django.utils import timezone
from base.models import CustomUser

@shared_task
def check_deletion():
    now = timezone.now()
    users_to_delete = CustomUser.objects.filter(deletion_date__lte=now)
    for user in users_to_delete:
        user.delete()
