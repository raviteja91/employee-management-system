from django.contrib import admin
from django.contrib import databrowse
from grappelli.actions import csv_export_selected
import fullhistory

from models import SampleModel

class SampleAdmin(fullhistory.admin.FullHistoryAdmin):

    # Options for admin
    list_display = ('name',
                    'description',
                    'processed',)

    list_filter = ('processed',)
    list_per_page = 20
    search_fields = ('name',
                     'description',)
    actions = ('mark_as_processed',
               'mark_as_not_processed',
               csv_export_selected,
              )


    def mark_as_processed(self, request, queryset):
        queryset.update(processed=True)

    def mark_as_not_processed(self, request, queryset):
        queryset.update(processed=False)


def register(model, modelAdmin):
    admin.site.register(model, modelAdmin)
    databrowse.site.register(model)
    fullhistory.register_model(model)

register(SampleModel, SampleAdmin)
