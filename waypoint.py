import os
import sys
try:
	from ConfigParser import SafeConfigParser
except ImportError:
	# renamed in py3k
	from configparser import SafeConfigParser

class Waypoints(object):
	def __init__(self):
		self.config = SafeConfigParser()
		self.configPath = os.path.expanduser('~/.config/waypoint/waypoint.config')
		self.config.read(self.configPath)
	
	def add(self, path, name='default', section='DEFAULT'):
		self.config.set(section, name, path)
		with open(self.configPath, 'w') as configFile:
			self.config.write(configFile)
	
	def goto(self, name='default', section='DEFAULT'):
		path = self.config.get(section, name)
		#os.chdir(path)
		with open(os.path.expanduser('~/.config/waypoint/scratch.sh'), 'w') as file:
			file.write('cd %s' % path)

if __name__=='__main__':
	waypoints = Waypoints()
	
	if sys.argv[1] == 'add':
		waypoints.add(os.getcwd())
	elif sys.argv[1] == 'goto':
		waypoints.goto()
