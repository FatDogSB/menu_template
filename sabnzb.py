import os
import sys
import re
import glob
import shutil
import time
from datetime import datetime

BASE_PATH = 'D:\\temp\\SabNZB\\output'

# ========================================================================================================
class sabnzb:

    ABE_FOLDER = 'D:\\temp\\1\\agent\\alt.binaries.erotica'
    vid_ext = ('.avi', '.flv','.mpg', '.mp4', '.mkv', '.wmv')

    # ------------------------------------------------------------------------
    def __init__(self, base_path):
        self.base_path = base_path


    # ------------------------------------------------------------------------
    def normalize(self, aFileName):
        '''The Do Everything function. Take a file name and return a cleand up version'''
        name = 'fubar'



