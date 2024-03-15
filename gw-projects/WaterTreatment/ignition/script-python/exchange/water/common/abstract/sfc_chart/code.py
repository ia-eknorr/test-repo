# Imports
from abc import ABCMeta
from exchange.water.common.logger import Logger

logger = Logger('SFC', 'Charts')

class AbstractSFC(object):
	"""Abstract SFC definition class"""
	_path = 'Exchange/Water'
	_project = system.util.getProjectName()
	_item = None
	_parameters = {}
	def __init__(self, **kwargs):
		self.parameters = self._parameters.copy()
		self.parameters.update({key: value for key, value in kwargs.items() if key in self._parameters.keys()})
		
	def start(self):
		"""Start the SFC chart"""
		logger.log("Starting SFC '{0}' with params '{1}'".format(self.path, str(self.parameters)))
		return system.sfc.startChart(*self.args)
		
	@property
	def path(self):
		"""Get the path to the SFC"""
		return system.util.getProperty('file.separator').join([self._path, self._item])
		
	@property
	def args(self):
		"""Get the chart args to be passed into the system.sfc.startChart function"""
		return [
			self._project
			, self.path
			, self.parameters
		]
		
	@classmethod
	def getParameterKeys(cls):
		"""Return the parameter keys for this SFC chart"""
		return list(cls._parameters.keys())