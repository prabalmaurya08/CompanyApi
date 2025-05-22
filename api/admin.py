from django.contrib import admin
from api.models import Company,Empolyee

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location')

class EmpolyeeAdmin(admin.ModelAdmin):
    list_display=('name','company_name')

admin.site.register(Company,CompanyAdmin)
admin.site.register(Empolyee,EmpolyeeAdmin)

# Register your models here.
