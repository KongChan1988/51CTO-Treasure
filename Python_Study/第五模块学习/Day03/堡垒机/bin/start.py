#-*-coding:utf-8 -*-
# Author: D.Gray
import os,sys
BASE_DESC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DESC)
sys.path.append(BASE_DESC)

from modules.actions import excute_from_command_line
excute_from_command_line(sys.argv)
