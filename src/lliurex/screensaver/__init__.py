
import os
import dbus
import sys
from codecs import open
from pathlib import Path

class InhibitScreensaver:

	def __init__(self):

			bus=dbus.SessionBus()
			proxy=bus.get_object("org.freedesktop.ScreenSaver","/ScreenSaver")
			self.iface = dbus.Interface(proxy,"org.freedesktop.ScreenSaver")
			self.cookie_path = os.path.join(str(Path.home()),'.inhibit_screensaver')
	def inHibit(self):

		self.unInhibit()
		cookie = self.iface.Inhibit("lliurex-up","Updating system...")
		with open(self.cookie_path,'w',encoding='utf-8') as fd:
			fd.write(str(cookie))

	#def inHibit

	def unInhibit(self):


		if os.path.exists(self.cookie_path):
			with open(self.cookie_path,'r',encoding='utf-8') as fd:
				cookie=fd.readline()
				self.iface.UnInhibit(int(cookie))
			os.remove(self.cookie_path)
	#def unInhibit


#class InhibitScreensaver
if __name__=="__main__":

	inhibit=InhibitScreensaver()			
