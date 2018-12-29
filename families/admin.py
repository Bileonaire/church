from django.contrib import admin

from .models import Family


class FamilyModel(admin.ModelAdmin):
    list_display = ('surname', 'jumuiya', 'full_name', )
    list_display_links = ('surname', 'full_name')
    search_fields = ('surname', 'jumuiya', 'full_name', 'id_number', 'phone_number')  # noqa E501

    fieldsets = (
        ('FAMILY DETAILS', {'fields': ('surname', 'jumuiya', )}),
        ('CONTACT PERSON', {'fields': ('full_name', 'id_number', 'phone_number',)}),  # noqa E501
    )


admin.site.register(Family, FamilyModel)
