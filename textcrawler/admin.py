from django.contrib import admin

# Registration of models in the admin panel
from django.contrib import admin
from .models import CrawlLog

@admin.register(CrawlLog)
class CrawlLogAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'status', 'error_message')

