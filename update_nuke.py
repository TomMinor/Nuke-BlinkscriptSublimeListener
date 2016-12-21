import sublime
import sublime_plugin
import urllib

class BlinkscriptSublime(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		if not (view.file_name().endswith(".rpp") or view.file_name().endswith(".h")):
			return
			
		post_data = view.file_name()
		try:
			urllib.request.urlopen("http://localhost:8000", data=post_data.encode() )
		except urllib.error.URLError as e:
			print(e)

		print("Updating Nuke blinkscripts, sending {0}".format(post_data))
