import os
import sys
import subprocess

exts = {'cpp': 0, 
        'c': 0, 
        'h': 0, 
        'hpp': 0}

def calc(file_name):
    out = subprocess.Popen(['wc', '-l', file_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
    return int(out.partition(b' ')[0]) + 1

rootdir = sys.argv[1]

if __name__ == '__main__':
    for folder, subs, files in os.walk(rootdir):
        for filename in files:
            ext = filename.split('.')[-1]
            if ext in exts:
                exts[ext] += calc(os.path.join(folder, filename))

    for key in exts:
        print("total {:6} lines of code with .{:6}".format(exts[key], key))