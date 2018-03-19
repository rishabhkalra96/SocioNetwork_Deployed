from django_project.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
