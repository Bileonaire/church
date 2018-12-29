from django.db import models

from jumuiyas.models import Jumuiya


class Family(models.Model):
    # family details
    surname = models.CharField(max_length=255)
    jumuiya = models.ForeignKey(Jumuiya, on_delete=models.CASCADE)

    # contact person
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "families"

    def __str__(self):
        return self.surname
