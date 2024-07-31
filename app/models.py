from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# User fields: first_name, last_name, email, username, password

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Sport(models.Model):
    name = models.CharField(max_length=128)


class Facility(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    id_sport = models.ForeignKey(Sport, on_delete=models.DO_NOTHING)


class Event(models.Model):
    id_organizer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    id_facility = models.ForeignKey(Facility, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField()
    estimated_time = models.IntegerField(choices=((30, "30"), (45, "45"), (60, "60"), (75, "75"), (90, "90"),
                                                  (105, "105"), (120, "120"), (135, "135"), (150, "150")))
    max_participants = models.IntegerField()
    description = models.TextField()


class Participation(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    id_event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=128)