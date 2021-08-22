from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
            ('done','done'),
            ('doing','doing'),
            ('todo','todo')
            )
    name = models.CharField('Name', max_length=500, blank=False)
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']

