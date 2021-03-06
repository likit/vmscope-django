import os
import random
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from wagtail.core.models import Page

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
        return '{}/{}{}'.format(self.artifact.group.name,
                   timezone.now().strftime('%Y%m%d_%H%M%S'), extension)

    image = models.ImageField(max_length=200,
                              upload_to=image_name)

    def image_dim(self):
        return '{}x{} pixels'.format(self.image.width, self.image.height)

    image_dim.short_description = 'Size'


    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<img src="%s" />' % escape(self.image.url))

    image_tag.short_description = 'Image'

    def image_url(self):
        return self.image.url

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

    def image_dim(self):
        return '{}x{} pixels'.format(self.image.width, self.image.height)

    image_dim.short_description = 'Size'

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe(u'<img src="%s" />' % escape(self.image.url))

    image_tag.short_description = 'Image'

    def image_url(self):
        return self.image.url

    def __str__(self):
        return '{}'.format(self.image.url)


class MicroscopeSection(models.Model):
    session = models.ForeignKey('main.Session', related_name='microscope_sections',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.name


class ParasiteComponent(models.Model):
    section = models.ForeignKey(MicroscopeSection, related_name='parasite_components',
                                on_delete=models.CASCADE)
    parasite = models.ForeignKey(Parasite, on_delete=models.CASCADE)
    stage = models.ForeignKey(ParasiteStage, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)

    def __str__(self):
        return 'Section ID={} ({}): {} of {}, {}'.format(self.section.pk,
                         self.section, self.number, self.parasite, self.stage)


class ArtifactComponent(models.Model):
    section = models.ForeignKey(MicroscopeSection, related_name='artifact_components',
                                on_delete=models.CASCADE)
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    oscillate = models.BooleanField(default=False)
    resizable = models.BooleanField(default=False)
    floating = models.BooleanField(default=False)

    def __str__(self):
        return 'Section ID={} ({}): {} of {}'.format(self.section.pk, self.section,
                                                     self.artifact, self.number)


class ParasitePage(models.Model):
    parasite = models.ForeignKey(Parasite, related_name='parasite_pages',
                                 on_delete=models.CASCADE)
    page = models.ForeignKey(Page, related_name='parasite_pages',
                             on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}, page slug={}'.format(self.parasite.genus, self.parasite.species, self.page.slug)


class MicroscopePlayRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    saved_at = models.DateTimeField(null=True)
    score = models.IntegerField(default=0)
    section = models.ForeignKey(MicroscopeSection, on_delete=models.CASCADE)
