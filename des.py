# -*- coding: utf8 -*-
from Crypto.Cipher import AES
import os

key = open('key.key','r').read()


def deal_file(name):
  raw = open('ts/%s'%name, 'rb').read()
  iv = raw[0:16]
  data = raw[16:]

  aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
  open('test/converted/%s'%name, 'wb').write(aes.decrypt(data))

# os.remove("test/converted")
# os.removedirs("test/converted")

if not os.path.exists("test/converted"):
  os.mkdir("test/converted")

paths = os.listdir("ts")
for path in paths:
  if path.find('.ts')<0:
    continue
  # print(path)
  deal_file(path)
  # break
  print(path)
