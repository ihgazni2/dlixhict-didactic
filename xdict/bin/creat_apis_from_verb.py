#import sys
from xdict.ide import *
from efuntool.efuntool import dflt_sysargv

#def dflt_sysargv(dflt,which):
#    try:
#        rslt = sys.argv[which]
#        print(which,rslt)
#    except:
#        rslt = dflt
#    else:
#        pass
#    return(rslt)


def main():
    pre = dflt_sysargv("",1)
    verb = dflt_sysargv("return",2)
    suf = dflt_sysargv("",3)
    print(sys.argv,pre,verb,suf)
    creat_apis_from_verb(pre,verb,suf)

