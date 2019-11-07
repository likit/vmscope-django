import os
from django.utils import timezone
from django.db import models


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


class Image(models.Model):
    parasite = models.ForeignKey(Parasite, related_name='images',
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, choices=(
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disabled', 'disabled')
    ), default='pending')
    upload_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    upload_by = models.ForeignKey('auth.User', related_name='images',
                                  on_delete=models.CASCADE)

    def image_name(self, filename):
        extension = os.path.splitext(filename)[-1]
        return 'photohunt/{}/{}/{}{}'.format(
                    self.parasite.genus,
                    self.parasite.species,
                    timezone.now().strftime('%Y%m%d_%H%M%S'),
                    extension)

    image = models.ImageField(max_length=200,
                              upload_to=image_name)

    def __str__(self):
        return '{}'.format(self.image.url)


class ImageTagSet(models.Model):
    image = models.ForeignKey(Image, related_name='tagsets',
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)


class ImageTag(models.Model):
    tagset = models.ForeignKey(ImageTagSet, related_name='tags',
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    x = models.FloatField(blank=False, null=False)
    y = models.FloatField(blank=False, null=False)