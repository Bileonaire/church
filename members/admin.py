from django.contrib import admin

from .models import Member


class MemberModel(admin.ModelAdmin):
    list_display = (
        'surname',
        'full_name',
        'phone',
        'id_number',
        'get_groups',
        'profession',
    )
    list_filter = (
        'baptism',
        'eucharist',
        'confirmation',
        'matrimony',
        'groups'
    )

    list_display_links = ('surname', 'full_name', )
    search_fields = (
        'surname',
        'other_names',
        'full_name',
        'phone',
        'email',
        'id_number',
        'profession',
        'jumuiya',
        'family',
        'groups',
    )

    fieldsets = (
        ('NAMES', {
            'fields': ('surname', 'other_names', 'full_name')
        }),
        ('BIO', {
            'fields': ('email', 'phone', 'id_number', 'category', 'profession')
        }),
        ('SACRAMENTS', {
            'fields': ('baptism', 'eucharist', 'confirmation', 'matrimony')
        }),
        ('JUMUIYA AND FAMILY', {
            'fields': ('jumuiya', 'family')
        }),
        ('GROUPS', {
            'fields': ('groups', )
        }),
    )


admin.site.register(Member, MemberModel)
