from django.db import models

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

    # bio
    email = models.EmailField(max_length=255, null=True, blank=True)
    id_no = models.IntegerField(null=True, blank=True)
    category = models.CharField(
        max_length=255, choices=CATEGORY, null=True, blank=True)

    # sacraments
    baptised = models.BooleanField()
    holy_communion = models.BooleanField()
    confirmed = models.BooleanField()
    matrimonial = models.BooleanField()

    # # family and jumuiya
    # family = models.ForeignKey(
    #     'Family',
    #     on_delete=models.CASCADE,
    # )
    # jumuiya = models.ForeignKey(
    #     'Jumuiya',
    #     on_delete=models.CASCADE,
    # )

    # # groups
    # main_group = models.ForeignKey(
    #     'Group',
    #     on_delete=models.CASCADE,
    # )
    # other_groups = models.ForeignKey(
    #     'Group',
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.surname
