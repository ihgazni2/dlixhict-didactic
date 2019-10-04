import sys
from xdict.ide import *
from efuntool.efuntool import dflt_sysargv

def main():
    s = dflt_sysargv(1,1)
    print(creat_apis_from_strblk(s))


