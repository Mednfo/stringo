#!/usr/bin/env python
import hashlib
import string
import random
import sys
def stringen(a,b,c,d,e):
 while True:
   allchar  = string.ascii_letters + string.digits
   password = "".join(random.choice(allchar) for x in range(A))
   hashd  = hashlib.sha256(password.encode('UTF-8')).hexdigest()
   rhash  = hashlib.md5(hashd.encode('UTF-8')).hexdigest()
   vhash  = hashlib.sha1(hashd.encode('UTF-8')).hexdigest()
   shash  = hashlib.sha256(hashd.encode('UTF-8')).hexdigest()
   mhash  = hashlib.sha512(hashd.encode('UTF-8')).hexdigest()
   if hashd[:1] == a and rhash[:1] == b and vhash[:1] == c and shash[:1] == d and mhash[:1] == e:
        #Dhash = hashlib.sha512(password).hexdigest()
        print ('##########################################################')
        print (mhash[:21], password)
        print ('##########################################################')
        break

if __name__== "__main__":
    stringen(str(sys.argv[1]),str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]))
