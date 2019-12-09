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

# The full version, including alpha/beta/rc tags
release = '2019-07-06.0'


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
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes']
html_theme_options = {
  'collapse_navigation': False,
  'navigation_depth': -1,
}
todo_include_todos = True
ct_separator = '\N{SINGLE RIGHT-POINTING ANGLE QUOTATION MARK}'

# An empty format for CheckExternalLinksBuilder (linkchecking) is required.
aafig_format = {
  'html': 'svg',
  'latex': 'pdf',
  'text': None,
  '': None
}
aafig_default_options = {
  'textual': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
