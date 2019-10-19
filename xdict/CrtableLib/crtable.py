import ltdict.ltdict as ltdict
from xdict import utils
from xdict import jprint
import spaint.spaint as spaint
import re
import copy
from efdir import fs

#######################################

def nimd2arr(nimd):
    ltd = get_indexonly_refdict(nimd)
    arr = ltdict.ltdict2list(ltd)
    return(arr)

def get_cnl_from_crtable(crtable):
    animd = crtable['animd']
    return(nimd2arr(animd))

def get_knl_from_crtable(crtable):
    knimd = crtable['knimd']
    return(nimd2arr(knimd))

def get_vnl_from_crtable(crtable):
    vnimd = crtable['vnimd']
    return(nimd2arr(vnimd))

def creat_from_crtable(crtbl):
    cnl = get_cnl_from_crtable(crtbl)
    knl = get_knl_from_crtable(crtbl)
    table = crtbl['table']
    crtb = crtable(colnameslist = cnl,table=table,keynameslist = knl)
    return(crtb)



######################################




def is_name_index_mirror_dict(name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(animd)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> is_name_index_mirror_dict(animd)
        True
        >>> pobj(not_nimd)
        {
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> is_name_index_mirror_dict(not_nimd)
        the value = 0 is not in name_index_mirror_dict
        False
        >>> 
    '''
    for k in name_index_mirror_dict:
        v = name_index_mirror_dict[k]
        if(utils.is_int(k)):
            cond = utils.is_str(v)
            if(cond):
                if(v in name_index_mirror_dict):
                    cv = name_index_mirror_dict[v]
                    if(k==cv):
                        pass
                    else:
                        print('name_index_mirror_dict[{0}]=={1} , but name_index_mirror_dict[{1}]!={0}'.format(k,v))
                        return(False)
                else:
                    print("the value = {0} is not in name_index_mirror_dict".format(v))
                    return(False)
            else:
                print("when key={0} is int,the value = {1} is not string".format(k,v))
                return(False)
        elif(utils.is_str(k)):
            cond = utils.is_int(v)
            if(cond):
                if(v in name_index_mirror_dict):
                    cv = name_index_mirror_dict[v]
                    if(k==cv):
                        pass
                    else:
                        print('name_index_mirror_dict[{0}]=={1} , but name_index_mirror_dict[{1}]!={0}'.format(k,v))
                        return(False)
                else:
                    print("the value = {0} is not in name_index_mirror_dict".format(v))
                    return(False)
            else:
                print("when key={0} is string,the value = {1} is not int".format(k,v))
                return(False)
        else:
            print("key={0} is neither int nor string".format(k))
            return(False)
    return(True)

def creat_mirror_dict(refdict,**kwargs):
    '''
        >>> 
        >>> pobj(refdict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire'
        }
        >>> pobj(creat_mirror_dict(refdict))
        {
         0: 'size', 
         1: 'color', 
         'language': 2, 
         3: 'expire', 
         'size': 0, 
         2: 'language', 
         'color': 1, 
         'expire': 3
        }
        >>> 
        >>> 
        >>> pobj(ref_dict)
        {
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> pobj(creat_mirror_dict(refdict))
        {
         0: 'size', 
         1: 'color', 
         'language': 2, 
         3: 'expire', 
         'size': 0, 
         2: 'language', 
         'color': 1, 
         'expire': 3
        }
        >>> 
        >>> 
        >>> pobj(ref_dict)
        {
         1: 'color', 
         3: 'expire', 
         'size': 0, 
         'language': 2
        }
        >>> pobj(creat_mirror_dict(refdict))
        {
         0: 'size', 
         1: 'color', 
         'language': 2, 
         3: 'expire', 
         'size': 0, 
         2: 'language', 
         'color': 1, 
         'expire': 3
        }
        >>> 
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    crd = {}
    for k in refdict:
        v = refdict[k]
        if(utils.is_int(k)):
            if(utils.is_str(v)):
                crd[k] = v
            else:
                pass
        elif(utils.is_str(k)):
            if(utils.is_int(v)):
                crd[k] = v
            else:
                pass
        else:
            pass
    ncrd = {}
    for k in crd:
        v = crd[k]
        if(v in crd):
            vk = crd[v]
            if(vk == k):
                ncrd[k] = v
                ncrd[v] = k
            else:
                if(index_dominant):
                    if(utils.is_int(k)):
                        ncrd[v] = k
                    else:
                        ncrd[v] = vk
                else:
                    if(utils.is_int(k)):
                        ncrd[v] = vk
                    else:
                        ncrd[v] = k
        else:
            ncrd[v] = k 
            ncrd[k] = v
    return(ncrd)

def get_indexonly_refdict(refdict,**kwargs):
    '''
        >>> 
        >>> 
        >>> pobj(refdict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> pobj(get_indexonly_refdict(refdict))
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire'
        }
        >>> pobj(get_nameonly_refdict(refdict))
        {
         'language': 2, 
         'size': 0, 
         'color': 1, 
         'expire': 3
        }
        >>> 
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    cd = creat_mirror_dict(refdict,index_dominant=index_dominant)
    icd = {}
    for k in cd:
        if(utils.is_int(k)):
            icd[k] = cd[k]
        else:
            pass
    return(icd)

def get_nameonly_refdict(refdict,**kwargs):
    '''
        >>> 
        >>> 
        >>> pobj(refdict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> pobj(get_indexonly_refdict(refdict))
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire'
        }
        >>> pobj(get_nameonly_refdict(refdict))
        {
         'language': 2, 
         'size': 0, 
         'color': 1, 
         'expire': 3
        }
        >>> 
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    cd = creat_mirror_dict(refdict,index_dominant=index_dominant)
    ncd = {}
    for k in cd:
        if(utils.is_str(k)):
            ncd[k] = cd[k]
        else:
            pass
    return(ncd)

def get_mirror_dict_via_indexeslist(indexes_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> indexes_list = [0,2]
        >>> pobj(get_mirror_dict_via_indexeslist(indexes_list,attribs_name_index_mirror_dict))
        {
         0: 'size', 
         2: 'language', 
         'language': 2, 
         'size': 0
        }
        >>> 
        >>> 
    '''
    cd = {}
    for k in attribs_name_index_mirror_dict: 
        v = attribs_name_index_mirror_dict[k]
        if(ltdict.is_ltdict(indexes_list)):
            cond = ltdict.include(indexes_list,k)
        else:
            cond = (k in indexes_list)
        if(cond):
            if(utils.is_int(k)):
                cd[k] = v
                cd[v] = k
            else:
                pass
        else:
            pass
    return(cd)

def get_mirror_dict_via_nameslist(names_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> names_list = ['color','language']
        >>> pobj(get_mirror_dict_via_nameslist(names_list,attribs_name_index_mirror_dict))
        {
         1: 'color', 
         'language': 2, 
         2: 'language', 
         'color': 1
        }
        >>> 
        >>> 
    '''
    cd = {}
    for k in attribs_name_index_mirror_dict:
        v = attribs_name_index_mirror_dict[k]
        if(ltdict.is_ltdict(names_list)):
            cond = ltdict.include(names_list,k)
        else:
            cond = (k in names_list)
        if(cond):
            if(utils.is_str(k)):
                cd[k] = v
                cd[v] = k
            else:
                pass
        else:
            pass
    return(cd)

def get_the_other_mirror_dict_via_indexeslist(indexes_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> indexes_list
        [0, 2]
        >>> pobj(get_the_other_mirror_dict_via_indexeslist(indexes_list,attribs_name_index_mirror_dict))
        {
         1: 'color', 
         3: 'expire', 
         'expire': 3, 
         'color': 1
        }
        >>> 
    '''
    cd = {}
    for k in attribs_name_index_mirror_dict: 
        v = attribs_name_index_mirror_dict[k]
        if(ltdict.is_ltdict(indexes_list)):
            cond = ltdict.include(indexes_list,k)
        else:
            cond = (k in indexes_list)
        cond = not(cond)
        if(cond):
            if(utils.is_int(k)):
                cd[k] = v
                cd[v] = k
            else:
                pass
        else:
            pass
    return(cd)

def get_the_other_mirror_dict_via_nameslist(names_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> names_list
        ['color', 'language']
        >>> pobj(get_the_other_mirror_dict_via_nameslist(names_list,attribs_name_index_mirror_dict))
        {
         0: 'size', 
         3: 'expire', 
         'size': 0, 
         'expire': 3
        }
        >>> 
    '''
    cd = {}
    for k in attribs_name_index_mirror_dict:
        v = attribs_name_index_mirror_dict[k]
        if(ltdict.is_ltdict(names_list)):
            cond = ltdict.include(names_list,k)
        else:
            cond = (k in names_list)
        cond = not(cond)
        if(cond):
            if(utils.is_str(k)):
                cd[k] = v
                cd[v] = k
            else:
                pass
        else:
            pass
    return(cd)

def get_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> names_list
        ['color', 'language']
        >>> get_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict)
        [1, 2]
        >>> indexes_list
        [1, 2]
        >>> get_names_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)
        ['color', 'language']
        >>> 
    '''
    md = get_mirror_dict_via_nameslist(names_list,attribs_name_index_mirror_dict)
    rd = get_indexonly_refdict(md,index_dominant=1)
    indexes_list = sorted(list(rd.keys()))
    return(indexes_list)

def get_names_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> names_list
        ['color', 'language']
        >>> get_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict)
        [1, 2]
        >>> indexes_list
        [1, 2]
        >>> get_names_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)
        ['color', 'language']
        >>> 
    '''
    indexes_list = sorted(indexes_list)
    names_list = []
    for i in range(0,indexes_list.__len__()):
        names_list.append(attribs_name_index_mirror_dict[indexes_list[i]])
    return(names_list)

def get_the_other_indexes_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> indexes_list
        [0, 2]
        >>> get_the_other_indexes_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)
        [1, 3]
        >>> 
        
    '''
    ai_set = set({})
    for k in attribs_name_index_mirror_dict.keys():
        if(utils.is_int(k)):
            ai_set.add(k)
    i_set = set(indexes_list)
    the_other_set = ai_set - i_set
    return(sorted(list(the_other_set)))

def get_the_other_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> names_list
        ['color', 'language']
        >>> get_the_other_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict)
        [0, 3]
        >>> 
        >>> 
    '''
    an_set = set({})
    for k in attribs_name_index_mirror_dict.keys():
        if(utils.is_str(k)):
            an_set.add(k)
    n_set = set(names_list)
    the_other_set = an_set - n_set
    the_other_names_list = list(the_other_set)
    the_other_indexes_list = get_indexes_list_via_names_list(the_other_names_list,attribs_name_index_mirror_dict)
    return(the_other_indexes_list)

def get_the_other_names_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> indexes_list
        [1, 2]
        >>> get_the_other_names_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)
        ['size', 'expire']
        >>> 
    '''
    the_other_indexes_list = get_the_other_indexes_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)
    the_other_names_list = get_names_list_via_indexes_list(the_other_indexes_list,attribs_name_index_mirror_dict)
    return(the_other_names_list)

def get_the_other_names_list_via_names_list(names_list,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> names_list
        ['color', 'language']
        >>> get_the_other_names_list_via_names_list(names_list,attribs_name_index_mirror_dict)
        ['size', 'expire']
        >>> 
    '''
    the_other_indexes_list = get_the_other_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict)
    the_other_names_list = get_names_list_via_indexes_list(the_other_indexes_list,attribs_name_index_mirror_dict)
    return(the_other_names_list)

def naturalize_refdict(refdict,**kwargs):
    '''
        refdict = {
         0: 'size', 
         4: 'color', 
         7: 'language', 
         8: 'expire', 
         'size': 0, 
         'language': 7, 
         'color': 4, 
         'expire': 8
        }
        pobj(naturalize_refdict(refdict))
        {
         0: 'size', 
         1: 'color', 
         'language': 2, 
         3: 'expire', 
         'color': 1, 
         'expire': 3, 
         'size': 0, 
         2: 'language'
        }
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    refd = get_indexonly_refdict(refdict,index_dominant=index_dominant)
    nrefd = {}
    ks = sorted(list(refd.keys()))
    for i in range(0,ks.__len__()):
        nrefd[i] = refd[ks[i]]
    nrefd = creat_mirror_dict(nrefd,index_dominant=index_dominant)
    return(nrefd)



## attribs_keys_values

def nameattribs_to_indexattribs(attribs,attribs_name_index_mirror_dict):
    '''
        >>> nameattribs
        {'language': 'espanol', 'size': 500, 'color': 'green', 'expire': '2018-dec-01'}
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> 
        >>> nameattribs_to_indexattribs(nameattribs,attribs_name_index_mirror_dict)
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
    '''
    na = {}
    for k in attribs:
        value = attribs[k]
        if(utils.is_str(k)):
            key = attribs_name_index_mirror_dict[k]
            na[key] = value
        elif(utils.is_int(k)):
            na[k] = value
        else:
            pass
    return(na)

def indexattribs_to_nameattribs(attribs,attribs_name_index_mirror_dict):
    '''
        >>> table[0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> indexattribs
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> 
        >>> pobj(indexattribs_to_nameattribs(indexattribs,attribs_name_index_mirror_dict))
        {
         'language': 'espanol', 
         'size': 500, 
         'color': 'green', 
         'expire': '2018-dec-01'
        }
        >>> 
    '''
    na = {}
    for k in attribs:
        value = attribs[k]
        if(utils.is_int(k)):
            key = attribs_name_index_mirror_dict[k]
            na[key] = value
        elif(utils.is_str(k)):
            na[k] = value
        else:
            pass
    return(na)


def format_attribs_indexdominant(attribs,attribs_name_index_mirror_dict):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> pobj(attribs)
        {
         'language': 'japanese', 
         2: 'espanol', 
         'size': 500, 
         'color': 'green', 
         'expire': '2018-dec-01'
        }
        >>> pobj(format_attribs_indexdominant(attribs,attribs_name_index_mirror_dict))
        {
         'expire': '2018-dec-01', 
         'language': 'espanol', 
         2: 'espanol', 
         'color': 'green', 
         'size': 500
        }
        >>> 
        >>> 
        
    '''
    na = {}
    for k in attribs:
        v = attribs[k]
        if(utils.is_str(k)):
            mirror_k = attribs_name_index_mirror_dict[k]
            if(mirror_k in attribs):
                realv = attribs[mirror_k]
                na[k] = realv
            else:
                na[k] = v
        else:
            na[k] = v
    return(na)

format_keys_indexdominant = format_attribs_indexdominant
format_values_indexdominant = format_attribs_indexdominant


def format_attribs_namedominant(attribs,attribs_name_index_mirror_dict):
    '''
    >>> 
    >>> pobj(attribs_name_index_mirror_dict)
    {
     0: 'size', 
     1: 'color', 
     2: 'language', 
     3: 'expire', 
     'size': 0, 
     'language': 2, 
     'color': 1, 
     'expire': 3
    }
    >>> pobj(attribs)
    {
     'language': 'japanese', 
     2: 'espanol', 
     'size': 500, 
     'color': 'green', 
     'expire': '2018-dec-01'
    }
    >>> pobj(format_attribs_namedominant(attribs,attribs_name_index_mirror_dict))
    {
     'expire': '2018-dec-01', 
     'language': 'japanese', 
     2: 'japanese', 
     'color': 'green', 
     'size': 500
    }
    >>> 

    '''
    na = {}
    for k in attribs:
        v = attribs[k]
        if(utils.is_int(k)):
            mirror_k = attribs_name_index_mirror_dict[k]
            if(mirror_k in attribs):
                realv = attribs[mirror_k]
                na[k] = realv
            else:
                na[k] = v
        else:
            na[k] = v
    return(na)

format_keys_namedominant = format_attribs_namedominant
format_values_namedominant = format_attribs_namedominant



def format_attribs_to_indexkeyonly(attribs,attribs_name_index_mirror_dict,**kwargs):
    '''
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> pobj(attribs)
        {
         'language': 'japanese', 
         2: 'espanol', 
         'size': 500, 
         'color': 'green', 
         'expire': '2018-dec-01'
        }
        >>> pobj(format_attribs_to_indexkeyonly(attribs,attribs_name_index_mirror_dict,index_dominant=1))
        {
         0: 500, 
         1: 'green', 
         2: 'espanol', 
         3: '2018-dec-01'
        }
        >>> pobj(format_attribs_to_indexkeyonly(attribs,attribs_name_index_mirror_dict,index_dominant=0))
        {
         0: 500, 
         1: 'green', 
         2: 'japanese', 
         3: '2018-dec-01'
        }
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    if(index_dominant):
        na = format_attribs_indexdominant(attribs,attribs_name_index_mirror_dict)
    else:
        na = format_attribs_namedominant(attribs,attribs_name_index_mirror_dict)
    nna = {}
    for key in na:
        if(utils.is_str(key)):
            nk = attribs_name_index_mirror_dict[key]
            nna[nk] = na[key]
        else:
            nna[key] = na[key]
    return(nna)

format_keys_to_indexkeyonly = format_attribs_to_indexkeyonly
format_values_to_indexkeyonly = format_attribs_to_indexkeyonly

def format_attribs_to_namekeyonly(attribs,attribs_name_index_mirror_dict,**kwargs):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> pobj(attribs)
        {
         'language': 'japanese', 
         2: 'espanol', 
         'size': 500, 
         'color': 'green', 
         'expire': '2018-dec-01'
        }
        >>> pobj(format_attribs_to_namekeyonly(attribs,attribs_name_index_mirror_dict,index_dominant=1))
        {
         'language': 'espanol', 
         'expire': '2018-dec-01', 
         'color': 'green', 
         'size': 500
        }
        >>> pobj(format_attribs_to_namekeyonly(attribs,attribs_name_index_mirror_dict,index_dominant=0))
        {
         'language': 'japanese', 
         'expire': '2018-dec-01', 
         'color': 'green', 
         'size': 500
        }
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    if(index_dominant):
        na = format_attribs_indexdominant(attribs,attribs_name_index_mirror_dict)
    else:
        na = format_attribs_namedominant(attribs,attribs_name_index_mirror_dict)
    nna = {}
    for key in na:
        if(utils.is_int(key)):
            nk = attribs_name_index_mirror_dict[key]
            nna[nk] = na[key]
        else:
            nna[key] = na[key]
    return(nna)


format_keys_to_namekeyonly = format_attribs_to_namekeyonly
format_values_to_namekeyonly = format_attribs_to_namekeyonly

def indextable_to_nametable(indextable,attribs_name_index_mirror_dict):
    '''
    '''
    nt = {}
    for seq in indextable:
        nt[seq] = indexattribs_to_nameattribs(indextable[seq],attribs_name_index_mirror_dict)
    return(nt)

def nametable_to_indextable(nametable,attribs_name_index_mirror_dict):
    '''
    '''
    nt = {}
    for seq in nametable:
        nt[seq] = nameattribs_to_indexattribs(nametable[seq],attribs_name_index_mirror_dict)
    return(nt)




## basic select 
def get_seqslist_via_attribs(attribs,crtable):
    '''
        >>> 
        >>> crtable.keys()
        dict_keys(['table', 'animd'])
        >>> pobj(crtable['animd'])
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5] 
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> attribs = {'size': 500, 'language': 'english', 'color': 'green', 'expire': '2017-oct-01'}
        >>> get_seqslist_via_attribs(attribs,crtable)
        [4, 5]
        >>> 
    '''
    attribs_name_index_mirror_dict = crtable['animd']
    na = format_attribs_to_indexkeyonly(attribs,attribs_name_index_mirror_dict)
    seqslist = []
    for seq in crtable['table']:
        if(na == crtable['table'][seq]):
            seqslist.append(seq)
    return(seqslist)

def get_seqslist_via_keys(keys,crtable):
    '''
        >>> crtable.keys()
        dict_keys(['table', 'animd'])
        >>> pobj(crtable['animd'])
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5] 
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        keys = {'language': 'english','color': 'blue'}
        >>> get_seqslist_via_keys(keys,crtable)
        [3]
        >>> 
    '''
    attribs_name_index_mirror_dict = crtable['animd']
    nks = format_keys_to_indexkeyonly(keys,attribs_name_index_mirror_dict)
    seqslist = []
    for seq in crtable['table']:
        attrib = crtable['table'][seq]
        cond = 1
        for index in nks:
            if(index in attrib):
                if(nks[index] == attrib[index]):
                    pass
                else:
                    cond = 0
                    break
            else:
                cond = 0
                break
        if(cond):
            seqslist.append(seq)
        else:
            pass
    return(seqslist)

get_seqslist_via_values = get_seqslist_via_keys

def get_values_in_attribs(keys,attribs,attribs_name_index_mirror_dict,**kwargs):
    '''
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> keys
        {'language': 'english', 'color': 'blue'}
        >>> attribs
        {'language': 'english', 'size': 500, 'color': 'green', 'expire': '2017-oct-01'}
        >>> 
        >>> get_values_in_attribs(keys,attribs,attribs_name_index_mirror_dict)
        {0: 500, 3: '2017-oct-01'}
        >>> get_values_in_attribs(keys,attribs,attribs_name_index_mirror_dict,index_key=0)
        {'size': 500, 'expire': '2017-oct-01'}
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    if('index_key' in kwargs):
        index_key = kwargs['index_key']
    else:
        index_key = 0
    nks = format_keys_to_indexkeyonly(keys,attribs_name_index_mirror_dict,index_dominant=index_dominant)
    nas = format_attribs_to_indexkeyonly(attribs,attribs_name_index_mirror_dict,index_dominant=index_dominant)
    values = {}
    for ak in nas:
        if(ak in nks):
            pass
        else:
            values[ak] = nas[ak]
    if(index_key):
        pass
    else:
        values = format_values_to_namekeyonly(values,attribs_name_index_mirror_dict,index_dominant=index_dominant)
    return(values)

get_keys_in_attribs = get_values_in_attribs

