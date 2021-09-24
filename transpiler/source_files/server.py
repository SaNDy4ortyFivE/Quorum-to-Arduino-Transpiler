import tornado.web
import tornado.ioloop
from firebase_handler import FirebaseFileHandler
from transpiler_beta_v2 import tester
import asyncio
import json
import fileHandler
import os
import sys

class HandleRequest(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')

    fbh = FirebaseFileHandler()

    ##fbh.printConfig()

    async def get(self):

        fileName = self.get_argument("fileName")

        print("Downloading File {}".format(fileName))
        result = await self.fbh.downloadFile(fileName)

        print("Result {}".format(result))
        sys.stdout.flush()

        arduino_code = json.dumps({"lines" : ["If you are seeing this line means there was some error during transpilation."]})

        if result:
            print("File {} downloaded".format(fileName))
            sys.stdout.flush()
            fileHandler.replaceN(fileName)
            ##transpiling
            print("Transpiling {}".format(fileName))
            sys.stdout.flush()
            try:
                arduino_code = await tester.startTranspiling("quorum_user_code/" + fileName)
                if(len(arduino_code) > 0):
                    print("Done transpiling of {}".format(fileName))
                    arduino_code = json.dumps({"lines" : arduino_code})
                    sys.stdout.flush()
                else:
                    print("An unexpected error occured in transpiling of {}".format(fileName))
                    json.dumps(["An unexpected error occured in transpiling of {}".format(fileName)])
                    sys.stdout.flush()
            except Exception as e:
                print(e)
            finally:
                fileHandler.deleteFile(fileName)
                self.write(arduino_code)

        else:
            self.write(json.dumps(["Failed to retrieve file..."]))


app = tornado.web.Application([(r"/", HandleRequest),])
port = int(os.environ.get("PORT", 5000))
print("starting on port:{}".format(port))
app.listen(port)
sys.stdout.flush()
tornado.ioloop.IOLoop.current().start()
