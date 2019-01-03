from django.contrib import admin

from .models import Member


class MemberModel(admin.ModelAdmin):
    list_display = (
        'surname',
        'other_names',
        'baptised',
        'holy_communion',
        'confirmed',
        'matrimonial'
    )
    list_filter = (
        'baptised',
        'holy_communion',
        'confirmed',
        'matrimonial'
    )

    list_display_links = ('surname', 'other_names')
    list_editable = (
        'baptised',
        'holy_communion',
        'confirmed',
        'matrimonial'
    )
    search_fields = ('surname', 'other_names', 'id_no', 'baptised',
                     'holy_communion', )


    fieldsets = (
        ('NAMES', {
            'fields': ('surname', 'other_names')
        }),
        ('BIO', {
            'fields': ('email', 'id_no', 'category')
        }),
        ('SACRAMENTS', {
            'fields': ('baptised', 'holy_communion', 'confirmed',
                       'matrimonial')
        })
    )

admin.site.register(Member, MemberModel)