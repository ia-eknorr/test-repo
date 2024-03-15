# Import Logger class
from exchange.water.common.logger import Logger

# Functions
def getLogger(domain, item):
	"""Get the Water/WasteWater resource logger
	
	Args:
		domain: Ignition "area" this logger is being run from (Perspective, AlarmPipelines, etc)
		item: where this logger is being run from inside the domain value
	Returns:
		logger class
	"""
	return Logger(domain, item)