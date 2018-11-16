from django.db import models
from django.utils import timezone


class Discipline(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Program(models.Model):
    discipline = models.ForeignKey(Discipline, related_name='programs',
                                   on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    target = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=(
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disabled', 'disabled')
    ), default='pending')

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    program = models.ForeignKey(Program, related_name='sessions',
                                on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=(
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disabled', 'disabled')
    ), default='pending')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    upload_by = models.ForeignKey('auth.User', related_name='sessions',
                                  on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Session, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


