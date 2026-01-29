# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python SCTP module'
copyright = '2025, Yves Legrandgérard'
author = 'Yves Legrandgérard'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.graphviz']

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'python_docs_theme'
html_static_path = ['_static']

asterisk = r'*'

rst_prolog = """
.. role:: C(code)
    :language: C
    :class: highlight

.. role:: Py(code)
    :language: python
    :class: highlight

.. role:: Bash(code)
    :language: console
    :class: highlight
"""
