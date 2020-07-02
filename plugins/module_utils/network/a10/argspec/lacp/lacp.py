# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020, A10 Networks Inc.
# GNU General Public License v3.0
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the acos_lacp module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class LacpArgs(object):
    """The arg spec for the acos_lacp module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {'options': {'system': {'options': {'priority': {'required': True, 'type': 'int'}},
                                          'type': 'dict'}
                               }, 'type': 'dict'
                   },
        'state': {'choices': ['merged', 'replaced', 'deleted'], 'default': 'merged',
                  'type': 'str'}
    }
