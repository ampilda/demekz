#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#скрипт для создания директории бэкапа и сохранения в него базы данных при каждом запуске manage.py
def backup():
    if not os.path.exists("backup"):
        os.popen("mkdir backup")
    
    if sys.platform == "win32":
        os.popen("copy database.db backup\\")
    else:
        os.popen("cp database.db backup/")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demexam.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    backup()
    main()
