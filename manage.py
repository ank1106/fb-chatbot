#!/usr/bin/env python
import os
import sys

try:
	with open('environment', 'r') as f:
		for row in f.read().split('\n'):
			key,val = row.split("=")
			os.environ[key] = val
except FileNotFoundError:
	pass

print(os.environ['SETTINGS'])
SETTINGS_MODULE = os.environ.get('SETTINGS', 'config.settings.local')
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
