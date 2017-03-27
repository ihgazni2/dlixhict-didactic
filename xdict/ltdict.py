import copy
from operator import itemgetter
from xdict import utils

    # '''
        # is_ltdict(obj)
        # is_json_ltdict(obj)
        # json_to_ltdict(obj,**kwargs)
        # ltdict_to_json(ltdict,**kwargs)
        # list_to_ltdict(array,**kwargs)
        # tuple_to_ltdict(fixed_array,**kwargs)
        # set_to_ltdict(this_set,**kwargs)
        # ltdict_to_list(ltdict,**kwargs)
        # ltdict_to_tuple(ltdict,**kwargs)
        # ltdict_to_set(ltdict,**kwargs)
        # ltdict_extend(ltdict_1,ltdict_2,**kwargs)
        # ltdict_prepend_extend(ltdict_1,ltdict_2,**kwargs)
        # ltdict_concat(ltdict_1,ltdict_2,**kwargs)
        # ltdict_first_continuous_indexes_slice(ltdict,value,**kwargs)
        # ltdict_last_continuous_indexes_slice(ltdict,value,**kwargs)
        # ltdict_all_continuous_indexes_slices_array(ltdict,value,**kwargs)
        # ltdict_indexes_array(ltdict,value,**kwargs)
        # ltdict_first_index(ltdict,value,**kwargs)
        # ltdict_last_index(ltdict,value,**kwargs)
        # ltdict_append(ltdict,value,**kwargs)
        # ltdict_prepend(ltdict,value,**kwargs)
        # ltdict_clear(ltdict,**kwargs)
        # ltdict_copy(ltdict,**kwargs)
        # ltdict_deepcopy(ltdict,**kwargs)
        # ltdict_insert(ltdict,index,value,**kwargs)
        # ltdict_insert_ltdict(ltdict_1,index,ltdict_2,**kwargs)
        # ltdict_include(ltdict,value,**kwargs)
        # ltdict_count(ltdict,value,**kwargs)
        # ltdict_pop(ltdict,index,**kwargs)
        # ltdict_pop_range(ltdict,start,end,**kwargs)
        # ltdict_pop_seqs(ltdict,seqs_set,**kwargs)
        # ltdict_remove_first(ltdict,value,**kwargs)
        # ltdict_remove_last(ltdict,value,**kwargs)
        # ltdict_remove_all(ltdict,value,**kwargs)
        # ltdict_reverse(ltdict,**kwargs)
        # ltdict_sort(ltdict,**kwargs)
    # '''
#ListTupleDict

def is_ltdict(obj):
    '''
        ltdict = {0:1,1:2,2:3}
        is_ltdict(ltdict) == True
        ltdict = {0:1,2:2,3:3}
        is_ltdict(ltdict) == False
        ltdict = {0:1,'1':2,2:3}
        is_ltdict(ltdict) == False
    '''
    if(utils.is_dict(obj)):
        pass
    else:
        return(False)
    index_set = set({})
    if(obj == {}):
        return(True)
    else:
        for key in obj:
            if(utils.is_int(key)):
                if(key >= 0):
                    index_set.add(key)
                else:
                    return(False)
            else:
                return(False)
        for i in range(0,obj.__len__()):
            if(i in index_set):
                pass
            else:
                return(False)
        return(True)
def is_json_ltdict(obj):
    '''
        ltdict = {0:1,1:2,2:3}
        is_json_ltdict(ltdict) == False
        ltdict = {'0':1,'2':2,'3':3}
        is_json_ltdict(ltdict) == False
        ltdict = {'a':0,'b':1,'c':2}
        is_json_ltdict(ltdict) == False
        ltdict = {'0':1,'1':2,'2':3}
        is_json_ltdict(ltdict) == True
    '''
    if(utils.is_dict(obj)):
        pass
    else:
        return(False)
    index_set = set({})
    if(obj == {}):
        return(True)
    else:
        for key in obj:
            try:
                int(key)
            except:
                return(False)
            else:
                pass
            if(utils.is_str(key)):
                if(int(key) >= 0):
                    index_set.add(int(key))
                else:
                    return(False)
            else:
                return(False)
        for i in range(0,obj.__len__()):
            if(i in index_set):
                pass
            else:
                return(False)
        return(True)
