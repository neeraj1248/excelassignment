from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Excl
# admin.site.register(Excl)
@admin.register(Excl)
class ExclAdmin(ImportExportModelAdmin):
    list_display = ('instructionid','case_ref_no','client_name','candidate_name','address','stay_period')
