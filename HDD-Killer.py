import random
import os
import string
import shutil
from psutil import virtual_memory

free = int(str(shutil.disk_usage("/")).split("free=")[1].split(")")[0])
print("Free: %s Gb" % (free/1000000000))
filesCreated = 0
sizeOnHDD = 0

while True:
  try:
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(15))
    with open(result_str + ".txt", 'w+') as bigfile:
      size = 262144000
      bigfile.write(random.choice(letters) * size)
      filesCreated = filesCreated + 1
      sizeOnHDD = sizeOnHDD + size
    print("File '" + result_str +"' has been created!")
    print("___ Created %s files ___ %s Gb used ___" % (filesCreated, sizeOnHDD/1000000000))
  except Exception as e:
    print("Cannot create any file anymore. Reason: %s" % e)
