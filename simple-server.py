#This is a simple server for the IT 566 key logger lab.
#THIS SERVER MUST BE RUNNING BEFORE THE STUDENTS START TO WORK ON THE LAB
#Once running, the server allows clients to connect to it and the clients will start
#capturing keystrokes and sending them to the server. Even though the server does not
#save any of the keystrokes in the long term, students should still be encouraged to
#treat the victim machine like any other victim machine. For example, they should not be typing in
#any of their personal information, since keystrokes are transmitted to this server
#unencrypted. REMEMBER: Give them these warnings without divulging that problem with the victim
#machine is that it has a keylogger on it.
import eventlet
import sys

def connection_handler(fd):
    print "client connected"
    while True:
        # pass through every non-eof line, but don't save any key information for privacy
        # any real key logging server would save the key log information
        x = fd.readline()
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
