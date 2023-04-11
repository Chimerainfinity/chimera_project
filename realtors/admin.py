from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','is_mvp','hire_date')
    list_editable = ('is_mvp',)
    list_display_links = ('name',)
    search_fields = ('name',)



admin.site.register(Realtor,RealtorAdmin)
