from django.db import models


class Group(models.Model):
    # group details
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.full_name}'
