# -*- coding: utf-8 -*-
# Description: netdata nginx-error-log collector
# Author: bytepark GmbH (fr@bytepark.de)

import re

from bases.FrameworkServices.LogService import LogService

ORDER = [
	'levels', 'errors'
]

CHARTS = {
	'errors': {
		'options': [None, 'Errors in log', 'errors', 'nginx errors', 'nginx.errors', 'line'],
		'lines' : [
			['Timeout'],
                        ['Refused'],
			['AccessForbidden'],
			['DirectoryIndexForbidden'],
			['NoSuchFile']
		]
	},
	'levels': {
		'options' : [None, 'Errors per level in error log', 'errors', 'nginx errors', 'nginx.errors', 'line'],
		'lines' : [
			['emerg'],
			['alert'],
			['crit'],
			['error'],
			['warn'],
			['notice'],
			['info'],
			['debug']
		]
	}	
}

REGEX = {
	'Timeout' : 'upstream timed out .*',
        'Refused' : 'Connection refused .*',
	'AccessForbidden' : 'access forbidden by rule',
	'DirectoryIndexForbidden' : 'directory index of \".*\" is forbidden',
	'NoSuchFile' : 'No such file or directory'
}

class Service(LogService):
	def __init__(self, configuration=None, name=None):
		LogService.__init__(self, configuration=configuration, name=name)
		self.order = ORDER
		self.definitions = CHARTS
		self.log_path = self.configuration.get('log_path', '/var/log/nginx/error.log')
		self.regex = '(?P<dateandtime>\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>[a-z]+)\] (?P<pid>[0-9]*)\#(?P<tid>[0-9]*): \*[0-9]* (?P<errorstring>.*)'
		self.data = dict()

	def _get_data(self):
		"""
		:return: dict
		"""
		raw = self._get_raw_data()

                for chart in CHARTS:
                    for line in CHARTS[chart]['lines']:
                        self.data[line[0]] = 0

		if not raw:
			return self.data
		
                for row in raw:
			match = re.search(self.regex, row)

			if not match:
				continue
			else:
				match_dict = match.groupdict()

			if 'level' in match_dict:
				lvl = match_dict['level']
				if not lvl in self.data:
					self.data[lvl] = 1
				else:
					self.data[lvl] += 1
			if 'errorstring' in match_dict:
				for key in REGEX:
					reg = REGEX[key]
					if  re.search(reg, match_dict['errorstring']):
						if not key in self.data:
							self.data[key] = 1
						else:
							self.data[key] += 1
		return self.data


