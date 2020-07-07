# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020, A10 Networks Inc.
# GNU General Public License v3.0
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The acos lldp_global fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


from copy import deepcopy
from ansible.module_utils.network.common import utils
from ansible_collections.a10.acos_cli.plugins.module_utils.network.a10.utils.utils import (
    get_interface_type,
    normalize_interface,
)
from ansible_collections.a10.acos_cli.plugins.module_utils.network.a10.argspec.lldp_global.lldp_global import (
    Lldp_globalArgs,
)

class Lldp_globalFacts(object):
    """ The acos lldp_global fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Lldp_globalArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for lldp_global
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        objs = dict()
        if not data:
            data = connection.get('show running-config with-default | section lldp')
        # operate on a collection of resource x
        config = data.split('\n')
        for conf in config:
            if conf:
                obj = self.render_config(self.generated_spec, conf)
                if obj:
                    objs.update(obj)
        facts = {}

        if objs:
            params = utils.validate_config(self.argument_spec, {'config': utils.remove_empties(objs)})
            facts['lldp_global'] = utils.remove_empties(params['config'])
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)

        system_name = utils.parse_conf_arg(conf, 'lldp system-name')
        notification_interval = utils.parse_conf_arg(conf, "lldp notification interval")
        fast_count = utils.parse_conf_arg(conf, 'lldp tx fast-count')
        fast_interval = utils.parse_conf_arg(conf, 'lldp tx fast-interval')
        holdtime = utils.parse_conf_arg(conf, 'lldp tx hold')
        interval = utils.parse_conf_arg(conf, 'lldp tx interval')
        reinit_delay = utils.parse_conf_arg(conf, 'lldp tx reinit-delay')
        if system_name:
            config['system_name'] = str(system_name)
        if notification_interval:
            config['notification_interval'] = int(notification_interval)
        if fast_count:
            config['fast_count'] = int(fast_count)
        if fast_interval:
            config['fast_interval'] = int(fast_interval)
        if holdtime:
            config['holdtime'] = int(holdtime)
        if 'enable' in conf:
            config['enabled'] = True
        if interval:
            config['interval'] = int(interval)
        if reinit_delay:
            config['reinit_delay'] = int(reinit_delay)

        return utils.remove_empties(config)
