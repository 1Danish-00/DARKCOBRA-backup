import os 
import subprocess
os.system("git clone https://github.com/dark-cobra/DARKCOBRA darkcobra")
os.chdir("darkcobra")
os.system("pip install aria2p")
process = subprocess.Popen(
        ["python3", "-m", "userbot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    print(er.decode())
print("::::::::::::::")
if out:
    print(out.decode())
