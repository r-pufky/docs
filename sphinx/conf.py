# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./_ext'))


# -- Project information -----------------------------------------------------

project = 'Generic service & computer documentation.'
copyright = '2019, r-pufky'
author = 'r-pufky'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.todo',
  'sphinx.ext.viewcode',
  'sphinxcontrib.aafig',
  'ct',
]

# pygments doesn't handle powershell well. Ignore warnings for code-blocks.
suppress_warnings = ['misc.highlighting_failure']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['Thumbs.db', '.DS_Store']

today_fmt = '%Y-%m-%d'

# Include TODOs.
todo_include_todos = True

# ConfigTable separator
ct_separator = '\N{SINGLE RIGHT-POINTING ANGLE QUOTATION MARK}'

# aafig: Empty format for CheckExternalLinksBuilder (linkchecking) is required.
aafig_format = {
  'html': 'svg',
  'latex': 'pdf',
  'text': None,
  '': None
}
aafig_default_options = {
  'textual': True,
}

# linkchecker exceptions. See: https://pythex.org
linkcheck_ignore = [
  # Broken: local state/context needed to resolve.
  r'(http|https)://localhost\.*',
  r'(http|https)://192.168.\.*',
  r'(http|https)://10\.*',
  # Broken: Will timeout after too many requests.
  r'https://v.firebog.net/hosts/\.*',
  # Broken: github dynamically adds anchors and cannot be checked.
  r'https://github.com/.*[#]+',
  # Redirects: latest tags are always redirected to versions on github.
  r'https://github.com/.*/latest.*',
  # Redirects: behind authentication wall.
  r'https://security.google.com/\.*',
  r'https://plexapp.zendesk.com/\.*',
]
linkcheck_workers = 10

# HTML rendering
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes']
html_theme_options = {
  'collapse_navigation': False,
  'navigation_depth': -1,
}
html_show_sourcelink = False
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