def json_to_ltdict(obj,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if the obj is a json_ltdict, return None if the obj is not a json_ltdict
       json_dict = {'0':'a','1':'b','2':'c'}
       json_to_ltdict(json_dict) == {0:'a',1:'b',2:'c'}
    '''
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_json_ltdict(obj)):
            pass
        else:
            return(None)
    else:
        pass
    ltdict = {}
    if(deepcopy):
        new = copy.deepcopy(obj)
    else:
        new = obj
    for key in new:
        ltdict[int(key)] = new[key]
    return(ltdict)
def ltdict_to_json(ltdict,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if the obj is a ltdict, return None if the obj is not a ltdict
       ltdict = {0:'a',1:'b',2:'c'}
       ltdict_to_json(ltdict) == {'1': 'b', '2': 'c', '0': 'a'}
    '''
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    j = {}
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    for key in new:
        j[str(key)] = new[key]
    return(j)
def list_to_ltdict(array,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if the array is a list, return None if the array is not a list
       array = ['a','b','c']
       list_to_ltdict(array) == {0: 'a', 1: 'b', 2: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(utils.is_list(array)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    ltdict = {}
    len = array.__len__()
    if(deepcopy):
        new = copy.deepcopy(array)
    else:
        new = array
    for i in range(0,len):
        ltdict[i] = new[i]
    return(ltdict)
def tuple_to_ltdict(fixed_array,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if the array is a tuple, return None if the array is not a tuple
       t = ('a','b','c')
       tuple_to_ltdict(t) == {0: 'a', 1: 'b', 2: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(utils.is_tuple(fixed_array)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    ltdict = {}
    len = fixed_array.__len__()
    if(deepcopy):
        new = copy.deepcopy(fixed_array)
    else:
        new = fixed_array
    for i in range(0,len):
        ltdict[i] = new[i]
    return(ltdict)
def set_to_ltdict(this_set,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if the array is a set, return None if the array is not a set
       s = {'a','b','c'}
       set_to_ltdict(s) == 
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(utils.is_set(this_set)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    ltdict = {}
    if(deepcopy):
        new = copy.deepcopy(this_set)
    else:
        new = this_set
    i = 0
    for each in this_set:
        ltdict[i] = each
        i = i + 1
    return(ltdict)
def ltdict_to_list(ltdict,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
       ltdict = {0: 'a', 1: 'b', 2: 'c'}
       ltdict_to_list(ltdict) == ['a', 'b', 'c']
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    l = []
    len = ltdict.__len__()
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    for i in range(0,len):
        l.append(new[i])
    return(l)
def ltdict_to_tuple(ltdict,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
       ltdict = {0: 'a', 1: 'b', 2: 'c'}
       ltdict_to_tuple(ltdict) == ('a', 'b', 'c')
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    l = []
    len = ltdict.__len__()
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    for i in range(0,len):
        l.append(new[i])
    return(tuple(l))
def ltdict_to_set(ltdict,**kwargs):
    '''not recursive;
       by default deepcopy=1: will not affect the origianl object;
       return a ltdict;
       by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
       ltdict = {0: 'a', 1: 'b', 2: 'c'}
       ltdict_to_set(ltdict) == 
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    s = set({})
    len = ltdict.__len__()
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    for i in range(0,len):
        s.add(new[i])
    return(s)
def ltdict_extend(ltdict_1,ltdict_2,**kwargs):
    '''not recursive;
       by default deepcopy_1=0 and deepcopy_2=0: a shallow copy ltdict_2 is is excuted;
       return a ltdict;
       by default check=1: will forcefully check if both are ltdicts, return None if either is not a ltdict
       ltdict_1 = {0: 'a', 1: 'b', 2: 'c'}
       ltdict_2 = {0: 'd', 1: 'e', 2: 'f'}
       ltdict_extend(ltdict_1,ltdict_2) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict_1) & is_ltdict(ltdict_2)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy_1' in kwargs):
        deepcopy_1 = kwargs['deepcopy_1']
    else:
        deepcopy_1 = 0
    if('deepcopy_2' in kwargs):
        deepcopy_2 = kwargs['deepcopy_2']
    else:
        deepcopy_2 = 0
    if(deepcopy_1):
        new_1 = copy.deepcopy(ltdict_1)
    else:
        new_1 = ltdict_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(ltdict_2)
    else:
        new_2 = copy.copy(ltdict_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    for i in range(0,len_2):
        new_1[i + len_1] = new_2[i]
    return(new_1)
def ltdict_prepend_extend(ltdict_1,ltdict_2,**kwargs):
    '''not recursive;
       by default deepcopy_1=0 and deepcopy_2=0: a shallow copy ltdict_2 is is excuted;
       return a ltdict;
       by default check=1: will forcefully check if both are ltdicts, return None if either is not a ltdict
       ltdict_1 = {0: 'a', 1: 'b', 2: 'c'}
       ltdict_2 = {0: 'd', 1: 'e', 2: 'f'}
       ltdict_prepend_extend(ltdict_1,ltdict_2) == {0: 'd', 1: 'e', 2: 'f', 3: 'a', 4: 'b', 5: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict_1) & is_ltdict(ltdict_2)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy_1' in kwargs):
        deepcopy_1 = kwargs['deepcopy_1']
    else:
        deepcopy_1 = 0
    if('deepcopy_2' in kwargs):
        deepcopy_2 = kwargs['deepcopy_2']
    else:
        deepcopy_2 = 0
    if(deepcopy_1):
        new_1 = copy.deepcopy(ltdict_1)
    else:
        new_1 = ltdict_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(ltdict_2)
    else:
        new_2 = copy.copy(ltdict_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    swap = {}
    for i in range(0,len_1):
        swap[len_2 + i] = new_1[i]
    for i in range(0,len_2):
        new_1[i] = new_2[i]
    for i in range(len_2,len_2+len_1):
        new_1[i] = swap[i]
    return(new_1)
def ltdict_concat(ltdict_1,ltdict_2,**kwargs):
    '''not recursive;
       by default deepcopy_1=1 and deepcopy_2=1;
       return a ltdict;
       by default check=1: will forcefully check if both are ltdicts, return None if either is not a ltdict
       ltdict_1 = {0: 'a', 1: 'b', 2: 'c'}
       ltdict_2 = {0: 'd', 1: 'e', 2: 'f'}
       ltdict_concat(ltdict_1,ltdict_2) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
       ltdict_1 == {0: 'a', 1: 'b', 2: 'c'}
       ltdict_2 == {0: 'd', 1: 'e', 2: 'f'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict_1) & is_ltdict(ltdict_2)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy_1' in kwargs):
        deepcopy_1 = kwargs['deepcopy_1']
    else:
        deepcopy_1 = 1
    if('deepcopy_2' in kwargs):
        deepcopy_2 = kwargs['deepcopy_2']
    else:
        deepcopy_2 = 1
    if(deepcopy_1):
        new_1 = copy.deepcopy(ltdict_1)
    else:
        new_1 = ltdict_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(ltdict_2)
    else:
        new_2 = ltdict_2
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    new = {}
    for i in range(0,len_1):
        new[i] = new_1[i]
    for i in range(len_1,len_1+len_2):
        new[i] = new_2[i-len_1]
    return(new)
def ltdict_first_continuous_indexes_slice(ltdict,value,**kwargs):
    '''
       select all the first continuous indexes whose value equals the given value;
       return a list ;       
       by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
       by default start=0
       ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
       ltdict_first_continuous_indexes_slice(ltdict,'c') == [2, 3]
    '''
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    rslt = []
    begin = 0
    for i in range(start,ltdict.__len__()):
        if(ltdict[i] == value):
            rslt.append(i)
            begin = i+1
            break
        else:
            pass
    for i in range(begin,ltdict.__len__()):
        if(ltdict[i] == value):
            rslt.append(i)
        else:
            break
    return(rslt)
def ltdict_last_continuous_indexes_slice(ltdict,value,**kwargs):
    '''
       select all the last continuous indexes whose value equals the given value;
       return a list ;       
       by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
       by default start= ltdict.__len__() -1  
       ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
       ltdict_last_continuous_indexes_slice(ltdict,'c') == [8, 9]
    '''
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = -1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if(start==-1):
        start = ltdict.__len__()-1
    rslt = []
    begin = 0
    for i in range(start,-1,-1):
        if(ltdict[i] == value):
            rslt.append(i)
            begin = i-1
            break
        else:
            pass
    for i in range(begin,-1,-1):
        if(ltdict[i] == value):
            rslt.append(i)
        else:
            break
    rslt.reverse()
    return(rslt)
def ltdict_all_continuous_indexes_slices_array(ltdict,value,**kwargs):    
    '''
        select all the continuous indexes whose value equals the given value;
        return a list ;       
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_all_continuous_indexes_slices_array(ltdict,'c') == [[2, 3], [5], [8, 9]]
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    len = ltdict.__len__()
    sarray = []
    start = 0
    while(start < len):
        rslt = ltdict_first_continuous_indexes_slice(ltdict,value,start=start,check=0)
        sarray.append(rslt)
        start = rslt[-1] +1
    return(sarray)
def ltdict_indexes_array(ltdict,value,**kwargs):
    '''
        select all the indexes whose value equals the given value;
        return a list ;       
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_indexes_array(ltdict,'c') == [2, 3, 5, 8, 9]
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    rslt = []
    for i in range(0,ltdict.__len__()):
        if(ltdict[i] == value):
            rslt.append(i)
        else:
            pass
    return(rslt)
def ltdict_first_index(ltdict,value,**kwargs):
    '''
        select all the first index whose value equals the given value;
        return a list ;       
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_first_index(ltdict,'c') == 2
    '''
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    for i in range(start,ltdict.__len__()):
        if(ltdict[i] == value):
            return(i)
        else:
            pass
    return(None)
def ltdict_last_index(ltdict,value,**kwargs):
    '''
        select all the last index whose value equals the given value;
        return a list ;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_last_index(ltdict,'c') == 9
    '''
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = -1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if(start == -1):
        start = ltdict.__len__() - 1
    for i in range(start,-1,-1):
        if(ltdict[i] == value):
            return(i)
        else:
            pass
    return(None)
def ltdict_append(ltdict,value,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0: 'a', 1: 'b', 2: 'c'}
        ltdict_append(ltdict,'d') == {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = ltdict.__len__()
    new[len] = value
    return(new)
def ltdict_prepend(ltdict,value,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0: 'a', 1: 'b', 2: 'c'}
        ltdict_prepend(ltdict,'d') == {0: 'd', 1: 'a', 2: 'b', 3: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = ltdict.__len__()
    swap = {}
    for i in range(0,len):
        swap[i + 1] = new[i]
    for i in range(1,len+1):
        new[i] = swap[i]
    new[0] = value
    return(new)
def ltdict_clear(ltdict,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0: 'a', 1: 'b', 2: 'c'}
        ltdict_clear(ltdict) == {}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = {}
    else:
        new = ltdict
        new.clear()
    return(new)
def ltdict_copy(ltdict,**kwargs):
    '''
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    ltdict = ltdict.copy()
    return(ltdict)
def ltdict_deepcopy(ltdict,**kwargs):
    '''
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    ltdict = copy.deepcopy(ltdict)
    return(ltdict)
def ltdict_insert(ltdict,index,value,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0: 'a', 1: 'b', 2: 'c'}
        ltdict_insert(ltdict,1,'d') == {0: 'a', 1: 'd', 2: 'b', 3: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = ltdict.__len__()
    swap = {}
    for i in range(0,index):
        swap[i] = new[i]
    swap[index] = value
    for i in range(index + 1,len+1):
        swap[i] = new[i-1]
    for i in range(0,len+1):
        new[i] = swap[i]
    return(new)
def ltdict_insert_ltdict(ltdict_1,index,ltdict_2,**kwargs):
    '''
        by default it will change the original ltdict_1: deepcopy_1 = 0;
                   and will do a shallow copy of ltdict_2: deepcopy_2 = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict_1 = {0: 'a', 1: 'b', 2: 'c'}
        ltdict_2 = {0: 'd', 1: 'e', 2: 'f'}
        ltdict_insert_ltdict(ltdict_1,1,ltdict_2) == {0: 'a', 1: 'd', 2: 'e', 3: 'f', 4: 'b', 5: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict_1) & is_ltdict(ltdict_2)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy_1' in kwargs):
        deepcopy_1 = kwargs['deepcopy_1']
    else:
        deepcopy_1 = 0
    if('deepcopy_2' in kwargs):
        deepcopy_2 = kwargs['deepcopy_2']
    else:
        deepcopy_2 = 0
    if(deepcopy_1):
        new_1 = copy.deepcopy(ltdict_1)
    else:
        new_1 = ltdict_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(ltdict_2)
    else:
        new_2 = copy.copy(ltdict_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    if(index >= len_1):
        return(new_1)
    else:
        pass
    swap = {}
    for i in range(0,index):
        swap[i] = new_1[i]
    for i in range(index,index + len_2):
        swap[i] = new_2[i-index]
    for i in range(index + len_2,len_1+len_2):
        swap[i] = new_1[i-len_2]
    for i in range(0,len_1+len_2):
        new_1[i] = swap[i]
    return(new_1)
def ltdict_include(ltdict,value,**kwargs):
    '''
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0: 'a', 1: 'b', 2: 'c'}
        ltdict_include(ltdict,'c') == True
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    for i in range(0,ltdict.__len__()):
        if(ltdict[i] == value):
            return(True)
    return(False)
def ltdict_count(ltdict,value,**kwargs):
    '''
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_count(ltdict,'c') == 5
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    num = 0
    for i in range(0,ltdict.__len__()):
        if(ltdict[i] == value):
            num = num + 1
    return(num)
def ltdict_pop(ltdict,index,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0: 'a', 1: 'b', 2: 'c'}
        ltdict_pop(ltdict,1) == 'b'
        ltdict == {0: 'a', 1: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = ltdict.__len__()
    if(index < 0):
        index = len + index
    else:
        pass
    if(index in range(0,len)):
        rslt = new[index]
    else:
        rslt = None
        return(rslt)
    for i in range(index,len-1):
        new[i] = new[i+1]
    del new[len-1]
    return(rslt)
def ltdict_pop_range(ltdict,start,end,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_pop_range(ltdict,1,7) == {0: 'b', 1: 'c', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f'}
        ltdict == {0: 'a', 1: 'c', 2: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = ltdict.__len__()
    if(start < 0):
        start = 0
    elif(start >= len):
        start = len
    else:
        pass
    if(end<start):
        end = start
    elif(end >= len-1):
        end = len-1 
    elif(end < 0):
        end = 0
    else:
        pass
    rslt = {}
    seq = 0
    for i in range(start,end+1):
        rslt[seq] = new[i]
        seq = seq + 1
    swap = {}
    range_len = end-start+1
    for i in range(0,start):
        swap[i] = new[i]
    for i in range(start,end+1):
        s = i+range_len
        if(s in new):
            swap[i] = new[s]
    for i in range(end+1,len):
        s = i+range_len
        if(s in new):
            swap[i] = new[s]
    for i in range(0,swap.__len__()):
        new[i] = swap[i]
    for i in range(swap.__len__(),len):
        del new[i]
    return(rslt)
def ltdict_pop_seqs(ltdict,seqs_set,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        seqs_set = {2,5,8}
        ltdict_pop_seqs(ltdict,seqs_set) == {0: 'c', 1: 'c', 2: 'c'}
        ltdict == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = new.__len__()
    rslt = {}
    if(utils.is_list(seqs_set)):
        pass
    elif(utils.is_set(seqs_set)):
        real_seqs = list(seqs_set)
    elif(utils.is_ltdict(seqs_set)):
        real_seqs = ltdict_to_list(seqs_set)
    else:
        print("Error: <seqs_set> Invalid")
        return(None)
    len = real_seqs.__len__()
    i = 0
    while((len > 0)&(i<len)):
        if(real_seqs[i] in new):
            pass
        else:
            real_seqs.pop(i)
        i = i + 1
        len = real_seqs.__len__()
    real_seqs.sort()
    j = 0
    for i in range(0,real_seqs.__len__()):
        seq = real_seqs[i]
        rslt[j] = new[seq]
        j = j + 1
    step = 0
    for i in range(0,real_seqs.__len__()):
        seq = real_seqs[i] - step 
        ltdict_pop(new,seq)
        step = step +1
    return(rslt)
def ltdict_remove_first(ltdict,value,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_remove_first(ltdict,'c') == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f', 7: 'c', 8: 'c'}
        ltdict == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f', 7: 'c', 8: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = new.__len__()
    start = len
    for i in range(0,len):
        if(new[i]==value):
            start = i
            break
    for i in range(start,len-1):
        new[i] = new [i+1]
    del new[len-1]
    return(new)
def ltdict_remove_last(ltdict,value,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_remove_last(ltdict,'c') == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'd', 5: 'c', 6: 'e', 7: 'f', 8: 'c'}
        ltdict == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'd', 5: 'c', 6: 'e', 7: 'f', 8: 'c'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = new.__len__()
    end = len
    for i in range(len-1,-1,-1):
        if(new[i]==value):
            end = i
            break
    for i in range(end,len-1):
        new[i] = new [i+1]
    del new[len-1]
    return(new)
def ltdict_remove_all(ltdict,value,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_remove_all(ltdict,'c') == {0: 'a', 1: 'b', 2: 'd', 3: 'e', 4: 'f'}
        ltdict == {0: 'a', 1: 'b', 2: 'd', 3: 'e', 4: 'f'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = new.__len__()
    i = 0
    while(i<len):
        step = 0
        if(new[i]==value):
            for j in range(i,len-1):
                new[j] = new [j+1]
            del new[len-1]
            step = 1
        len = new.__len__()
        i = i + 1 -step
    return(new)
def ltdict_reverse(ltdict,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_reverse(ltdict) == {0: 'c', 1: 'c', 2: 'f', 3: 'e', 4: 'c', 5: 'd', 6: 'c', 7: 'c', 8: 'b', 9: 'a'}
        ltdict == {0: 'c', 1: 'c', 2: 'f', 3: 'e', 4: 'c', 5: 'd', 6: 'c', 7: 'c', 8: 'b', 9: 'a'}
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = new.__len__()
    if(len%2):
        mid = len//2
    else:
        mid = len//2 - 1
    for i in range(0,mid+1):
        temp = new[len-1-i]
        new[len-1-i] = new[i]
        new[i] = temp
    return(new)
def ltdict_sort(ltdict,**kwargs):
    '''
        by default it will change the original ltdict: deepcopy = 0;
        by default check=1: will forcefully check if it is a ltdict, return None if it is not a ltdict
        ltdict = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        ltdict_sort(ltdict) == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'c', 5: 'c', 6: 'c', 7: 'd', 8: 'e', 9: 'f'}
        ltdict == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'c', 5: 'c', 6: 'c', 7: 'd', 8: 'e', 9: 'f'}
    '''
    if('inverse' in kwargs):
        inverse = kwargs['inverse']
    else:
        inverse = False
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        new = copy.deepcopy(ltdict)
    else:
        new = ltdict
    len = new.__len__()
    ol = sorted(new.items(), key=itemgetter(1),reverse=inverse)
    for i in range(0,ol.__len__()):
        new[i] = ol[i][1]
    return(new)

def ltdict_comprise(ltdict1,ltdict2,**kwargs):
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_ltdict(ltdict1)):
            pass
        else:
            return(None)
        if(is_ltdict(ltdict2)):
            pass
        else:
            return(None)
    else:
        pass
    len_1 = ltdict1.__len__()
    len_2 = ltdict2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        ltdict1 = ltdict_to_list(ltdict1)
        ltdict2 = ltdict_to_list(ltdict2)
        if(strict):
            if(ltdict2 == ltdict1[:len_2]):
                return(True)
            else:
                return(False)
        else:
            end = len_1 - len_2
            for i in range(0,end+1):
                if(ltdict2 == ltdict1[i:(i+len_2)]):
                    print(i)
                    return(i)
                else:
                    pass
            return(False)
            
