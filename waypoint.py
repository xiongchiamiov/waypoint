import os
import sys
try:
	from ConfigParser import SafeConfigParser
except ImportError:
	# renamed in py3k
	from configparser import SafeConfigParser
from argparse import ArgumentParser

class Waypoints(object):
	def __init__(self):
		self.config = SafeConfigParser()
		self.configPath = os.path.expanduser('~/.config/waypoint/waypoint.config')
		self.config.read(self.configPath)
	
	def add(self, name, section):
		path = os.getcwd()
		
		self.config.set(section, name, path)
		with open(self.configPath, 'w') as configFile:
			self.config.write(configFile)
		
		# This is a quite hacky way of preventing the calling shell script from
		# causing a cd to the current directory.
		sys.exit(1)
	
	def goto(self, name, section):
		path = self.config.get(section, name)
		#os.chdir(path)
		with open(os.path.expanduser('~/.config/waypoint/scratch.sh'), 'w') as file:
			file.write('cd %s' % path)

if __name__=='__main__':
	waypoints = Waypoints()
	
	parser = ArgumentParser(description='Teleport around your shell.')
	subparsers = parser.add_subparsers()
	
	parser_add = subparsers.add_parser('add')
	parser_add.add_argument('name', default='default', nargs='?')
	parser_add.add_argument('section', default='DEFAULT', nargs='?')
	parser_add.set_defaults(func=waypoints.add)
	
	parser_goto = subparsers.add_parser('goto')
	parser_goto.add_argument('name', default='default', nargs='?')
	parser_goto.add_argument('section', default='DEFAULT', nargs='?')
	parser_goto.set_defaults(func=waypoints.goto)
	
	# Because I didn't want to pass an argparse.Namespace to the functions and
	# have to access everything through args.foo, we pull out the values as a
	# dictionary and splat 'em in.
	# (Shallow-)Copying the dict is necessary, since we want to avoid passing
	# the going-to-be-called function in as a parameter to itself.
	args = parser.parse_args().__dict__
	function = args['func']
	del args['func']
	function(**args)
