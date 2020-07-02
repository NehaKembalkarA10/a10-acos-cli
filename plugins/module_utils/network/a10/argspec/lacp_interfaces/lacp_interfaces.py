# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020, A10 Networks Inc.
# GNU General Public License v3.0
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the acos_lacp_interfaces module
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class Lacp_InterfacesArgs(object):
    """The arg spec for the acos_lacp_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "name": {"required": True, "type": "str"},
                "port_priority": {"type": "int"},
                "trunk_group": {"type": "str"},
                "timeout": {"type": "str"},
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "rendered",
                "parsed",
                "gathered",
            ],
            "default": "merged",
            "type": "str",
        },
    }
