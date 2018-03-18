import copy
from operator import itemgetter
import functools
from xdict import utils

def is_dict_list(obj):
    if(utils.is_list(obj)):
        pass
    else:
        return(False)
    if(obj == []):
        return(True)
    else:
        for each in obj:
            if(utils.is_dict(each)):
                if(each.__len__()==1):
                    return(True)
                else:
                    return(False)
            else:
                return(False)

def dict_list_to_json(dict_list,**kwargs):
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    j = {}
    if(deepcopy):
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    for i in range(0,new.__len__()):
        temp = new[i]
        key = list(temp.keys())[0]
        value = list(temp.values())[0]
        j[str(key)] = new[key]
    return(j)

def dict_to_dict_list(this_dict,**kwargs):
    '''
        >>> dict_to_dict_list({1:2,3:4})
        [{1: 2}, {3: 4}]
        >>>
    ''' 
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(utils.is_dict(this_dict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    dict_list = []
    if(deepcopy):
        new = copy.deepcopy(this_dict)
    else:
        new = this_dict
    for key in this_dict:
        value = this_dict[key]
        dict_list.append({key:value})
    return(dict_list)

def dict_list_to_dict(dict_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    d = {}
    length = dict_list.__len__()
    if(deepcopy):
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    for i in range(0,length):
        temp = new[i]
        key = list(temp.keys())[0]
        value = list(temp.values())[0]
        d[key] = value
    return(s)

def kv_list_to_dict_list(klist,vlist,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(utils.is_list(klist)):
            pass
        else:
            return(None)
        if(utils.is_list(vlist)):
            pass
        else:
            return(None)
        if(klist.__len__()==vlist.__len__()):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    dict_list = {}
    len = klist.__len__()
    if(deepcopy):
        newk = copy.deepcopy(klist)
        newv = copy.deepcopy(vlist)
    else:
        newk = klist
        newv = vlist
    for i in range(0,len):
        key = newk[i]
        value = newv[i]
        dict_list[i] = {key:value}
    return(dict_list)

def dict_list_to_kv_list(dict_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    kl = []
    vl = []
    len = dict_list.__len__()
    if(deepcopy):
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    for i in range(0,len):
        temp = new[i]
        key = list(temp.keys())[0]
        value = list(temp.values())[0]
        kl.append(key)
        vl.append(value)
    return({"klist":kl,"vlist":vl})

#180
def dict_list_extend(dict_list_1,dict_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list_1) & is_dict_list(dict_list_2)):
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
        new_1 = copy.deepcopy(dict_list_1)
    else:
        new_1 = dict_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(dict_list_2)
    else:
        new_2 = copy.copy(dict_list_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    for i in range(0,len_2):
        new_1.append(new_2[i])
    return(new_1)

def dict_list_prepend_extend(dict_list_1,dict_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list_1) & is_dict_list(dict_list_2)):
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
        new_1 = copy.deepcopy(dict_list_1)
    else:
        new_1 = dict_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(dict_list_2)
    else:
        new_2 = copy.copy(dict_list_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    swap = []
    for i in range(0,len_2):
        swap.append(new_2[i])
    for i in range(0,len_1):
        swap.append(new_1[i])
    return(swap)

def dict_list_concat(dict_list_1,dict_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list_1) & is_dict_list(dict_list_2)):
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
        new_1 = copy.deepcopy(dict_list_1)
    else:
        new_1 = dict_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(dict_list_2)
    else:
        new_2 = dict_list_2
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    new = []
    for i in range(0,len_1):
        new.append(new_1[i])
    for i in range(0,len_2):
        new.append(new_2[i])
    return(new)
#287
def dict_list_first_continuous_indexes_slice(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    rslt = []
    begin = 0
    for i in range(start,dict_list.__len__()):
        temp = dict_list[i]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        if(mode == 'key'):
            if(k == key):
                rslt.append(i)
                begin = i+1
                break
            else:
                pass
        elif(mode == 'value'):
            if(v == value):
                rslt.append(i)
                begin = i+1
                break
            else:
                pass
        else:
            if((v == value)&(k == key)):
                rslt.append(i)
                begin = i+1
                break
            else:
                pass
    for i in range(begin,dict_list.__len__()):
        temp = dict_list[i]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        if(mode == 'key'):
            if(k == key):
                rslt.append(i)
            else:
                break
        elif(mode == 'value'):
            if(v == value):
                rslt.append(i)
            else:
                break
        else:
            if((v == value)&(k == key)):
                rslt.append(i)
            else:
                break
    return(rslt)
#359
def dict_list_last_continuous_indexes_slice(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = -1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    if(start==-1):
        start = dict_list.__len__()-1
    rslt = []
    begin = 0
    for i in range(start,-1,-1):
        temp = dict_list[i]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        if(mode == 'key'):
            if(k == key):
                rslt.append(i)
                begin = i-1
                break
            else:
                pass
        elif(mode == 'value'):
            if(v == value):
                rslt.append(i)
                begin = i-1
                break
            else:
                pass
        else:
            if((v == value)&(k == key)):
                rslt.append(i)
                begin = i-1
                break
            else:
                pass
    for i in range(begin,-1,-1):
        temp = dict_list[i]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        if(mode == 'key'):
            if(k == key):
                rslt.append(i)
            else:
                break
        elif(mode == 'value'):
            if(v == value):
                rslt.append(i)
            else:
                break
        else:
            if((v == value)&(k == key)):
                rslt.append(i)
            else:
                break
    rslt.reverse()
    return(rslt)
#434
def dict_list_all_continuous_indexes_slices_array(dict_list,**kwargs):    
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    len = dict_list.__len__()
    sarray = []
    start = 0
    while(start < len):
        if(mode == 'key'):
            rslt = dict_list_first_continuous_indexes_slice(dict_list,key=key,start=start,check=0,mode='key')
        elif(mode == 'value'):
            rslt = dict_list_first_continuous_indexes_slice(dict_list,value=value,start=start,check=0,mode='value')
        else:
            rslt = dict_list_first_continuous_indexes_slice(dict_list,key=key,value=value,start=start,check=0,mode='key_value')
        sarray.append(rslt)
        start = rslt[-1] +1
    return(sarray)

def dict_list_indexes_array(dict_list,value,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    rslt = []
    for i in range(0,dict_list.__len__()):
        temp = dict_list[i]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        if(mode == 'key'):
            if(k == key):
                rslt.append(i)
            else:
                pass
        elif(mode == 'value'):
            if(v == value):
                rslt.append(i)
            else:
                pass
        else:
            if((v == value)&(k == key)):
                rslt.append(i)
            else:
                pass
    return(rslt)

def dict_list_first_index(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = 0
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    for i in range(start,dict_list.__len__()):
        temp = dict_list[i]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        if(mode == 'key'):
            if(k == key):
                return(i)
            else:
                pass
        elif(mode == 'value'):
            if(v == value):
                return(i)
            else:
                pass
        else:
            if((v == value)&(k == key)):
                return(i)
            else:
                pass
    return(None)

def dict_list_last_index(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('start' in kwargs):
        start = kwargs['start']
    else:
        start = -1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    if(start == -1):
        start = dict_list.__len__() - 1
    for i in range(start,-1,-1):
        temp = dict_list[i]
        k = list(temp.keys())[0]
        v = list(temp.values())[0]
        if(mode == 'key'):
            if(k == key):
                return(i)
            else:
                pass
        elif(mode == 'value'):
            if(v == value):
                return(i)
            else:
                pass
        else:
            if((v == value)&(k == key)):
                return(i)
            else:
                pass
    return(None)

def dict_list_append(dict_list,key,value,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    new.append((key,value))
    return(new)

def dict_list_prepend(dict_list,key,value,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = dict_list.__len__()
    swap = []
    swap.append((key,value))
    for i in range(0,len):
        swap.append(new[i])
    return(swap)

def dict_list_clear(dict_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = []
    else:
        new = dict_list
        new.clear()
    return(new)

def dict_list_copy(dict_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    dict_list = dict_list.copy()
    return(dict_list)

def dict_list_deepcopy(dict_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    dict_list = copy.deepcopy(dict_list)
    return(dict_list)

def dict_list_insert(dict_list,index,key,value,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    new.insert(index,(key,value))
    return(new)


def dict_list_insert_dict_list(dict_list_1,index,dict_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list_1) & is_dict_list(dict_list_2)):
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
        new_1 = copy.deepcopy(dict_list_1)
    else:
        new_1 = dict_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(dict_list_2)
    else:
        new_2 = copy.copy(dict_list_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    if(index >= len_1):
        return(new_1)
    else:
        pass
    swap = []
    for i in range(0,index):
        swap.append(new_1[i])
    for i in range(index,index + len_2):
        swap.append(new_2[i-index])
    for i in range(index + len_2,len_1+len_2):
        swap.append(new_1[i-len_2])
    return(swap)


def dict_list_include(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    if(mode =='key'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(k == key):
                return(True)
    elif(mode == 'value'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(v == value):
                return(True)
    else:
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                return(True)
    return(False)


def dict_list_count(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
            pass
        else:
            return(None)
    else:
        pass
    num = 0
    if(mode =='key'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(k == key):
                num = num + 1
    elif(mode == 'value'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(v == value):
                num = num + 1
    else:
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                num = num + 1
    return(num)

def dict_list_pop(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'index'
    if('key' in kwargs):
        key = kwargs['key']
    if('index' in kwargs):
        index = kwargs['index']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = dict_list.__len__()
    if(mode == 'index'):
        if(index in range(0,len)):
            rslt = new.pop(index)
        else:
            rslt = None
    else:
        rslt = []
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(k == key):
                rslt.append(dict_list.pop(i))
    return(rslt)

def dict_list_pop_range(dict_list,start,end,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = dict_list.__len__()
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
    rslt = []
    seq = 0
    for i in range(start,end+1):
        rslt.append(new.pop(i))
        seq = seq + 1
    return(rslt)

def dict_list_pop_seqs(dict_list,seqs_set,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = new.__len__()
    rslt = []
    if(utils.is_list(seqs_set)):
        pass
    elif(utils.is_set(seqs_set)):
        real_seqs = list(seqs_set)
    elif(utils.is_dict_list(seqs_set)):
        real_seqs = dict_list_to_list(seqs_set)
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
    for i in range(0,real_seqs.__len__()):
        seq = real_seqs[i]
        rslt.append(new.pop(seq))
    return(rslt)

def dict_list_remove_first(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = new.__len__()
    if(mode =='key'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(k == key):
                new.remove(temp)
                break
    elif(mode == 'value'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(v == value):
                new.remove(temp)
                break
    else:
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                new.remove(temp)
                break
    return(new)

def dict_list_remove_last(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = new.__len__()
    if(mode =='key'):
        for i in range(len-1,-1,-1):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(k == key):
                new.remove(temp)
                break
    elif(mode == 'value'):
        for i in range(len-1,-1,-1):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(v == value):
                new.remove(temp)
                break
    else:
        for i in range(len-1,-1,-1):
            temp = dict_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                new.remove(temp)
                break
    return(new)

def dict_list_remove_all(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = new.__len__()
    i = 0
    if(mode =='key'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(k == key):
                new.remove(temp)
    elif(mode == 'value'):
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            k = list(temp.keys())[0]
            v = list(temp.values())[0]
            if(v == value):
                new.remove(temp)
    else:
        for i in range(0,dict_list.__len__()):
            temp = dict_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                new.remove(temp)
    return(new)

def dict_list_reverse(dict_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = new.__len__()
    new.reverse()
    return(new)

def dict_list_sort(dict_list,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'key'
    if('key' in kwargs):
        key = kwargs['key']
    if('value' in kwargs):
        value = kwargs['value']
    if('inverse' in kwargs):
        inverse = kwargs['inverse']
    else:
        inverse = False
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list)):
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
        new = copy.deepcopy(dict_list)
    else:
        new = dict_list
    len = new.__len__()
    if(mode == 'key'):
        new = sorted(new,reverse=inverse)
    else:
        sorted(new, key=itemgetter(1),reverse=inverse)
    return(new)

def dict_list_comprise(dict_list1,dict_list2,**kwargs):
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_dict_list(dict_list1)):
            pass
        else:
            return(None)
        if(is_dict_list(dict_list2)):
            pass
        else:
            return(None)
    else:
        pass
    len_1 = dict_list1.__len__()
    len_2 = dict_list2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        dict_list1 = dict_list_to_list(dict_list1)
        dict_list2 = dict_list_to_list(dict_list2)
        if(strict):
            if(dict_list2 == dict_list1[:len_2]):
                return(True)
            else:
                return(False)
        else:
            end = len_1 - len_2
            for i in range(0,end+1):
                if(dict_list2 == dict_list1[i:(i+len_2)]):
                    print(i)
                    return(i)
                else:
                    pass
            return(False)
           

#
def dict_list_to_tuple_list(dl):
    tl = []
    for i in range(0,dl.__len__()):
        ele = tuple_to_dict_ele(dl[i])
        tl.append(ele)
    return(tl)


#------------------------




def cmp_dict(d1,d2,**kwargs):
    '''
    '''
    def default_eq_func(value1,value2):
        cond = (value1 == value2)
        return(cond)
    def default_gt_func(value1,value2):
        cond = (value1 > value2)
        return(cond)
    def default_lt_func(value1,value2):
        cond = (value1 < value2)
        return(cond)
    if('eq_func' in kwargs):
        eq_func = kwargs['eq_func']
    else:
        eq_func = default_eq_func
    if('gt_func' in kwargs):
        gt_func = kwargs['gt_func']
    else:
        gt_func = default_gt_func
    if('lt_func' in kwargs):
        lt_func = kwargs['lt_func']
    else:
        lt_func = default_lt_func
    keys = kwargs['cond_keys']
    length = keys.__len__()
    for i in range(0,length):
        key = keys[i]
        cond = eq_func(d1[key],d2[key])
        if(cond):
            pass
        else:
            cond = gt_func(d1[key],d2[key])
            if(cond):
                return(1)
            else:
                return(-1)
    return(0)



def sort_dictList(dictList,**kwargs):
    '''
        students = [
            {'name':'john','class':'A', 'year':15},
            {'name':'jane','class':'B', 'year':12},
            {'name':'dave','class':'B', 'year':10}
        ]
        
        rslt = sort_dictList(students,cond_keys=['name','class','year'])
        pobj(rslt)
        rslt = sort_dictList(students,cond_keys=['name','year','class'])
        pobj(rslt)
        rslt = sort_dictList(students,cond_keys=['class','name','year'])
        pobj(rslt)
        rslt = sort_dictList(students,cond_keys=['class','year','name'])
        pobj(rslt)
        rslt = sort_dictList(students,cond_keys=['year','name','class'])
        pobj(rslt)
        rslt = sort_dictList(students,cond_keys=['year','name','class'])
        pobj(rslt)
    '''
    def default_eq_func(value1,value2):
        cond = (value1 == value2)
        return(cond)
    def default_gt_func(value1,value2):
        cond = (value1 > value2)
        return(cond)
    def default_lt_func(value1,value2):
        cond = (value1 < value2)
        return(cond)
    if('eq_func' in kwargs):
        eq_func = kwargs['eq_func']
    else:
        eq_func = default_eq_func
    if('gt_func' in kwargs):
        gt_func = kwargs['gt_func']
    else:
        gt_func = default_gt_func
    if('lt_func' in kwargs):
        lt_func = kwargs['lt_func']
    else:
        lt_func = default_lt_func
    keys = kwargs['cond_keys']
    def cmp_dict(d1,d2):
        '''
        '''
        length = keys.__len__()
        for i in range(0,length):
            key = keys[i]
            cond = eq_func(d1[key],d2[key])
            if(cond):
                pass
            else:
                cond = gt_func(d1[key],d2[key])
                if(cond):
                    return(1)
                else:
                    return(-1)
        return(0)
    ndl = dictList
    ndl = sorted(ndl,key=functools.cmp_to_key(cmp_dict))
    return(ndl)













 
