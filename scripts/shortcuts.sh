
# Add this file to your ~/.bashrc
# Example :
#    . ~/scripts/employee_management_system/scripts/shortcuts.sh

function employee_management_system()
{
    workon employee_management_system
    cd ~/scripts/employee_management_system
    export DJANGO_SETTINGS_MODULE=employee_management_system.settings.settings
    scripts/restart_webserver.sh
}
