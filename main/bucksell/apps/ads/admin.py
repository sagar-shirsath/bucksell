from django.contrib import admin
from ads.models import Ad
class AdAdmin(admin.ModelAdmin):
    list_display= ['title']
admin.site.register(Ad,AdAdmin)



