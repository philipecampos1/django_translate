from django.contrib import admin
from . import models
# Register your models here.


class TiposAdmin(admin.ModelAdmin):
    list_display = ('tipo', )
    search_fields = ('tipo', )


admin.site.register(models.Tipos, TiposAdmin)
