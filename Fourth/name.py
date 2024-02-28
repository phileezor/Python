import sys
# accessing sys.argv

"""
type python name.py in the terminal followed
by an input in this case the readers name, and it'll be added once the code runs
"""

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
"""elif len(sys.argv) > 2:
    sys.exit("Too many arguemnts")"""

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)


"""
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""


"""
i.e. python name.py ReadersName
Hello, my name is ReadersName
Note its argv[1], because argv[0] is the name of the python file
in this case name.py"""