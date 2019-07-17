========================
sphinxcontrib-collations
========================

.. image:: https://travis-ci.org/sphinx-contrib/sphinxcontrib-collations.svg?branch=master
    :target: https://travis-ci.org/sphinx-contrib/sphinxcontrib-collations

.. note::
    This extension is currently WIP. It will probably be a mid-August
    before a minimally usable release is available.

Tools to maintain consistency across a collection of closely related
packages, such as those belonging to a single umbrella project.

Overview
--------

This extension, when paired with a remote instance of ``tendril-collations``
served by a ``tendril-prefab-server`` or compatible JSON API server, allows
projects belonging to a collation of related projects to use a centralized
configuration for sphinx documentation generation.

This is largely related only to styling and visual consistency. This package
does not get into larger issues like build process and deployment, which
should be dealt with by your CI solution.

Who this is for
---------------

This extension is unlikely to be useful for most, if not all projects, even
those belonging to larger collections. The added effort of setting up the
JSON API server itself is unlikely to make it worthwhile to use.

If you do wish to use this extension, though, go right ahead. Pull requests
and bug reports are welcome for features that aren't already there, and
you may either open an Issue on Github (preferable) or write to me directly
for a discussion on suitability for your application or the architecture
used. Any ideas which help generalize the extension will be especially
welcome.

Features
--------

- (TODO) Use an intersphinx inventory collection including all the
  projects of the collation
- (TODO) Use documentation options commonly set across each of the
  projects, including :

  - (TODO) Generic module level members of ``conf.py``
  - (TODO) Custom templates
  - (TODO) Collation logo
  - (TODO) Custom CSS

- (TODO) Provide collation-level dependency information, including :

  - (TODO) Immediate dependencies of the documented project
  - (TODO) Recursive dependencies of the documented project
    upto the border of the collation
  - (TODO) Usage of the documented project within the collation


Limitations and Known Issues
----------------------------

- Does not support changing the underlying theme itself, and currently
  assumes the use of an underlying alabaster based theme.
- Does not perform any kind of validation of the provided information.
  it is left to the developer to ensure the collation configuration is
  correct, secure, and is applied in the correct sequence in ``conf.py``
  when applying any package specific overrides.
- The JSON API server is currently expected to be public, which means
  your logo and branding can be used by anyone without any
  authorization from you.


Links
-----

- Source: https://github.com/sphinx-contrib/sphinxcontrib-collations
- Bugs: https://github.com/sphinx-contrib/sphinxcontrib-collations/issues
