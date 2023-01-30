# manage.py
import os
import sys
import subprocess

if __name__ == '__main__':
    args = sys.argv[1:]
    subprocess.run(['flask', *args], env={
        **os.environ,
        'FLASK_RUN_PORT': '3000',
        'FLASK_RUN_HOST': '0.0.0.0'
    })