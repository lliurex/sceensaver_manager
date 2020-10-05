
import os
import dbus
import sys

COOKIE_PATH="/var/lib/lliurex/inhibit_screensaver"

class InhibitScreensaver:

	def __init__(self,args=None):

			bus=dbus.SessionBus()

			proxy=bus.get_object("org.freedesktop.ScreenSaver","/ScreenSaver")
			self.iface = dbus.Interface(proxy,"org.freedesktop.ScreenSaver")

	def inHibit(self):

		self.unInhibit()
		cookie = self.iface.Inhibit("lliurex-up","Updating system...")
		f=open(COOKIE_PATH,'w')
		f.write(str(cookie))
		f.close()

	#def inHibit

	def unInhibit(self):


		if os.path.exists(COOKIE_PATH):
			f=open(COOKIE_PATH,'r')
			cookie=f.readline()
			f.close()

			self.iface.UnInhibit(int(cookie))
			os.remove(COOKIE_PATH)
	#def unInhibit


#class InhibitScreensaver
if __name__=="__main__":

	inhibit=InhibitScreensaver()			
