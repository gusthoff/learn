# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import json
import os
import sys

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'learn.adacore.com'
copyright = u'2018 – 2021, AdaCore'
author = u'AdaCore' if 'SPHINX_AUTHOR' not in os.environ else \
    os.environ['SPHINX_AUTHOR']
title = u'Learn Ada (Complete)' if 'SPHINX_TITLE' not in os.environ else \
    os.environ['SPHINX_TITLE']

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'2021-01'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Find the widgets extension
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import widget_extension

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
#    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'widget_extension',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build',
                     'Thumbs.db',
                     '.DS_Store',
                     'old-content',
                     'sass',
                     '**/node_modules',
                     'internal',
                     '**/package.json',
                     '**/webpack.config.js'
                     'built',
                     'dist',
                     'src']

# Exclude internal and unfinished material from final site build
if 'GEN_LEARN_SITE' in os.environ and os.environ['GEN_LEARN_SITE'] == "yes":
    exclude_patterns += ['**internal/**',
                         '**training_examples/**',
                         '**courses/intro-to-embedded-sys-prog/**',
                         '**courses/advanced-ada/**',
                         '**courses/advanced-spark/**']

else:
    # When not building final site, `todo` and `todoList` produce output
    todo_include_todos = True


show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

nitpicky = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'learn_theme'

html_title = "learn.adacore.com"
smartquotes = False

html_theme_path = ['.'] # make sphinx search for themes in current dir

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "beta": False,
    'sticky_navigation': False,
}

html_logo = "img/logo.svg"

html_favicon = "img/favicon.ico"

html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['img',]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_copy_source = False

html_context = {
    'year': datetime.date.today().strftime('%Y'),
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'learnadacorecomdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
\usepackage{pmboxdraw} \usepackage{unicode-math}
\fvset{fontsize=\small}
''',

    # Font package inclusion
    #
    'fontpkg': r'''
\setmainfont{Open Sans}
\setsansfont{Open Sans}
\setmonofont{DejaVu Sans Mono}
''',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',

    # Avoid blank page for chapters on odd pages
    # 'extraclassoptions': 'openany',

    # Sphinx Setup (LaTeX-type customization)
    #
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',

    'sphinxsetup': '''
VerbatimBorderColor={rgb}{0.90,0.90,0.90},
VerbatimColor={rgb}{0.99,0.99,0.99},
TitleColor={named}{MidnightBlue}
''',
    # 'verbatimwithframe=false'

    # Inline code cannot be highlighted, see
    # https://github.com/sphinx-doc/sphinx/issues/5157
}

latex_logo = 'img/logo.png'

latex_show_urls = 'footnote'

latex_show_pagerefs = True

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'learnadacorecom.tex', title,
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'learnadacorecom', title,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'learnadacorecom', title,
     author, 'learnadacorecom', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {'learn': ('https://learn.adacore.com/', None)}


def setup(app):
    try:
        manifest = os.path.join(os.getcwd(), "build-manifest.json")
        with open(manifest, 'r') as infile:
            data = json.load(infile)

        for chunk, files in data.items():
            if "css" in files.keys():
                for css in files["css"]:
                    print("Adding {} to css...".format(css))
                    app.add_stylesheet(css)
            if "js" in files.keys():
                for js in files["js"]:
                    print("Adding {} to js...".format(js))
                    app.add_javascript(js)
    except FileNotFoundError as e:
        print("Warning: build-manifest.json not available")

        if not os.getenv('SPHINX_LOCAL_BUILD'):
            raise e
