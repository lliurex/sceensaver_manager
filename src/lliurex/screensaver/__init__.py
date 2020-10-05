
import os
import dbus
import sys
import codecs

class InhibitScreensaver:

	def __init__(self,user):

			bus=dbus.SessionBus()
			self.base_cookie_path="/var/lib/lliurex/inhibit_screensaver"
			proxy=bus.get_object("org.freedesktop.ScreenSaver","/ScreenSaver")
			self.iface = dbus.Interface(proxy,"org.freedesktop.ScreenSaver")
			self.user = user
			self.cookie_path = os.path.join(self.base_cookie_path,user)
	def inHibit(self):

		self.unInhibit()
		cookie = self.iface.Inhibit("lliurex-up","Updating system...")
		with codecs.open(self.cookie_path,'w',encoding='utf-8') as fd:
			fd.write(str(cookie))

	#def inHibit

	def unInhibit(self):


		if os.path.exists(self.cookie_path):
			with codecs.open(self.cookie_path,'r',encoding='utf-8') as fd:
				cookie=fd.readline()
				self.iface.UnInhibit(int(cookie))
			os.remove(self.cookie_path)
	#def unInhibit


#class InhibitScreensaver
if __name__=="__main__":

	inhibit=InhibitScreensaver()			
