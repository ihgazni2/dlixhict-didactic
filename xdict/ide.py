import efuntool.ebooltool as ebtl
import elist.elist as elel
import itertools


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
    l1 = "    pass"
    return(l0+"\n"+l1)

def creat_apis_via_names(api_names):
    arr = []
    for name in api_names:
        cd = creat_empty_def(name)
        print(cd)
        arr.append(cd)
    return(arr)

def creat_apis(pre,verb,suf):
    names = creat_api_names(pre,verb,suf)
    apis = creat_apis_via_names(names)
    return(apis)