def get_valueslist_via_keys(keys,crtable,**kwargs):
    '''
        >>> 
        >>> crtable.keys()
        dict_keys(['table', 'animd'])
        >>> pobj(crtable['animd'])
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> keys = {'color':'green'}
        >>> valueslist = get_valueslist_via_keys(keys,crtable)
        >>> pobj(valueslist)
        [
         {
          'language': 'espanol', 
          'size': 500, 
          'expire': '2018-dec-01'
         }, 
         {
          'language': 'chinese', 
          'size': 74, 
          'expire': '2017-oct-01'
         }, 
         {
          'language': 'spanish', 
          'size': 300, 
          'expire': '2017-oct-01'
         }, 
         {
          'language': 'english', 
          'size': 100000, 
          'expire': '2018-dec-01'
         }
        ]
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    if('index_key' in kwargs):
        index_key = kwargs['index_key']
    else:
        index_key = 0
    valueslist = []
    seqslist = get_seqslist_via_keys(keys,crtable)
    for i in range(0,seqslist.__len__()):
        attribs = crtable['table'][i]
        values = get_values_in_attribs(keys,attribs,crtable['animd'],index_dominant=index_dominant,index_key=index_key)
        valueslist.append(values)
    return(valueslist)

get_keyslist_via_values = get_valueslist_via_keys

def get_column_via_attribindex(index,crtable):
    '''
        >>> 
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> column = get_column_via_attribindex(0,crtable)
        >>> pobj(column)
        {
         0: 500, 
         1: 74, 
         2: 300, 
         3: 100000, 
         4: 500, 
         5: 500
        }
        >>> 
        >>> 
    '''
    column = {}
    for seq in crtable['table']:
        attribs = crtable['table'][seq]
        cv = attribs[index]
        column[seq] = cv
    return(column)

def get_column_via_attribname(name,crtable):
    '''
        >>> 
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> pobj(get_column_via_attribindex(0,crtable))
        {
         0: 500, 
         1: 74, 
         2: 300, 
         3: 100000, 
         4: 500, 
         5: 500
        }
        >>> pobj(get_column_via_attribname('size',crtable))
        {
         0: 500, 
         1: 74, 
         2: 300, 
         3: 100000, 
         4: 500, 
         5: 500
        }
        >>> 
    '''
    index = crtable['animd'][name]
    return(get_column_via_attribindex(index,crtable))

def get_attribslist_of_column_via_attribindex(index,crtable):
    '''
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> pobj(get_attribslist_of_column_via_attribindex(0,crtable))
        [
         500, 
         74, 
         300, 
         100000, 
         500, 
         500
        ]
        >>> 
    '''
    column = get_column_via_attribindex(index,crtable)
    attribslist = []
    for seq in column:
        attribslist.append(column[seq])
    return(attribslist)

def get_attribslist_of_column_via_attribname(name,crtable):
    '''
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> pobj(get_attribslist_of_column_via_attribname('size',crtable))
        [
         500, 
         74, 
         300, 
         100000, 
         500, 
         500
        ]
        >>> 
    '''
    column = get_column_via_attribname(name,crtable)
    attribslist = []
    for seq in column:
        attribslist.append(column[seq])
    return(attribslist)

def get_seqslist_of_column_via_attribindex(index,crtable):
    '''
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> pobj(get_seqslist_of_column_via_attribindex(0,crtable))
        [
         0, 
         1, 
         2, 
         3, 
         4, 
         5
        ]
        >>> pobj(get_seqslist_of_column_via_attribname('size',crtable))
        [
         0, 
         1, 
         2, 
         3, 
         4, 
         5
        ]
        >>> 
    '''
    column = get_column_via_attribindex(index,crtable)
    seqslist = []
    for seq in column:
        seqslist.append(seq)
    return(seqslist)

def get_seqslist_of_column_via_attribname(name,crtable):
    '''
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> pobj(get_seqslist_of_column_via_attribindex(0,crtable))
        [
         0, 
         1, 
         2, 
         3, 
         4, 
         5
        ]
        >>> pobj(get_seqslist_of_column_via_attribname('size',crtable))
        [
         0, 
         1, 
         2, 
         3, 
         4, 
         5
        ]
        >>> 
    '''
    column = get_column_via_attribname(name,crtable)
    seqslist = []
    for seq in column:
        seqslist.append(seq)
    return(seqslist)

def get_domainset_of_column_via_attribindex(index,crtable):
    '''
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> get_domainset_of_column_via_attribindex(0,crtable)
        {100000, 74, 500, 300}
        >>> get_domainset_of_column_via_attribname('size',crtable)
        {100000, 74, 500, 300}
        >>> 
        >>> 
    '''
    column = get_column_via_attribindex(index,crtable)
    domainset = set({})
    for seq in column:
        domainset.add(column[seq])
    return(domainset)

def get_domainset_of_column_via_attribname(name,crtable):
    '''
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
        >>> get_domainset_of_column_via_attribindex(0,crtable)
        {100000, 74, 500, 300}
        >>> get_domainset_of_column_via_attribname('size',crtable)
        {100000, 74, 500, 300}
        >>> 
        >>> 
    '''
    column = get_column_via_attribname(name,crtable)
    domainset = set({})
    for seq in column:
        domainset.add(column[seq])
    return(domainset)


## creat,init,append,prepend,del,modify,insert
def creat_empty_crtable(column_name_dict,**kwargs):
    '''
        column_name_dict = {0: 'size', 1: 'color', 2: 'language', 3: 'expire'}
        keys_nameslist = ['language', 'expire']
        >>> db = creat_empty_crtable(column_name_dict,keys_nameslist=keys_nameslist)
        >>> pobj(db)
        {
         'table': 
                  {}, 
         'vnimd': 
                  {
                   0: 'size', 
                   1: 'color', 
                   'size': 0, 
                   'color': 1
                  }, 
         'knimd': 
                  {
                   'language': 2, 
                   3: 'expire', 
                   2: 'language', 
                   '
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    name_index_mirror_dict = creat_mirror_dict(column_name_dict,index_dominant = index_dominant)
    crtable = {}
    crtable['animd'] = name_index_mirror_dict
    crtable['table'] = {}
    if('keys_nameslist' in kwargs):
        keys_nameslist = kwargs['keys_nameslist']
        crtable['knimd'] = get_mirror_dict_via_nameslist(keys_nameslist,crtable['animd'])
        crtable['vnimd'] = get_the_other_mirror_dict_via_nameslist(keys_nameslist,crtable['animd'])
    else:
        pass
    return(crtable)

def expand_part_attribs(attribs,attribs_name_index_mirror_dict,**kwargs):
    '''
        >>> 
        >>> pobj(attribs_name_index_mirror_dict)
        {
         0: 'size', 
         1: 'color', 
         2: 'language', 
         3: 'expire', 
         'size': 0, 
         'language': 2, 
         'color': 1, 
         'expire': 3
        }
        >>> attribs = {0: 500, 1: 'green'}
        >>> expand_part_attribs(attribs,attribs_name_index_mirror_dict,index_dominant=1)
        {0: 500, 1: 'green', 2: None, 3: None}
        >>> attribs = {'size': 500, 'color': 'green'}
        >>> expand_part_attribs(attribs,attribs_name_index_mirror_dict,index_dominant=0)
        {'language': None, 'size': 500, 'color': 'green', 'expire': None}
        >>> 
        >>> 
    '''
    if('index_dominant' in kwargs):
        index_dominant = kwargs['index_dominant']
    else:
        index_dominant = 1
    na = copy.deepcopy(attribs)
    if(index_dominant):
        for k in attribs_name_index_mirror_dict:
            if(utils.is_int(k)):
                if(k in attribs):
                    pass
                else:
                    na[k] = None
            else:
                pass
    else:
        for k in attribs_name_index_mirror_dict:
            if(utils.is_str(k)):
                if(k in attribs):
                    pass
                else:
                    na[k] = None
            else:
                pass
    return(na)

def append_row(row,crtable):
    '''
        >>> 
        >>> 
            crtable = {}
            crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
            crtable['table'] = {}
            crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
            crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
            crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
            crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
            row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
            crtable = append_row(row,crtable)
            crtable['table'].keys()
            crtable['table'][4]
            >>> crtable['table'].keys()
            dict_keys([0, 1, 2, 3, 4])
            >>> crtable['table'][4]
            {0: 700, 1: 'pink', 2: 'espanol', 3: None}
            >>> 
        >>> 
        >>> 
    '''
    if(isinstance(row,list)):
        cnl = ltdict.to_list(get_indexonly_refdict(crtable['animd']))
        #kvlist2d
        d = {}
        for i in range(0,cnl.__len__()):
            k = cnl[i]
            v = row[i]
            d[k] = v
        row = d
    else:
        pass
    row = format_attribs_to_indexkeyonly(row,crtable['animd'],index_dominant=1)
    seqs = list(crtable['table'].keys())
    if(seqs.__len__() == 0):
        nxt = 0
    else:
        nxt = max(seqs) + 1
    crtable['table'][nxt] = expand_part_attribs(row,crtable['animd'],index_dominant=1)
    return(crtable)

#####

def append_row_with_array(crtb,arr):
    cnl = crtb.colnameslist
    d = eded.kvlist2d(cnl,arr)
    crtb.append_row(d)
    return(crtb)


#####





def append_col(col,crtable):
    '''
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        col = {'owner':['dli','dli','dli','dli']}
        crtable = append_col(col,crtable)
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['animd'][4]
        'owner'
        >>> crtable['animd']['owner']
        4
        >>> 
    '''
    col_should_len = crtable['table'].__len__()
    col_name = list(col.keys())[0]
    col_list = col[col_name]
    for i in range(col_list.__len__(),col_should_len):
        col_list.append(None)
    col_nums = list(get_indexonly_refdict(crtable['animd']).keys())
    next = max(col_nums) + 1
    crtable['animd'][next] = col_name
    crtable['animd'][col_name] = next
    if('vnimd' in crtable):
        crtable['vnimd'][next] = col_name
        crtable['vnimd'][col_name] = next
    else:
        pass
    for k in crtable['table']:
        crtable['table'][k][next] = col_list[k]
    return(crtable)

def append_rows(rows,crtable):
    '''
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
                {'size': 555, 'color': 'yellow', 'language': 'korean'}]
    >>> crtable['table'].keys()
    dict_keys([0, 1, 2, 3])
    >>> crtable = append_rows(rows,crtable)
    >>> crtable['table'].keys()
    dict_keys([0, 1, 2, 3, 4, 5])
    >>> crtable['table'][4]
    {0: 555, 1: 'yellow', 2: 'chinese', 3: None, 4: None}
    >>> crtable['table'][5]
    {0: 555, 1: 'yellow', 2: 'korean', 3: None, 4: None}
    >>> 
    '''
    for row in rows:
        append_row(row,crtable)
    return(crtable)

def append_cols(cols,crtable):
    '''  
        crtable = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        cols = [{'id':['2271','2272','2273','2274']},
                {'tid':['t1','t2','t3','t4']}]
        crtable = append_cols(cols,crtable)
        crtable['table'][0]
        crtable['table'][1]
        crtable['table'][2]
        crtable['table'][3]
        crtable['animd']
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01', 4: '2271', 5: 't1'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01', 4: '2272', 5: 't2'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01', 4: '2273', 5: 't3'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01', 4: '2274', 5: 't4'}
        >>> crtable['animd']
        {0: 'size', 1: 'color', 2: 'language', 3: 'expire', 4: 'id', 'size': 0, 'color': 1, 'language': 2, 'id': 4, 'tid': 5, 'expire': 3, 5: 'tid'}
        >>> 
    '''
    for col in cols:
        append_col(col,crtable)
    return(crtable)

def prepend_row(row,crtable):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
        crtable = prepend_row(row,crtable)
        >>> crtable.keys()
        dict_keys(['table', 'animd'])
        >>> crtable['table'].keys()
        dict_keys([0, 1, 2, 3, 4])
        >>> crtable['table'][4]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> 
    '''
    nrow = format_attribs_to_indexkeyonly(row,crtable['animd'],index_dominant=1)
    nrow = expand_part_attribs(nrow,crtable['animd'],index_dominant=1)
    crtable['table'] = ltdict.prepend(crtable['table'],nrow)
    return(crtable)

def prepend_col(col,crtable):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        col = {'owner':['dli','dli','dli','dli']}
        >>> crtable = prepend_col(col,crtable)
        >>> crtable['table'][0] 
        {0: 'dli', 1: 500, 2: 'green', 3: 'espanol', 4: '2018-dec-01'}
        >>> crtable['table'][1] 
        {0: 'dli', 1: 74, 2: 'green', 3: 'chinese', 4: '2017-oct-01'}
        >>> crtable['table'][2] 
        {0: 'dli', 1: 300, 2: 'darkblack', 3: 'spanish', 4: '2017-oct-01'}
        >>> crtable['table'][3] 
        {0: 'dli', 1: 100000, 2: 'blue', 3: 'english', 4: '2018-dec-01'}
        >>> pobj(crtable['animd'])
        {
         0: 'owner', 
         1: 'size', 
         2: 'color', 
         3: 'language', 
         4: 'expire', 
         'size': 1, 
         'owner': 0, 
         'language': 3, 
         'color': 2, 
         'expire': 4
        }
    '''
    refd = get_indexonly_refdict(crtable['animd'])
    nrefd = {}
    for k in refd:
        nrefd[k+1] = refd[k]
    crtable['animd'] = creat_mirror_dict(nrefd)
    col_name = list(col.keys())[0]
    col_list = col[col_name]
    crtable['animd'][0] = col_name
    crtable['animd'][col_name] = 0
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        crtable['table'][rownum] = ltdict.prepend(row,col_list[rownum])
    return(crtable)

def prepend_rows(rows,crtable):
    '''
        crtable = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
                {'size': 555, 'color': 'yellow', 'language': 'korean'}]
        crtable = prepend_rows(rows,crtable)
        >>> crtable['table'][0]
        {0: 555, 1: 'yellow', 2: 'chinese', 3: None}
        >>> crtable['table'][1]
        {0: 555, 1: 'yellow', 2: 'korean', 3: None}
        >>> crtable['table'][2]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][3]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][4]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][5]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][6]
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        KeyError: 6
        >>> 
    '''
    rows = ltdict.list2ltdict(rows)
    for k in rows:
        row = rows[k]
        row = nameattribs_to_indexattribs(row,crtable['animd'])
        row = expand_part_attribs(row,crtable['animd'])
        rows[k] = row 
    crtable['table'] = ltdict.prextend(crtable['table'],rows,deepcopy_1=1,deepcopy_2=1)
    return(crtable)

def prepend_cols(cols,crtable):
    '''
        >>> crtable = {}
        >>> crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        >>> crtable['table'] = {}
        >>> crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> cols = [{'id':['2271','2272','2273','2274']},
        ...         {'tid':['t1','t2','t3','t4']}]
        >>> crtable = prepend_cols(cols,crtable)
        >>> crtable['table'][0]
        {0: '2271', 1: 't1', 2: 500, 3: 'green', 4: 'espanol', 5: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: '2272', 1: 't2', 2: 74, 3: 'green', 4: 'chinese', 5: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: '2273', 1: 't3', 2: 300, 3: 'darkblack', 4: 'spanish', 5: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: '2274', 1: 't4', 2: 100000, 3: 'blue', 4: 'english', 5: '2018-dec-01'}
        >>> pobj(crtable['animd'])
        {
         0: 'id', 
         1: 'tid', 
         2: 'size', 
         3: 'color', 
         'tid': 1, 
         'size': 2, 
         'color': 3, 
         'language': 4, 
         'id': 0, 
         4: 'language', 
         'expire': 5, 
         5: 'expire'
        }
        >>> 
    '''
    for i in range(cols.__len__()-1,-1,-1):
        col = cols[i]
        crtable = prepend_col(col,crtable)
    return(crtable)

def del_col_via_colnum(colnum,crtable,**kwargs):
    '''
        crtable = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        crtable = del_col_via_colnum(2,crtable)
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: '2018-dec-01'}
        >>> pobj(crtable['animd'])
        {
         0: 'size', 
         1: 'color', 
         2: 'expire'
        }
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    col_name = crtable['animd'][colnum]
    if(reorder):
        crtable = naturalize_crtable(crtable)
        crtable['animd'] = get_indexonly_refdict(crtable['animd'])
        ltdict.pop(crtable['animd'],colnum)
        try:
            del crtable['knimd'][colnum]
        except:
            pass
        else:
            pass
        try:
            del crtable['knimd'][col_name]
        except:
            pass
        else:
            pass
        try:
            del crtable['vnimd'][colnum]
        except:
            pass
        else:
            pass
        try:
            del crtable['vnimd'][col_name]
        except:
            pass
        else:
            pass
    else:
        del crtable['animd'][colnum]
        del crtable['animd'][col_name]
        try:
            del crtable['knimd'][colnum]
        except:
            pass
        else:
            pass
        try:
            del crtable['knimd'][col_name]
        except:
            pass
        else:
            pass
        try:
            del crtable['vnimd'][colnum]
        except:
            pass
        else:
            pass
        try:
            del crtable['vnimd'][col_name]
        except:
            pass
        else:
            pass
    #
    krefd = get_indexonly_refdict(crtable['knimd'])
    vrefd = get_indexonly_refdict(crtable['vnimd'])
    nkrefd = {}
    nvrefd = {}
    for index in krefd:
        if(index >= colnum):
            nkrefd[index-1] = krefd[index]
        else:
            nkrefd[index] = krefd[index]
    for index in vrefd:
        if(index in krefd):
            pass
        else:
            if(index >= colnum):
                nvrefd[index-1] = vrefd[index]
            else:
                nvrefd[index] = vrefd[index]
    crtable['knimd'] = creat_mirror_dict(nkrefd)
    crtable['vnimd'] = creat_mirror_dict(nvrefd)
    #
    for seq in crtable['table']:
        if(reorder):
            
            ltdict.pop(crtable['table'][seq],colnum)
        else:
            del crtable['table'][seq][colnum]
    return(crtable)

def del_cols_via_colnumslist(colnumslist,crtable,**kwargs):
    '''
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    seq = 0
    for colnum in colnumslist:
        colnum = colnum - seq
        del_col_via_colnum(colnum,crtable,reorder=reorder)
        seq = seq + 1
    return(crtable)

def del_col_via_colname(colname,crtable,**kwargs):
    '''
        crtable = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        crtable = del_col_via_colname('color',crtable)
        >>> crtable['table'][0]
        {0: 500, 1: 'espanol', 2: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'chinese', 2: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'spanish', 2: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'english', 2: '2018-dec-01'}
        >>> pobj(crtable['animd'])
        {
         0: 'size', 
         1: 'language', 
         2: 'expire'
        }
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    colnum = crtable['animd'][colname]
    crtable = del_col_via_colnum(colnum,crtable,reorder=reorder)
    return(crtable)

def del_cols_via_colnameslist(colnameslist,crtable,**kwargs):
    '''
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    colnumslist = get_indexes_list_via_names_list(colnameslist,crtable['animd'])
    return(del_cols_via_colnumslist(colnumslist,crtable,reorder=reorder))

def del_rows_via_attribs(attribs,crtable,**kwargs):
    '''
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    seqslist = get_seqslist_via_attribs(attribs,crtable)
    if(reorder):
        crtable = naturalize_crtable(crtable)
        seqslist = get_seqslist_via_keys(keys,crtable)
        ltdict.pop_seqs(crtable['table'],set(seqslist))
    else:
        del crtable['table'][seq]
    return(crtable)

def del_rows_via_keys(keys,crtable,**kwargs):
    '''
        crtable = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        keys = {'color':'green'}
        >>> crtable = del_rows_via_keys(keys,crtable)
        >>> crtable['table'][0] 
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][1] 
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'].keys()
        dict_keys([0, 1])
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    seqslist = get_seqslist_via_keys(keys,crtable)
    if(reorder):
        crtable = naturalize_crtable(crtable)
        seqslist = get_seqslist_via_keys(keys,crtable)
        ltdict.pop_seqs(crtable['table'],set(seqslist))
    else:
        del crtable['table'][seq]
    return(crtable)

del_rows_via_values = del_rows_via_keys

def modify_rows_via_seq(seq,crtable,modified_to):
    '''
        >>> 
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][6]
        {0: 700, 1: 'pink', 2: 'espanol', 3: None, 4: None}
        >>> modified_to = {'color':'black'}
        >>> crtable = modify_rows_via_seq(6,crtable,modified_to)
        >>> crtable['table'][6]
        {0: 700, 1: 'black', 2: 'espanol', 3: None, 4: None}
        >>> 
        >>> 
    '''
    for k in modified_to:
        v = modified_to[k]
        i = crtable['animd'][k]
        if(i in crtable['table'][seq]):
            crtable['table'][seq][i] = v
    return(crtable)

def modify_rows_via_attribs(attribs,crtable,modified_to):
    '''
    '''
    seqslist = get_seqslist_via_attribs(attribs,crtable)
    for seq in seqslist:
        crtable = modify_rows_via_seq(seq,crtable,modified_to)
    return(crtable) 

def modify_rows_via_keys(keys,crtable,modified_to,**kwargs):
    '''
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][6]
        {0: 700, 1: 'black', 2: 'espanol', 3: None, 4: None}
        >>> keys = {'expire':'2017-oct-01','language':'english'}
        >>> modified_to = {'owner':'ihga'}
        >>> crtable = modify_rows_via_keys(keys,crtable,modified_to)
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'ihga'}
        >>> crtable['table'][6]
        {0: 700, 1: 'black', 2: 'espanol', 3: None, 4: None}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'ihga'}
        >>> 
        >>> 
        
    '''
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 1
    if(strict):
        ntbm = {}
        for k in modified_to:
            if(k in keys):
                pass
            else:
                ntbm[k] = modified_to[k]
    else:
        ntbm = copy.deepcopy(modified_to)
    seqslist = get_seqslist_via_keys(keys,crtable)
    for seq in seqslist:
        crtable = modify_rows_via_seq(seq,crtable,ntbm)
    return(crtable) 

modify_rows_via_values = modify_rows_via_keys

def modify_col_via_colnum(colnum,crtable,modified_to):
    '''
    '''
    if(isinstance(modified_to,list)):
        modified_to = ltdict.list2ltdict(modified_to)
    else:
        pass
    for rownum in modified_to:
        if(rownum in crtable['table']):
            crtable['table'][rownum][colnum] = modified_to[rownum]
        else:
            pass
    return(crtable)

def modify_col_via_colname(colname,crtable,modified_to):
    '''
        >>> 
        >>> 
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01', 4: 'dli'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01', 4: 'dli'}
        >>> crtable['table'][4]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'ihga'}
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'ihga'}
        >>> crtable['table'][6]
        {0: 700, 1: 'black', 2: 'espanol', 3: None, 4: None}
        >>> 
        >>> modified_to = {0:'terry',2:'terry'}
        >>> crtable = modify_col_via_colname('owner',crtable,modified_to)
        >>> crtable['table'][5]
        {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01', 4: 'ihga'}
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01', 4: 'terry'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01', 4: 'terry'}
        >>> 
        >>> 
        >>> 
        
    '''
    if(isinstance(modified_to,list)):
        modified_to = ltdict.list2ltdict(modified_to)
    else:
        pass
    colnum = crtable['animd'][colname]
    return(modify_col_via_colnum(colnum,crtable,modified_to))

def insert_col(colnum,col,crtable,**kwargs):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        col = {'owner':['dli','dlx','dly','dlz']}
        >>> crtable = insert_col(2,col,crtable)
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'dli', 3: 'espanol', 4: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'dlx', 3: 'chinese', 4: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'dly', 3: 'spanish', 4: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'dlz', 3: 'english', 4: '2018-dec-01'}
        >>> 
    '''
    crtable = naturalize_crtable(crtable)
    col_name = list(col.keys())[0]
    col_list = col[col_name] 
    refd = get_indexonly_refdict(crtable['animd'])
    nrefd = ltdict.insert(refd,colnum,col_name)
    crtable['animd'] = creat_mirror_dict(nrefd)
    #
    krefd = get_indexonly_refdict(crtable['knimd'])
    vrefd = get_indexonly_refdict(crtable['vnimd'])
    nkrefd = {}
    nvrefd = {}
    for index in krefd:
        if(index >= colnum):
            nkrefd[index+1] = krefd[index]
        else:
            nkrefd[index] = krefd[index]
    for index in vrefd:
        if(index in krefd):
            pass
        else:
            if(index >= colnum):
                nvrefd[index+1] = vrefd[index]
            else:
                nvrefd[index] = vrefd[index]
    if('as_value' in kwargs):
        as_value = kwargs['as_value']
    else:
        as_value = 1
    if(as_value):
        nvrefd[colnum] = col_name
    else:
        nkrefd[colnum] = col_name
    crtable['knimd'] = creat_mirror_dict(nkrefd)
    crtable['vnimd'] = creat_mirror_dict(nvrefd)
    #
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        crtable['table'][rownum] = ltdict.insert(crtable['table'][rownum],colnum,col_list[rownum])
    return(crtable)

def insert_cols(colnumlist,cols,crtable,**kwargs):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        cols = [
            {'owner':['dli','dlx','dly','dlz']},
            {'uid':['ua','ub','uc','ud']}
        ]
        colnumlist = [1,3]
        crtable = insert_cols(colnumlist,cols,crtable)
        >>> crtable['table'][0]
        {0: 500, 1: 'dli', 2: 'green', 3: 'ua', 4: 'espanol', 5: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'dlx', 2: 'green', 3: 'ub', 4: 'chinese', 5: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'dly', 2: 'darkblack', 3: 'uc', 4: 'spanish', 5: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'dlz', 2: 'blue', 3: 'ud', 4: 'english', 5: '2018-dec-01'}
        >>> pobj(crtable['animd'])
        {
         0: 'size', 
         1: 'owner', 
         2: 'color', 
         3: 'uid', 
         4: 'language', 
         'size': 0, 
         'uid': 3, 
         'color': 2, 
         'language': 4, 
         'owner': 1, 
         'expire': 5, 
         5: 'expire'
        }
        >>> 
    '''
    if('shift' in kwargs):
        shift = kwargs['shift']
    else:
        shift = 1
    for i in range(0,colnumlist.__len__()):
        colnum = colnumlist[i]
        if(shift):
            colnum = colnum + i
        else:
            pass
        crtable = insert_col(colnum,cols[i],crtable)
    return(crtable)

