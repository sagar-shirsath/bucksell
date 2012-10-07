from django.contrib import admin
from universities.models import University
class UniversityAdmin(admin.ModelAdmin):
    exclude = ('latitude','longitude')
    list_display= ['name','city','zip_code']

admin.site.register(University,UniversityAdmin)