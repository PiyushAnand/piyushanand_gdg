from django.contrib import admin
from models import Img , About_us , About_img

class ImgAdmin(admin.ModelAdmin):
    fields = ["image"]
    list_display = ["image"]
admin.site.register(Img,ImgAdmin)

class About_us_Admin(admin.ModelAdmin):
    fields = ["about_gdg" , "about_gdj" , "about_team"]
    list_display = ["about_gdg" , "about_gdj" , "about_team"]
admin.site.register(About_us,About_us_Admin)

class About_img_Admin(admin.ModelAdmin):
    fields = ["img"]
    list_display = ["img"]
admin.site.register(About_img,About_img_Admin)


# Register your models here.
