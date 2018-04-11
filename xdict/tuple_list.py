import copy
from operator import itemgetter
from xdict import utils

def is_tuple_list(obj):
    if(utils.is_list(obj)):
        pass
    else:
        return(False)
    if(obj == []):
        return(True)
    else:
        for each in obj:
            if(utils.is_tuple(each)):
                if(each.__len__()==2):
                    return(True)
                else:
                    return(False)
            else:
                return(False)

def tuple_list_to_json(tuple_list,**kwargs):
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    j = {}
    if(deepcopy):
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    for i in range(0,new.__len__()):
        temp = new[i]
        key = temp[0]
        value = temp[1]
        j[str(key)] = new[key]
    return(j)

def dict_to_tuple_list(this_dict,**kwargs):
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
    tuple_list = {}
    if(deepcopy):
        new = copy.deepcopy(this_dict)
    else:
        new = this_dict
    i = 0
    for key in this_dict:
        value = this_dict[key]
        tuple_list[i] = (key,value)
        i = i + 1
    return(tuple_list)

def tuple_list_to_dict(tuple_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
    length = tuple_list.__len__()
    if(deepcopy):
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    for i in range(0,length):
        temp = new[i]
        key = temp[0]
        value = temp[1]
        d[key] = value
    return(s)

def kv_list_to_tuple_list(klist,vlist,**kwargs):
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
    tuple_list = {}
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
        tuple_list[i] = (key,value)
    return(tuple_list)


def tuple_list_to_kv_list(tuple_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
    len = tuple_list.__len__()
    if(deepcopy):
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    for i in range(0,len):
        temp = new[i]
        key = temp[0]
        value = temp[1]
        kl.append(key)
        vl.append(value)
    return({"klist":kl,"vlist":vl})


def tuple_list_extend(tuple_list_1,tuple_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list_1) & is_tuple_list(tuple_list_2)):
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
        new_1 = copy.deepcopy(tuple_list_1)
    else:
        new_1 = tuple_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(tuple_list_2)
    else:
        new_2 = copy.copy(tuple_list_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    for i in range(0,len_2):
        new_1.append(new_2[i])
    return(new_1)

def tuple_list_prepend_extend(tuple_list_1,tuple_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list_1) & is_tuple_list(tuple_list_2)):
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
        new_1 = copy.deepcopy(tuple_list_1)
    else:
        new_1 = tuple_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(tuple_list_2)
    else:
        new_2 = copy.copy(tuple_list_2)
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    swap = []
    for i in range(0,len_2):
        swap.append(new_2[i])
    for i in range(0,len_1):
        swap.append(new_1[i])
    return(swap)

def tuple_list_concat(tuple_list_1,tuple_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list_1) & is_tuple_list(tuple_list_2)):
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
        new_1 = copy.deepcopy(tuple_list_1)
    else:
        new_1 = tuple_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(tuple_list_2)
    else:
        new_2 = tuple_list_2
    len_1 = new_1.__len__()
    len_2 = new_2.__len__()
    new = []
    for i in range(0,len_1):
        new.append(new_1[i])
    for i in range(0,len_2):
        new.append(new_2[i])
    return(new)

