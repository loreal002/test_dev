from django.contrib import admin
from personal.models.project import Project
from personal.models.module import Module

# Register your models here.
class ProjctAdmin(admin.ModelAdmin):
    list_display = ["name","describe","status","create_time"]
    search_fields = ["name"]
    list_filter = ["status"]

class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name","describe","create_time","project"]
    search_fields = ["name"]
    list_filter = ["project"]


admin.site.register(Project,ProjctAdmin)
admin.site.register(Module,ModuleAdmin)
