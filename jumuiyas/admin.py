from django.contrib import admin

from .models import Jumuiya


class JumuiyaModel(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )

    fieldsets = (('JUMIYA DETAILS', {'fields': ('name',)}),)


admin.site.register(Jumuiya, JumuiyaModel)