def insert_row(rownum,row,crtable):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        row = {'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'}
        crtable = insert_row(1,row,crtable)
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 8888, 1: 'blue', 2: 'russian', 3: '2018-dec-01'}
        >>> crtable['table'][2]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][4]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> 
    '''
    crtable = naturalize_crtable(crtable)
    row = nameattribs_to_indexattribs(row,(crtable['animd']))
    crtable['table'] = ltdict.insert(crtable['table'],rownum,row)
    return(crtable)

def insert_rows(rownumlist,rows,crtable,**kwargs):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        rows = [{'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'},
                {'size': 666, 'color': 'azure', 'language': 'russian', 'expire': '2017-dec-01'}]
        rownumlist = [0,2]
        crtable = insert_rows(rownumlist,rows,crtable)
        >>> rownumlist = [0,2]
        >>> crtable = insert_rows(rownumlist,rows,crtable)
        >>> crtable['table'][0]
        {0: 8888, 1: 'blue', 2: 'russian', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][2]
        {0: 666, 1: 'azure', 2: 'russian', 3: '2017-dec-01'}
        >>> crtable['table'][3]
        {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        >>> 
    '''
    if('shift' in kwargs):
        shift = kwargs['shift']
    else:
        shift = 1
    for i in range(0,rownumlist.__len__()):
        num = rownumlist[i]
        if(shift):
            num = num + i
        else:
            pass
        crtable = insert_row(num,rows[i],crtable)
    return(crtable)


## relation ship

def product_mirror_dicts(mds):
    '''
        >>> pobj(mds)
        [
         {
          0: 'size', 
          1: 'color', 
          2: 'language', 
          3: 'expire', 
          4: 'owner', 
          'size': 0, 
          'owner': 4, 
          'language': 2, 
          'color': 1, 
          'expire': 3
         }, 
         {
          0: 'size', 
          1: 'color', 
          2: 'language', 
          3: 'expire', 
          4: 'owner', 
          'size': 0, 
          'owner': 4, 
          'language': 2, 
          'color': 1, 
          'expire': 3
         }
        ]
        >>> 
        >>> pmds = product_mirror_dict(mds)
        >>> pobj(pmds)
        {
         0: 'size-0', 
         1: 'color-0', 
         2: 'language-0', 
         3: 'expire-0', 
         4: 'owner-0', 
         5: 'size-1', 
         6: 'color-1', 
         7: 'language-1', 
         8: 'expire-1', 
         9: 'owner-1', 
         'size-0': 0, 
         'owner-1': 9, 
         'size-1': 5, 
         'owner-0': 4, 
         'expire-1': 8, 
         'language-0': 2, 
         'color-0': 1, 
         'expire-0': 3, 
         'language-1': 7, 
         'color-1': 6
        }
        >>> 

    '''
    pmds = {}
    nmds = {}
    nmdlens = {}
    for i in range(0,mds.__len__()):
        nmds[i] = get_indexonly_refdict(mds[i],index_dominant=1)
        nmdlens[i] = nmds[i].__len__()
    curr_seq = 0
    for i in range(0,nmds.__len__()):
        nmd = nmds[i]
        nmd_kl = sorted(list(nmd.keys()))
        for j in range(0,nmd_kl.__len__()):
            k = nmd_kl[j]
            pmds[curr_seq] = ''.join((nmd[k],'-',str(i)))
            curr_seq = curr_seq + 1
    pmds = creat_mirror_dict(pmds,index_dominant=1)
    return(pmds)

def product_two_tables(table_1,table_2):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1', 2: 'c1'}, 
                      1: {0: 'a1', 1: 'b2', 2: 'c2'}, 
                      2: {0: 'a2', 1: 'b2', 2: 'c1'}
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b2', 2: 'c1'}, 
                      1: {0: 'a1', 1: 'b3', 2: 'c2'}, 
                      2: {0: 'a2', 1: 'b2', 2: 'c1'}
                  }
        
        table = product_two_tables(table_1,table_2)
        table.keys()
        dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8])
        >>> table[0]
        {0: 'a1', 1: 'b1', 2: 'c1', 3: 'a1', 4: 'b2', 5: 'c1'}
        >>> table[1]
        {0: 'a1', 1: 'b1', 2: 'c1', 3: 'a1', 4: 'b3', 5: 'c2'}
        >>> table[2]
        {0: 'a1', 1: 'b1', 2: 'c1', 3: 'a2', 4: 'b2', 5: 'c1'}
        >>> table[3]
        {0: 'a1', 1: 'b2', 2: 'c2', 3: 'a1', 4: 'b2', 5: 'c1'}
        >>> table[4]
        {0: 'a1', 1: 'b2', 2: 'c2', 3: 'a1', 4: 'b3', 5: 'c2'}
        >>> table[5]
        {0: 'a1', 1: 'b2', 2: 'c2', 3: 'a2', 4: 'b2', 5: 'c1'}
        >>> table[6]
        {0: 'a2', 1: 'b2', 2: 'c1', 3: 'a1', 4: 'b2', 5: 'c1'}
        >>> table[7]
        {0: 'a2', 1: 'b2', 2: 'c1', 3: 'a1', 4: 'b3', 5: 'c2'}
        >>> table[8]
        {0: 'a2', 1: 'b2', 2: 'c1', 3: 'a2', 4: 'b2', 5: 'c1'}
        >>> 
    '''
    table = {}
    tb1_len = table_1.__len__()
    tb2_len = table_2.__len__()
    tb_len = tb1_len * tb2_len
    cols_len = tb1_len + tb2_len
    curr_seq = 0
    tb1_kl = sorted(list(table_1.keys()))
    tb2_kl = sorted(list(table_2.keys()))
    
    for i in range(0,tb1_len):
        k1 = tb1_kl[i]
        head_tb1 = table_1[k1]
        for j in range(0,tb2_len):
            k2 = tb2_kl[j]
            tail_tb2 = table_2[k2]
            table[curr_seq] = {}
            seq = 0
            cl1 = sorted(list(head_tb1.keys()))
            cl2 = sorted(list(tail_tb2.keys()))
            for m in range(0,cl1.__len__()):
                key = cl1[m]
                table[curr_seq][seq] = head_tb1[key]
                seq = seq + 1
            for m in range(0,cl2.__len__()):
                key = cl2[m]
                table[curr_seq][seq] = tail_tb2[key]
                seq = seq + 1
            curr_seq = curr_seq + 1
    return(table)

def product_tables(tables):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b2'} 
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b2'}, 
                      1: {0: 'a1', 1: 'b3'} 
                  }
        table_3 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b3'}
                  }
        tables = [table_1,table_2,table_3]
        >>> tables = [table_1,table_2,table_3]
        >>> table = product_tables(tables)
        >>> table.keys()
        dict_keys([0, 1, 2, 3, 4, 5, 6, 7])
        >>> table[0]
        {0: 'a1', 1: 'b1', 2: 'a1', 3: 'b2', 4: 'a1', 5: 'b1'}
        >>> table[1]
        {0: 'a1', 1: 'b1', 2: 'a1', 3: 'b2', 4: 'a1', 5: 'b3'}
        >>> table[2]
        {0: 'a1', 1: 'b1', 2: 'a1', 3: 'b3', 4: 'a1', 5: 'b1'}
        >>> table[3]
        {0: 'a1', 1: 'b1', 2: 'a1', 3: 'b3', 4: 'a1', 5: 'b3'}
        >>> table[4]
        {0: 'a1', 1: 'b2', 2: 'a1', 3: 'b2', 4: 'a1', 5: 'b1'}
        >>> table[5]
        {0: 'a1', 1: 'b2', 2: 'a1', 3: 'b2', 4: 'a1', 5: 'b3'}
        >>> table[6]
        {0: 'a1', 1: 'b2', 2: 'a1', 3: 'b3', 4: 'a1', 5: 'b1'}
        >>> table[7]
        {0: 'a1', 1: 'b2', 2: 'a1', 3: 'b3', 4: 'a1', 5: 'b3'}
        >>> 
    '''
    tbs_len = tables.__len__()
    cursor = 1
    prev_table = tables[0]
    while(cursor < tbs_len):
        curr_table = tables[cursor]
        prev_table = product_two_tables(prev_table,curr_table)
        cursor = cursor + 1
    return(prev_table)

