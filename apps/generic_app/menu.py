from django.core.urlresolvers import reverse
from admin_tools.menu import items, Menu

# to activate your custom menu add the following to your settings.py:
#
# ADMIN_TOOLS_MENU = 'employee_management_system.menu.CustomMenu'

class CustomMenu(Menu):
    """
    Custom Menu for employee_management_system admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children.append(items.Bookmarks(title='Bookmarks'))

        self.children.append(items.AppList(
            title='Master Data',
            include_list=('employee.models.Employee',
                          'employee.models.Unit',
                          'employee.models.Designation',
                          'employee.models.Status', )
        ))
        self.children.append(items.AppList(
            title='Transactions',
            include_list=('employee.models.SalaryDetail',)
        ))

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass
