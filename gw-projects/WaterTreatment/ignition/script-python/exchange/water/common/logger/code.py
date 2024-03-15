# Logger Exceptions
class InvalidLevelError(Exception):
	""" """
	_message = {
		'base': "Invalid level '{0}'."
		, 'default': "Invalid level '{0}' entered using default level '{1}'."
	}
	def __init__(self, level, default=None):
		message = self._message['default'].format(level, default) if default != None else self._message['base'].format(level)
		super(InvalidLevelError, self).__init__(message)

# Logger Class
class Logger(object):
	"""Generic Logger to be used through out the project
	
	Args:
		domain: Ignition "area" this logger is being run from (Perspective, AlarmPipelines, etc)
		item: where this logger is being run from inside the domain value
	"""
	_logger = 'exchange.{projectName}.{domain}.{item}'
	_levels = {'fatal', 'error', 'warn', 'info', 'debug', 'trace',}
	_defaultLevel = 'debug'
	def __init__(self, domain, item):
		self.domain = domain
		self.item = item
		self.logger = system.util.getLogger(self.name)
		
	@property
	def name(self):
		"""Logger name property"""
		return self._logger.format(projectName=system.project.getProjectName(), domain=self.domain, item=self.item)
		
	def log(self, message, level='info'):
		"""Log the message with a level"""
		level = self.isValidLevel(level)
		if level == 'fatal':
			self.logger.fatal(message)
		elif level == 'error':
			self.logger.error(message)
		elif level == 'warn':
			self.logger.warn(message)
		elif level == 'info':
			self.logger.info(message)
		elif level == 'debug':
			self.logger.debug(message)
		elif level == 'trace':
			self.logger.trace(message)
		return None
	
	def isValidLevel(self, level):
		"""Check the the level arg is a valid logging level
		
		Args:
			level: level to check for validity
		Returns:
			level or default level if invalid level (raise exception if no default level is set)
		"""
		# Check if the level is valid
		if level not in self.getLoggerLevels():
			# Log the invalid level entered
			self.logger.warn(InvalidLevelError(level, self._defaultLevel))
			# Raise exception if no default level is set
			if self._defaultLevel == None:
				raise InvalidLevelError(level)
			else:
				# Set the level to the default
				level = self._defaultLevel
		return level
		
	@classmethod
	def getLoggerLevels(cls):
		"""Return a list of the logger levels on this logger"""
		return list(cls._levels)
	