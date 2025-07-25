from django.contrib import admin
from django.core.paginator import Paginator
from django.db import (
    connection,
    models
)
from django.utils.functional import cached_property



class BaseModelAdmin(admin.ModelAdmin):
    default_readonly_fields = ('created_at', 'uuid')
    ordering = ('-created_at',)
    search_fields = ('uuid',)
    foreign_key_fields = ()

    def get_readonly_fields(self, request, obj=None):
        # Get all foreign key field names in the model
        foreign_keys = [f.name for f in self.model._meta.get_fields() if isinstance(f, models.ForeignKey)]
        return tuple(foreign_keys) + ('uuid', 'created_at', 'updated_at')