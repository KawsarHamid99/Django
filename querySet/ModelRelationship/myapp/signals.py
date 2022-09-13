from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

## signals.py >> apps.py >> __init__.py

@receiver(post_delete,sender=Page)
def delete_related_user(sender,instance,**kwargs):
    print("Page_post_Delete")
    instance.user.delete()