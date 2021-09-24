import tornado.web
import tornado.ioloop
from firebase_handler import FirebaseFileHandler
import runner_v2
import asyncio
import json
import fileHandler
import os

class HandleRequest(tornado.web.RequestHandler):
	def set_default_headers(self):
		self.set_header("Content-Type", 'application/json')

	fbh = FirebaseFileHandler()

	fbh.printConfig()

	def get(self):
		fileName = self.get_argument("fileName")

		print("Downloading File {}".format(fileName))
		result = self.fbh.downloadFile(fileName)
		if result:
			print("File {} downloaded".format(fileName))
			##replacing newline characters
			fileHandler.replaceN(fileName)
			##starting compilations
			compile_result = runner_v2.compile(fileName)
			fileHandler.deleteFile(fileName)
			##fileHandler.deleteFile(fileName)
			self.write(json.dumps({"lines":compile_result}))
		else:
			self.write(json.dumps(["Failed to retrieve file..."]))

app = tornado.web.Application([(r"/", HandleRequest),])
port = int(os.environ.get("PORT", 5000))
print("starting on port:{}".format(port))
app.listen(port)
tornado.ioloop.IOLoop.current().start()
