# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020, A10 Networks Inc.
# GNU General Public License v3.0
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the acos_lldp_global module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Lldp_globalArgs(object):

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'options': {'system_name': {'type': 'str'},
                                            'notification_interval': {'type': 'int'},
                                            'fast_count': {'type': 'int'},
                                            'fast_interval': {'type': 'int'},
                                            'holdtime': {'type': 'int'},
                                            'reinit_delay': {'type': 'int'},
                                            'enabled': {'type': 'bool'},
                                            'interval': {'type': 'int'},
                                            },
                                'type': 'dict'},
                     'state': {'choices': ['merged', 'replaced', 'deleted'],
                               'default': 'merged',
                               'type': 'str'}}
