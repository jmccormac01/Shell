#
# Python script to set terminal title
# Too many terminals open at times, can't keep track...
#

import os, sys

def title (name):
  	os.system("printf '\033]0;%s\007'" % (name))
	return 0
	
if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		print "usage: title name\n"
		sys.exit()
		
	title(sys.argv[1])
	
	