from xdict import cmdline
from xdict.jprint import pobj
import sys
from efdir import fs
from xdict.utils import dict_getitem_via_path_list


obj = fs.rjson(sys.argv[1])
cmdt = cmdline.cmdict(dict=obj)

def main():
    try:
        match = sys.argv[2]
    except:
        pobj(obj)
    else:
        rslt=cmdt[match]
        try:
            seq = int(sys.argv[3])
        except:
            if(isinstance(rslt,tuple)):
                pass
            else:
                pobj(rslt)
        else:
            if(isinstance(rslt,tuple)):
                opts = rslt[1]
                pl = opts[seq][1]
                pobj(dict_getitem_via_path_list(obj,pl))
            else:
                pobj(rslt)


