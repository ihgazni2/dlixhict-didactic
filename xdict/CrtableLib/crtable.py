from xdict import ltdict
from xdict import utils


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
            cond = ltdict.ltdict_include(indexes_list,k)
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
            cond = ltdict.ltdict_include(names_list,k)
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
            cond = ltdict.ltdict_include(indexes_list,k)
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
            cond = ltdict.ltdict_include(names_list,k)
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
        elif(utils.is_int(k)):
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
    row = format_attribs_to_indexkeyonly(row,crtable['animd'],index_dominant=1)
    seqs = list(crtable['table'].keys())
    next = max(seqs) + 1
    crtable['table'][next] = expand_part_attribs(row,crtable['animd'],index_dominant=1)
    return(crtable)

def append_col(col,crtable):
    '''
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'] = {}
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        col = {'owner':['dli','dli','dli','dli']}
        crtable = add_col(col,crtable)
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
        add_col(col,crtable)
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
    crtable['table'] = ltdict.ltdict_prepend(crtable['table'],row)
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
        crtable['table'][rownum] = ltdict.ltdict_prepend(row,col_list[rownum])
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
    rows = ltdict.list_to_ltdict(rows)
    for k in rows:
        row = rows[k]
        row = nameattribs_to_indexattribs(row,crtable['animd'])
        row = expand_part_attribs(row,crtable['animd'])
        rows[k] = row 
    crtable['table'] = ltdict.ltdict_prepend_extend(crtable['table'],rows,deepcopy_1=1,deepcopy_2=1)
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
        crtable['animd'] = get_indexonly_refdict(crtable['animd'])
        ltdict.ltdict_pop(crtable['animd'],colnum)
    else:
        del crtable['animd'][colnum]
        del crtable['animd'][col_name]
    for seq in crtable['table']:
        if(reorder):
            
            ltdict.ltdict_pop(crtable['table'][seq],colnum)
        else:
            del crtable['table'][seq][colnum]
    return(crtable)

def del_cols_via_colnumslist(colnumlist,crtable,**kwargs):
    '''
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    for colnum in colnumlist:
        del_col_via_colnum(colnum,crtable,reorder=reorder)
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
    return(del_cols_via_colnumslist(colnumlist,crtable,reorder=reorder))


def del_rows_via_attribs(attribs,crtable,**kwargs):
    '''
    '''
    if('reorder' in kwargs):
        reorder = kwargs['reorder']
    else:
        reorder = 1
    seqslist = get_seqslist_via_attribs(attribs,crtable)
    if(reorder):
        ltdict.ltdict_pop_seqs(crtable['table'],set(seqslist))
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
        ltdict.ltdict_pop_seqs(crtable['table'],set(seqslist))
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
        >>>  crtable['table'][5]
          File "<stdin>", line 1
            crtable['table'][5]
            ^
        IndentationError: unexpected indent
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
    colnum = crtable['animd'][colname]
    return(modify_col_via_colnum(colnum,crtable,modified_to))

def insert_col(colnum,col,crtable):
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
    col_name = list(col.keys())[0]
    col_list = col[col_name]    
    refd = get_indexonly_refdict(crtable['animd'])
    nrefd = ltdict.ltdict_insert(refd,colnum,col_name)
    crtable['animd'] = creat_mirror_dict(nrefd)
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        crtable['table'][rownum] = ltdict.ltdict_insert(crtable['table'][rownum],colnum,col_list[rownum])
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
    row = nameattribs_to_indexattribs(row,(crtable['animd']))
    crtable['table'] = ltdict.ltdict_insert(crtable['table'],rownum,row)
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
    tables = {}
    crtb = {}
    for i in range(0,crtables.__len__()):
        mds[i] = crtables[i]['animd']
        tables[i] = crtables[i]['table']
    crtb['animd'] = product_mirror_dicts(mds)
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
            ltdict.ltdict_pop_seqs(row,pop_seqs)
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
            vset.add(ltdict.ltdict_to_tuple(pt[k]))
        tslen = vset.__len__()
        freq = {}
        for k in pt:
            v = ltdict.ltdict_to_tuple(pt[k])
            if(v in freq):
                freq[v] = freq[v] + 1
                seqs_for_del.append(k)
            else:
                freq[v] = 0
        if(reorder):
            ltdict.ltdict_pop_seqs(pt,set(seqs_for_del))
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
    crtable['animd'] = project_mirror_dict(crtable['animd'],colnameslist)
    crtable['table'] = project_table(colnumslist,table,reorder=reorder,unique=unique)
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
            cl = ltdict.list_to_ltdict(col[name])
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
            cl = ltdict.list_to_ltdict(col[name])
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
        vset.add(ltdict.ltdict_to_tuple(pt[k]))
    tslen = vset.__len__()
    freq = {}
    for k in pt:
        v = ltdict.ltdict_to_tuple(pt[k])
        if(v in freq):
            freq[v] = freq[v] + 1
            seqs_for_del.append(k)
        else:
            freq[v] = 0
    if(reorder):
        ltdict.ltdict_pop_seqs(pt,set(seqs_for_del))
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


def partlyrow_in_crtable(row,crtable):
    '''
        crtable['table'] = {}
        crtable['animd'] = creat_mirror_dict({0: 'size', 1: 'color', 2: 'language', 3: 'expire'})
        crtable['table'][0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
        crtable['table'][1] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
        crtable['table'][2] = {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
        crtable['table'][3] = {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
        row = {'color': 'green', 'language': 'espanol'}
        
    '''
    nr = nameattribs_to_indexattribs(row,crtable['animd'])
    cond = 0
    for rownum in crtable['table']:
        row = crtable['table'][rownum]
        cond = utils.dict_comprise(row,nr)
        if(cond):
            return(True)
    return(False)

#----------------------------------------------------->

