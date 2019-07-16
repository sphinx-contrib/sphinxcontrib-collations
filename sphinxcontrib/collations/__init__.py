"""
    sphinxcontrib.collations
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Tools to maintain consistency across a collection of closely related packages, such as those belonging to a single umbrella project

    :copyright: Copyright 2017 by Chintalagiri Shashank <shashank.chintalagiri@gmail.com>
    :license: BSD, see LICENSE for details.
"""

import pbr.version

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

__version__ = pbr.version.VersionInfo(
    'collations').version_string()


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    return {'version': __version__, 'parallel_read_safe': True}
