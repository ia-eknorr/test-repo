# Imports
from abc import ABCMeta

# Abstract Delegate
class AbstractDelegate(type):
	""" """
	__metaclass__ = ABCMeta
	_package = None
	
	def __getattr__(cls, attr):
		try:
			return getattr(cls._package, attr)
		except:
			raise AttributeError