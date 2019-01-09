from django.db import models

from jumuiyas.models import Jumuiya
from families.models import Family
from groups.models import Group

CATEGORY = (
    ('MEN', 'MEN'),
    ('WOMEN', 'WOMEN'),
    ('YOUTH', 'YOUTH'),
    ('CHILDREN', 'CHILDREN')
)


class Member(models.Model):

    # names
    surname = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)

    # bio
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    id_number = models.CharField(max_length=255, unique=True, null=True, blank=True)  # noqa E501
    category = models.CharField(max_length=255, choices=CATEGORY, null=True, blank=True)  # noqa E501
    profession = models.CharField(max_length=255, null=True, blank=True)

    # sacraments
    baptism = models.BooleanField(default=False)
    eucharist = models.BooleanField(default=False)
    confirmation = models.BooleanField(default=False)
    matrimony = models.BooleanField(default=False)

    # jumuiya and family
    jumuiya = models.ForeignKey(Jumuiya, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    # groups
    groups = models.ManyToManyField(Group, blank=True)

    # the underscore is for differentiating it with the groups column
    def groups_(self):
        return "\n".join([group.name for group in self.groups.all()])

    def __str__(self):
        return f'{self.full_name} - {self.id_number}'
