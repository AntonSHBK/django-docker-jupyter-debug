from .settings import *

if "django_extensions" not in INSTALLED_APPS:    
    INSTALLED_APPS.append("django_extensions")

SHELL_PLUS = "ipython"
SHELL_PLUS_PRINT_SQL = True
IPYTHON_ARGUMENTS = [
    "--ext",
    "django_extensions.management.notebook_extension",
    "--debug",
]

IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"
NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--port",
    "8888",
    "--allow-root",
    "--no-browser",
    # "--NotebookApp.iopub_data_rate_limit=1e5",
    # "--NotebookApp.token=''",
]

DJANGO_ALLOW_ASYNC_UNSAFE = True
