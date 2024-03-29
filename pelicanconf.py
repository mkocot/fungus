#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'm'
SITENAME = u'FungUs'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ["bua", "cake"]

TIMEZONE = 'Europe/Warsaw'
TYPOGRIFY = True
THEME = "themes/pl/notmyidea"

DEFAULT_LANG = u'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n']
        }

PLUGINS = ['i18n_subsites']
PLUGIN_PATHS = ['pelican-plugins']


I18N_SUBSITES = {
        'en': {
                "THEME": "themes/en/notmyidea",
                "STATIC_PATHS": STATIC_PATHS,
        }
}
