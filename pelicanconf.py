AUTHOR = 'Edward Gomez'
SITESUBTITLE = '13 &amp; 15 August 2024 - IAU GA2024 Focus Meeting 10'
SITENAME = 'Teaching capacity of remote observing facilities for Universities and High Schools'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

THEME = 'themes/bulma_profile/'

# Blogroll
LINKS = (
        ('Home','/'),
        ('Scientific Rationale', '/rationale/'),
         ('Talks & Posters', '/talks/'),
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

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True