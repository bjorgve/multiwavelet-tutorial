# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = "Multiwavelet tutorial"
copyright = "2021, The contributors"
author = "The contributors"
github_user = "MRChemSoft"
github_repo_name = "multiwavelet-tutorial"  # auto-detected from dirname if blank
github_version = "master"
conf_py_path = "/content/"  # with leading and trailing slash
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # githubpages just adds a .nojekyll file
    "sphinx.ext.githubpages",
    "sphinx_lesson",
    # 'sphinx.ext.intersphinx',
    "sphinxcontrib.bibtex",
    "sphinx.ext.todo",
    "sphinx_thebe",
]
# configure myst_nb
source_suffix = {".rst": "restructuredtext", ".ipynb": "myst-nb", ".myst": "myst-nb"}
# configure sphinxcontrib.bibtex
bibtex_bibfiles = ["bibliography.bib"]
# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/use/execute.html#triggering-notebook-execution
jupyter_execute_notebooks = "off"  # no notebook execution
# jupyter_execute_notebooks = "auto"   # *only* execute if at least one output is missing.
# jupyter_execute_notebooks = "force"  # *always* execute notebooks
# jupyter_execute_notebooks = "cache"  # *cache* execution outputs

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
    "notebooks/solutions/*.ipynb",
    "notebooks/visualization_*.ipynb"
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "img/hylleraas-logo.png"
html_title = ""  # project
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js",
    "https://3Dmol.org/build/3Dmol-min.js"
]
# sphinx-book-theme options
html_theme_options = {
    "repository_url": f"https://github.com/{github_user}/{github_repo_name}",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "repository_branch": "master",
    "path_to_docs": "content",
    "use_download_button": True,
    "home_page_in_toc": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "thebe": True,
        "notebook_interface": "jupyterlab",
    },
}
html_sidebars = {
    "**": [ "sidebar-logo.html", "sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "inputs"]
# html_css_files = ["overrides.css"]
# HTML context:
from os.path import basename, dirname, realpath

html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}
# Intersphinx mapping.  For example, with this you can use
# :py:mod:`multiprocessing` to link straight to the Python docs of that module.
# List all available references:
#   python -msphinx.ext.intersphinx https://docs.python.org/3/objects.inv
# intersphinx_mapping = {
#    #'python': ('https://docs.python.org/3', None),
#    #'sphinx': ('https://www.sphinx-doc.org/', None),
#    }

# the epilog
rst_epilog = f"""
.. role:: red
.. role:: blue
.. _MRChemSoft: https://github.com/MRChemSoft
"""
