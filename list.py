import os
import pyperclip

str = ""
result = []

paths = os.listdir("test/converted")
for path in paths:
  if path.find(".ts")<0:
    continue
  result.append(path)

result.sort(key= lambda x:int(x[:-3]))

final_path = ''.join(['converted/%s|'%path for path in result])

pyperclip.copy("concat:%s"%final_path)

