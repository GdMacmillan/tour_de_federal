from django.contrib import admin

from .models import Restaraunt

class RestarauntAdmin(admin.ModelAdmin):
    ordering     = ('name', )
    list_display = ('name','formatted_address', )
    search_fields = ['name']

admin.site.register(Restaraunt, RestarauntAdmin)
