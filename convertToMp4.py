import os
import subprocess
import sys

procname = "ffmpeg"

src = "/home/data/dachuang/framework/vid_display"
dst = "/home/data/dachuang/framework/vid_display_mp4"

fileList = os.listdir(src)

for file in fileList:
    procArgs = procname + " -y -i " + os.path.join(src, file) + " -vf scale=iw:-2 " + os.path.join(dst, (file + ".mp4"))
    try:
        p = subprocess.Popen(procArgs, shell=True)
        p.wait()
    except Exception as e:
        print("failed {}".format(e))
