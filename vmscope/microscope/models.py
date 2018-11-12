import os
from django.db import models
from django.utils import timezone

# Create your models here.
class ArtifactType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Artifact(models.Model):
    group = models.ForeignKey('ArtifactType', related_name='artifacts',
                              on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.group, self.desc)


class ArtifactImage(models.Model):
    artifact = models.ForeignKey(Artifact, related_name='images',
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, choices=(
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disabled', 'disabled')
    ), default='pending')
    upload_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    upload_by = models.ForeignKey('auth.User', related_name='artifact_images',
                                  on_delete=models.CASCADE)

    def image_name(self, filename):
        extension = os.path.splitext(filename)[-1]
        return '{}/{}'.format(self.artifact.group.name,
                   timezone.now().strftime('%Y%m%d_%H%M%S'), extension)

    image = models.ImageField(max_length=200,
                              upload_to=image_name)

    def __str__(self):
        return '{}'.format(self.image.url)



class Parasite(models.Model):
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    kind = models.CharField(max_length=200, choices=(
        ('nematode', 'nematode'),
        ('cestode', 'cestode'),
        ('trematode', 'trematode'),
        ('protozoa', 'protozoa')
    ))

    def __str__(self):
        return '{} {}'.format(self.genus, self.species)


class ParasiteStage(models.Model):
    stage = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.stage)


class ParasiteImage(models.Model):
    parasite = models.ForeignKey('Parasite', related_name='images',
                                 on_delete=models.CASCADE)
    stage = models.ForeignKey('ParasiteStage', related_name='images',
                              on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, choices=(
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disabled', 'disabled')
    ), default='pending')

    upload_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    upload_by = models.ForeignKey('auth.User', related_name='parasite_images',
                                  on_delete=models.CASCADE)

    def image_name(self, filename):
        extension = os.path.splitext(filename)[-1]
        return '{}/{}/{}{}'.format(self.parasite.genus, self.stage,
                    timezone.now().strftime('%Y%m%d_%H%M%S'), extension)

    image = models.ImageField(max_length=200,
                              upload_to=image_name)

    def __str__(self):
        return '{}'.format(self.image.url)


