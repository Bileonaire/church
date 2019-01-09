from django.contrib import admin

from .models import Group


class GroupModel(admin.ModelAdmin):
    list_display = ('name', 'full_name')
    list_display_links = ('name', 'full_name')
    search_fields = ('name', 'full_name')

    fieldsets = (('GROUP DETAILS', {'fields': ('name', 'full_name')}), )


admin.site.register(Group, GroupModel)
