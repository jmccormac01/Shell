# script to make a directory 
# and go directly in

import os, sys

if len(sys.argv) != 2:
	print "\nUSAGE: mkdiri dir_name"
else:
	os.mkdir(sys.argv[1])
	os.chdir(sys.argv[1])

