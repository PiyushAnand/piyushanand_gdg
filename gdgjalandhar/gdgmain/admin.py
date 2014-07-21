from django.contrib import admin
from models import menu,banner,social

class MenuAdmin(admin.ModelAdmin):
    fields = ['menu_title' , 'menu_subtitle' , 'href']
    list_display = ['menu_title' , 'menu_subtitle' , 'href']
admin.site.register(menu,MenuAdmin)

class BannerAdmin(admin.ModelAdmin):
    fields = ['banner1']
    list_display = ['banner1']
admin.site.register(banner,BannerAdmin)

class SocialAdmin(admin.ModelAdmin):
    fields = ['logo' , 'facebook' , 'google' , 'email' , 'social1']
    list_display = ['logo' , 'facebook' , 'google' , 'email' , 'social1']
admin.site.register(social,SocialAdmin)
# Register your models here.
