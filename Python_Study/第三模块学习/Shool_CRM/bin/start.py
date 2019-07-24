#-*- Coding:utf-8 -*-
# Author: D.Gray

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)
from core import core

if __name__ == '__main__':
    a = core.Conter()
    a.run()