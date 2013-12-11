from django.contrib import admin

# Register your models here.
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('name','header', 'create_date','update_date')
    ordering = ['name']
    search_fields = ['header', 'body_text']
    

admin.site.register(Page, PageAdmin)