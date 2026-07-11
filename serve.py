"""
WSGI entry point for running this site behind nginx via NSSM on Windows Server.

NSSM service command example:
    Application:  C:\\path\\to\\venv\\Scripts\\python.exe
    Arguments:    D:\\Django\\myproject\\mysite\\serve.py
    Startup dir:  D:\\Django\\myproject\\mysite

nginx should reverse_proxy to 127.0.0.1:8001 and serve /static/ directly
from the STATIC_ROOT collected via `python manage.py collectstatic`.
"""
import os

from waitress import serve

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django  # noqa: E402

django.setup()

from config.wsgi import application  # noqa: E402

if __name__ == '__main__':
    serve(application, host='127.0.0.1', port=8001, threads=8)
