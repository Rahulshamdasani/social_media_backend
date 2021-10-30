from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
# from django.contrib.auth.models import User

# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=220, blank=True, default="firstname")
    last_name = models.CharField(max_length=220, blank=True, default="lastname")
    display_name = models.CharField(max_length=220, blank=True, default="displayname")
    locations = models.CharField(max_length=220, blank=True, default="locations")
    bio = models.TextField(max_length=1000,blank=True, default="bio")

# Creating profile for a user
def user_did_save(sender, instance, created, *args, **kwargs):
    Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save, sender=User)

