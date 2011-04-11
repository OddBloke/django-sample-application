# -*- coding: utf-8 -*-

import os.path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'benchmark.db',                 # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# static assets
MEDIA_URL = '/assets/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'assets/')

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd6jnorlaq6=g4!i7)5o44$jr2ffvttxl(t=d-84aw#jvuf(dea'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'benchmark.urls'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'), )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'benchmark_app',
)


TEST_DATA = [
    "Lorizzle yo tellivizzle sit gangster, black mah nizzle bling bling. Nullizzle sapien velit, i saw beyonces tizzles and my pizzle went crizzle stuff, suscipizzle quis, own yo' , cool. Pellentesque eget tortor. Gizzle erizzle. Nizzle yo rizzle sheezy turpis tempizzle shizznit. Mauris pellentesque nibh my shizz turpis. Bizzle izzle doggy. Pellentesque eleifend rhoncizzle daahng dawg. In pimpin' habitasse platea dictumst. Ghetto fo shizzle. Curabitur tellus urna, pretizzle eu, mattizzle ac, check it out vitae, nunc. Stuff suscipizzle. Boofron dawg my shizz sizzle purizzle.",
    "Vestibulizzle hizzle ipsum uhuh ... yih! izzle bow wow wow orci boom shackalack et posuere boofron Curae; Da bomb vitae nulla da bomb neque ornare aliquizzle. Gangsta euismizzle dawg. Praesent volutpizzle pot fo. crunk cool, adipiscing vitae, gravida sed, interdizzle vitae, ante. Bizzle malesuada bibendizzle crackalackin. Shiz izzle the bizzle et yippiyo bow wow wow sheezy. Nizzle sed augue. Vivamizzle sagittizzle. Check out this mammasay mammasa mamma oo sa lacus quis pimpin' posuere fo shizzle. Donizzle shut the shizzle up tellizzle tellivizzle yo mamma tincidunt mollizzle. Integer odio. Check it out dope. Sheezy magna check it out, dignissim vitae, porttitor ac, imperdiet egestizzle, dope. Dang doggy boofron lectizzle. Etizzle sollicitudizzle yippiyo sizzle. Hizzle mi stuff, convallis my shizz, pellentesque bling bling, yippiyo pimpin', fo. Fusce erizzle bizzle, facilisizzle eu, sollicitudin shizzle my nizzle crocodizzle, aliquizzle break yo neck, yall, lectizzle. The bizzle maurizzle risizzle, varius its fo rizzle, adipiscing dope, blandizzle check it out shiznit, enim.",
    "In check it out ligula fo shizzle est. Gangsta ullamcorpizzle. Etiam tempizzle. Things izzle for sure a eros imperdizzle vehicula. Dizzle vel my shizz. Sed break it down est izzle crackalackin. Praesent yo mamma vitae urna shut the shizzle up ullamcorpizzle. Integizzle pimpin' go to hizzle. Vivamizzle lobortizzle lacus i'm in the shizzle gangster. Morbi egizzle . Etizzle mah nizzle dui izzle magna phat stuff. Morbi placerizzle, away non owned porta, nisl phat adipiscing nunc, rizzle ornare mi dolizzle sizzle amet boofron. Morbi turpizzle. Shut the shizzle up ante ipsum things izzle da bomb luctizzle izzle crackalackin posuere cubilia Boofron; Own yo' vehicula, for sure laoreet tincidunt hendrerizzle, fo shizzle lorem tellivizzle nunc, i saw beyonces tizzles and my pizzle went crizzle that's the shizzle urna metizzle stuff break it down. Pot mofo erat yo mamma we gonna chung. Phasellizzle hizzle. Cizzle socizzle dang shizzle my nizzle crocodizzle crunk for sure dis parturient montizzle, bling bling ridiculizzle black. Dawg et gangsta for sure quizzle shizzlin dizzle dope. Donec crazy brizzle.",
    "Nulla away . Dang porta commodo tellus. Aenean viverra, fizzle izzle boom shackalack hendrerizzle, libero doggy hendrerit leo, check out this condimentizzle shit dizzle gangster fo. Ghetto eu dolor. Vestibulum daahng dawg felizzle. Sed elementizzle faucibizzle erizzle. Integizzle nulla gangster, volutpat mammasay mammasa mamma oo sa, volutpat eget, auctor egizzle, nunc. Da bomb nizzle. Nunc nisi. Dang sizzle brizzle leo fizzle ass blandit dignissim. Ass laorizzle gangsta sizzle daahng dawg enizzle. Aenean tempizzle dignissim phat.",
    "Crunk tempizzle crackalackin izzle sizzle. Pellentesque shiz pimpin' pot ligula dapibus interdizzle. Etiam auctor dizzle dui. Aliquam break it down yo neque. Aliquizzle stuff fo shizzle. In sizzle amizzle for sure. Pellentesque fo shizzle felizzle hizzle nunc. a brizzle. Quisque lorem justo, own yo' dapibizzle, izzle, doggy nizzle, mi. We gonna chung ass felizzle in sapien egestas consequizzle. Sizzle nizzle black. Crizzle sure. The bizzle nisi tortizzle, fo shizzle brizzle, pharetra a, malesuada izzle, go to hizzle. Pellentesque dapibizzle ultricizzle mi. Ghetto fizzle orci, aliquet quis, vehicula shizznit, boom shackalack sizzle, augue. Nullam i saw beyonces tizzles and my pizzle went crizzle. Morbi dang sapizzle in boom shackalack shut the shizzle up mattizzle. Sizzle lectizzle sheezy, gizzle vestibulum, yo eu, fo izzle, ante.",
    "Ass interdizzle. I'm in the shizzle potenti. Maecenizzle nisl. For sure go to hizzle, bizzle quizzle, ullamcorper ut, scelerisque bow wow wow, leo. Pimpin' mofo pimpin'. Go to hizzle tellivizzle. Morbi nizzle, phat vitae fringilla cursus, libero mi varizzle felis, shut the shizzle up dizzle neque cool shiznit augue. Curabitizzle things hizzle that's the shizzle elit. Fusce bibendizzle dolor nec libero. Sizzle i'm in the shizzle, metus shiz varizzle lacinia, lorem eros pharetra ghetto, eu luctus phat est funky fresh daahng dawg.    ",
]
