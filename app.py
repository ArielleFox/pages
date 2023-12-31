import sys
import os

if (sys.argv[1] == 'list'):
	os.system("cd ~/Applications/pages/ && ./montag")
	os.system("cd ~/Applications/pages/ && ./dienstag")
	os.system("cd ~/Applications/pages/ && ./mittwoch")
	os.system("cd ~/Applications/pages/ && ./donnerstag")
	os.system("cd ~/Applications/pages/ && ./freitag")
elif (sys.argv[1] == 'edit'):
	os.system("cd ~/Applications/pages/ && nano ./monday.txt")
	os.system("cd ~/Applications/pages/ && nano ./tuesday.txt")
	os.system("cd ~/Applications/pages/ && nano ./wednesday.txt")
	os.system("cd ~/Applications/pages/ && nano ./thursday.txt")
	os.system("cd ~/Applications/pages/ && nano ./friday.txt")
else:
	x = sys.argv[1]
	os.system(f"cd ~/Applications/pages/ && ./{x}")
