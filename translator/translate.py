# -*- coding: utf-8 -*-
from utils import *

import json
import sys

def main():
    if len(sys.argv) == 1:
        print("please enter your words")
        return
        
    if len(sys.argv) == 2:
        res = baidu_translate(sys.argv[1])
        print(res)
    else:
        str = " ".join(sys.argv[2:-1])
        res = baidu_translate(str)
        print(res)
    
if __name__ == "__main__":
    main()