def tuple_list_first_continuous_indexes_slice(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    rslt = []
    begin = 0
    for i in range(start,tuple_list.__len__()):
        temp = tuple_list[i]
        k = temp[0]
        v = temp[1]
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
    for i in range(begin,tuple_list.__len__()):
        temp = tuple_list[i]
        k = temp[0]
        v = temp[1]
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

def tuple_list_last_continuous_indexes_slice(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    if(start==-1):
        start = tuple_list.__len__()-1
    rslt = []
    begin = 0
    for i in range(start,-1,-1):
        temp = tuple_list[i]
        k = temp[0]
        v = temp[1]
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
        temp = tuple_list[i]
        k = temp[0]
        v = temp[1]
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

def tuple_list_all_continuous_indexes_slices_array(tuple_list,**kwargs):    
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    len = tuple_list.__len__()
    sarray = []
    start = 0
    while(start < len):
        if(mode == 'key'):
            rslt = tuple_list_first_continuous_indexes_slice(tuple_list,key=key,start=start,check=0,mode='key')
        elif(mode == 'value'):
            rslt = tuple_list_first_continuous_indexes_slice(tuple_list,value=value,start=start,check=0,mode='value')
        else:
            rslt = tuple_list_first_continuous_indexes_slice(tuple_list,key=key,value=value,start=start,check=0,mode='key_value')
        sarray.append(rslt)
        start = rslt[-1] +1
    return(sarray)

def tuple_list_indexes_array(tuple_list,value,**kwargs):
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    rslt = []
    for i in range(0,tuple_list.__len__()):
        temp = tuple_list[i]
        k = temp[0]
        v = temp[1]
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

def tuple_list_first_index(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    for i in range(start,tuple_list.__len__()):
        temp = tuple_list[i]
        k = temp[0]
        v = temp[1]
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

def tuple_list_last_index(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    if(start == -1):
        start = tuple_list.__len__() - 1
    for i in range(start,-1,-1):
        temp = tuple_list[i]
        k = temp[0]
        v = temp[1]
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

def tuple_list_append(tuple_list,key,value,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    new.append((key,value))
    return(new)

def tuple_list_prepend(tuple_list,key,value,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = tuple_list.__len__()
    swap = []
    swap.append((key,value))
    for i in range(0,len):
        swap.append(new[i])
    return(swap)

def tuple_list_clear(tuple_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
        new = tuple_list
        new.clear()
    return(new)

def tuple_list_copy(tuple_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    tuple_list = tuple_list.copy()
    return(tuple_list)

def tuple_list_deepcopy(tuple_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    tuple_list = copy.deepcopy(tuple_list)
    return(tuple_list)

def tuple_list_insert(tuple_list,index,key,value,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    new.insert(index,(key,value))
    return(new)


def tuple_list_insert_tuple_list(tuple_list_1,index,tuple_list_2,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list_1) & is_tuple_list(tuple_list_2)):
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
        new_1 = copy.deepcopy(tuple_list_1)
    else:
        new_1 = tuple_list_1
    if(deepcopy_2):
        new_2 = copy.deepcopy(tuple_list_2)
    else:
        new_2 = copy.copy(tuple_list_2)
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


def tuple_list_include(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    if(mode =='key'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(k == key):
                return(True)
    elif(mode == 'value'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(v == value):
                return(True)
    else:
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                return(True)
    return(False)


def tuple_list_count(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    num = 0
    if(mode =='key'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(k == key):
                num = num + 1
    elif(mode == 'value'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(v == value):
                num = num + 1
    else:
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                num = num + 1
    return(num)

def tuple_list_pop(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = tuple_list.__len__()
    if(mode == 'index'):
        if(index in range(0,len)):
            rslt = new.pop(index)
        else:
            rslt = None
    else:
        rslt = []
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(k == key):
                rslt.append(tuple_list.pop(i))
    return(rslt)

def tuple_list_pop_range(tuple_list,start,end,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = tuple_list.__len__()
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

def tuple_list_pop_seqs(tuple_list,seqs_set,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = new.__len__()
    rslt = []
    if(utils.is_list(seqs_set)):
        pass
    elif(utils.is_set(seqs_set)):
        real_seqs = list(seqs_set)
    elif(utils.is_tuple_list(seqs_set)):
        real_seqs = tuple_list_to_list(seqs_set)
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

def tuple_list_remove_first(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = new.__len__()
    if(mode =='key'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(k == key):
                new.remove(temp)
                break
    elif(mode == 'value'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(v == value):
                new.remove(temp)
                break
    else:
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                new.remove(temp)
                break
    return(new)

def tuple_list_remove_last(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = new.__len__()
    if(mode =='key'):
        for i in range(len-1,-1,-1):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(k == key):
                new.remove(temp)
                break
    elif(mode == 'value'):
        for i in range(len-1,-1,-1):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(v == value):
                new.remove(temp)
                break
    else:
        for i in range(len-1,-1,-1):
            temp = tuple_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                new.remove(temp)
                break
    return(new)

def tuple_list_remove_all(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = new.__len__()
    i = 0
    if(mode =='key'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(k == key):
                new.remove(temp)
    elif(mode == 'value'):
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            k = temp[0]
            v = temp[1]
            if(v == value):
                new.remove(temp)
    else:
        for i in range(0,tuple_list.__len__()):
            temp = tuple_list[i]
            key = temp[0]
            value = temp[1]
            if((k==key)&(v==value)):
                new.remove(temp)
    return(new)

def tuple_list_reverse(tuple_list,**kwargs):
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = new.__len__()
    new.reverse()
    return(new)

def tuple_list_sort(tuple_list,**kwargs):
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
        if(is_tuple_list(tuple_list)):
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
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    len = new.__len__()
    if(mode == 'key'):
        new = sorted(new,reverse=inverse)
    else:
        sorted(new, key=itemgetter(1),reverse=inverse)
    return(new)

def tuple_list_comprise(tuple_list1,tuple_list2,**kwargs):
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tuple_list(tuple_list1)):
            pass
        else:
            return(None)
        if(is_tuple_list(tuple_list2)):
            pass
        else:
            return(None)
    else:
        pass
    len_1 = tuple_list1.__len__()
    len_2 = tuple_list2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        tuple_list1 = tuple_list_to_list(tuple_list1)
        tuple_list2 = tuple_list_to_list(tuple_list2)
        if(strict):
            if(tuple_list2 == tuple_list1[:len_2]):
                return(True)
            else:
                return(False)
        else:
            end = len_1 - len_2
            for i in range(0,end+1):
                if(tuple_list2 == tuple_list1[i:(i+len_2)]):
                    print(i)
                    return(i)
                else:
                    pass
            return(False)
           

#
def tuple_list_to_dict_list(tl):
    dl =[]
    for i in range(0,tl.__len__()):
        ele = utils.tuple_to_dict_ele(tl[i])
        dl.append(ele)
    return(dl)

#


def set_tupleList_which(tl,key,value,which=0):
    '''
    '''
    length = tl.__len__()
    cursor = 0
    for i in range(0,length):
        t = tl[i]
        k = t[0]
        v = t[1]
        if(k == key):
            cond = (cursor == which)
            if(cond):
                nt = (key,value)
                tl[i] = nt
                break
            else:
                pass
            cursor = cursor + 1
        else:
            pass
    return(tl)


def get_tupleList_which(tl,key,which=0):
    '''
    '''
    length = tl.__len__()
    cursor = 0
    for i in range(0,length):
        t = tl[i]
        k = t[0]
        v = t[1]
        if(k == key):
            cond = (cursor == which)
            if(cond):
                return(v)
            else:
                pass
            cursor = cursor + 1
        else:
            pass
    raise KeyError(key)

####### 
