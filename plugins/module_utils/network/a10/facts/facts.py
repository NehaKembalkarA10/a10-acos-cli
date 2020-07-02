# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020, A10 Networks Inc.
# GNU General Public License v3.0
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import FactsBase
from ansible_collections.a10.acos_cli.plugins.module_utils.network.a10.facts.lacp_interfaces.lacp_interfaces import (
    Lacp_InterfacesFacts,
)
from ansible_collections.a10.acos_cli.plugins.module_utils.network.a10.facts.lacp.lacp import (
    LacpFacts,
)
from ansible_collections.a10.acos_cli.plugins.module_utils.network.a10.facts.base import (
    Default, Hardware, Interfaces, Config)

FACT_LEGACY_SUBSETS = dict(
    default=Default,
    hardware=Hardware,
    interfaces=Interfaces,
    config=Config
)

FACT_RESOURCE_SUBSETS = dict(
    lacp_interfaces=Lacp_InterfacesFacts,
    lacp=LacpFacts
)


class Facts(FactsBase):
    """ The fact class for ACOS """

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(self, legacy_facts_type=None, resource_facts_type=None, data=None):
        """ Collects the facts for ACOS device
        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(
                FACT_RESOURCE_SUBSETS, resource_facts_type, data
            )

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(FACT_LEGACY_SUBSETS,
                                          legacy_facts_type)

        return self.ansible_facts, self._warnings
