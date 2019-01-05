from django.contrib import admin

from .models import Group


class GroupModel(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )

    fieldsets = (('GROUP DETAILS', {'fields': ('name', )}), )


admin.site.register(Group, GroupModel)
