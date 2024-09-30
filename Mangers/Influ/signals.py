from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserInfo

""" This code snippet is a Django signal handler using the 
    @receiver decorator and post_save signal
""" 

"""
Notes:
Ensure that your UserInfo model (from .models import UserInfo) is properly defined with a user 
field, likely a OneToOneField to User, 
to maintain the relationship correctly.
Django signals are powerful tools for decoupling and handling events like model saves, 
allowing for modular and extensible application logic without directly coupling models together 
in code.
"""

@receiver(post_save, sender=User)
def user_receiver(sender, instance, created, **kwargs):
    user = instance


    if created:
        UserInfo.objects.create(user = user,)