def product_crtables(crtables):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b2'} 
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b2'}, 
                      1: {0: 'a1', 1: 'b3'} 
                  }
        table_3 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b3'}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_3 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_3['table'] = table_3
        crtable_3['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtables = [crtable_1,crtable_2,crtable_3]
        products = product_crtables(crtables)
        products['animd']
        products['table']
    '''
    mds = {}
    kmds = {}
    vmds = {}
    tables = {}
    crtb = {}
    for i in range(0,crtables.__len__()):
        kmds[i] = crtables[i]['knimd']
        vmds[i] = crtables[i]['vnimd']
        mds[i] = crtables[i]['animd']
        tables[i] = crtables[i]['table']
    crtb['animd'] = product_mirror_dicts(mds)
    crtb['knimd'] = {}
    crtb['vnimd'] = {}
    prev_len = 0
    for i in range(0,crtables.__len__()):
        for j in kmds[i]:
            if(utils.is_int(j)):
                seq = prev_len + j
                v = kmds[i][j] + '-' +str(i)
                crtb['knimd'][seq] = v
                crtb['knimd'][v] = seq 
            else:
                pass
        for j in vmds[i]:
            if(utils.is_int(j)):
                seq = prev_len + j
                v = vmds[i][j] + '-' +str(i)
                crtb['vnimd'][seq] = v
                crtb['vnimd'][v] = seq 
            else:
                pass
        prev_len = prev_len + int(mds[i].__len__()/2)
    crtb['table'] = product_tables(tables)
    return(crtb)

def project_mirror_dict(md,colnameslist):
    '''
        >>> 
        >>> 
        >>> colnameslist = ['size','color']
        >>> md = {0: 'size', 1: 'color', 'language': 2, 3: 'expire', 'size': 0, 2: 'language', 'color': 1, 'expire': 3}
        >>> pobj(md)
        {
         0: 'size', 
         1: 'color', 
         'language': 2, 
         3: 'expire', 
         'size': 0, 
         2: 'language', 
         'color': 1, 
         'expire': 3
        }
        >>> pobj(project_mirror_dict(md,colnameslist)){
         0: 'size', 
         1: 'color', 
         'size': 0, 
         'color': 1
        }
        >>> 
        >>> 
    '''
    pmd = {}
    for key in md:
        if(key in colnameslist):
            pmd[key] = md[key]
        elif(md[key] in colnameslist):
            pmd[md[key]] = key
    pmd = creat_mirror_dict(pmd)
    return(pmd)

def project_table(colnumslist,table,**kwargs):
    '''
        table = {
                      0: {0: 'a1', 1: 'b1', 2: 'c1'}, 
                      1: {0: 'a1', 1: 'b2', 2: 'c2'}, 
                      2: {0: 'a2', 1: 'b1', 2: 'c1'}
                }
        colnumslist = [1,2]
        project_table(colnumslist,table)
        project_table(colnumslist,table,unique=0)
        >>> 
        >>> project_table(colnumslist,table)
        {0: {0: 'b1', 1: 'c1'}, 1: {0: 'b2', 1: 'c2'}}
        >>> 
        >>> project_table(colnumslist,table,unique=0)
        {0: {0: 'b1', 1: 'c1'}, 1: {0: 'b2', 1: 'c2'}, 2: {0: 'b1', 1: 'c1'}}
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    if('unique' in kwargs):
        unique = kwargs['unique']
    else:
        unique = 1
    pt = {}
    if(reorder):
        for seq in table:
            row = copy.deepcopy(table[seq])
            pop_seqs = set({})
            for colnum in row:
                if(colnum in colnumslist):
                    pass
                else:
                    pop_seqs.add(colnum)
                    pt[seq]= row
            ltdict.pop_seqs(row,pop_seqs)
            pt[seq]= row
    else:
        for seq in table:
            row = copy.deepcopy(table[seq])
            for colnum in row:
                if(colnum in colnumslist):
                    pt[seq][colnum]= row[colnum]
                else:
                    pass
    
    seqs_for_del =[]
    if(unique):
        vset = set({})
        for k in pt:
            vset.add(ltdict.to_tuple(pt[k]))
        tslen = vset.__len__()
        freq = {}
        for k in pt:
            v = ltdict.to_tuple(pt[k])
            if(v in freq):
                freq[v] = freq[v] + 1
                seqs_for_del.append(k)
            else:
                freq[v] = 0
        if(reorder):
            ltdict.pop_seqs(pt,set(seqs_for_del))
        else:
            npt = {}
            for k in pt:
                if(k in seqs_for_del):
                    pass
                else:
                    npt[k] = pt[k]
            pt = npt
    else:
        pass
    return(pt)

def project_crtable(colnameslist,crtable,**kwargs):
    '''
        crtable = {}
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        colnameslist = ['color','language']
        >>> crtable = project_crtable(colnameslist,crtable)
        >>> pobj(crtable)
        {
         'table': 
                  {
                   0: 
                      {
                       0: 'b1', 
                       1: 'c1'
                      }, 
                   1: 
                      {
                       0: 'b2', 
                       1: 'c2'
                      }
                  }, 
         'animd': 
                  {
                   1: 'color', 
                   2: 'language', 
                   'language': 2, 
                   'color': 1
                  }
        }
        >>> 

    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    if('unique' in kwargs):
        unique = kwargs['unique']
    else:
        unique = 1
    colnumslist = get_indexes_list_via_names_list(colnameslist,crtable['animd'])
    crtable['animd'] = project_mirror_dict(crtable['animd'],colnameslist)
    crtable['table'] = project_table(colnumslist,crtable['table'],reorder=reorder,unique=unique)
    return(crtable)

def row_in_crtable(row,crtable):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        row = {'size': 74, 'color': 'green', 'language': 'espanol', 'expire': '2017-oct-01'}
        row_in_crtable(row,crtable)
        row = {'size': 111, 'color': 'green', 'language': 'espanol', 'expire': '2017-oct-01'}
        row_in_crtable(row,crtable)
        row = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        row_in_crtable(row,crtable)
        row = {0: 111, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        row_in_crtable(row,crtable)
    '''
    seqslist = get_seqslist_via_attribs(row,crtable)
    if(seqslist.__len__() == 0):
        return(False)
    else:
        return(True)

def col_in_crtable(col,crtable,**kwargs):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        col = {'size':[500,74,300,100000]}
        col_in_crtable(col,crtable)
        col_in_crtable(col,crtable,strict=0)
        col = {'size':[500,74,300]}
        col_in_crtable(col,crtable)
        col_in_crtable(col,crtable,strict=0)
        col = {'length':[500,74,300,100000]}
        col_in_crtable(col,crtable,strict=0)
        >>> col = {'size':[500,74,300,100000]}
        >>> col_in_crtable(col,crtable)
        True
        >>> col_in_crtable(col,crtable,strict=0)
        True
        >>> col = {'size':[500,74,300]}
        >>> col_in_crtable(col,crtable)
        False
        >>> col_in_crtable(col,crtable,strict=0)
        False
        >>> col = {'length':[500,74,300,100000]}
        >>> col_in_crtable(col,crtable,strict=0)
        True
        >>> 
    '''
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 1
    if(strict):
        name = list(col.keys())[0]
        colist = get_column_via_attribname(name,crtable)
        if(utils.is_list(col[name])):
            cl = ltdict.list2ltdict(col[name])
        else:
            cl = col[name]
        cond = (cl == colist)
        if(cond):
            return(True)
        else:
            return(False)
    else:
        name = list(col.keys())[0]
        refd = get_nameonly_refdict(crtable['animd'])
        if(utils.is_list(col[name])):
            cl = ltdict.list2ltdict(col[name])
        else:
            cl = col[name]
        for colname in refd:
            colist = get_column_via_attribname(colname,crtable)
            cond = (cl == colist)
            if(cond):
                return(True)
            else:
                pass
        return(False)

def partlyrow_in_crtable(row,crtable):
    '''
        crtable = {}
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        row = {'color': 'green', 'language': 'espanol'}
        >>> partlyrow_in_crtable(row,crtable)
        True
    '''
    nr = nameattribs_to_indexattribs(row,crtable['animd'])
    cond = 0
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        cond = utils.dict_comprise(row,nr)
        if(cond):
            return(True)
    return(False)

def partlycol_in_crtable(col,crtable,**kwargs):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        col = {'size':[74,300]}
        >>> partlycol_in_crtable(col,crtable)
        True
        >>> col = {'length':[74,300]}
        >>> partlycol_in_crtable(col,crtable)
        False
        >>> partlycol_in_crtable(col,crtable,strict=0)
        1
        True
        >>> 
        >>> 
    '''
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 1
    if(strict):
        name = list(col.keys())[0]
        refd = get_nameonly_refdict(crtable['animd'])
        if(name in refd):
            pass
        else:
            return(False)
        colist = get_column_via_attribname(name,crtable)
        if(utils.is_list(col[name])):
            cl = ltdict.list2ltdict(col[name])
        else:
            cl = col[name]
        cond = ltdict.comprise(colist,cl,strict=0)
        if(cond):
            return(True)
        else:
            return(False)
    else:
        name = list(col.keys())[0]
        refd = get_nameonly_refdict(crtable['animd'])
        if(utils.is_list(col[name])):
            cl = ltdict.list2ltdict(col[name])
        else:
            cl = col[name]
        for colname in refd:
            colist = get_column_via_attribname(colname,crtable)
            cond = ltdict.comprise(colist,cl,strict=0)
            if(cond):
                return(True)
            else:
                pass
        return(False)

def unique_crtable(crtable,**kwargs):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable = unique_crtable(crtable)
        >>> crtable['table'].keys()
        dict_keys([0, 1, 2])
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> crtable['table'][3]
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        KeyError: 3
        >>> 
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    pt = crtable['table']
    seqs_for_del =[]
    vset = set({})
    for k in pt:
        vset.add(ltdict.to_tuple(pt[k]))
    tslen = vset.__len__()
    freq = {}
    for k in pt:
        v = ltdict.to_tuple(pt[k])
        if(v in freq):
            freq[v] = freq[v] + 1
            seqs_for_del.append(k)
        else:
            freq[v] = 0
    if(reorder):
        ltdict.pop_seqs(pt,set(seqs_for_del))
    else:
        npt = {}
        for k in pt:
            if(k in seqs_for_del):
                pass
            else:
                npt[k] = pt[k]
        pt = npt
    crtable['table'] = pt
    return(crtable)

def union_crtables(crtables):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b2'} 
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b2'}, 
                      1: {0: 'a1', 1: 'b3'} 
                  }
        table_3 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b3'}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_3 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_3['table'] = table_3
        crtable_3['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtables = [crtable_1,crtable_2,crtable_3]
        crtable = union_crtables(crtables)
        crtable['table'].keys()
        crtable['table'][0]
        crtable['table'][1]
        crtable['table'][2]
        >>> crtable['table'].keys()
        dict_keys([0, 1, 2])
        >>> crtable['table'][0]
        {0: 'a1', 1: 'b1'}
        >>> crtable['table'][1]
        {0: 'a1', 1: 'b2'}
        >>> crtable['table'][2]
        {0: 'a1', 1: 'b3'}
        >>> 
    '''
    crtb = {}
    crtb['animd'] = crtables[0]['animd']
    crtb['knimd'] = crtables[0]['knimd']
    crtb['vnimd'] = crtables[0]['vnimd']
    crtb['table'] = {}
    rn = 0
    for crtable in crtables:
        table = crtable['table']
        for rownum in table:
            crtb['table'][rn] = table[rownum]
            rn = rn + 1
    crtb= unique_crtable(crtb)
    return(crtb)

def intersec_two_crtables(crtable_1,crtable_2,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b2'} 
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b2'}, 
                      1: {0: 'a1', 1: 'b3'} 
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable = intersec_two_crtables(crtable_1,crtable_2)
        crtable
        {'table': {0: {0: 'a1', 1: 'b2'}}, 'animd': {0: 'A', 1: 'B', 'A': 0, 'B': 1}}
    '''
    if('colname_strict' in kwargs):
        colname_strict = kwargs['colname_strict']
    else:
        colname_strict = 1
    if('table_strict' in kwargs):
        table_strict = kwargs['table_strict']
    else:
        table_strict = 0
    if(colname_strict):
        if(crtable_1['animd'] == crtable_2['animd']):
            pass
        else:
            return({'table':{},'animd':{}})
    else:
        pass
    crtable = {}
    crtable['animd'] = crtable_1['animd']
    #####################################
    crtable['knimd'] = crtable_1['knimd']
    crtable['vnimd'] = crtable_1['vnimd']
    #####################################
    crtable['table'] = {} 
    tb1 = crtable_1['table']
    tb2 = crtable_2['table']
    seq = 0
    for rownum in tb1:
        row1 = tb1[rownum]
        if(table_strict):
            row2 = tb2[rownum]
            cond = (row1 == row2)
        else:
            cond = row_in_crtable(row1,crtable_2)
        if(cond):
            crtable['table'][seq] = row1
            seq = seq + 1
        else:
            pass
    return(crtable)

def intersec_crtables(crtables,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b3'} 
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b2'}, 
                      1: {0: 'a1', 1: 'b3'} 
                  }
        table_3 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b3'}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_3 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_3['table'] = table_3
        crtable_3['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtables = [crtable_1,crtable_2,crtable_3]
        crtable = intersec_crtables(crtables)
        crtable
        {'table': {0: {0: 'a1', 1: 'b3'}}, 'animd': {0: 'A', 1: 'B', 'A': 0, 'B': 1}}
    '''
    if('colname_strict' in kwargs):
        colname_strict = kwargs['colname_strict']
    else:
        colname_strict = 1
    if('table_strict' in kwargs):
        table_strict = kwargs['table_strict']
    else:
        table_strict = 0
    crtable = crtables[0]
    for i in range(1,crtables.__len__()):
        currtb = crtables[i]
        crtable = intersec_two_crtables(crtable,currtb,colname_strict=colname_strict,table_strict=table_strict)
    return(crtable)

def naturalize_table(table):
    '''        
        table = {}
        table[0] = {0: 500, 4: 'green', 8: 'espanol', 7: '2018-dec-01'}
        table[3] = {0: 74, 4: 'green', 8: 'espanol', 7: '2017-oct-01'}
        table[5] = {0: 300, 4: 'darkblack', 8: 'spanish', 7: '2017-oct-01'}
        table[6] = {0: 100000, 4: 'blue', 8: 'english', 7: '2018-dec-01'}
        >>> table.keys()
        dict_keys([0, 1, 2, 3])
        >>> table[0]
        {0: 500, 1: 'green', 2: '2018-dec-01', 3: 'espanol'}
        >>> table[1]
        {0: 74, 1: 'green', 2: '2017-oct-01', 3: 'espanol'}
        >>> table[2]
        {0: 300, 1: 'darkblack', 2: '2017-oct-01', 3: 'spanish'}
        >>> table[3]
        {0: 100000, 1: 'blue', 2: '2018-dec-01', 3: 'english'}
        >>> 
    '''
    ntb = ltdict.naturalize_intkeydict(table)
    for seq in ntb:
        row = ntb[seq]
        ntb[seq] = ltdict.naturalize_intkeydict(row)
    return(ntb)

def naturalize_crtable(crtable):
    '''
        crtable = {}
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 4: 'color', 7: 'language', 8: 'expire'})
        crtable['table'][1] = {0: 500, 4: 'green', 7: 'espanol', 8: '2018-dec-01'}
        crtable['table'][6] = {0: 74, 4: 'green', 7: 'espanol', 8: '2017-oct-01'}
        crtable['table'][9] = {0: 300, 4: 'darkblack', 7: 'spanish', 8: '2017-oct-01'}
        crtable['table'][10] = {0: 100000, 4: 'blue', 7: 'english', 8: '2018-dec-01'}
        crtable = naturalize_crtable(crtable)
        >>> crtable['animd']
        {0: 'size', 1: 'color', 'language': 2, 3: 'expire', 'expire': 3, 'color': 1, 'size': 0, 2: 'language'}
        >>> crtable['table'][0]
        {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> 
    '''
    crtable['animd'] = naturalize_refdict(crtable['animd'])
    if('table' in crtable):
        crtable['table'] = naturalize_table(crtable['table'])
    else:
        pass
    return(crtable)

def comprise_table(table_1,table_2,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1',2:'c1'}, 
                      1: {0: 'a2', 1: 'b2',2:'c2'},
                      2: {0: 'a3', 1: 'b3',2:'c3'}
                  }
        table_2 = {
                      0: {0: 'b2', 1: 'c2'}, 
                      1: {0: 'b3', 1: 'c3'} 
                  }
        comprise_table(table_1,table_2)
    '''
    if('startcol' in kwargs):
        startcol = kwargs['startcol']
    else:
        startcol = 0
    tb_1 = naturalize_table(table_1)
    tb_2 = naturalize_table(table_2)
    width_1 = tb_1[0].__len__()
    width_2 = tb_2[0].__len__()
    length_1 = tb_1.__len__()
    length_2 = tb_2.__len__()
    colnum = 0
    for rownum in range(0,length_1-length_2+1):
        for colnum in range(startcol,width_1-width_2+1):
            cond = 1
            bki = 0
            for i in range(0,length_2):
                if(bki):
                    break
                else:
                    for j in range(0,width_2):
                        if(tb_2[i][j] == tb_1[rownum+i][colnum+j]):
                            pass
                        else:
                            cond = 0
                            bki = 1
                            break
            if(cond):
                return((True,colnum,colnum+width_2))
            else:
                pass
    return((False,colnum,-1))

def comprise_crtable(crtable_1,crtable_2,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1',2:'c1'}, 
                      1: {0: 'a2', 1: 'b2',2:'c2'},
                      2: {0: 'a3', 1: 'b3',2:'c3'}
                  }
        table_2 = {
                      0: {0: 'b2', 1: 'c2'}, 
                      1: {0: 'b3', 1: 'c3'} 
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_1['table'] = table_1
        crtable_2['table'] = table_2
        crtable_1['animd'] = creat_mirror_dict({0:'A',1:'B',2:'C'})
        crtable_2['animd'] = creat_mirror_dict({0:'B',1:'C'})
        comprise_crtable(crtable_1,crtable_2)
        True
        crtable_1['animd'] = creat_mirror_dict({0:'A',1:'X',2:'C'})
        crtable_2['animd'] = creat_mirror_dict({0:'B',1:'C'})
        comprise_crtable(crtable_1,crtable_2)
        False
        comprise_crtable(crtable_1,crtable_2,strict=0)
        True
    '''
    def get_acond(lt1,lt2,colnum):
        for i in range(0,lt2.__len__()):
            if(lt2[i] == lt1[colnum+i]):
                pass
            else:
                return(False)
        return(True)
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 1
    crtb1 = naturalize_crtable(crtable_1)
    crtb2 = naturalize_crtable(crtable_2)
    if(strict):
        lt1 = get_indexonly_refdict(crtb1['animd'])
        lt2 = get_indexonly_refdict(crtb2['animd'])
        tcond,colnum,nextcolnum = comprise_table(crtb1['table'],crtb2['table'])
        acond = get_acond(lt1,lt2,colnum)
        while((not(acond)) & tcond):
            if((nextcolnum +lt2.__len__()) <= lt1.__len__()):
                tcond,colnum,nextcolnum = comprise_table(crtb1['table'],crtb2['table'],startcol=nextcolnum)
                acond = get_acond(lt1,lt2,colnum)
            else:
                break
        return(acond & tcond)
    else:
        return(comprise_table(crtb1['table'],crtb2['table'])[0])

def equal(crtable_1,crtable_2,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b2'} 
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b2'} 
                  }
        table_3 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b3'}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_3 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_3['table'] = table_3
        crtable_3['animd'] = {0:'A',1:'B','A':0,'B':1}
        >>> equal(crtable_1,crtable_2)
        True
        >>> equal(crtable_1,crtable_3)
        False
        >>> 
    '''
    if('colname_strict' in kwargs):
        colname_strict = kwargs['colname_strict']
    else:
        colname_strict = 1
    if('table_strict' in kwargs):
        table_strict = kwargs['table_strict']
    else:
        table_strict = 0
    if(colname_strict):
        if(crtable_1['animd'] == crtable_2['animd']):
            pass
        else:
            return(False)
    else:
        pass
    if(table_strict):
        if(crtable_1['table'].__len__() == crtable_2['table'].__len__()):
            for seq in crtable_1['table']:
                row1 = crtable_1['table'][seq]
                if(seq in crtable_2['table']):
                    row2 = crtable_2['table'][seq]
                    if(row1 == row2):
                        pass
                    else:
                        return(False)
                else:
                    return(False)
            return(True)
        else:
            return(False)
    else:
        if(crtable_1['table'].__len__() == crtable_2['table'].__len__()):
            tb_1 = naturalize_table(crtable_1['table'])
            tb_2 = naturalize_table(crtable_2['table'])
            for seq in tb_1:
                row1 = crtable_1['table'][seq]
                row2 = crtable_2['table'][seq]
                if(row1 == row2):
                    pass
                else:
                    return(False)
            return(True)
        else:
            return(False)

def get_newcrtable_via_colnumslist(colnumslist,crtable,**kwargs):
    '''
        crtable = {}
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['knimd'] = creat_mirror_dict({0: 'size'})
        crtable['vnimd'] = creat_mirror_dict({1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        colnumslist = [0,2,3]
        >>> crtable = get_newcrtable_via_colnumslist(colnumslist,crtable)
        >>> pobj(crtable['animd'])
        {
         0: 'size', 
         1: 'language', 
         'language': 1, 
         'expire': 2, 
         'size': 0, 
         2: 'expire'
        }
        >>> crtable['table'][0]
        {0: 500, 1: 'espanol', 2: '2018-dec-01'}
        >>> crtable['table'][1]
        {0: 74, 1: 'espanol', 2: '2017-oct-01'}
        >>> crtable['table'][2]
        {0: 300, 1: 'spanish', 2: '2017-oct-01'}
        >>> crtable['table'][3]
        {0: 100000, 1: 'english', 2: '2018-dec-01'}
        >>> 
    '''
    if('naturalize' in kwargs):
        naturalize = kwargs['naturalize']
    else:
        naturalize = 1
    refd = get_indexonly_refdict(crtable['animd'])
    nrefd = {}
    for index in refd:
        if(index in colnumslist):
            nrefd[index] = refd[index]
        else:
            pass
    nkrefd = {}
    nvrefd = {}
    for index in nrefd:
        name = nrefd[index]
        if(name in crtable['knimd']):
            nkrefd[index] = name
        else:
            nvrefd[index] = name
    ####
    if(naturalize):
        nnkrefd = {}
        nnvrefd = {}
        nnrefd = naturalize_refdict(nrefd)
        nirefd = get_indexonly_refdict(naturalize_refdict(nnrefd))
        for ncolnum in nirefd:
            colname = nirefd[ncolnum]
            if(colname in nkrefd.values()):
                nnkrefd[ncolnum] = colname 
            else:
                pass
        for ncolnum in nirefd:     
            colname = nirefd[ncolnum]
            if(colname in nvrefd.values()):
                nnvrefd[ncolnum] = colname
            else:
                pass
        nkrefd = nnkrefd
        nvrefd = nnvrefd
        nrefd = nnrefd
    else:
        pass
    ####
    crtb = {}
    crtb['animd'] = creat_mirror_dict(nrefd)
    crtb['knimd'] = creat_mirror_dict(nkrefd)
    crtb['vnimd'] = creat_mirror_dict(nvrefd)
    crtb['table'] = {}
    ####
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        nr = {}
        for index in row:
            ####
            cond1 = (index in colnumslist)
            cond2 = (int(index) in colnumslist)
            cond = (cond1 | cond2)
            ####
            if(cond):
                nr[index] = row[index]
            else:
                pass
        crtb['table'][rownum] = nr
    if(naturalize):
        return(naturalize_crtable(crtb))
    else:
        return(crtb)

def get_newcrtable_via_colnameslist(colnameslist,crtable,**kwargs):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['knimd'] = creat_mirror_dict({0: 'size'})
        crtable['vnimd'] = creat_mirror_dict({1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        colnameslist = ['size','language','expire']
        crtable = get_newcrtable_via_colnameslist(colnameslist,crtable)
        pobj(crtable['animd'])
        crtable['table'][0]
        crtable['table'][1]
        crtable['table'][2]
        crtable['table'][3]
        >>> 
    '''
    if('naturalize' in kwargs):
        naturalize = kwargs['naturalize']
    else:
        naturalize = 1
    colnumslist = get_indexes_list_via_names_list(colnameslist,crtable['animd'])
    crtb = get_newcrtable_via_colnumslist(colnumslist,crtable,naturalize = naturalize)
    return(crtb)

def diff_two_crtables(crtable_1,crtable_2,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1'}, 
                      1: {0: 'a1', 1: 'b2'} 
                  }
        table_2 = {
                      0: {0: 'a1', 1: 'b2'}, 
                      1: {0: 'a1', 1: 'b3'} 
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'A',1:'B','A':0,'B':1}
        crtable = diff_two_crtables(crtable_1,crtable_2)
        crtable['table']
        crtable = diff_two_crtables(crtable_2,crtable_1)
        crtable['table']
    '''
    if('colname_strict' in kwargs):
        colname_strict = kwargs['colname_strict']
    else:
        colname_strict = 1
    if('rownum_strict' in kwargs):
        rownum_strict = kwargs['rownum_strict']
    else:
        rownum_strict = 0
    if(colname_strict):
        if(crtable_1['animd'] == crtable_2['animd']):
            pass
        else:
            return(False)
    else:
        pass
    crtable = {}
    crtable['animd'] = crtable_1['animd']
    crtable['knimd'] = crtable_1['knimd']
    crtable['vnimd'] = crtable_1['vnimd']
    crtable['table'] = {}
    if(rownum_strict):
        tb1 = crtable_1['table']
        tb2 = crtable_2['table']
        for rownum in tb1:
            row = tb1[rownum]
            if(rownum in tb2):
                pass
            else:
                cond = (tb1['rownum'] == tb2['rownum'])
                if(cond):
                    pass
                else:
                    crtable['table'][rownum] = row
    else:
        tb1 = crtable_1['table']
        tb2 = crtable_2['table']
        for rownum in tb1:
            row = tb1[rownum]
            cond = row_in_crtable(row,crtable_2)
            if(cond):
                pass
            else:
                crtable['table'][rownum] = row
    if('naturalize' in kwargs):
        naturalize = kwargs['naturalize']
    else:
        naturalize = 1
    if(naturalize):
        crtable = naturalize_crtable(crtable)
    else:
        pass
    return(crtable)

def thetajoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2,theta_function,**kwargs): 
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1', 2: 5}, 
                      1: {0: 'a1', 1: 'b2', 2: 6},
                      2: {0: 'a2', 1: 'b3', 2: 8},
                      3: {0: 'a2', 1: 'b4', 2: 12}
                  }
        table_2 = {
                      0: {0: 'b1', 1: 3}, 
                      1: {0: 'b2', 1: 7},
                      2: {0: 'b3', 1: 10},
                      3: {0: 'b3', 1: 2},
                      4: {0: 'b5', 1: 2}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B',2:'C','A':0,'B':1,'C':2}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'B',1:'E','B':0,'E':1}
        colnameslist_1 =['C']
        colnameslist_2 =['E']
        def theta_function(subrow_1,subrow_2):
            k1 = list(subrow_1.keys())[0]
            k2 = list(subrow_2.keys())[0]
            if(subrow_1[k1] < subrow_2[k2]):
                return(True)
            else:
                return(False)
        
        crtable = thetajoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2,theta_function)
        
        >>> pobj(crtable['animd'])
        {
         0: 'A-0', 
         1: 'B-0', 
         2: 'C-0', 
         3: 'B-1', 
         'E-1': 4, 
         'C-0': 2, 
         'A-0': 0, 
         4: 'E-1', 
         'B-1': 3, 
         'B-0': 1
        }
        >>> 
        >>> crtable['table']
        {0: {0: 'a1', 1: 'b1', 2: 5, 3: 'b2', 4: 7}, 1: {0: 'a1', 1: 'b1', 2: 5, 3: 'b3', 4: 10}, 2: {0: 'a1', 1: 'b2', 2: 6, 3: 'b2', 4: 7}, 3: {0: 'a1', 1: 'b2', 2: 6, 3: 'b3', 4: 10}, 4: {0: 'a2', 1: 'b3', 2: 8, 3: 'b3', 4: 10}}
        >>> 
        
    '''
    crtb_1 = naturalize_crtable(crtable_1)
    crtb_2 = naturalize_crtable(crtable_2)
    tb_1 =  crtb_1['table']
    tb_2 =  crtb_2['table']
    subcrtb_1 = get_newcrtable_via_colnameslist(colnameslist_1,crtb_1,naturalize = 0)
    subcrtb_2 = get_newcrtable_via_colnameslist(colnameslist_2,crtb_2,naturalize = 0)
    subtb_1 = subcrtb_1['table']
    subtb_2 = subcrtb_2['table']
    crtable = {}
    crtable['animd'] = product_mirror_dicts([crtable_1['animd'],crtable_2['animd']])
    ####
    ####
    kmds = {}
    vmds = {}
    mds = {}
    crtables = [crtb_1,crtb_2]
    for i in range(0,crtables.__len__()):
        kmds[i] = crtables[i]['knimd']
        vmds[i] = crtables[i]['vnimd']
        mds[i] = crtables[i]['animd']
    crtable['knimd'] = {}
    crtable['vnimd'] = {}
    prev_len = 0
    for i in range(0,crtables.__len__()):
        for j in kmds[i]:
            if(utils.is_int(j)):
                seq = prev_len + j
                v = kmds[i][j] + '-' +str(i)
                crtable['knimd'][seq] = v
                crtable['knimd'][v] = seq 
            else:
                pass
        for j in vmds[i]:
            if(utils.is_int(j)):
                seq = prev_len + j
                v = vmds[i][j] + '-' +str(i)
                crtable['vnimd'][seq] = v
                crtable['vnimd'][v] = seq 
            else:
                pass
        prev_len = prev_len + int(mds[i].__len__()/2)
    ####
    ####
    crtable['table'] = {} 
    colnums = int(crtable['animd'].__len__() / 2)
    seq = 0
    for rownum1 in subtb_1:
        subrow_1 = subtb_1[rownum1]
        for rownum2 in subtb_2:
            subrow_2 = subtb_2[rownum2]
            cond = theta_function(subrow_1,subrow_2)
            if(cond):
                crtable['table'][seq] = ltdict.concat(tb_1[rownum1],tb_2[rownum2])
                seq = seq + 1
            else:
                pass
    if('naturalize' in kwargs):
        naturalize = kwargs['naturalize']
    else:
        naturalize = 1
    if(naturalize):
        crtable = naturalize_crtable(crtable)
    else:
        pass
    return(crtable)

def equijoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1', 2: 5}, 
                      1: {0: 'a1', 1: 'b2', 2: 6},
                      2: {0: 'a2', 1: 'b3', 2: 8},
                      3: {0: 'a2', 1: 'b4', 2: 12}
                  }
        table_2 = {
                      0: {0: 'b1', 1: 3}, 
                      1: {0: 'b2', 1: 7},
                      2: {0: 'b3', 1: 10},
                      3: {0: 'b3', 1: 2},
                      4: {0: 'b5', 1: 2}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B',2:'C','A':0,'B':1,'C':2}
        crtable_1['knimd'] = {0:'A','A':0}
        crtable_1['vnimd'] = {1:'B',2:'C','B':1,'C':2}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'B',1:'E','B':0,'E':1}
        crtable_2['knimd'] = {0:'B','B':0}
        crtable_2['vnimd'] = {1:'E','E':1}
        colnameslist_1 =['B']
        colnameslist_2 =['B']
        crtable = equijoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2)
        >>> crtable = equijoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2)
        >>> crtable['animd']
        {0: 'A-0', 1: 'B-0', 2: 'C-0', 3: 'B-1', 'E-1': 4, 'C-0': 2, 'A-0': 0, 4: 'E-1', 'B-1': 3, 'B-0': 1}
        >>> crtable['table']
        {
         0: {0: 'a1', 1: 'b1', 2: 5, 3: 'b1', 4: 3}, 
         1: {0: 'a1', 1: 'b2', 2: 6, 3: 'b2', 4: 7}, 
         2: {0: 'a2', 1: 'b3', 2: 8, 3: 'b3', 4: 10}, 
         3: {0: 'a2', 1: 'b3', 2: 8, 3: 'b3', 4: 2}
        }
        >>> 
        >>> 
    '''
    def theta_function(subrow_1,subrow_2):
        subrow_l1 = ltdict.naturalize_intkeydict(subrow_1)
        subrow_l2 = ltdict.naturalize_intkeydict(subrow_2)
        if(subrow_l1 == subrow_l2):
            return(True)
        else:
            return(False)
    if('naturalize' in kwargs):
        naturalize = kwargs['naturalize']
    else:
        naturalize = 1
    crtable = thetajoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2,theta_function,naturalize = naturalize)
    return(crtable)

def naturaljoin_mirror_dict(md):
    '''
        md = {
         0: 'A-0', 
         1: 'B-0', 
         2: 'C-0', 
         3: 'B-1', 
         'E-1': 4, 
         'C-0': 2, 
         'A-0': 0, 
         4: 'E-1', 
         'B-1': 3, 
         'B-0': 1
        }
        md = naturaljoin_mirror_dict(md)
        pobj(md)
        {
         0: 'A', 
         1: 'B', 
         2: 'C', 
         3: 'E', 
         'C': 2, 
         'E': 3, 
         'A': 0, 
         'B': 1
        }
    '''
    refd = get_indexonly_refdict(md)
    refd = utils.dict_unique_value(refd)
    regex = re.compile('(.*)\-[0-9]+')
    nrefd = {}
    for seq in refd:
        v = refd[seq]
        m = regex.search(v)
        nrefd[seq] = m.group(1)
    nrefd = utils.dict_unique_value(nrefd)
    nrefd = ltdict.naturalize_intkeydict(nrefd)
    return(creat_mirror_dict(nrefd))

def naturaljoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2,**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1', 2: 5}, 
                      1: {0: 'a1', 1: 'b2', 2: 6},
                      2: {0: 'a2', 1: 'b3', 2: 8},
                      3: {0: 'a2', 1: 'b4', 2: 12}
                  }
        table_2 = {
                      0: {0: 'b1', 1: 3}, 
                      1: {0: 'b2', 1: 7},
                      2: {0: 'b3', 1: 10},
                      3: {0: 'b3', 1: 2},
                      4: {0: 'b5', 1: 2}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B',2:'C','A':0,'B':1,'C':2}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'B',1:'E','B':0,'E':1}
        colnameslist_1 =['B']
        colnameslist_2 =['B']
        crtable = naturaljoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2)
        crtable['animd']
        crtable['table']
        >>> crtable['animd']
        {0: 'A', 1: 'B', 2: 'C', 3: 'E', 'C': 2, 'E': 3, 'A': 0, 'B': 1}
        >>> crtable['table']
        {
         0: {0: 'a1', 1: 'b1', 2: 5, 3: 3}, 
         1: {0: 'a1', 1: 'b2', 2: 6, 3: 7}, 
         2: {0: 'a2', 1: 'b3', 2: 8, 3: 10}, 
         3: {0: 'a2', 1: 'b3', 2: 8, 3: 2}
         }
    '''
    if('naturalize' in kwargs):
        naturalize = kwargs['naturalize']
    else:
        naturalize = 1
    crtb = equijoin_two_crtables(colnameslist_1,crtable_1,colnameslist_2,crtable_2,naturalize = naturalize)
    to_be_deleted = get_indexes_list_via_names_list(colnameslist_2,crtable_2['animd'])
    to_be_deleted = map(lambda x: x + int(crtable_1['animd'].__len__()/2), to_be_deleted)
    crtable = {}
    crtable = del_cols_via_colnumslist(to_be_deleted,crtb)
    crtable['animd'] = naturaljoin_mirror_dict(crtb['animd'])
    return(crtable)

def get_image_sets_dict(crtable,colnameslist):
    '''
        table = {
                      0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                      1: {0: 'a2', 1: 'b3', 2: 'c7'},
                      2: {0: 'a3', 1: 'b4', 2: 'c6'},
                      3: {0: 'a1', 1: 'b2', 2: 'c3'},
                      4: {0: 'a4', 1: 'b6', 2: 'c6'}, 
                      5: {0: 'a2', 1: 'b2', 2: 'c3'},
                      6: {0: 'a1', 1: 'b2', 2: 'c1'}
                  }
        crtable = {'table':table,}
        crtable['animd'] = {0:'A',1:'B',2:'C','A':0,'B':1,'C':2}
        colnameslist =['A']
        image_sets_dict = get_image_sets_dict(crtable,colnameslist)
        pobj(image_sets_dict,fixed_indent=1)
        >>> pobj(image_sets_dict,fixed_indent=1)
        {
            'mapping': {
                ('A', ): ['B', 'C']
            },
            'image_sets': {
                ('a1', ): {
                    ('b1', 'c2'), ('b2', 'c1'), ('b2', 'c3')
                },
                ('a3', ): {
                    ('b4', 'c6')
                },
                ('a2', ): {
                    ('b3', 'c7'), ('b2', 'c3')
                },
                ('a4', ): {
                    ('b6', 'c6')
                }
            }
        }
        >>> 
    '''
    indexes_list = get_indexes_list_via_names_list(colnameslist,crtable['animd'])
    values_indexes_list = get_the_other_indexes_list_via_indexes_list(indexes_list,crtable['animd'])
    image_sets = {}
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        key = []
        for i in range(0,indexes_list.__len__()):
            key.append(row[indexes_list[i]])
        key = tuple(key)
        value = []
        for i in range(0,values_indexes_list.__len__()):
            value.append(row[values_indexes_list[i]])
        value = tuple(value)
        if(key in image_sets):
            image_sets[key].add(value)
        else:
            image_sets[key] = {value}
    mapping = {}
    key = []
    for i in range(0,indexes_list.__len__()):
        key.append(crtable['animd'][indexes_list[i]])
    key = tuple(key)
    value = []
    for i in range(0,values_indexes_list.__len__()):
        value.append(crtable['animd'][values_indexes_list[i]])
    mapping[key] = value
    value = tuple(value)
    rslt = {'image_sets':image_sets,'mapping':mapping}
    return(rslt)

def divide_two_crtables(crtable_1,crtable_2,colnameslist=[],**kwargs):
    '''
        table_1 = {
                      0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                      1: {0: 'a2', 1: 'b3', 2: 'c7'},
                      2: {0: 'a3', 1: 'b4', 2: 'c6'},
                      3: {0: 'a1', 1: 'b2', 2: 'c3'},
                      4: {0: 'a4', 1: 'b6', 2: 'c6'}, 
                      5: {0: 'a2', 1: 'b2', 2: 'c3'},
                      6: {0: 'a1', 1: 'b2', 2: 'c1'}
                  }
        table_2 = {
                      0: {0: 'b1', 1: 'c2', 2: 'd1'}, 
                      1: {0: 'b2', 1: 'c1', 2: 'd1'},
                      2: {0: 'b2', 1: 'c3', 2: 'd2'}
                  }
        crtable_1 = {}
        crtable_2 = {}
        crtable_1['table'] = table_1
        crtable_1['animd'] = {0:'A',1:'B',2:'C','A':0,'B':1,'C':2}
        crtable_2['table'] = table_2
        crtable_2['animd'] = {0:'B',1:'C',2:'D','B':0,'C':1,'D':2}
        colnameslist =['B','C']
        crtable = divide_two_crtables(crtable_1,crtable_2,colnameslist)
        >>> crtable
        {'animd': {0: 'A', 'A': 0}, 'table': {0: {0: 'a1'}}}
        >>> 
    '''
    if(colnameslist == []):
        refd1 = get_nameonly_refdict(crtable_1['animd'])
        refd2 = get_nameonly_refdict(crtable_2['animd'])
        for name in refd1:
            if(name in refd2):
                colnameslist.append(name)
            else:
                pass
    else:
        pass
    crtable_1 = naturalize_crtable(crtable_1)
    crtable_2 = naturalize_crtable(crtable_2)
    theothercolnameslist = get_the_other_names_list_via_names_list(colnameslist,crtable_1['animd'])
    image_sets_dict_1 = get_image_sets_dict(crtable_1,theothercolnameslist)
    image_sets = image_sets_dict_1['image_sets']
    mapping = image_sets_dict_1['mapping']
    projection_2 = project_crtable(colnameslist,crtable_2)
    projection_set = set({})
    for rownum in projection_2['table']:
        row = projection_2['table'][rownum]
        t = ltdict.to_tuple(row)
        projection_set.add(t)
    divtb = {}
    lmk = list(mapping.keys())[0]
    divtb['animd'] = {}
    for i in range(0,lmk.__len__()):
        divtb['animd'][lmk[i]] = i
        divtb['animd'][i] = lmk[i]
    divtb['knimd'] = {}
    divtb['vnimd'] = {}
    for k in divtb['animd']:
        if(k in crtable_1['knimd']):
            divtb['knimd'][k] = crtable_1['knimd'][k]
        else:
            divtb['vnimd'][k] = crtable_1['vnimd'][k]
    divtb['table'] = {}
    seq = 0
    for key in image_sets:
        if(image_sets[key] == projection_set):
            key = ltdict.tuple_to_ltdict(key)
            divtb['table'][seq] = key
    return(divtb)

def is_single_candidate_key(crtable,name):
    '''
        crtable = {}
        crtable['animd'] = {0: 'A', 1: 'B', 2: 'C', 3: 'E', 'C': 2, 'E': 3, 'A': 0, 'B': 1}
        crtable['table'] = {
            0: {0: 'a1', 1: 'b1', 2: 5, 3: 3}, 
            1: {0: 'a1', 1: 'b2', 2: 6, 3: 7}, 
            2: {0: 'a2', 1: 'b3', 2: 8, 3: 10}, 
            3: {0: 'a2', 1: 'b3', 2: 8, 3: 2}
        }
        is_single_candidate_key(crtable,'A')
        is_single_candidate_key(crtable,'B')
        is_single_candidate_key(crtable,'C')
        is_single_candidate_key(crtable,'E')
        >>> is_single_candidate_key(crtable,'A')
        False
        >>> is_single_candidate_key(crtable,'B')
        False
        >>> is_single_candidate_key(crtable,'C')
        False
        >>> is_single_candidate_key(crtable,'E')
        True
        >>> 
    '''
    indexeslist = get_indexes_list_via_names_list([name],crtable['animd'])
    colnum = indexeslist[0]
    cond = 1
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        keys = {colnum:row[colnum]}
        seqslist = get_seqslist_via_keys(keys,crtable)
        if(seqslist.__len__()==1):
            pass
        else:
            cond = 0
            break
    if(cond):
        return(True)
    else:
        return(False)

def is_candidate_key_combo(crtable,colnameslist):
    '''
        crtable = {}
        crtable['animd'] = {0: 'A', 1: 'B', 2: 'C', 3: 'E', 'C': 2, 'E': 3, 'A': 0, 'B': 1}
        crtable['table'] = {
            0: {0: 'a1', 1: 'b1', 2: 5, 3: 3}, 
            1: {0: 'a1', 1: 'b2', 2: 6, 3: 7}, 
            2: {0: 'a2', 1: 'b3', 2: 8, 3: 10}, 
            3: {0: 'a2', 1: 'b3', 2: 8, 3: 2}
        }
        colnameslist = ['A']
        is_candidate_key_combo(crtable,colnameslist)
        colnameslist = ['B']
        is_candidate_key_combo(crtable,colnameslist)
        colnameslist = ['C']
        is_candidate_key_combo(crtable,colnameslist)
        colnameslist = ['E']
        is_candidate_key_combo(crtable,colnameslist)
        colnameslist = ['B','C']
        is_candidate_key_combo(crtable,colnameslist)
        colnameslist = ['C','E']
        is_candidate_key_combo(crtable,colnameslist)
        colnameslist = ['A','B','C']
        is_candidate_key_combo(crtable,colnameslist)
        colnameslist = ['A','B','E']
        is_candidate_key_combo(crtable,colnameslist)
        >>> colnameslist = ['A']
        >>> is_candidate_key_combo(crtable,colnameslist)
        False
        >>> colnameslist = ['B']
        >>> is_candidate_key_combo(crtable,colnameslist)
        False
        >>> colnameslist = ['C']
        >>> is_candidate_key_combo(crtable,colnameslist)
        False
        >>> colnameslist = ['E']
        >>> is_candidate_key_combo(crtable,colnameslist)
        True
        >>> colnameslist = ['B','C']
        >>> is_candidate_key_combo(crtable,colnameslist)
        False
        >>> colnameslist = ['C','E']
        >>> is_candidate_key_combo(crtable,colnameslist)
        False
        >>> colnameslist = ['A','B','C']
        >>> is_candidate_key_combo(crtable,colnameslist)
        False
        >>> colnameslist = ['A','B','E']
        >>> is_candidate_key_combo(crtable,colnameslist)
        False
        >>> 
    '''
    rslts = []
    crtable = naturalize_crtable(crtable)
    total_cols = int(crtable['animd'].__len__() / 2)
    del_sets = set({})
    refd = get_indexonly_refdict(crtable['animd'])
    for k in refd:
        name = refd[k]
        cond = is_single_candidate_key(crtable,name)
        if(cond):
            bitmap = []
            for i in range(0,total_cols):
                if(k == i):
                    bitmap.append(1)
                else:
                    bitmap.append(0)
            del_sets.add(tuple(bitmap))
            rslts.append(tuple(name))
        else:
            pass
    for lv in range(2,colnameslist.__len__()+1):
        unhandled = utils.subset_bitmap(total_cols,lv)
        for seq in unhandled:
            bitmap = unhandled[seq]
            for bm in del_sets:
                cond = utils.bitmaplist_contain(bitmap,list(bm))
                if(cond):
                    pass
                else:
                    keys = {}
                    names =[]
                    for colnum in refd:
                        if(bitmap[colnum] == 1):
                            keys[colnum] = row[colnum]
                            names.append(crtable['animd'][colnum])
                        else:
                            pass
                    seqslist = get_seqslist_via_keys(keys,crtable)
                    if(seqslist.__len__() == 1):
                        rslts.append(tuple(sorted(names)))
                        del_sets.add(tuple(bitmap))
                    else:
                        pass
    cond = (tuple(sorted(colnameslist)) in rslts)
    return(cond)

def get_all_candidate_key_combo(crtable):
    '''
        crtable = {}
        crtable['animd'] = {0: 'A', 1: 'B', 2: 'C', 3: 'E', 'C': 2, 'E': 3, 'A': 0, 'B': 1}
        crtable['table'] = {
            0: {0: 'a1', 1: 'b1', 2: 5, 3: 3}, 
            1: {0: 'a1', 1: 'b2', 2: 6, 3: 7}, 
            2: {0: 'a2', 1: 'b3', 2: 8, 3: 10}, 
            3: {0: 'a2', 1: 'b3', 2: 8, 3: 2}
        }
        combos = get_all_candidate_key_combo(crtable)
        pobj(combos,fixed_indent=1)
        >>> combos = get_all_candidate_key_combo(crtable)
        >>> pobj(combos,fixed_indent=1)
        [('E', )]
        >>> 
    '''
    rslts = []
    crtable = naturalize_crtable(crtable)
    total_cols = int(crtable['animd'].__len__() / 2)
    del_sets = set({})
    refd = get_indexonly_refdict(crtable['animd'])
    for k in refd:
        name = refd[k]
        cond = is_single_candidate_key(crtable,name)
        if(cond):
            bitmap = []
            for i in range(0,total_cols):
                if(k == i):
                    bitmap.append(1)
                else:
                    bitmap.append(0)
            del_sets.add(tuple(bitmap))
            rslts.append(tuple(name))
        else:
            pass
    for lv in range(2,total_cols):
        unhandled = utils.subset_bitmap(total_cols,lv)
        for seq in unhandled:
            bitmap = unhandled[seq]
            for bm in del_sets:
                cond = utils.bitmaplist_contain(bitmap,list(bm))
                if(cond):
                    pass
                else:
                    keys = {}
                    names =[]
                    for colnum in refd:
                        if(bitmap[colnum] == 1):
                            keys[colnum] = refd[colnum]
                            names.append(crtable['animd'][colnum])
                        else:
                            pass
                    seqslist = get_seqslist_via_keys(keys,crtable)
                    if(seqslist.__len__() == 1):
                        rslts.append(tuple(sorted(names)))
                        del_sets.add(tuple(bitmap))
                    else:
                        pass
    return(rslts)

def max_rows_in_table_via_cols_dict(COLs):
    '''
    COLs = {
        0: {0: 'TBqESO', 1: 'apxjPB', 2: 'alYhP'}, 
        1: {0: 'jVymZLRRhj', 1: 'iSdHTH', 2: 'lOST'}, 
        2: {0: 'VlWVOMszE', 1: 'WuqefeO', 2: 'anQOLA'}
    }
    max_rows_in_table_via_cols_dict(COLs)
    >>> max_rows_in_table_via_cols_dict(COLs)
    3
    '''
    max = 0
    total_Cols = COLs.__len__()
    for i in range(0,total_Cols):
        if(COLs[i].__len__()>max):
            max = COLs[i].__len__()
    return(max)

def max_cols_in_table_via_rows_dict(ROWs):
    '''
    ROWs = {
          0: {0: 'TBqESO', 1: 'jVymZLRRhj', 2: 'VlWVOMszE'}, 
          1: {0: 'apxjPB', 1: 'iSdHTH', 2: 'WuqefeO'}, 
          2: {0: 'alYhP', 1: 'lOST', 2: 'anQOLA'}
         }
    max_cols_in_table_via_rows_dict(ROWs)
    >>> max_cols_in_table_via_rows_dict(ROWs)
    3
    '''
    
    max = 0
    total_Rows = ROWs.__len__()
    for i in range(0,total_Rows):
        if(ROWs[i].__len__()>max):
            max = ROWs[i].__len__()
    return(max)

def padding_rows(ROWs):
    '''
    ROWs = {
          0: {0: 'TBqESO', 1: 'jVymZLRRhj', 2: 'VlWVOMszE'}, 
          1: {0: 'apxjPB', 1: 'iSdHTH'}, 
          2: {0: 'alYhP'}
         }
    >>> padding_rows(ROWs)
    {
        0: {0: 'TBqESO', 1: 'jVymZLRRhj', 2: 'VlWVOMszE'}, 
        1: {0: 'apxjPB', 1: 'iSdHTH', 2: ''}, 
        2: {0: 'alYhP', 1: '', 2: ''}
    }
    >>> 
    '''
    max = max_cols_in_table_via_rows_dict(ROWs)
    total_Rows = ROWs.__len__()
    for i in range(0,total_Rows):
        if(ROWs[i].__len__()<max):
            for j in range(0,max):
                if j in ROWs[i]:
                    pass
                else:
                    ROWs[i][j] = ''
    return(ROWs)

def padding_cols(COLs):
    '''
    COLs = {
        0: {0: 'TBqESO', 1: 'apxjPB', 2: 'alYhP'}, 
        1: {0: 'jVymZLRRhj'}, 
        2: {0: 'VlWVOMszE', 1: 'WuqefeO', 2: 'anQOLA'}
    }
    >>> padding_cols(COLs)
    {
        0: {0: 'TBqESO', 1: 'apxjPB', 2: 'alYhP'}, 
        1: {0: 'jVymZLRRhj', 1: '', 2: ''}, 
        2: {0: 'VlWVOMszE', 1: 'WuqefeO', 2: 'anQOLA'}
    }
    >>> 
    '''
    max = max_rows_in_table_via_cols_dict(COLs)
    total_Cols = COLs.__len__()
    for i in range(0,total_Cols):
        if(COLs[i].__len__()<max):
            for j in range(0,max):
                if j in COLs[i]:
                    pass
                else:
                    COLs[i][j] = ''
    return(COLs)

def rows_to_cols(ROWs):
    '''
    ROWs = {
          0: {0: 'TBqESO', 1: 'jVymZLRRhj', 2: 'VlWVOMszE'}, 
          1: {0: 'apxjPB', 1: 'iSdHTH', 2: 'WuqefeO'}, 
          2: {0: 'alYhP', 1: 'lOST', 2: 'anQOLA'}
         }
    COLs = rows_to_cols(ROWs)
    COLs
    {
        0: {0: 'TBqESO', 1: 'apxjPB', 2: 'alYhP'}, 
        1: {0: 'jVymZLRRhj', 1: 'iSdHTH', 2: 'lOST'}, 
        2: {0: 'VlWVOMszE', 1: 'WuqefeO', 2: 'anQOLA'}
    }
    '''
    COLs = {}
    total_Cols = max_cols_in_table_via_rows_dict(ROWs)
    for i in range(0,total_Cols):
        COLs[i] = {}
    total_Rows = ROWs.__len__()
    for i in range(0,total_Cols):
        for j in range(0,total_Rows):
            COLs[i][j] = ROWs[j][i]
    return(COLs)

def cols_to_rows(COLs):
    '''
    COLs = 
    {
        0: {0: 'TBqESO', 1: 'apxjPB', 2: 'alYhP'}, 
        1: {0: 'jVymZLRRhj', 1: 'iSdHTH', 2: 'lOST'}, 
        2: {0: 'VlWVOMszE', 1: 'WuqefeO', 2: 'anQOLA'}
    }
    ROWs = cols_to_rows(COLs)
    ROWs
    {
          0: {0: 'TBqESO', 1: 'jVymZLRRhj', 2: 'VlWVOMszE'}, 
          1: {0: 'apxjPB', 1: 'iSdHTH', 2: 'WuqefeO'}, 
          2: {0: 'alYhP', 1: 'lOST', 2: 'anQOLA'}
    }
    '''
    ROWs = {}
    total_Rows = max_rows_in_table_via_cols_dict(COLs)
    for i in range(0,total_Rows):
        ROWs[i] = {}
    total_Cols = COLs.__len__()
    for i in range(0,total_Rows):
        for j in range(0,total_Cols):
            ROWs[i][j] = COLs[j][i]
    return(ROWs)

def display_table_via_rows(ROWs,**kwargs):
    '''
    ROWs = {
          0: {0: 'TBqESO', 1: 'jVymZLRRhj', 2: 'VlWVOMszE'}, 
          1: {0: 'apxjPB', 1: 'iSdHTH', 2: 'WuqefeO'}, 
          2: {0: 'alYhP', 1: 'lOST', 2: 'anQOLA'}
         }
    >>> display_table_via_rows(ROWs)
    +++++++++++++++++++++++++++++
    |TBqESO|jVymZLRRhj|VlWVOMszE|
    +++++++++++++++++++++++++++++
    |apxjPB|    iSdHTH|  WuqefeO|
    +++++++++++++++++++++++++++++
    | alYhP|      lOST|   anQOLA|
    +++++++++++++++++++++++++++++
    >>> 
    colormatrix = {
          0: {0: 'yellow', 1: 'green', 2: 'blue'}, 
          1: {0: 'red', 1: 'yellow', 2: 'green'}, 
          2: {0: 'blue', 1: 'yellow', 2: 'green'}
         }
    display_table_via_rows(ROWs,colormatrix =colormatrix)
    '''
    if('colcolorsdict' in kwargs):
        colored = 1
        colcolorsdict = kwargs['colcolorsdict']
        colormatrix = {}
        for rownum in ROWs:
            colormatrix[rownum] = {}
            for colnum in ROWs[rownum]:
                if(colnum in colcolorsdict):
                    colormatrix[rownum][colnum] = colcolorsdict[colnum]
                else:
                    colormatrix[rownum][colnum] = 'default'
    else:
        colored = 0
    if('colormatrix' in kwargs):
        colored = 1
        colormatrix = kwargs['colormatrix']
    else:
        pass
    COLs = rows_to_cols(ROWs)
    display_COLs = {}
    widths = {}
    widths[0] =  utils.dict_get_max_word_displaywidth(COLs[0])
    display_COLs[0] = {}
    for j in range(0,COLs[0].__len__()):
        display_COLs[0][j] = '|{0}|'.format(utils.str_prepend_basedon_displaywidth(COLs[0][j],widths[0]))
    for i in range(1,COLs.__len__()):
        widths[i] =  utils.dict_get_max_word_displaywidth(COLs[i])
        display_COLs[i] = {}
        for j in range(0,COLs[i].__len__()):
            display_COLs[i][j] = '{0}|'.format(utils.str_prepend_basedon_displaywidth(COLs[i][j],widths[i]))
    boundary = '+'
    for i in range (0,widths.__len__()):
        boundary = '{0}{1}+'.format(boundary,'+'*widths[i])
    print(boundary)
    #######
    windows = utils.is_win()
    ######
    for i in range(0,ROWs.__len__()):
        if(windows):
            s = ''
            color_sec ={}
            cursor = 0
            for j in range(0,COLs.__len__()):
                if(colored):
                    s = s + display_COLs[j][i]
                    length = display_COLs[j][i].__len__()
                    color_sec[j+1] = (cursor,cursor+length - 1,colormatrix[i][j])
                    cursor = cursor+length
                else:
                    print(display_COLs[j][i],end='')
            if(colored):
                s = s +'\n'+boundary
                color_sec[COLs.__len__()+1] = (cursor,cursor+boundary.__len__(),"white")
                spaint.paint(s,color_sec=color_sec)
            else:
                print('\n',end='')
                print(boundary)
        else:
            for j in range(0,COLs.__len__()):
                ####
                #print(display_COLs[j][i])
                ####
                if(colored):
                    #print(spaint.paint_str(display_COLs[j][i],single_color=colormatrix[i][j]),end='')
                    spaint.paint(display_COLs[j][i],single_color=colormatrix[i][j],lend='',bg=0)
                else:
                    print(display_COLs[j][i],end='')
            print('\n',end='')
            print(boundary)
    if('returned' in kwargs):
        returned = kwargs['returned']
    else:  
        returned = False
    if(returned):
        return(display_COLs)
    else:
        return(None)

def display_table_via_cols(COLs,**kwargs):
    '''
    COLs = 
    {
        0: {0: 'TBqESO', 1: 'apxjPB', 2: 'alYhP'}, 
        1: {0: 'jVymZLRRhj', 1: 'iSdHTH', 2: 'lOST'}, 
        2: {0: 'VlWVOMszE', 1: 'WuqefeO', 2: 'anQOLA'}
    }
    >>> display_table_via_cols(COLs)
    +++++++++++++++++++++++++++++
    |TBqESO|jVymZLRRhj|VlWVOMszE|
    +++++++++++++++++++++++++++++
    |apxjPB|    iSdHTH|  WuqefeO|
    +++++++++++++++++++++++++++++
    | alYhP|      lOST|   anQOLA|
    +++++++++++++++++++++++++++++
    >>> 
    '''
    if('rowcolorsdict' in kwargs):
        colored = 1
        rowcolorsdict = kwargs['rowcolorsdict']
        colormatrix = {}
        for rownum in ROWs:
            colormatrix[rownum] = {}
            for colnum in ROWs[rownum]:
                if(colnum in rowcolorsdict):
                    colormatrix[rownum][colnum] = rowcolorsdict[colnum]
                else:
                    colormatrix[rownum][colnum] = 'default'
    else:
        colored = 0
    if('colormatrix' in kwargs):
        colored = 1
        colormatrix = kwargs['colormatrix']
    else:
        pass
    ROWs = rows_to_cols(COLs)
    display_COLs = {}
    widths = {}
    widths[0] =  utils.dict_get_max_word_displaywidth(COLs[0])
    display_COLs[0] = {}
    for j in range(0,COLs[0].__len__()):
        display_COLs[0][j] = '|{0}|'.format(utils.str_prepend_basedon_displaywidth(COLs[0][j],widths[0]))
    for i in range(1,COLs.__len__()):
        widths[i] =  utils.dict_get_max_word_displaywidth(COLs[i])
        display_COLs[i] = {}
        for j in range(0,COLs[i].__len__()):
            display_COLs[i][j] = '{0}|'.format(utils.str_prepend_basedon_displaywidth(COLs[i][j],widths[i]))
    boundary = '+'
    for i in range (0,widths.__len__()):
        boundary = '{0}{1}+'.format(boundary,'+'*widths[i])
    print(boundary)
    ####
    windows = utils.is_win()
    ####
    for i in range(0,ROWs.__len__()):
        if(windows):
            s = ''
            color_sec ={}
            cursor = 0
            for j in range(0,COLs.__len__()):
                if(colored):
                    s = s + display_COLs[j][i]
                    length = display_COLs[j][i].__len__()
                    color_sec[j+1] = (cursor,cursor+length - 1,colormatrix[i][j])
                    cursor = cursor+length
                else:
                    print(display_COLs[j][i],end='')
            if(colored):
                s = s +'\n'+boundary
                color_sec[COLs.__len__()+1] = (cursor,cursor+boundary.__len__(),"white")
                spaint.paint(s,color_sec=color_sec)
            else:
                print('\n',end='')
                print(boundary)
        else:
            for j in range(0,COLs.__len__()):
                if(colored):
                    #print(spaint.paint_str(display_COLs[j][i],single_color=colcolorsdict[i][j]),end='')
                    spaint.paint(display_COLs[j][i],single_color=colormatrix[i][j],lend='',bg=0)
                else:
                    print(display_COLs[j][i],end='')
            print('\n',end='')
            print(boundary)
    if('returned' in kwargs):
        returned = kwargs['returned']
    else:
        returned = False
    if(returned):
        return(display_COLs)
    else:
        return(None)


def ltlyr2colorstr(lyr,color_layer):
    s = ""
    for i in range(len(lyr)):
        word = spaint.paint(str(lyr[i]),single_color=color_layer[i],lend='',rtrn=True)
        s = s + word
    return(s)

def ltmat2colorstr(tbl,colormat):
    s = ""
    for i in range(len(tbl)):
        lyr = tbl[i]
        color_layer = colormat[i]
        line = ltlyr2colorstr(lyr,color_layer) 
        s = s + line + "\n"
    return(s.strip("\n"))
        


def show_crtable(crtable,**kwargs):
    '''
        crtable = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['knimd'] = creat_mirror_dict({0: 'size', 2: 'language'})
        crtable['vnimd'] = creat_mirror_dict({1: 'color',3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        >>> show_crtable(crtable)
        +++++++++++++++++++++++++++++++++++++++
        |  size|    color|language|     expire|
        +++++++++++++++++++++++++++++++++++++++
        |   500|    green| espanol|2018-dec-01|
        +++++++++++++++++++++++++++++++++++++++
        |    74|    green| chinese|2017-oct-01|
        +++++++++++++++++++++++++++++++++++++++
        |   300|darkblack| spanish|2017-oct-01|
        +++++++++++++++++++++++++++++++++++++++
        |100000|     blue| english|2018-dec-01|
        +++++++++++++++++++++++++++++++++++++++
        >>> 
    '''
    #
    crtable = naturalize_crtable(crtable)
    #
    display_tb = {}
    display_tb[0] = get_indexonly_refdict(crtable['animd'])
    if('table' in crtable):
        for i in range(1,crtable['table'].__len__()+1):
            display_tb[i] = crtable['table'][i-1]
    else:
        pass
    colored = 0
    colcolorsdict = {}
    if('knimd' in crtable):
        colored = 1
        kcd = get_indexonly_refdict(crtable['knimd'])
        for i in kcd :
            colcolorsdict[i] = 'blue'
    if('vnimd' in crtable):
        colored = 1
        vcd =  get_indexonly_refdict(crtable['vnimd'])
        for i in vcd :
            colcolorsdict[i] = 'yellow'
    if(colored):
        rslt = display_table_via_rows(display_tb,colcolorsdict=colcolorsdict,**kwargs)
    else:
        rslt = display_table_via_rows(display_tb,**kwargs)
    if(rslt == None):
        pass
    else:
        rslt = rows_to_cols(rslt)
        cm = [colcolorsdict] * len(rslt)
        rslt = ltmat2colorstr(rslt,cm)
    return(rslt)


def lm2ltdm(m):
    for i in range(len(m)):
        m[i] = ltdict.list2ltdict(m[i])
    m = ltdict.list2ltdict(m)
    return(m)


def shmat(m,*args,**kwargs):
    m = lm2ltdm(m)
    lyr_lngth = len(m[0])
    dflt_colors = [("green" if(i%2 ==0) else "yellow") for i in range(lyr_lngth)]
    colors = args[0] if(len(args)>0) else dflt_colors
    colors = ltdict.list2ltdict(colors)
    rslt = display_table_via_rows(m,colcolorsdict=colors,**kwargs)
    if(rslt == None):
        pass
    else:
        rslt = rows_to_cols(rslt)
        cm = [colors] * len(rslt)
        rslt = ltmat2colorstr(rslt,cm)
    return(rslt)




#Class 
class crtable():
    def __init__(self,**kwargs):
        '''
            import xdict.CrtableLib.crtable as xcr
            colnameslist = ['size','color','language','expire']
            keynameslist = ['size','language']
            table = {}
            table[0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
            table[1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
            table[2] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
            crtb = xcr.crtable(colnameslist = colnameslist,table=table,keynameslist = keynameslist)
            crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
            
            import copy
            crtb.crtable
            {'animd': {0: 'size', 1: 'color', 2: 'language', 'size': 0, 3: 'expire', 'expire': 3, 'color': 1, 'language': 2}, 'knimd': {0: 'size', 2: 'language', 'size': 0, 'language': 2}, 'vnimd': {'expire': 3, 3: 'expire', 'color': 1, 1: 'color'}, 'table': {0: {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}, 1: {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}, 2: {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}}}
            crtable = copy.deepcopy(crtb.crtable)
            crtb2 = xcr.crtable(crtable=crtable)
            crtb2
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
                 
        '''
        self.crtable = {}
        self.crtable['table'] = {}
        self.crtable['animd'] = {}
        self.colnameslist = []
        self.keynameslist = []
        self.valuenameslist = []
        if('debug' in kwargs):
            self.debug = kwargs['debug']
        else:
            self.debug = False
        if('crtable' in kwargs):
            ncrtb = copy.deepcopy(kwargs['crtable'])
            self.crtable = ncrtb
            self.keynameslist = ltdict.to_list(get_indexonly_refdict(ncrtb['knimd']))
            vrefd = get_indexonly_refdict(ncrtb['vnimd'])
            vrefd = ltdict.naturalize_intkeydict(vrefd)
            self.valuenameslist = ltdict.to_list(vrefd)
            self.colnameslist = ltdict.to_list(get_indexonly_refdict(ncrtb['animd']))
        else:
            if('colnameslist' in kwargs):
                ####
                colnameslist = copy.deepcopy(kwargs['colnameslist'])
                for k in range(0,colnameslist.__len__()):
                    colnameslist[k] = str(colnameslist[k]) 
                ####
                refdict = ltdict.list2ltdict(colnameslist)
                self.crtable['animd'] = creat_mirror_dict(refdict)
                self.colnameslist = colnameslist
            else:
                pass
            if('table' in kwargs):
            ####
                table = copy.deepcopy(kwargs['table'])
                if(utils.is_list(table)):
                    table = ltdict.list2ltdict(table)
                else:
                    pass
                for kseq in table:
                    eachrow = copy.deepcopy(table[kseq])
                    if(utils.is_list(eachrow)):
                        table[kseq] = ltdict.list2ltdict(eachrow)
                    else:
                        pass
            ####
            #
            ####
                self.crtable['table'] = nametable_to_indextable(table,self.crtable['animd'])
            else:
                pass
            condk = ('keynameslist' in kwargs)
            ####
            if(condk):
                keynameslist = copy.deepcopy(kwargs['keynameslist'])
                for k in range(0,keynameslist.__len__()):
                    keynameslist[k] = str(keynameslist[k])
                self.keynameslist = keynameslist
            else:
                pass
            ####
            condv = ('valuenameslist' in kwargs)
            ####
            if(condv):
                valuenameslist = copy.deepcopy(kwargs['valuenameslist'])
                for k in range(0,valuenameslist.__len__()):
                    valuenameslist[k] = str(valuenameslist[k])
                self.valuenameslist = valuenameslist
            else:
                pass
            ####
            if(condk & condv):
                self.crtable['knimd'] = get_mirror_dict_via_nameslist(kwargs['keynameslist'],self.crtable['animd'])
                self.crtable['vnimd'] = get_the_other_mirror_dict_via_nameslist(kwargs['keynameslist'],self.crtable['animd'])
            elif(condk):
                self.crtable['knimd'] = get_mirror_dict_via_nameslist(kwargs['keynameslist'],self.crtable['animd'])
                self.crtable['vnimd'] = get_the_other_mirror_dict_via_nameslist(kwargs['keynameslist'],self.crtable['animd'])
                #####
                vrefd = get_indexonly_refdict(self.crtable['vnimd'])
                vrefd_items_list = sorted(vrefd.items(),key=lambda a_tuple:a_tuple[0])
                valuenameslist = list(map(lambda a_tuple:a_tuple[1],vrefd_items_list))
                self.valuenameslist = valuenameslist
                #####
            elif(condv):
                self.crtable['vnimd'] = get_mirror_dict_via_nameslist(kwargs['valuenameslist'],self.crtable['animd'])
                self.crtable['knimd'] = get_the_other_mirror_dict_via_nameslist(kwargs['valuenameslist'],self.crtable['animd'])
                #####
                krefd = get_indexonly_refdict(self.crtable['vnimd'])
                krefd_items_list = sorted(krefd.items(),key=lambda a_tuple:a_tuple[0])
                keynameslist = list(map(lambda a_tuple:a_tuple[1],krefd_items_list))
                self.keynameslist = keynameslist
                #####
            else:
                self.crtable['knimd'] = {}
                self.crtable['vnimd'] = self.crtable['animd'] 
    def __repr__(self):
        '''
            crtb
        '''
        show_crtable(self.crtable,returned=True)
        if(self.debug):
            spaint.paint("====keys====:",single_color='blue')
            spaint.paint("    :{0}".format(get_nameonly_refdict(self.crtable['knimd'])),single_color='blue')
            spaint.paint("====values==:",single_color='yellow')
            spaint.paint("    :{0}".format(get_nameonly_refdict(self.crtable['vnimd'])),single_color='yellow')
        else:
            pass
        #if(spaint.is_win()):
            return('')
        #else:
        #    return(rslt)
    ## select
    def __getitem__(self,keys):
        '''
            from xdict.jprint import pobj
            keys_1 = {'language':'espanol','color':'green'}
            values_1 = crtb[keys_1]
            keys_2 = {'color':'green'}
            values_2 = crtb[keys_2]
            values_1
            pobj(values_1)
            values_2
            pobj(values_2)
            >>> values_1
            [{'size': 500, 'expire': '2018-dec-01'}, {'size': 74, 'expire': '2017-oct-01'}]
            >>> pobj(values_1)
            [
             {
              'size': 500, 
              'expire': '2018-dec-01'
             }, 
             {
              'size': 74, 
              'expire': '2017-oct-01'
             }
            ]
            >>> 
            >>> 
            >>> values_2
            [{'size': 500, 'language': 'espanol', 'expire': '2018-dec-01'}, {'size': 74, 'language': 'chinese', 'expire': '2017-oct-01'}, {'size': 74, 'language': 'espanol', 'expire': '2017-oct-01'}]
            >>> pobj(values_2)
            [
             {
              'size': 500, 
              'language': 'espanol', 
              'expire': '2018-dec-01'
             }, 
             {
              'size': 74, 
              'language': 'chinese', 
              'expire': '2017-oct-01'
             }, 
             {
              'size': 74, 
              'language': 'espanol', 
              'expire': '2017-oct-01'
             }
            ]
            >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        rslt = []
        for i in seqslist:
            values = get_values_in_attribs(keys,self.crtable['table'][i],self.crtable['animd'])
            rslt.append(values)
        return(rslt)
    def select_rownums(self,keys):
        '''
            crtb
            keysorvalues = {'color':'green'}
            rownums = crtb.select_rownums(keysorvalues)
            rownums
            keysorvalues = {'language':'espanol'}
            rownums = crtb.select_rownums(keysorvalues)
            rownums
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
            
            >>> keysorvalues = {'color':'green'}
            >>> rownums = crtb.select_rownums(keysorvalues)
            >>> rownums
            [0, 1, 2]
            >>> keysorvalues = {'language':'espanol'}
            >>> rownums = crtb.select_rownums(keysorvalues)
            >>> rownums
            [0, 2]
            >>> 
        '''
        rownumslist = get_seqslist_via_keys(keys,self.crtable)
        return(rownumslist)
    def select_attribs(self,keys):
        '''
            crtb
            keysorvalues = {'color':'green'}
            attribs = crtb.select_attribs(keysorvalues)
            pobj(attribs)
            keysorvalues = {'language':'espanol'}
            attribs = crtb.select_attribs(keysorvalues)
            pobj(attribs)
        >>> crtb
        +++++++++++++++++++++++++++++++++
        |size|color|language|     expire|
        +++++++++++++++++++++++++++++++++
        | 500|green| espanol|2018-dec-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| chinese|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| espanol|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        ====keys====:
            :{'size': 0, 'language': 2}
        ====values==:
            :{'color': 1, 'expire': 3}
        
        >>> keysorvalues = {'color':'green'}
        >>> attribs = crtb.select_attribs(keysorvalues)
        >>> pobj(attribs)
        [
         {
          0: 500, 
          1: 'green', 
          2: 'espanol', 
          3: '2018-dec-01'
         }, 
         {
          0: 74, 
          1: 'green', 
          2: 'chinese', 
          3: '2017-oct-01'
         }, 
         {
          0: 74, 
          1: 'green', 
          2: 'espanol', 
          3: '2017-oct-01'
         }
        ]
        >>> keysorvalues = {'language':'espanol'}
        >>> attribs = crtb.select_attribs(keysorvalues)
        >>> pobj(attribs)
        [
         {
          0: 500, 
          1: 'green', 
          2: 'espanol', 
          3: '2018-dec-01'
         }, 
         {
          0: 74, 
          1: 'green', 
          2: 'espanol', 
          3: '2017-oct-01'
         }
        ]
        >>> 
        >>> 
        
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        rslt = []
        for i in seqslist:
            attribs = self.crtable['table'][i]
            rslt.append(attribs)
        return(rslt)
    def select_values(self,keys):
        '''
            crtb
            keys = {'language':'espanol'}
            values = crtb.select_values(keys)
            pobj(values)
            keys = {'language':'espanol','size':74}
            values = crtb.select_values(keys)
            pobj(values)
        >>> 
        >>> crtb
        +++++++++++++++++++++++++++++++++
        |size|color|language|     expire|
        +++++++++++++++++++++++++++++++++
        | 500|green| espanol|2018-dec-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| chinese|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| espanol|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        ====keys====:
            :{'size': 0, 'language': 2}
        ====values==:
            :{'color': 1, 'expire': 3}
        
        >>> keys = {'language':'espanol'}
        >>> values = crtb.select_values(keys)
        >>> pobj(values)
        [
         {
          'size': 500, 
          'color': 'green', 
          'expire': '2018-dec-01'
         }, 
         {
          'size': 74, 
          'color': 'green', 
          'expire': '2017-oct-01'
         }
        ]
        >>> keys = {'language':'espanol','size':74}
        >>> values = crtb.select_values(keys)
        >>> pobj(values)
        [
         {
          'color': 'green', 
          'expire': '2017-oct-01'
         }
        ]
        >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        rslt = []
        for i in seqslist:
            values = get_values_in_attribs(keys,self.crtable['table'][i],self.crtable['animd'])
            rslt.append(values)
        return(rslt)
    def choose_cols(self,colslist):
        '''
        crtb
        colslist = [0,2]
        subcols = crtb.choose_cols(colslist)
        xcr.show_crtable(subcols)
        colslist = ['size','color']
        subcols = crtb.choose_cols(colslist)
        xcr.show_crtable(subcols)
        >>> 
        >>> crtb
        +++++++++++++++++++++++++++++++++
        |size|color|language|     expire|
        +++++++++++++++++++++++++++++++++
        | 500|green| espanol|2018-dec-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| chinese|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| espanol|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        ====keys====:
            :{'size': 0, 'language': 2}
        ====values==:
            :{'color': 1, 'expire': 3}
        
        >>> colslist = [0,2]
        >>> subcols = crtb.choose_cols(colslist)
        >>> xcr.show_crtable(subcols)
        +++++++++++++++
        |size|language|
        +++++++++++++++
        | 500| espanol|
        +++++++++++++++
        |  74| chinese|
        +++++++++++++++
        |  74| espanol|
        +++++++++++++++
        >>> colslist = ['size','color']
        >>> subcols = crtb.choose_cols(colslist)
        >>> xcr.show_crtable(subcols)
        ++++++++++++
        |size|color|
        ++++++++++++
        | 500|green|
        ++++++++++++
        |  74|green|
        ++++++++++++
        |  74|green|
        ++++++++++++
        >>> 
        '''
        if(utils.is_int(colslist[0])):
            ncrtb = get_newcrtable_via_colnumslist(colslist,self.crtable)
        else:
            ncrtb = get_newcrtable_via_colnameslist(colslist,self.crtable)
        return(ncrtb)
    ####
    def col(self,colname,show=1):
        '''
            crtb
            crtb.col('color')
            crtb.col('color',show=0)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'language': 2, 'size': 0}
            ====values==:
                :{'color': 1, 'expire': 3}
            
            >>> crtb.col('color')
            +++++++
            |color|
            +++++++
            |green|
            +++++++
            |green|
            +++++++
            |green|
            +++++++
            ['green', 'green', 'green']
            >>> crtb.col('color',show=0)
            ['green', 'green', 'green']
            >>> 
        '''
        colslist = [colname]
        subcols = self.choose_cols(colslist)
        if(show):
            show_crtable(subcols)
        col = []
        table = subcols['table']
        for i in range(0,table.__len__()):
            col.append(table[i][0])
        return(col)
    def cols(self,subcolnameslist,show=1):
        '''
            crtb
            crtb.cols(['size','language'])
            crtb.cols(['size','language'],show=0)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> crtb.cols(['size','language'])
            +++++++++++++++
            |size|language|
            +++++++++++++++
            | 500| espanol|
            +++++++++++++++
            |  74| chinese|
            +++++++++++++++
            |  74| espanol|
            +++++++++++++++
            {'size': [500, 74, 74], 'language': ['espanol', 'chinese', 'espanol']}
            >>> crtb.cols(['size','language'],show=0)
            {'size': [500, 74, 74], 'language': ['espanol', 'chinese', 'espanol']}

        '''
        subcols = self.choose_cols(subcolnameslist)
        if(show):
            show_crtable(subcols)
        cols = {}
        table = subcols['table']
        nrefd = get_nameonly_refdict(subcols['animd'])
        for name in nrefd:
            colnum = nrefd[name]
            col = []
            for i in range(0,table.__len__()):
                col.append(table[i][colnum])
                cols[name] = col
        return(cols)
    def sub(self,subcolnameornumslist,subrownumslist,show=1):
        '''
            crtb
            crtb.sub(['color','language'],[1,2])
            crtb.sub(['color','language'],[1,2],show=0)

            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|black|  korean|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
            
            >>> crtb.sub(['color','language'],[1,2])
            ++++++++++++++++
            |color|language|
            ++++++++++++++++
            |green| chinese|
            ++++++++++++++++
            |green| espanol|
            ++++++++++++++++
            {'vnimd': {0: 'color', 'color': 0}, 'animd': {0: 'color', 1: 'language', 'color': 0, 'language': 1}, 'knimd': {1: 'language', 'language': 1}, 'table': {0: {0: 'green', 1: 'chinese'}, 1: {0: 'green', 1: 'espanol'}}}
            >>> crtb.sub(['color','language'],[1,2],show=0)
            {'vnimd': {0: 'color', 'color': 0}, 'animd': {0: 'color', 1: 'language', 'color': 0, 'language': 1}, 'knimd': {1: 'language', 'language': 1}, 'table': {0: {0: 'green', 1: 'chinese'}, 1: {0: 'green', 1: 'espanol'}}}
            >>> 

        '''
        subcols_crtable = self.choose_cols(subcolnameornumslist)
        ncrtb = copy.deepcopy(subcols_crtable)
        realrownumslist = sorted(list(subcols_crtable['table'].keys()))
        ncrtb['table'] = {}
        seq = 0
        for i in subrownumslist:
            ncrtb['table'][seq] = subcols_crtable['table'][realrownumslist[i]]
            seq = seq + 1
        if(show):
            show_crtable(ncrtb)
        else:
            pass
        return(ncrtb)
    ####
    def choose_rows(self,rownumslist):
        '''
            crtb
            rownumslist = [1,2]
            subrows = crtb.choose_rows(rownumslist)
            xcr.show_crtable(subrows)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> rownumslist = [1,2]
            >>> subrows = crtb.choose_rows(rownumslist)
            >>> xcr.show_crtable(subrows)
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            >>> 
        '''
        ncrtb = copy.deepcopy(self.crtable)
        realrownumslist = sorted(list(self.crtable['table'].keys()))
        ncrtb['table'] = {}
        seq = 0
        for i in rownumslist:
            ncrtb['table'][seq] = self.crtable['table'][realrownumslist[i]]
            seq = seq + 1
        return(ncrtb)
    ## prepend append
    def append_row(self,row):
        '''
            crtb
            row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
            crtb.append_row(row)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
            >>> crtb.append_row(row)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 700| pink| espanol|       None|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> 
            
        '''
        self.crtable = append_row(row,self.crtable)
    def append_rows(self,rows):
        '''
            crtb
            rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
                    {'size': 555, 'color': 'yellow', 'language': 'korean'}]
            crtb.append_rows(rows)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 700| pink| espanol|       None|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
            ...         {'size': 555, 'color': 'yellow', 'language': 'korean'}]
            >>> crtb.append_rows(rows)
            >>> crtb
            ++++++++++++++++++++++++++++++++++
            |size| color|language|     expire|
            ++++++++++++++++++++++++++++++++++
            | 500| green| espanol|2018-dec-01|
            ++++++++++++++++++++++++++++++++++
            |  74| green| chinese|2017-oct-01|
            ++++++++++++++++++++++++++++++++++
            |  74| green| espanol|2017-oct-01|
            ++++++++++++++++++++++++++++++++++
            | 700|  pink| espanol|       None|
            ++++++++++++++++++++++++++++++++++
            | 555|yellow| chinese|       None|
            ++++++++++++++++++++++++++++++++++
            | 555|yellow|  korean|       None|
            ++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
        '''
        self.crtable = append_rows(rows,self.crtable)
    def prepend_row(self,row):
        '''
            crtb
            row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
            crtb.prepend_row(row)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'language': 2, 'size': 0}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
            >>> crtb.prepend_row(row)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 700| pink| espanol|       None|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'language': 2, 'size': 0}
            ====values==:
                :{'expire': 3, 'color': 1}
            >>> 
        '''
        self.crtable = prepend_row(row,self.crtable)
    def prepend_rows(self,rows):
        '''
            crtb
            rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
                    {'size': 555, 'color': 'yellow', 'language': 'korean'}]
            crtb.prepend_rows(rows)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 700| pink| espanol|       None|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'language': 2, 'size': 0}
            ====values==:
                :{'expire': 3, 'color': 1}
            >>> rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
            ...         {'size': 555, 'color': 'yellow', 'language': 'korean'}]
            >>> crtb.prepend_rows(rows)
            >>> crtb
            ++++++++++++++++++++++++++++++++++
            |size| color|language|     expire|
            ++++++++++++++++++++++++++++++++++
            | 555|yellow| chinese|       None|
            ++++++++++++++++++++++++++++++++++
            | 555|yellow|  korean|       None|
            ++++++++++++++++++++++++++++++++++
            | 700|  pink| espanol|       None|
            ++++++++++++++++++++++++++++++++++
            | 500| green| espanol|2018-dec-01|
            ++++++++++++++++++++++++++++++++++
            |  74| green| chinese|2017-oct-01|
            ++++++++++++++++++++++++++++++++++
            |  74| green| espanol|2017-oct-01|
            ++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'language': 2, 'size': 0}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> 
        '''
        self.crtable = prepend_rows(rows,self.crtable)
    def append_col(self,col):
        '''
            crtb
            col = {'owner':['dli','dli','dli','dli']}
            crtb.append_col(col)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'language': 2, 'size': 0}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> col = {'owner':['dli','dli','dli','dli']}
            >>> crtb.append_col(col)
            >>> crtb
            +++++++++++++++++++++++++++++++++++++++
            |size|color|language|     expire|owner|
            +++++++++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|  dli|
            +++++++++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|  dli|
            +++++++++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|  dli|
            +++++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'language': 2, 'size': 0}
            ====values==:
                :{'expire': 3, 'owner': 4, 'color': 1}
            
            >>> 
        '''
        self.crtable = append_col(col,self.crtable)
    def append_cols(self,cols):
        '''
            crtb
            cols = [{'id':['2271','2272','2273','2274']},
                    {'tid':['t1','t2','t3','t4']}]
            crtb.append_cols(cols)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            >>> cols = [{'id':['2271','2272','2273','2274']},
            ...         {'tid':['t1','t2','t3','t4']}]
            >>> crtb.append_cols(cols)
            >>> 
            >>> crtb
            ++++++++++++++++++++++++++++++++++++++++++
            |size|color|language|     expire|  id|tid|
            ++++++++++++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|2271| t1|
            ++++++++++++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|2272| t2|
            ++++++++++++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|2273| t3|
            ++++++++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'id': 4, 'tid': 5, 'color': 1}
        '''
        self.crtable = append_cols(cols,self.crtable)
    def prepend_col(self,col):
        '''
            crtb
            col = {'owner':['dli','dli','dli','dli']}
            crtb.prepend_col(col)
            crtb
            >>> crtb
            ++++++++++++++++++++++++++++++++++++++++++
            |size|color|language|     expire|  id|tid|
            ++++++++++++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|2271| t1|
            ++++++++++++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|2272| t2|
            ++++++++++++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|2273| t3|
            ++++++++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'id': 4, 'tid': 5, 'color': 1}
            
            >>> col = {'owner':['dli','dli','dli','dli']}
            >>> crtb.prepend_col(col)
            >>> crtb
            ++++++++++++++++++++++++++++++++++++++++++++++++
            |owner|size|color|language|     expire|  id|tid|
            ++++++++++++++++++++++++++++++++++++++++++++++++
            |  dli| 500|green| espanol|2018-dec-01|2271| t1|
            ++++++++++++++++++++++++++++++++++++++++++++++++
            |  dli|  74|green| chinese|2017-oct-01|2272| t2|
            ++++++++++++++++++++++++++++++++++++++++++++++++
            |  dli|  74|green| espanol|2017-oct-01|2273| t3|
            ++++++++++++++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'id': 4, 'tid': 5, 'color': 1}
            >>> 
        '''
        self.crtable = prepend_col(col,self.crtable)
    def prepend_cols(self,cols):
        '''
            crtb
            cols = [{'nickname':['kk','vv','tt','dd']},
                    {'uid':['u1','u2','u3','u4']}]
            
            crtb.prepend_cols(cols)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
            >>> 
            >>> cols = [{'nickname':['kk','vv','tt','dd']},
            ...         {'uid':['u1','u2','u3','u4']}]
            >>> 
            >>> crtb.prepend_cols(cols)
            >>> crtb
            ++++++++++++++++++++++++++++++++++++++++++++++
            |nickname|uid|size|color|language|     expire|
            ++++++++++++++++++++++++++++++++++++++++++++++
            |      kk| u1| 500|green| espanol|2018-dec-01|
            ++++++++++++++++++++++++++++++++++++++++++++++
            |      vv| u2|  74|green| chinese|2017-oct-01|
            ++++++++++++++++++++++++++++++++++++++++++++++
            |      tt| u3|  74|green| espanol|2017-oct-01|
            ++++++++++++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
        '''
        self.crtable = prepend_cols(cols,self.crtable)
    ## modify
    def __setitem__(self,keys,values):
        '''
            crtb
            keys = {'size':88,'language':'korean'}
            values = {'color':'azure'}
            crtb[keys] = values
            crtb
            keys = {'language':'espanol'}
            values = {'color':'darkblack'}
            crtb[keys] = values
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
            
            >>> keys = {'size':88,'language':'korean'}
            >>> values = {'color':'azure'}
            >>> crtb[keys] = values
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  88|azure|  korean|       None|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
            
            >>> keys = {'language':'espanol'}
            >>> values = {'color':'darkblack'}
            >>> crtb[keys] = values
            >>> crtb
            +++++++++++++++++++++++++++++++++++++
            |size|    color|language|     expire|
            +++++++++++++++++++++++++++++++++++++
            | 500|darkblack| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++++++
            |  74|    green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++++++
            |  74|darkblack| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++++++
            |  88|    azure|  korean|       None|
            +++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'color': 1, 'expire': 3}
            >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            row = utils.dict_extend(keys,values)
            self.crtable = append_row(row,self.crtable)
        else:
            self.crtable = modify_rows_via_keys(keys,self.crtable,values)
    def modify_first_row(self,keys,values):
        '''
        crtb
        keys = {'size':74}
        values = {'color':'purple'}
        crtb.modify_first_row(keys,values)
        crtb
        >>> crtb
        +++++++++++++++++++++++++++++++++
        |size|color|language|     expire|
        +++++++++++++++++++++++++++++++++
        | 500|green| espanol|2018-dec-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| chinese|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        |  74|green| espanol|2017-oct-01|
        +++++++++++++++++++++++++++++++++
        ====keys====:
            :{'size': 0, 'language': 2}
        ====values==:
            :{'expire': 3, 'color': 1}
        >>> 
        >>> keys = {'size':74}
        >>> values = {'color':'purple'}
        >>> crtb.modify_first_row(keys,values)
        >>> crtb
        ++++++++++++++++++++++++++++++++++
        |size| color|language|     expire|
        ++++++++++++++++++++++++++++++++++
        | 500| green| espanol|2018-dec-01|
        ++++++++++++++++++++++++++++++++++
        |  74|purple| chinese|2017-oct-01|
        ++++++++++++++++++++++++++++++++++
        |  74| green| espanol|2017-oct-01|
        ++++++++++++++++++++++++++++++++++
        ====keys====:
            :{'size': 0, 'language': 2}
        ====values==:
            :{'expire': 3, 'color': 1}
        >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            pass
        else:
            seq = seqslist[0]
            self.crtable = modify_rows_via_seq(seq,self.crtable,values)
    def modify_last_row(self,keys,values):
        '''
            crtb
            keys = {'size':74}
            values = {'color':'purple'}
            crtb.modify_last_row(keys,values)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            
            >>> keys = {'size':74}
            >>> values = {'color':'purple'}
            >>> crtb.modify_last_row(keys,values)
            >>> crtb
            ++++++++++++++++++++++++++++++++++
            |size| color|language|     expire|
            ++++++++++++++++++++++++++++++++++
            | 500| green| espanol|2018-dec-01|
            ++++++++++++++++++++++++++++++++++
            |  74| green| chinese|2017-oct-01|
            ++++++++++++++++++++++++++++++++++
            |  74|purple| espanol|2017-oct-01|
            ++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'size': 0, 'language': 2}
            ====values==:
                :{'expire': 3, 'color': 1}
            >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            pass
        else:
            seq = seqslist[-1]
            self.crtable = modify_rows_via_seq(seq,self.crtable,values)
    def modify_specific_row(self,keys,values,whichrow):
        '''
            crtb
            keys = {'color':'green'}
            values = {'language':'korean'}
            crtb.modify_specific_row(keys,values,1)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            >>> 
            >>> keys = {'color':'green'}
            >>> values = {'language':'korean'}
            >>> crtb.modify_specific_row(keys,values,1)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green|  korean|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            pass
        else:
            seq = seqslist[whichrow]
            self.crtable = modify_rows_via_seq(seq,self.crtable,values)   
    def modify_all_rows(self,keys,values):
        '''
            crtb
            keys = {'color':'green'}
            values = {'language':'korean'}
            crtb.modify_all_rows(keys,values)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            
            >>> keys = {'color':'green'}
            >>> values = {'language':'korean'}
            >>> crtb.modify_all_rows(keys,values)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green|  korean|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green|  korean|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green|  korean|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            row = utils.dict_extend(keys,values)
            self.crtable = append_row(row,self.crtable)
        else:
            self.crtable = modify_rows_via_keys(keys,self.crtable,values)
    def modify_col(self,whichcol,col):
        '''
            crtb
            col = {0:50,1:50,2:50}
            crtb.modify_col(0,col)
            crtb
            col = {0:60,1:60}
            crtb.modify_col('size',col)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            >>> 
            >>> col = {0:50,1:50,2:50}
            >>> crtb.modify_col(0,col)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            |  50|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  50|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  50|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            >>> 
        '''
        if(utils.is_int(whichcol)):
            self.crtable = modify_col_via_colnum(whichcol,self.crtable,col)
        else:
            self.crtable = modify_col_via_colname(whichcol,self.crtable,col)
    ##insert
    def insert_col(self,colnum,col):
        '''
            crtb
            col = {'owner':['dli','dlx','dly','dlz']}
            crtb.insert_col(1,col)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'expire': 3, 'language': 2, 'size': 0}
            >>> 
            >>> col = {'owner':['dli','dlx','dly','dlz']}
            >>> crtb.insert_col(1,col)
            >>> crtb
            +++++++++++++++++++++++++++++++++++++++
            |size|owner|color|language|     expire|
            +++++++++++++++++++++++++++++++++++++++
            | 500|  dli|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++++++++
            |  74|  dlx|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++++++++
            |  74|  dly|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 2}
            ====values==:
                :{'color': 2, 'owner': 1}
            >>> 
        '''
        self.crtable = insert_col(colnum,col,self.crtable)
    def insert_cols(self,colnumlist,cols):
        '''
            crtb
            cols = [
                {'owner':['dli','dlx','dly','dlz']},
                {'uid':['ua','ub','uc','ud']}
            ]
            colnumlist = [1,3]
            crtb.insert_cols(colnumlist,cols)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'language': 2, 'expire': 3}
            >>> 
            >>> cols = [
            ...     {'owner':['dli','dlx','dly','dlz']},
            ...     {'uid':['ua','ub','uc','ud']}
            ... ]
            >>> colnumlist = [1,3]
            >>> crtb.insert_cols(colnumlist,cols)
            >>> crtb
            +++++++++++++++++++++++++++++++++++++++++++
            |size|owner|color|language|uid|     expire|
            +++++++++++++++++++++++++++++++++++++++++++
            | 500|  dli|green| espanol| ua|2018-dec-01|
            +++++++++++++++++++++++++++++++++++++++++++
            |  74|  dlx|green| chinese| ub|2017-oct-01|
            +++++++++++++++++++++++++++++++++++++++++++
            |  74|  dly|green| espanol| uc|2017-oct-01|
            +++++++++++++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 2}
            ====values==:
                :{'owner': 1, 'size': 0, 'uid': 4, 'expire': 5, 'language': 3}
            
            >>> 
        '''
        self.crtable = insert_cols(colnumlist,cols,self.crtable)
    def insert_row(self,rownum,row):
        '''
            crtb
            row = {'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'}
            crtb.insert_row(1,row)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            >>> 
            >>> row = {'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'}
            >>> crtb.insert_row(1,row)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |8888| blue| russian|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            >>> 
        '''
        self.crtable = insert_row(rownum,row,self.crtable)
    def insert_rows(self,rownumlist,rows):
        '''
            crtb
            rows = [{'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'},
                    {'size': 666, 'color': 'azure', 'language': 'russian', 'expire': '2017-dec-01'}]
            rownumlist = [0,2]
            crtb.insert_rows(rownumlist,rows)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            >>> 
            >>> rows = [{'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'},
            ...         {'size': 666, 'color': 'azure', 'language': 'russian', 'expire': '2017-dec-01'}]
            >>> rownumlist = [0,2]
            >>> crtb.insert_rows(rownumlist,rows)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            |8888| blue| russian|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 666|azure| russian|2017-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            >>> 
        '''
        self.crtable = insert_rows(rownumlist,rows,self.crtable)
    ##delete 
    def __delitem__(self,keys):
        '''
            crtb
            keys =  {'language':'espanol'}
            del crtb[keys]
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            
            >>> del crtb[{'language':'espanol'}]
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            >>> 
        '''
        self.crtable = del_rows_via_keys(keys,self.crtable)
    def delete_first_row(self,keys):
        '''
            crtb
            keys =  {'language':'espanol'}
            crtb.delete_first_row(keys)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            
            >>> keys =  {'language':'espanol'}
            >>> crtb.delete_first_row(keys)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            pass
        else:
            seq = seqslist[0]
            ltdict.pop(self.crtable['table'],seq)
    def delete_last_row(self,keys):
        '''
            crtb
            keys =  {'language':'espanol'}
            crtb.delete_last_row(keys)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            
            >>> keys =  {'language':'espanol'}
            >>> crtb.delete_last_row(keys)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            pass
        else:
            seq = seqslist[-1]
            ltdict.pop(self.crtable['table'],seq)
    def delete_specific_row(self,keys,whichrow):
        '''
            crtb
            keys =  {'language':'espanol'}
            crtb.delete_specific_row(keys,1)
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            
            >>> keys =  {'language':'espanol'}
            >>> crtb.delete_specific_row(keys,1)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            >>> 
        '''
        seqslist = get_seqslist_via_keys(keys,self.crtable)
        if(seqslist.__len__() == 0):
            pass
        else:
            seq = seqslist[whichrow]
            ltdict.pop(self.crtable['table'],seq)
    def delete_all_rows(self,keys):
        '''
            crtb
            keys =  {'language':'espanol'}
            crtb.delete_all_rows(keys)
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            
            >>> keys =  {'language':'espanol'}
            >>> crtb.delete_all_rows(keys)
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'expire': 3, 'size': 0}
            
            >>> 
        '''
        self.crtable = del_rows_via_keys(keys,self.crtable)
    ####
    def del_col(self,colnum_or_colname):
        '''
            crtb
            crtb.del_col('language')
            crtb
            crtb.del_col(0)
            crtb
            
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'expire': 3, 'size': 0, 'language': 2}
            >>> 
            >>> 
            >>> crtb.del_col('language')
            >>> crtb
            ++++++++++++++++++++++++
            |size|color|     expire|
            ++++++++++++++++++++++++
            | 500|green|2018-dec-01|
            ++++++++++++++++++++++++
            |  74|green|2017-oct-01|
            ++++++++++++++++++++++++
            |  74|green|2017-oct-01|
            ++++++++++++++++++++++++
            | 888|green|2018-oct-01|
            ++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'expire': 3, 'size': 0}
            
            >>> crtb.del_col(0)
            >>> crtb
            +++++++++++++++++++
            |color|     expire|
            +++++++++++++++++++
            |green|2018-dec-01|
            +++++++++++++++++++
            |green|2017-oct-01|
            +++++++++++++++++++
            |green|2017-oct-01|
            +++++++++++++++++++
            |green|2018-oct-01|
            +++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'expire': 3}
            
        '''
        if(utils.is_int(colnum_or_colname)):
            colnum = colnum_or_colname
            self.crtable = del_col_via_colnum(colnum,self.crtable)
        else:
            colname = colnum_or_colname
            self.crtable = del_col_via_colname(colname,self.crtable)
    def del_cols(self,numslist_or_nameslist):
        '''
            crtb
            crtb.del_cols(['size','language'])
            crtb
            crtb
            crtb.del_cols([0,3])
            crtb
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'size': 0, 'expire': 3}
            
            >>> crtb.del_cols([0,3])
            >>> crtb
            ++++++++++++++++
            |color|language|
            ++++++++++++++++
            |green| espanol|
            ++++++++++++++++
            |green| chinese|
            ++++++++++++++++
            |green| espanol|
            ++++++++++++++++
            |green| espanol|
            ++++++++++++++++
            ====keys====:
                :{'color': 0}
            ====values==:
                :{'language': 1}
            >>> 
        '''
        ele = numslist_or_nameslist[0]
        if(utils.is_int(ele)):
            colnumslist = numslist_or_nameslist
            self.crtable = del_cols_via_colnumslist(colnumslist,self.crtable)
        else:
            colnameslist = numslist_or_nameslist
            self.crtable = del_cols_via_colnameslist(colnameslist,self.crtable)
    ## keys values items 
    def keys(self):
        '''
            crtb
            crtb.keys()
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'size': 0, 'expire': 3}
            
            >>> crtb.keys()
            [{'color': 'green'}, {'color': 'green'}, {'color': 'green'}, {'color': 'green'}]
            >>> crtb.values()
            [{'language': 'espanol', 'size': 500, 'expire': '2018-dec-01'}, {'language': 'chinese', 'size': 74, 'expire': '2017-oct-01'}, {'language': 'espanol', 'size': 74, 'expire': '2017-oct-01'}, {'language': 'espanol', 'size': 888, 'expire': '2018-oct-01'}]
            >>> 
            >>> 
        '''
        if(self.crtable['knimd'] == {}):
            return([])
        else:
            colnameslist = get_indexonly_refdict(self.crtable['knimd'])
            colnameslist = ltdict.naturalize_intkeydict(colnameslist)
            colnameslist = ltdict.to_list(colnameslist)
            keys_list = []
            colnumslist = get_indexes_list_via_names_list(colnameslist,self.crtable['animd'])
            rownumslist = sorted(list(self.crtable['table'].keys()))
            for i in range(0,rownumslist.__len__()):
                rownum = rownumslist[i]
                keys = {}
                for colnum in colnumslist:
                    keys[self.crtable['animd'][colnum]] = self.crtable['table'][rownum][colnum]
                keys_list.append(keys)
            return(keys_list)
    def values(self):
        '''
            crtb
            crtb.keys()
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'language': 2, 'size': 0, 'expire': 3}
            
            >>> crtb.keys()
            [{'color': 'green'}, {'color': 'green'}, {'color': 'green'}, {'color': 'green'}]
            >>> crtb.values()
            [{'language': 'espanol', 'size': 500, 'expire': '2018-dec-01'}, {'language': 'chinese', 'size': 74, 'expire': '2017-oct-01'}, {'language': 'espanol', 'size': 74, 'expire': '2017-oct-01'}, {'language': 'espanol', 'size': 888, 'expire': '2018-oct-01'}]
            >>> 
            >>> 
         '''   
        if(self.crtable['vnimd'] == {}):
            return([])
        else:
            colnameslist = get_indexonly_refdict(self.crtable['vnimd'])
            colnameslist = ltdict.naturalize_intkeydict(colnameslist)
            colnameslist = ltdict.to_list(colnameslist)
            values_list = []
            colnumslist = get_indexes_list_via_names_list(colnameslist,self.crtable['animd'])
            rownumslist = sorted(list(self.crtable['table'].keys()))
            for i in range(0,rownumslist.__len__()):
                rownum = rownumslist[i]
                values = {}
                for colnum in colnumslist:
                    values[self.crtable['animd'][colnum]] = self.crtable['table'][rownum][colnum]
                values_list.append(values)
        return(values_list)
    def items(self):
        '''
            crtb
            crtb.items()
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'language': 2, 'expire': 3}
            
            >>> crtb.items()
            [({'color': 'green'}, {'size': 500, 'language': 'espanol', 'expire': '2018-dec-01'}), ({'color': 'green'}, {'size': 74, 'language': 'chinese', 'expire': '2017-oct-01'}), ({'color': 'green'}, {'size': 74, 'language': 'espanol', 'expire': '2017-oct-01'}), ({'color': 'green'}, {'size': 888, 'language': 'espanol', 'expire': '2018-oct-01'})]
            >>> 
        '''
        if( (self.crtable['knimd'] == {}) & (self.crtable['vnimd'] == {})):
            return([])
        else:
            keys_list = self.keys()
            values_list = self.values()
            items_list = []
            for i in range(0,keys_list.__len__()):
                items = (keys_list[i],values_list[i])
                items_list.append(items)
        return(items_list)
    #  clear copy
    def clear(self):
        '''
            crtb
            crtb.clear()
            crtb
            >>> 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'language': 2, 'expire': 3}
            
            >>> crtb.clear()
            >>> crtb
            ++++++++++++++++++++++++++++
            |size|color|language|expire|
            ++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'language': 2, 'expire': 3}
            
            >>> 
        '''
        self.crtable['table'] = {}
    def copy(self):
        return(copy.deepcopy(self))
    # operator
    def __mul__(self,crtb_2):
        '''
            table_1 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            table_2 = {
                          0: {0: 'a1', 1: 'b2'}, 
                          1: {0: 'a1', 1: 'b3'} 
                      }
            colnameslist = ['A','B']
            keynameslist = ['A']
            crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
            crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
            crtb = crtb1 * crtb2
            crtb
            +++++++++++++++++
            |A-0|B-0|A-1|B-1|
            +++++++++++++++++
            | a1| b1| a1| b2|
            +++++++++++++++++
            | a1| b1| a1| b3|
            +++++++++++++++++
            | a1| b2| a1| b2|
            +++++++++++++++++
            | a1| b2| a1| b3|
            +++++++++++++++++
            ====keys====:
                :{'A-1': 2, 'A-0': 0}
            ====values==:
                :{'B-0': 1, 'B-1': 3}
            
            >>> 
        '''
        crtb_1 = copy.deepcopy(self)
        crtb_1.crtable = product_crtables([crtb_1.crtable,crtb_2.crtable])
        return(crtb_1)
    def project(self,colnameslist):
        '''
            crtb
            colnameslist = ['color','language']
            crtb.project(colnameslist)
            crtb
            >>> 
            >>> crtb
            ++++++++++++++++
            |color|language|
            ++++++++++++++++
            |green| espanol|
            ++++++++++++++++
            |green| chinese|
            ++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'language': 2, 'expire': 3}
            
            >>> colnameslist = ['color','language']
            >>> crtb.project(colnameslist)
            >>> crtb
            ++++++++++++++++
            |color|language|
            ++++++++++++++++
            |green| espanol|
            ++++++++++++++++
            |green| chinese|
            ++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'language': 2, 'expire': 3}
            
            >>> 
        '''
        self.crtable = project_crtable(colnameslist,self.crtable)
    def __add__(self,crtb_2):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            table_2 = {
                          0: {0: 'a1', 1: 'b2'}, 
                          1: {0: 'a1', 1: 'b3'} 
                      }
            colnameslist = ['A','B']
            keynameslist = ['A']
            crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
            crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
            crtb = crtb1 + crtb2
            crtb
            >>> 
            >>> import xdict.CrtableLib.crtable as xcr
            >>> table_1 = {
            ...               0: {0: 'a1', 1: 'b1'}, 
            ...               1: {0: 'a1', 1: 'b2'} 
            ...           }
            >>> table_2 = {
            ...               0: {0: 'a1', 1: 'b2'}, 
            ...               1: {0: 'a1', 1: 'b3'} 
            ...           }
            >>> colnameslist = ['A','B']
            >>> keynameslist = ['A']
            >>> crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
            >>> crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
            >>> crtb = crtb1 + crtb2
            >>> crtb 
            +++++++
            | A| B|
            +++++++
            |a1|b1|
            +++++++
            |a1|b2|
            +++++++
            |a1|b3|
            +++++++
            ====keys====:
                :{'A': 0}
            ====values==:
                :{'B': 1}
            >>> 
        '''
        crtb_1 = copy.deepcopy(self)
        crtb_1.crtable = union_crtables([crtb_1.crtable,crtb_2.crtable])
        return(crtb_1)
    def __sub__(self,crtb_2):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            table_2 = {
                          0: {0: 'a1', 1: 'b2'}, 
                          1: {0: 'a1', 1: 'b3'} 
                      }
            colnameslist = ['A','B']
            keynameslist = ['A']
            crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
            crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
            crtb = crtb1 - crtb2
            crtb
        '''
        crtb_1 = copy.deepcopy(self)
        crtb_1.crtable = diff_two_crtables(crtb_1.crtable,crtb_2.crtable)
        return(crtb_1)
    def __truediv__(self,crtb_2):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                          1: {0: 'a2', 1: 'b3', 2: 'c7'},
                          2: {0: 'a3', 1: 'b4', 2: 'c6'},
                          3: {0: 'a1', 1: 'b2', 2: 'c3'},
                          4: {0: 'a4', 1: 'b6', 2: 'c6'}, 
                          5: {0: 'a2', 1: 'b2', 2: 'c3'},
                          6: {0: 'a1', 1: 'b2', 2: 'c1'}
                      }
            table_2 = {
                          0: {0: 'b1', 1: 'c2', 2: 'd1'}, 
                          1: {0: 'b2', 1: 'c1', 2: 'd1'},
                          2: {0: 'b2', 1: 'c3', 2: 'd2'}
                      }
            colnameslist1 =['A','B','C']
            colnameslist2 =['B','C','D']
            keynameslist1 = ['A']
            keynameslist2 = ['B','C']
            crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
            crtb = crtb1 / crtb2
            crtb
        '''
        crtb_1 = copy.deepcopy(self)
        crtb_1.crtable = divide_two_crtables(crtb_1.crtable,crtb_2.crtable)
        return(crtb_1)
    def unique(self):
        '''
            crtb
            crtb.unique()
            crtb 
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            >>> crtb.unique()
            >>> crtb
            +++++++++++++++++++++++++++++++++
            |size|color|language|     expire|
            +++++++++++++++++++++++++++++++++
            | 500|green| espanol|2018-dec-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| chinese|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            |  74|green| espanol|2017-oct-01|
            +++++++++++++++++++++++++++++++++
            | 888|green| espanol|2018-oct-01|
            +++++++++++++++++++++++++++++++++
            ====keys====:
                :{'color': 1}
            ====values==:
                :{'size': 0, 'expire': 3, 'language': 2}
            >>> 
        '''
        self.crtable = unique_crtable(self.crtable)
    def naturalize(self):
        '''
            #no need to call this ,this will be auto executed
            crtb
            crtb.naturalize()
            crtb
        '''
        self.crtable = naturalize_crtable(self.crtable)
    def intersec(self,crtb_2):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            table_2 = {
                          0: {0: 'a1', 1: 'b2'}, 
                          1: {0: 'a1', 1: 'b3'} 
                      }
            colnameslist = ['A','B']
            keynameslist = ['A']
            crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
            crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
            crtb1
            crtb2
            crtb = crtb1.intersec(crtb2)
            crtb
        '''
        crtb_1 = copy.deepcopy(self)
        crtb_1.crtable = intersec_two_crtables(crtb_1.crtable,crtb_2.crtable)
        return(crtb_1)
    def __eq__(self,crtb_2):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            table_2 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            colnameslist = ['A','B']
            keynameslist = ['A']
            crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
            crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
            crtb1 == crtb2
        '''
        return(equal(self.crtable,crtb_2.crtable))
    def __ne__(self,crtb_2):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            table_2 = {
                          0: {0: 'a1', 1: 'b1'}, 
                          1: {0: 'a1', 1: 'b2'} 
                      }
            colnameslist = ['A','B']
            keynameslist = ['A']
            crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
            crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
            crtb1 != crtb2
        '''
        return(not(equal(self.crtable,crtb_2.crtable)))
    def __contains__(self,crtb_2):
        '''
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                          1: {0: 'a2', 1: 'b3', 2: 'c7'},
                          2: {0: 'a3', 1: 'b4', 2: 'c6'},
                          3: {0: 'a1', 1: 'b2', 2: 'c3'}
                      }
            table_2 = {
                          0: {0: 'b3', 1: 'c7'}, 
                          1: {0: 'b4', 1: 'c6'},
                          2: {0: 'b2', 1: 'c3'}
                      }
            colnameslist1 =['A','B','C']
            colnameslist2 =['B','C']
            keynameslist1 = ['A']
            keynameslist2 = ['B']
            crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
            crtb2 in crtb1
        '''
        return(comprise_crtable(self.crtable,crtb_2.crtable))
    def include_row(self,row):
        '''
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                          1: {0: 'a2', 1: 'b3', 2: 'c7'},
                          2: {0: 'a3', 1: 'b4', 2: 'c6'},
                          3: {0: 'a1', 1: 'b2', 2: 'c3'}
                      }
            colnameslist1 =['A','B','C']
            keynameslist1 = ['A']
            crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            row = {'A': 'a2', 'B': 'b3', 'C': 'c7'}
            crtb.include_row(row)
        '''
        return(row_in_crtable(row,self.crtable))
    def include_col(self,col):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                          1: {0: 'a2', 1: 'b3', 2: 'c7'},
                          2: {0: 'a3', 1: 'b4', 2: 'c6'},
                          3: {0: 'a1', 1: 'b2', 2: 'c3'}
                      }
            colnameslist1 =['A','B','C']
            keynameslist1 = ['A']
            crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            col = {'B': ['b1','b3','b4','b2']}
            crtb.include_col(col)
        '''
        return(col_in_crtable(col,self.crtable))
    def include_row_slice(self,row):
        '''
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                          1: {0: 'a2', 1: 'b3', 2: 'c7'},
                          2: {0: 'a3', 1: 'b4', 2: 'c6'},
                          3: {0: 'a1', 1: 'b2', 2: 'c3'}
                      }
            colnameslist1 =['A','B','C']
            keynameslist1 = ['A']
            crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            part_row = {'B': 'b3', 'C': 'c7'}
            crtb.include_row_slice(part_row)
        '''
        return(partlyrow_in_crtable(row,self.crtable))
    def include_col_slice(self,col):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
                          1: {0: 'a2', 1: 'b3', 2: 'c7'},
                          2: {0: 'a3', 1: 'b4', 2: 'c6'},
                          3: {0: 'a1', 1: 'b2', 2: 'c3'}
                      }
            colnameslist1 =['A','B','C']
            keynameslist1 = ['A']
            crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            part_col = {'B': ['b3','b4']}
            crtb.include_col_slice(part_col)
        '''
        return(partlycol_in_crtable(col,self.crtable))
    def thetajoin(self,crtb2,**kwargs):
        '''
            import xdict.CrtableLib.crtable as xcr
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 3}, 
                          1: {0: 'a1', 1: 'b2', 2: 6},
                          2: {0: 'a2', 1: 'b3', 2: 2},
                          3: {0: 'a2', 1: 'b4', 2: 12}
                      }
            table_2 = {
                          0: {0: 'e1', 1: 3}, 
                          1: {0: 'e2', 1: 7},
                          2: {0: 'e3', 1: 10},
                          3: {0: 'e3', 1: 2},
                          4: {0: 'e5', 1: 2}
                      }
            colnameslist1 =['A','B','C']
            colnameslist2 =['E','C']
            keynameslist1 = ['A']
            keynameslist2 = ['E']
            crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
            def theta_function(subrow_1,subrow_2):
                k1 = list(subrow_1.keys())[0]
                k2 = list(subrow_2.keys())[0]
                if(subrow_1[k1] < subrow_2[k2]):
                    return(True)
                else:
                    return(False)
            
            crtb = crtb1.thetajoin(crtb2,theta=theta_function)
            crtb 
            +++++++++++++++++++++
            |A-0|B-0|C-0|E-1|C-1|
            +++++++++++++++++++++
            | a1| b1|  3| e2|  7|
            +++++++++++++++++++++
            | a1| b1|  3| e3| 10|
            +++++++++++++++++++++
            | a1| b2|  6| e2|  7|
            +++++++++++++++++++++
            | a1| b2|  6| e3| 10|
            +++++++++++++++++++++
            | a2| b3|  2| e1|  3|
            +++++++++++++++++++++
            | a2| b3|  2| e2|  7|
            +++++++++++++++++++++
            | a2| b3|  2| e3| 10|
            +++++++++++++++++++++
            ====keys====:
                :{'E-1': 3, 'A-0': 0}
            ====values==:
                :{'C-0': 2, 'B-0': 1, 'C-1': 4}
            >>> 

            from xdict import ltdict
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 3}, 
                          1: {0: 'a1', 1: 'b2', 2: 6},
                          2: {0: 'a2', 1: 'b3', 2: 2},
                          3: {0: 'a2', 1: 'b4', 2: 12}
                      }
            table_2 = {
                          0: {0: 'b1', 1: 3}, 
                          1: {0: 'b2', 1: 7},
                          2: {0: 'b3', 1: 10},
                          3: {0: 'b3', 1: 2},
                          4: {0: 'b5', 1: 2}
                      }
            colnameslist1 =['A','B','C']
            colnameslist2 =['B','C']
            keynameslist1 = ['A']
            keynameslist2 = ['B']
            crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
            def theta_function(subrow_1,subrow_2):
                subrow_l1 = ltdict.naturalize_intkeydict(subrow_1)
                subrow_l2 = ltdict.naturalize_intkeydict(subrow_2)
                if(subrow_l1 == subrow_l2):
                    return(True)
                else:
                    return(False)
            
            crtb = crtb1.thetajoin(crtb2,theta=theta_function)
            crtb 
            +++++++++++++++++++++
            |A-0|B-0|C-0|B-1|C-1|
            +++++++++++++++++++++
            | a1| b1|  3| b1|  3|
            +++++++++++++++++++++
            | a2| b3|  2| b3|  2|
            +++++++++++++++++++++
            ====keys====:
                :{'B-1': 3, 'A-0': 0}
            ====values==:
                :{'C-0': 2, 'B-0': 1, 'C-1': 4}
            
            >>> 
        '''
        crtb1 = copy.deepcopy(self)
        def theta_function(subrow_1,subrow_2):
            subrow_l1 = ltdict.naturalize_intkeydict(subrow_1)
            subrow_l2 = ltdict.naturalize_intkeydict(subrow_2)
            if(subrow_l1 == subrow_l2):
                return(True)
            else:
                return(False)
        if('theta' in kwargs):
            theta = kwargs['theta']
        else:
            theta = theta_function
        if('colnameslist_1' in kwargs):
            colnameslist_1 = kwargs['colnameslist_1']
        else:
            colnameslist_1 = []
        if('colnameslist_2' in kwargs):
            colnameslist_2 = kwargs['colnameslist_2']
        else:
            colnameslist_2 = []
        if((colnameslist_1 == [])|(colnameslist_2 == [])):
            refd1 = get_nameonly_refdict(crtb1.crtable['animd'])
            refd2 = get_nameonly_refdict(crtb2.crtable['animd'])
            colnameslist_1 = sorted(list(refd1.keys()))
            colnameslist_2 = sorted(list(refd2.keys()))
            set_1 = set(colnameslist_1)
            set_2 = set(colnameslist_2)
            common = sorted(list(set_1.intersection(set_2)))
            colnameslist_1 =  common
            colnameslist_2 =  common
        else:
            pass
        crtb1.crtable = thetajoin_two_crtables(colnameslist_1,crtb1.crtable,colnameslist_2,crtb2.crtable,theta)
        return(crtb1)
    def equijoin(self,crtb2,**kwargs):
        '''
            import xdict.CrtableLib.crtable as xcr 
            from xdict import ltdict
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 3}, 
                          1: {0: 'a1', 1: 'b2', 2: 6},
                          2: {0: 'a2', 1: 'b3', 2: 2},
                          3: {0: 'a2', 1: 'b4', 2: 12}
                      }
            table_2 = {
                          0: {0: 'b1', 1: 3}, 
                          1: {0: 'b2', 1: 7},
                          2: {0: 'b3', 1: 10},
                          3: {0: 'b3', 1: 2},
                          4: {0: 'b5', 1: 2}
                      }
            colnameslist1 =['A','B','C']
            colnameslist2 =['B','C']
            keynameslist1 = ['A']
            keynameslist2 = ['B']
            crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
            crtb = crtb1.equijoin(crtb2)
            crtb 
            +++++++++++++++++++++
            |A-0|B-0|C-0|B-1|C-1|
            +++++++++++++++++++++
            | a1| b1|  3| b1|  3|
            +++++++++++++++++++++
            | a2| b3|  2| b3|  2|
            +++++++++++++++++++++
            ====keys====:
                :{'A-0': 0, 'B-1': 3}
            ====values==:
                :{'C-0': 2, 'C-1': 4, 'B-0': 1}
            >>> 
        '''
        crtb1 = copy.deepcopy(self)
        if('colnameslist_1' in kwargs):
            colnameslist_1 = kwargs['colnameslist_1']
        else:
            colnameslist_1 = []
        if('colnameslist_2' in kwargs):
            colnameslist_2 = kwargs['colnameslist_2']
        else:
            colnameslist_2 = []
        if((colnameslist_1 == [])|(colnameslist_2 == [])):
            refd1 = get_nameonly_refdict(crtb1.crtable['animd'])
            refd2 = get_nameonly_refdict(crtb2.crtable['animd'])
            colnameslist_1 = sorted(list(refd1.keys()))
            colnameslist_2 = sorted(list(refd2.keys()))
            set_1 = set(colnameslist_1)
            set_2 = set(colnameslist_2)
            common = sorted(list(set_1.intersection(set_2)))
            colnameslist_1 =  common
            colnameslist_2 =  common
        else:
            pass
        crtb1.crtable = equijoin_two_crtables(colnameslist_1,crtb1.crtable,colnameslist_2,crtb2.crtable)
        return(crtb1)
    def naturaljoin(self,crtb2,**kwargs):
        '''
            import xdict.CrtableLib.crtable as xcr 
            from xdict import ltdict
            table_1 = {
                          0: {0: 'a1', 1: 'b1', 2: 3}, 
                          1: {0: 'a1', 1: 'b2', 2: 6},
                          2: {0: 'a2', 1: 'b3', 2: 2},
                          3: {0: 'a2', 1: 'b4', 2: 12}
                      }
            table_2 = {
                          0: {0: 'b1', 1: 3}, 
                          1: {0: 'b2', 1: 7},
                          2: {0: 'b3', 1: 10},
                          3: {0: 'b3', 1: 2},
                          4: {0: 'b5', 1: 2}
                      }
            colnameslist1 =['A','B','C']
            colnameslist2 =['B','C']
            keynameslist1 = ['A']
            keynameslist2 = ['B']
            crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
            crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
            crtb = crtb1.naturaljoin(crtb2)
            crtb 
        '''
        crtb1 = copy.deepcopy(self)
        if('colnameslist_1' in kwargs):
            colnameslist_1 = kwargs['colnameslist_1']
        else:
            colnameslist_1 = []
        if('colnameslist_2' in kwargs):
            colnameslist_2 = kwargs['colnameslist_2']
        else:
            colnameslist_2 = []
        if((colnameslist_1 == [])|(colnameslist_2 == [])):
            refd1 = get_nameonly_refdict(crtb1.crtable['animd'])
            refd2 = get_nameonly_refdict(crtb2.crtable['animd'])
            colnameslist_1 = sorted(list(refd1.keys()))
            colnameslist_2 = sorted(list(refd2.keys()))
            set_1 = set(colnameslist_1)
            set_2 = set(colnameslist_2)
            common = sorted(list(set_1.intersection(set_2)))
            colnameslist_1 =  common
            colnameslist_2 =  common
        else:
            pass
        crtb1.crtable =  naturaljoin_two_crtables(colnameslist_1,crtb1.crtable,colnameslist_2,crtb2.crtable)
        return(crtb1)
    def candidates(self):
        ''' 
            import xdict.CrtableLib.crtable as xcr 
            from xdict import ltdict
            table = {
                0: {0: 'a1', 1: 'b1', 2: 5, 3: 3}, 
                1: {0: 'a1', 1: 'b2', 2: 6, 3: 7}, 
                2: {0: 'a2', 1: 'b3', 2: 8, 3: 10}, 
                3: {0: 'a2', 1: 'b3', 2: 8, 3: 2}
            }
            colnameslist = ['A','B','C','E']
            keynameslist = ['A']
            crtb = xcr.crtable(colnameslist = colnameslist,table=table,keynameslist = keynameslist)
            crtb
        '''
        return(get_all_candidate_key_combo(self.crtable))

###########################
def creat_xytbl(rn,cnl,rnl,table):
    crtb = xcr.crtable(colnameslist = cnl,table=table)
    knl = [rn]
    col = knl + rnl
    crtb.prepend_col(col)
    table = crtb.crtable['table']
    ncrtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    return(ncrtb)

def xy2value(crtb,rowname,colname):
    cnl = crtb.colnameslist
    rnl = crtb.col(cnl[0])
    rownum = rnl.index(rowname)+1
    col = crtb.col(colname)
    return(col[rownum-1])

####增加把某一个元素染色的功能#####
####利用colormatrix参数############

###########################

def load_crtable_from_json(js):
    js = naturalize_crtable(js)
    return(js)

    
def tb2dlist(tb,cnl):
    dl = []
    if(isinstance(tb,list)):
        for i in range(0,tb.__len__()):
            row = tb[i]
            d = {}
            for j in range(0,row.__len__()):
                k = cnl[j]
                v = row[j]
                d[k] = v
                dl.append(d)
    else:
        for k in tb:
            row = tb[k]
            d = {}
            for j in range(0,row.__len__()):
                k = cnl[j]
                v = row[j]
                d[k] = v
                dl.append(d)
    return(dl)
    


##########################



def load_crtb_from_file(fn):
    j = fs.rjson(fn)
    crtbl = load_crtable_from_json(j)
    crtb=crtable(crtable=crtbl)
    return(crtb)


def save_crtb_to_file(fn,crtb):
    fs.wjson(fn,crtb.crtable)
