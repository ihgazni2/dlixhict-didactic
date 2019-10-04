import efuntool.ebooltool as ebtl
import efuntool.efuntool as eftl
import elist.elist as elel
import itertools
import estring.estring as eses


def creat_apifix(s):
    arr = ebtl.combinate_all(s)
    arr = elel.mapv(arr,elel.join,[""])
    arr.reverse()
    arr.remove('')
    return(arr)


def creat_api_names(pre,verb,suf):
    params = creat_apifix(pre)
    rtrns = creat_apifix(suf)
    tl = list(itertools.product(params,rtrns))
    names = elel.mapv(tl,lambda ele:ele[0]+verb+ele[1])
    return(names)

def creat_empty_def(name):
    l0 = "def " + name +"():"
    l1 = "    rslt="
    l2 = "    return(rslt)"
    return(l0+"\n"+l1+"\n"+l2+"\n")

def creat_apis_via_names(api_names):
    arr = []
    for name in api_names:
        cd = creat_empty_def(name)
        print(cd)
        print("\n")
        arr.append(cd)
    return(arr)

def creat_apis_from_verb(pre,verb,suf):
    names = creat_api_names(pre,verb,suf)
    apis = creat_apis_via_names(names)
    return(apis)


def creat_apis_from_strblk(s):
    s = s.strip("\n").strip(" ").strip("\n").strip(" ")
    s = s.replace("\n\n","\n")
    s = s.replace("\n\n","\n")
    api_names = s.split("\n")
    return(creat_apis_via_names(api_names))



###

def qw(s,comma=',',quote='"'):
    l = s.split(comma)
    rslt = ''
    for i in range(0,l.__len__()):
        ele = l[i]
        nele = quote+ele+quote
        rslt = rslt + nele + comma
    rslt = eses.rstrip(rslt,comma,1)
    return(rslt)


def indent(code,*args,**kwargs):
    '''
    '''
    indent = eftl.optional_arg("    ",*args)
    indent = ("    "*indent) if(isinstance(indent,int)) else indent
    line_sp = '\n'
    lines = code.split(line_sp)
    ncode = ''
    length = lines.__len__()
    for i in range(0,length-1):
        line = indent + lines[i] + line_sp
        ncode = ncode + line
    ncode = ncode + indent + lines[length-1]
    return(ncode)



