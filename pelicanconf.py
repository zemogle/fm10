AUTHOR = 'Edward Gomez'
SITENAME = 'IAU GA2024 Focus Meeting 10'
SITESUBTITLE = 'Teaching capacity of remote observing facilities for the Universities and High Schools'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

THEME = 'themes/bulma_profile/'

# Blogroll
LINKS = (
        ('Home','/'),
        ('Program', '/program/'),
         ('Talks', '/talks/'),
         ('SOC','/scientific-organizing-committee/')
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

READERS = {"html": None}

STATIC_PATHS = ['images',]


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True