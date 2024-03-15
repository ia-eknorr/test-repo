## TODO: Document
# Imports
from abc import ABCMeta

# Excpetions
class DoesNotExistError(Exception):
	""" """
	_message = "Tag '{path}' does not exist."
	def __init__(self, tagPath):
		message = self._message.format(path=tagPath)
		super(DoesNotExistError, self).__init__(message)
		
class InvalidTagTypeError(Exception):
	""" """
	_message = "Tag at '{path}' is not of type '{udt}'."
	def __init__(self, tagPath, baseType):
		message = self._message.format(path=tagPath, udt=baseType)
		super(InvalidTagTypeError, self).__init__(message)
		
class InvalidWriteError(Exception):
	""" """
	_message = "Number of write paths, {paths}, does not match the number of values, {values}."
	def __init__(self, writePaths, writeValues):
		message = self._message.format(paths=len(writePaths), values=len(writeValues))
		super(InvalidWriteError, self).__init__(message)

# Abstract Class
class AbstractUdt(object):
	"""Abstract Tag definition class"""
	__metaclass__ = ABCMeta
	_udtType = None
	def __init__(self, tagPath):
		self.__checkTagType(tagPath)
		self._readPaths = list()
		self._writePaths = list()
		self._writeValues = list()
		self.tagPath = tagPath
		
	def __checkTagType(self, tagPath):
		"""Check that the udt tag path is of the class type
		
		Args:
			tagPath: path to tag to check for udt instance type
		Returns:
			None
		"""
		if not system.tag.exists(tagPath):
			raise DoesNotExistError(tagPath)
			
		path = '{tagPath}.typeId'.format(tagPath=tagPath)
		typeId = system.tag.readBlocking([path])[0].value
		if str(typeId) != self._udtType:
			raise InvalidTagTypeError(tagPath, self._udtType)
		return None
		
	def _getPath(self, item):
		""" """
		return '{0}/{1}'.format(self.tagPath, item)
		
	def _setValue(self, path, value, immediate):
		""" """
		self.addWrites(path, value)
		if immediate: self.writeTags()
		return None
	
	def addReads(self, items):
		""" """
		if isinstance(items, str):
			items = [items]
			
		self._readPaths += list(map(self._getPath, items))
		return None
		
	def addExternalReads(self, items):
		""" """
		if isinstance(items, str):
			items = [items]
			
		self._readPaths += list(items)
		return None
		
	def addWrites(self, items, values):
		""" """
		if isinstance(items, str):
			items, values = [items], [values]
			
		if len(items) != len(values):
			raise InvalidWriteError(items, values)
			
		self._writePaths += list(map(self._getPath, items))
		self._writeValues += list(values)
		return None
		
	def addExternalWrites(self, items, values):
		""" """
		if isinstance(items, str):
			items, values = [items], [values]
			
		if len(items) != len(values):
			raise InvalidWriteError(items, values)
			
		self._writePaths += list(items)
		self._writeValues += list(values)
		return None
		
	def flushReads(self):
		""" """
		self._readPaths = list()
		return None
		
	def flushWrites(self):
		""" """
		self._writePaths, self._writeValues = list(), list()
		return None
		
	def writeTags(self):
		""" """
		if not bool(self._writePaths):
			raise Exception("No paths present to write.")
		elif not bool(self._writeValues):
			raise Exception("No values present to write.")
		elif len(self._writePaths) != len(self._writeValues):
			raise InvalidWriteError(self._writePaths, self._writeValues)
			
		writes = system.tag.writeBlocking(self._writePaths, self._writeValues)
		self.flushWrites()
		return all(writes)
		
	def readTags(self):
		""" """
		if not bool(self._readPaths):
			raise Exception
		
		values = system.tag.readBlocking(self._readPaths)
		self.flushReads()
		return values
		
	def set(self, item, value):
		""" """
		path = self._getPath(item)
		return all(system.tag.writeBlocking([path], [value]))
		
	def get(self, item):
		""" """
		path = self._getPath(item)
		return system.tag.readBlocking([path])[0].value