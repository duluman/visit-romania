from testare_git.settings.base import *

DEBUG = True
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_ROOT = 'media/'

