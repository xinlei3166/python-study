#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import os

from pyinotify import WatchManager, Notifier, ProcessEvent, IN_DELETE, IN_CREATE, IN_MODIFY


class EventHandler(ProcessEvent):
	"""事件处理"""

	def process_IN_CREATE(self, event):
		print("Create file: % s" % os.path.join(event.path, event.name))

	def process_IN_DELETE(self, event):
		print("Deletefile: % s" % os.path.join(event.path, event.name))

	def process_IN_MODIFY(self, event):
		print("Modifyfile: % s" % os.path.join(event.path, event.name))


def FSMonitor(path):
	wm = WatchManager()

	mask = IN_DELETE | IN_CREATE | IN_MODIFY

	notifier = Notifier(wm, EventHandler())

	wm.add_watch(path, mask, auto_add=True, rec=True)

	print('now starting monitor % s' % (path))


	while True:

		try:
			notifier.process_events()

			if notifier.check_events():

				notifier.read_events()

		except KeyboardInterrupt:

			notifier.stop()

			break

if __name__ == "__main__":
	FSMonitor('/root')

