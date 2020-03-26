from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stuid = models.CharField(max_length=7, blank=True)
    study_program = models.CharField(max_length=500, blank=True)
    institution = models.CharField(max_length=500, blank=True)
    email = models.EmailField(max_length=256, blank=True)

    @property
    def is_empty(self):
        return any([self.email, self.stuid, self.study_program, self.institution])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
