import pyrebase
import asyncio
import random
import os
import json
import sys
import traceback

class FirebaseFileHandler:

  config = {}

  firebase_instance = None
  storage_instance = None
  path_to_quorum = None
  path_to_arduino = None
  converted_file = None
  downloaded_file = None

  def __init__(self):
    try:
      print("setting config vars")
      ##self.setConfig()
      self.config = {
      "apiKey": os.environ.get("apiKey"),
      "authDomain": os.environ.get("authDomain"),
      "databaseURL": os.environ.get("databaseURL"),
      "storageBucket": os.environ.get("storageBucket"),
      "serviceAccount": "private_key/quorum-to-arduino-firebase-adminsdk-b9t7j-c5eacdc4cf.json"
      }

      print(self.config)
      sys.stdout.flush()

      ##firebase instance
      self.firebase_instance = pyrebase.initialize_app(self.config)
      ##firebase storage instance
      self.storage_instance = self.firebase_instance.storage()
      ##initialize file paths here
      ##path to arduino codes inside firebase
      self.path_to_arduino = "arduino_codes/"
      ##path to qorum codes inside firebase
      self.path_to_quorum = "quorum_codes/"
      ##path to arduino files which are successfully converted
      self.converted_file = "converted/"
      ##path to quorum files downloaded from firebase
      self.downloaded_file = "quorum_user_code/"
    except:
      pass
    else:
      pass
    finally:
      pass

  def printConfig(self):
      print(self.config)
      sys.stdout.flush()

  async def uploadFile(self, fileName):
    done = False
    try:
      ##append fileName to filePath for firebase
      firebase_file_path = self.path_to_arduino + fileName
      ##append fileName to filePath for local
      local_file_path = self.converted_file + fileName
      ##upload file
      self.storage_instance.child(firebase_file_path).put(local_file_path)
    except:
      done = False
    else:
      done = True
    finally:
      return done

  async def downloadFile(self, fileName):
    done = False
    print("downloading file {}".format(fileName))
    try:
      ##append fileName to filePath for firebase
      firebase_file_path = self.path_to_quorum + fileName
      print("firebase_file_path:{}".format(firebase_file_path))
      ##append fileName to filePath for local
      local_file_path = self.downloaded_file + fileName
      print("local_file_path:{}".format(local_file_path))

      self.storage_instance.child(firebase_file_path).download(local_file_path)
      print("{} downloaded".format(fileName))
    except:
        print("Error:{}".format(sys.exc_info()[0]))
        traceback.print_exc()
        done = False
    else:
        print("Complete...")
        done = True
    finally:
      sys.stdout.flush()
      return done
