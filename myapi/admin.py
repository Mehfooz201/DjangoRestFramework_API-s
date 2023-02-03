from django.contrib import admin
from myapi.models import Company, Employee


# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position')
    list_filter = ('company',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)


