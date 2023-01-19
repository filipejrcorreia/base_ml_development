import sys
import sys
import IPython as IPython

secret=sys.argv[0]
hash = IPython.lib.passwd(secret)
print(hash)