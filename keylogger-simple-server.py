
import eventlet
import sys

def connection_handler(fd):
    print "client connected"
    while True:
        # pass through every non-eof line, but don't save any key information for privacy
        # any real key logging server would save the key log information
        x = fd.read()
        if not x: break
    print "client disconnected"

def main():

    if len(sys.argv) != 2:
        print "Usage: You must include a port number.\nExample: python keylogger-simple-server.py <port>"
        exit(0)

    port = int(sys.argv[1])
    print "server socket listening on port", port
    server = eventlet.listen(('0.0.0.0', port))

    while True:
        try:
            new_sock, address = server.accept()
            print "accepted", address
            eventlet.spawn_n(connection_handler, new_sock.makefile('rw'))
        except (SystemExit, KeyboardInterrupt):
            break

if __name__ == '__main__':
    main()
