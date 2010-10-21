#!/usr/bin/env bash

PROJECT_ROOT=`python -c 'from employee_management_system.settings import settings; print settings.PROJECT_ROOT'`

echo 'Stopping employee_management_system_fcgi.py'
pkill -f employee_management_system_fcgi.py

sleep 1

echo 'Starting employee_management_system_fcgi.py'
python ${PROJECT_ROOT}/deploy/employee_management_system_fcgi.py

