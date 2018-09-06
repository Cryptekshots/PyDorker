# /usr/bin/env python

#the most simple and fast dorker by @aggr3ssor
#modify and enjoy
#python version: 2.7

import os
import sys
import time

def main():
	banner()
	
	try:
		a  = raw_input("Enter Ur Prefix (i.e., \"INURL:\") File Location: ").replace('"',''); open(a).close()
		b = raw_input("Enter Ur KeyWord (i.e., \"Fortnite\") File Location: ").replace('"',''); open(b).close()
		c = raw_input("Enter Ur FileType (i.e., \".php?\") File Location: ").replace('"',''); open(c).close()
		d = raw_input("Enter Ur Parameter (i.e., \"id=\") File Location: ").replace('"',''); open(d).close()
		e = raw_input("Enter Ur Afterfix (i.e., \"Game\") File Location: ").replace('"',''); open(e).close()
	except:
		print "\nNo such file... exit"
		sys.exit()
		
	o = open(raw_input("\nNow Enter Ur  Output File Location: ").replace('"',''),"w")
	
	start = int(time.time())
	
	print "wait ..."
	
	af  = open(a)
	for prefix in af.read().split('\n'):
		bf = open(b)
		for keyword in bf.read().split('\n'):
			cf = open(c)
			for filetype in cf.read().split('\n'):
				df = open(d)
				for parameter in df.read().split('\n'):
					ef = open(e)
					for afterfix in ef.read().split('\n'):
						o.write(prefix + keyword + filetype + parameter +  " + \"" + afterfix + "\"\n")
					ef.close()
				df.close()
			cf.close()
		bf.close()
	af.close()
	
	print "\nFinished in %d seconds" % (int(time.time()) - start)
	
def banner():
	print r"""
	 ____           ____                   __         
	/\  _`\        /\  _`\                /\ \        
	\ \ \L\ \__  __\ \ \/\ \    ___   _ __\ \ \/'\    
	 \ \ ,__/\ \/\ \\ \ \ \ \  / __`\/\`'__\ \ , <    
	  \ \ \/\ \ \_\ \\ \ \_\ \/\ \L\ \ \ \/ \ \ \\`\  
	   \ \_\ \/`____ \\ \____/\ \____/\ \_\  \ \_\ \_\
	    \/_/  `/___/> \\/___/  \/___/  \/_/   \/_/\/_/
	             /\___/                               
	             \/__/    by @aggr3ssor & @kostrikov                        
"""

if __name__ == "__main__":
	main()