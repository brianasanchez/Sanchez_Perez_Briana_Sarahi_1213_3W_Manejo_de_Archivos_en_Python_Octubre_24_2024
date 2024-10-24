print(" ")

import os
if os.path.exists("papa.txt"):
  os.remove("papa.txt")
else:
  print("The file does not exist")

print(" ")