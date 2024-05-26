from django.contrib import admin
from .models import *
# Register your models here.


class UpdateApiDateTimeAdmin(admin.ModelAdmin):
    readonly_fields = ["api_update_time"]

admin.site.register(Currency)
admin.site.register(UpdateApiDateTime, UpdateApiDateTimeAdmin)