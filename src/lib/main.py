import socket
from irc import Irc
from sys import argv
from config import config

def main():
	try:
		Irc(config['server'],config['port']).join(config['password'],config['username'],config['channel'])
	except Exception as e:
		print "Error: " + str(e)


if __name__ == "__main__":
	main()

