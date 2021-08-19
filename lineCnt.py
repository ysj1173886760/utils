import os
import sys
import subprocess

exts = ['cpp', 'c', 'h', 'hpp']

def calc(file_name):
    out = subprocess.Popen(['wc', '-l', file_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    return int(out.partition(b' ')[0]) + 1

rootdir = sys.argv[1]

if __name__ == '__main__':
    res = 0
    for folder, subs, files in os.walk(rootdir):
        for filename in files:
            if filename.split('.')[-1] in exts:
                res += calc(os.path.join(folder, filename))
    print("total {} lines", res)