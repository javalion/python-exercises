# Access Environment Variable

import os

homePath = os.environ['HOME']
xyz = os.environ.get('xyz', None)


print("Home Path: " + homePath)
print("xyz: " + str(xyz))
