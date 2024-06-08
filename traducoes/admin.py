from django.contrib import admin
from . import models


class TraducoesAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'pt_br', 'en_gb')
    search_fields = ('tipo', )


admin.site.register(models.Traducoes, TraducoesAdmin)
