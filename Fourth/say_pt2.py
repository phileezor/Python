import sys
# "custom lib imported..."
from sayings import goodbye_yetagain

if len(sys.argv) == 2:
    goodbye_yetagain(sys.argv[1])