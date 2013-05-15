# -*- coding:utf-8 -*-
# Made by Kei Choi(hanul93@gmail.com)

import hashlib
import os

# Open a file
fp = open('eicar.txt', 'rb')
fbuf = fp.read()
fp.close()

# Create MD5 hash
md5 = hashlib.md5()
md5.update(fbuf)
fmd5 = md5.hexdigest()

# Detection of malware
if fmd5 == '44d88612fea8a8f36de82e1278abb02f' :
	print 'Found Virus & Repaired Virus'
	os.remove('eicar.txt') # Remove malware
else :
	print 'Not Found'