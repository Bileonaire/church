from django.db import models


class Jumuiya(models.Model):
    # jumuiya details
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
