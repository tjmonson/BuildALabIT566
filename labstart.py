# Before students start on this lab, edit the host and port variables to point to where the
# simple-server.py is running.
# After editing the host and port, use pyinstaller to compile this script into an exe file.
# ------ pyinstaller --onefile --windowed --icon=exe.ico labstart.py
# The compiled exe will be in the dist folder and will be called labstart.exe.
# Distribute labstart.exe with the Windows XP virtual machine to the students.
# The students will copy labstart.exe to the virtual machine and double click it to start the lab.
# Instruct the students not to open labstart.exe in a file editor. This would give away much
# of the lab and would be cheating.
import os

conf_path="C:\WINDOWS\Help\wmconf"

#Edit the host and port variables to be the host and port of simple-server
host="128.187.81.220" #example: host="192.168.0.55"
port="9090" #example: port="9090"

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

    os.system("\"C:\WINDOWS\Help\svmost.exe local\"")

if __name__ == '__main__':
    main()
