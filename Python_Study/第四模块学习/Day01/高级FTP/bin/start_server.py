#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import ftp_server
fs = ftp_server.Ftp_server()