# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020, A10 Networks Inc.
# GNU General Public License v3.0
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the acos_interfaces module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class InterfacesArgs(object):

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
                                'options': {'interface-type': {'type': 'str', 'required': True},
                                            'name': {'type': 'str'},
                                            'description': {'type': 'str'},
                                            'load-interval': {'type': 'int'},
                                            'enabled': {'default': True, 'type': 'bool'}},
                                'type': 'list'},
                     'state': {'choices': ['merged', 'replaced', 'overridden', 'deleted'],
                               'default': 'merged',
                               'type': 'str'}}
