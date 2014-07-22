from django.contrib import admin
from models import event

class EventAdmin(admin.ModelAdmin):
    fields = ["img","img_logo","location","status","event_title","event_desc"]
    list_display = ["img","img_logo","location","status","event_title","event_desc"]
admin.site.register(event,EventAdmin)

# Register your models here.
