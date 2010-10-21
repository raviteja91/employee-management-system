
from employee_management_system.settings.settings import *

DEBUG = False

INSTALLED_APPS = list(INSTALLED_APPS)
# django-sane-testing is throwing errors when south is enabled. So disable south
INSTALLED_APPS.remove('south')
