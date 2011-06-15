import os
import sys
try:
	from ConfigParser import SafeConfigParser, NoOptionError, NoSectionError
except ImportError:
	# renamed in py3k
	from configparser import SafeConfigParser, NoOptionError, NoSectionError
from argparse import ArgumentParser

def print_error(message):
	'''Print `message` to stderr, in either py2k or py3k.'''
	# This is really quite terrible, but without the exec statements, it won't
	# compile.
	try:
		exec('print(message, file=sys.stderr)')
	except SyntaxError:
		exec('print >> sys.stderr, message')

class Waypoints(object):
	def __init__(self):
		self.config = SafeConfigParser()
		self.configPath = os.path.expanduser('~/.config/waypoint/waypoint.config')
		self.config.read(self.configPath)
	
	def add(self, name, section):
		path = os.getcwd()
		
		if not self.config.has_section(section):
			self.config.add_section(section)
		self.config.set(section, name, path)
		try:
			configFile = open(self.configPath, 'w')
			self.config.write(configFile)
		finally:
			configFile.close()
	
	def remove(self, name, section):
		self.config.remove_option(section, name)
		# Did we remove the last option in a section?
		if not self.config.options(section):
			self.config.remove_section(section)
		try:
			configFile = open(self.configPath, 'w')
			self.config.write(configFile)
		finally:
			configFile.close()
	
	def goto(self, name, section):
		path = self.config.get(section, name)
		#os.chdir(path)
		try:
			file = open(os.path.expanduser('~/.config/waypoint/scratch.sh'), 'w')
			file.write('cd %s' % path)
		finally:
			file.close()
	
	def list(self, section, name):
		if name:
			print("%s = %s" % (name, self.config.get(section, name)))
			return
		
		if section:
			sections = [section]
		else:
			sections = self.config.sections()
		
		for section in sections:
			print("[%s]" % section)
			for key, value in self.config.items(section):
				print("%s = %s" % (key, value))
			print('')

if __name__=='__main__':
	waypoints = Waypoints()
	
	parser = ArgumentParser(description='Teleport around your shell.')
	subparsers = parser.add_subparsers()
	
	parser_add = subparsers.add_parser('add')
	parser_add.add_argument('name', default='default', nargs='?')
	parser_add.add_argument('section', default='default', nargs='?')
	parser_add.set_defaults(func=waypoints.add)
	
	parser_remove = subparsers.add_parser('rm')
	parser_remove.add_argument('name', default='default', nargs='?')
	parser_remove.add_argument('section', default='default', nargs='?')
	parser_remove.set_defaults(func=waypoints.remove)
	
	parser_goto = subparsers.add_parser('goto')
	parser_goto.add_argument('name', default='default', nargs='?')
	parser_goto.add_argument('section', default='default', nargs='?')
	parser_goto.set_defaults(func=waypoints.goto)
	
	parser_list = subparsers.add_parser('list')
	parser_list.add_argument('section', default=None, nargs='?')
	parser_list.add_argument('name', default=None, nargs='?')
	parser_list.set_defaults(func=waypoints.list)
	
	# Because I didn't want to pass an argparse.Namespace to the functions and
	# have to access everything through args.foo, we pull out the values as a
	# dictionary and splat 'em in.
	# (Shallow-)Copying the dict is necessary, since we want to avoid passing
	# the going-to-be-called function in as a parameter to itself.
	args = parser.parse_args().__dict__
	function = args['func']
	del args['func']
	try:
		function(**args)
	except NoOptionError, exception:
		print_error(exception.message)
	except NoSectionError, exception:
		print_error(exception.message)
