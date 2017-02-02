import os

if os.name == 'nt':
    PHANTOM_JS_PATH = 'C:\phantomjs-2.1.1-windows\phantomjs.exe'
else:
    PHANTOM_JS_PATH = None

DATE_FORMAT = '%d/%m/%Y'    # date format for output

SITE_SETTINGS = {
    'oktv.ua': {
        'xpath': '//div[@data-time-default]',       # where to find cells in calendar
        'date-format': '%d.%m.%Y',                  # date format on a site
        'date-attr': 'data-time-default',           # where to find a date
        'busy-attr': 'data-busy',                   # where to find a status on that day
        'is_free': lambda s: 'free' in s            # how to check if it free or busy from 'busy_attr'
    },

    'dobovo.com': {
        'xpath': '//div[@date]',
        'date-format': '%Y-%m-%d',
        'date-attr': 'date',
        'busy-attr': 'class',
        'is_free': lambda s: not ('is-inactive' in s or 'is-last-days' in s)
    }
}
