"""
Formats the retrieved values from SSM into a JSON,
then prints the value to let it be echoed in a bash
script.
"""
import json
import os


MIGRATION_MANAGER_KEYS = os.getenv('MIGRATION_MANAGER_KEYS')

print(json.dumps(MIGRATION_MANAGER_KEYS, indent=4, sort_keys=True))
