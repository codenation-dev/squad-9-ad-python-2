from django.contrib import admin

from comission.models import ComissionPlan


class ComissionPlanAdmin(admin.ModelAdmin):
    # Show collumns for table model ComissionPlan
    list_display = ['lower_percentage', 'upper_percentage', 'min_value']
    search_fields = ['lower_percentage', 'upper_percentage', 'min_value']
    list_filter = ['lower_percentage', 'upper_percentage', 'min_value']


# Register your models here.
admin.site.register(ComissionPlan, ComissionPlanAdmin)
