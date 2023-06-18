import sys
import sys
import IPython as IPython

secret=str(sys.argv[1])
hash = IPython.lib.passwd(secret)
print(hash)