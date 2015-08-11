# Contains main IRC module

import socket
from sys import argv

class Irc:
	"""
	Irc contains most methods needed for basic irc connections
	without sending.
	"""
	def __init__(self,server,port):
		"""
		Takes information from config in order to keep inforation private.
		"""
		self.server = server
		self.port = port
		self.sock = socket.socket()

	def connect(self, server, port):
		"""
		Basic connection, raises error exception if issue.
		"""
		try:
			self.sock.connect((server, port))
		except Exception as e:
			print "Error connecting:" + str(e)

	def join(self, password, username, channel):
		"""
		Joins channel and recieves raw data.
		"""
		self.connect(self.server,self.port)
		for param in [
			'PASS ' + password + '\r\n',
			'NICK ' + username + '\r\n',
			'USER ' + username + '\r\n',
			'JOIN #' + channel + '\r\n'
			]:
			try:
				self.sock.send(param)
			except Exception as e:
				print "Error joining:" + str(e)
		buf = ""
		while 1:
			recvd = self.sock.recv(4096)
			lines = recvd.split('\n')
			last = len(lines)
			last -= 1
			if not lines[last].count('\r'):
				buf = lines.pop()
			for line in lines:
				print line

			msg = line.split(':')
			if msg[0].count("PING"):
				self.sock.send("PONG :" + msg[1] + '\r\n')

