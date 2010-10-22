from django.contrib import admin
from django.contrib import databrowse
from grappelli.actions import csv_export_selected
import fullhistory

from models import Unit, Designation, Status, Employee, SalaryDetail

class DefaultAdmin(fullhistory.admin.FullHistoryAdmin):
    pass

class SalaryDetailAdmin(fullhistory.admin.FullHistoryAdmin):
    list_display = ('employee',
                    'year',
                    'month',
                    'basic',
                    'da',
                    'hra',
                    'allowance',
                    'total_salary',
                    'loss_of_pay',
                    'contribution_to_pf',
                    'repayment_of_loan',
                    'total_remittence',
                    'admin_charges',
                    'total_deductions',
                    )

    list_editable = ('basic',
                    'da',
                    'hra',
                    'allowance',
                    'loss_of_pay',
                    'repayment_of_loan',
                    )

    list_filter = ('year',
                   'month',
                  )

    #readonly_fields = ('contribution_to_pf', 'admin_charges', 'total')

    fieldsets = ((None,
                  {'fields': ('employee', 'year', 'month',)
                  }
                 ),
                 ('Salary Details',
                  {'classes': ('collapse','closed',),
                   'fields': ('basic',
                              'da',
                              'hra',
                              'allowance',
                              #'total_salary',
                              'loss_of_pay',
                             )
                  }
                 ),
                 ('Remittence Details',
                  {'classes': ('collapse','closed',),
                   'fields': (#'contribution_to_pf',
                              'repayment_of_loan',
                              #'total_remittence',
                              #'admin_charges',
                              #'total_deductions',
                             )
                  }
                 ))


class EmployeeAdmin(fullhistory.admin.FullHistoryAdmin):

    # Options for admin
    list_display = ('name',
                    'code',
                    'unit',
                    'designation',
                    'status')

    list_filter = ('active',
                   'status',
                   'designation',
                   'unit',
                   'date_of_joining',
                  )
    list_per_page = 20
    search_fields = ('name',
                     'code',
                     #'designation',
                     #'comments',
                     #'address'
                    )
    search_fields_verbose = ('Name',
                             'Employee Code',
                             #'Designation',
                             #'Comments',
                             #'Address'
                            )

    fieldsets = ((None,
                  {'fields': ('code', 'name', 'unit',)
                  }
                 ),
                 ('Professional Details',
                  {'classes': ('collapse','closed',),
                   'fields': ('designation', 'date_of_joining', 'status', 'active', 'comments')
                  }
                 ),
                 ('Personal Details',
                  {'classes': ('collapse','closed',),
                   'fields': ('date_of_birth', 'address',)
                  }
                 ))

    actions = ('re_activate',
               'de_activate',
               csv_export_selected,
              )


    def re_activate(self, request, queryset):
        queryset.update(active=True)

    def de_activate(self, request, queryset):
        queryset.update(active=False)


def register(model, modelAdmin):
    admin.site.register(model, modelAdmin)
    databrowse.site.register(model)
    fullhistory.register_model(model)

register(Unit, DefaultAdmin)
register(Designation, DefaultAdmin)
register(Status, DefaultAdmin)
register(Employee, EmployeeAdmin)
register(SalaryDetail, SalaryDetailAdmin)
