from django.contrib import admin
from models import location,contact,Info_Form

class InfoAdmin(admin.ModelAdmin):
    fields = ["name","contact","email","message"]
    list_display = ["name","contact","email","message"]
admin.site.register(Info_Form,InfoAdmin)

class LocationAdmin(admin.ModelAdmin):
    fields = ["map","address"]
    list_display = ["map","address"]
admin.site.register(location,LocationAdmin)

class contactAdmin(admin.ModelAdmin):
    fields=["social","address","email"]
    list_display = ["social","address","email"]
admin.site.register(contact,contactAdmin)

# Register your models here.
