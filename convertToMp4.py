import os
import subprocess

procname = "ffmpeg"

src = ""
dst = ""

fileList = os.listdir(src)

for file in fileList:
    procArgs = procname + " -y -i " + os.path.join(src, file) + " -vf scale=iw:-2 " + os.path.join(dst, (file.split('.')[0] + ".mp4"))
    try:
        p = subprocess.Popen(procArgs, shell=True)
        p.wait()
    except Exception as e:
        print("failed {}".format(e))
