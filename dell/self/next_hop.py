#!/usr/bin/python
from __future__ import print_function
import commands
<<<<<<< HEAD
import subprocess
=======
>>>>>>> 29ae95516994073d9e934b30fe3fa8cea49753fa
import re

prefix = raw_input("Please enter prefix: ")

out = commands.getoutput('hshell -c "l3 defip show" | grep ' + prefix)

next_hop = re.search('(100*.)',out)
print(next_hop.group(0))

single_next = commands.getoutput('hshell -c "l3 egress show "' + next_hop.group(0))
print(single_next)