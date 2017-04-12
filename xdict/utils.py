#https://github.com/ihgazni2/dlixhict-didactic/blob/master/utils.md
import re
import struct
import copy

#Utils
## for object type judgement

def is_list(obj):
    if(type(obj)==type([])):
        return(True)
    else:
        return(False)
def is_tuple(obj):
    if(type(obj)==type(())):
        return(True)
    else:
        return(False)
def is_dict(obj):
    if(type(obj)==type({})):
        return(True)
    else:
        return(False)
def is_set(obj):
    if(type(obj)==type({1})):
        return(True)
    else:
        return(False)
def is_str(obj):
    if(type(obj)==type('')):
        return(True)
    else:
        return(False)
def is_int(obj):
    if(type(obj)==type(0)):
        return(True)
    else:
        return(False)
def is_float(obj):
    if(type(obj)==type(0.0)):
        return(True)
    else:
        return(False)
def is_number(obj):
    if(is_int(obj)|is_float(obj)):
        return(True)
    else:
        return(False)
def is_bool(obj):
    if(type(obj)==type(True)):
        return(True)
    else:
        return(False)
def is_none(obj):
    if(type(obj)==type(None)):
        return(True)
    else:
        return(False)
def is_recursive_type(obj):
    #is_set(obj)
    #you cant add list/dict into set
    #you can also add tuple into set ,if the tuple has recusively dict/list
    if(is_list(obj)|is_tuple(obj)|is_dict(obj)):
        return(True)
    else:
        return(False)
def is_module(obj):
    if(type(obj)==type(os)):
        return(True)
    else:
        return(False)
def is_non_buildin_function(obj):
    def a_function():
        pass
    if(type(obj)==type(a_function)):
        return(True)
    else:
        return(False)
def is_buildin_function(obj):
    if(type(obj)==type(os.system)):
        return(True)
    else:
        return(False)
def is_function(obj):
    if(is_non_buildin_function(obj)|is_buildin_function(obj)):
        return(True)
    else:
        return(False)
def is_type(obj):
    if(type(obj)==type(int)):
        return(True)
    else:
        return(False)
def is_customer_defined_type(obj):
    if(is_recursive_type(obj)|is_str(obj)|is_bool(obj)|is_none(onj)|is_number(obj)|is_function(obj)|is_type(obj)|is_module(obj)):
        return(False)
    else:
        return(True)
def is_hashable_type(obj):
    try:
        d = {obj:1}
    except:
        return(False)
    else:
        return(True)
def is_unhashable_type(obj):
    try:
        d = {obj:1}
    except:
        return(True)
    else:
        return(False)

def is_json(obj,strict=False):
    try:
        json.loads(obj,strict=strict)
    except:
        return(False)
    else:
        return(True)

def get_type_name(obj):
    class_str = str(type(obj))
    regex = re.compile('\'(.*)\'')
    m = regex.search(class_str)
    return(m.group(1))

def is_bytes(obj):
    if(type(obj)==type(b'x')):
        return(True)
    else:
        return(False)


#path string 
def is_slash_end(path_string,delimiter='/'):
    if(path_string == ''):
        return(False)
    if(path_string[-1] == delimiter):
        return(True)
    else:
        return(False)

def get_dir_string_head(path_string,delimiter='/'):
    '''
        >>> get_dir_string_head('a/b/c')
        'a/b/'
        >>> 
        >>> get_dir_string_head('/a/b/c')
        '/a/b/'
        >>> get_dir_string_head('a/b/c/')
        'a/b/'
        >>> get_dir_string_head('/a/b/c/')
        '/a/b/'
    '''
    if(path_string == ''):
        return('')
    path_len = path_string.__len__()
    last_index = path_len - 1
    if(is_slash_end(path_string,delimiter)):
        frm = last_index-1
    else:
        frm = last_index
    sign = 0
    for i in range(frm,-1,-1):
        if(path_string[i] == delimiter):
            sign = 1
            break
    if(sign == 0):
        return('')
    else:
        return(path_string[:(i+1)])

def get_dir_string_tail(path_string,delimiter='/'):
    '''
        >>> get_dir_string_tail('a/b/c')
        'c'
        >>> get_dir_string_tail('/a/b/c')
        'c'
        >>> get_dir_string_tail('a/b/c/')
        'c/'
        >>> get_dir_string_tail('/a/b/c/')
        'c/'
    '''
    if(path_string == ''):
        return('')
    path_len = path_string.__len__()
    last_index = path_len - 1
    if(is_slash_end(path_string,delimiter)):
        frm = last_index-1
    else:
        frm = last_index
    sign = 0
    for i in range(frm,-1,-1):
        if(path_string[i] == delimiter):
            sign = 1
            break
    if(sign == 0):
        return(path_string)
    else:
        return(path_string[(i+1):])
        

def path_str_to_path_list(path_str,sp="/",keep_head_sp=0,keep_end_sp=0):
    if(keep_head_sp):
        path_str = path_str
    else:
        path_str = str_lstrip(path_str,sp,1)
    if(keep_end_sp):
        path_str = path_str
    else:
        path_str = str_rstrip(path_str,sp,1)
    sps = path_str.split(sp)
    return(sps)
    
    
def path_list_to_path_str(path_list,sp="/",keep_head_sp=0,keep_end_sp=0):
    if(keep_head_sp):
        path_list = path_list
    else:
        path_list = path_list[1:]
    if(keep_end_sp):
        path_list = path_list
    else:
        path_list = path_list[:path_list.__len__()-1]
    for i in range(0,path_list.__len__()):
        path_str=''.join((path_str,sp))
    return(path_str)
    

def is_parent_path(son,parent):
    son = son.rstrip('/')
    parent = parent.rstrip('/')
    sks = son.split('/')
    pks = parent.split('/')
    if(pks.__len__() >= sks.__len__()):
        return(0)
    if((sks.__len__() - pks.__len__()) == 1):
        for i in range(0,pks.__len__()):
            if(sks[i] == pks[i]):
                pass
            else:
                return(0)
        return(1)
    else:
        return(0)

def get_parent_path(son):
    if(son == ''):
        son = '/'
    regex = re.compile('(.*)/(.*?)')
    m = regex.search(son)
    return(m.group(1))

def get_rel_path(abs):
    if(abs == ''):
        abs = '/'
    regex = re.compile('(.*)/([^/]*)')
    m = regex.search(abs)
    return(m.group(2))

def is_parent_path_list(parent_pl,son_pl):
    sl_len = son_pl.__len__()
    pl_len = parent_pl.__len__()
    if((sl_len - 1) == pl_len):
        for i in range(0,pl_len):
            if(parent_pl[i] == son_pl[i]):
                pass
            else:
                return(False)
        return(True)
    else:
        return(False)


def is_son_path_list(son_pl,parent_pl):
    sl_len = son_pl.__len__()
    pl_len = parent_pl.__len__()
    if((sl_len - 1) == pl_len):
        for i in range(0,pl_len):
            if(parent_pl[i] == son_pl[i]):
                pass
            else:
                return(False)
        return(True)
    else:
        return(False)

def is_ancestor_path_list(ances_pl,des_pl):
    dl_len = des_pl.__len__()
    al_len = ances_pl.__len__()
    if(dl_len > al_len):
        for i in range(0,al_len):
            if(ances_pl[i] == des_pl[i]):
                pass
            else:
                return(False)
        return(True)
    else:
        return(False)


def is_descedant_path_list(des_pl,ances_pl):
    dl_len = des_pl.__len__()
    al_len = ances_pl.__len__()
    if(dl_len > al_len):
        for i in range(0,al_len):
            if(ances_pl[i] == des_pl[i]):
                pass
            else:
                return(False)
        return(True)
    else:
        return(False)

    
    
#string



def loose_str_to_bool(str):
    if((str == 'False') | (str == 'false')):
        return(False)
    elif((str == 'True') | (str == 'true')):
        return(True)
    else:
        return(None)

def str_lstrip(s,char,count):
    if(s.__len__()<count):
        return(s)
    else:
        for i in range(0,count+1):
            if(s[i] == char):
                pass
            else:
                break
        return(s[i:])

def str_rstrip(s,char,count):
    c = 0
    for i in range(s.__len__()-1,-1,-1):
        if(c==count):
            break
        else:
            if(s[i] == char):
                c = c+1
            else:
                break
    if(c==0):
        return(s)
    else:
        return(s[:(i+1)])


def str_prepend(s,char,n):
    prepend = ''
    for i in range(1,n+1):
        prepend = ''.join((prepend,char))
    return(''.join((prepend,s)))

def str_apppend(s,char,n):
    append = ''
    for i in range(1,n+1):
        append = ''.join((append,char))
    return(''.join((s,append)))

def is_number_str(old_index):
    try:
        int(old_index)
    except:
        return(False)
    else:
        return(True)
    
def str_at_begin_of_str(str1,str2):
    len1 = str1.__len__()
    begin = str2[:len1]
    if(str1 == begin):
        return(True)
    else:
        return(False)



def str_at_end_of_str(str1,str2):
    len1 = str1.__len__()
    len2 = str2.__len__()
    end = str2[(len2-len1):]
    if(str1 == end):
        return(True)
    else:
        return(False)




def string_display_width(s):
    '''
        >>> string_display_width('a')
        1
        >>> string_display_width('去')
        2
        >>> 
    '''
    s= str(s)
    width = 0
    len = s.__len__()
    for i in range(0,len):
        sublen = s[i].encode().__len__()
        sublen = int(sublen/2 + 1/2)
        width = width + sublen
    return(width)

def prepend_spaces_before_str_basedon_displaywidth(s,mw):
    s = str(s)
    w = string_display_width(s)
    space_Len = mw - w
    new_S = ''
    for i in range(0,space_Len):
        new_S = ''.join((' ' , new_S))
    new_S = ''.join((new_S,s))
    return(new_S)



#list dict tuple

def creat_default_list_with_len(len,element=None):
    rslt = []
    for i in range(0,len):
        rslt.append(element)
    return(rslt)

def set_default_dict_items_via_path_list(external_dict,path_list,n2s=0,s2n=0):
    #if path_list already in external_dict, will do nothing 
    this = external_dict
    for i in range(0,path_list.__len__()):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        try:
            this.__getitem__(key)
        except:
            try:
                this.__setitem__(key,{})
            except:
                return(external_dict)
            else:
                pass
            this = this.__getitem__(key)
        else:
            this = this.__getitem__(key)
    return(external_dict)

def path_list_in_dict(external_dict,path_list,n2s=0,s2n=0):
    this = external_dict
    for i in range(0,path_list.__len__()):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        try:
            this = this.__getitem__(key)
        except:
            return(False)
        else:
            pass
    return(True)

def set_dict_items_via_path_list(external_dict,path_list,value,n2s=0,s2n=0):
    this = external_dict
    for i in range(0,path_list.__len__()-1):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        this = this.__getitem__(key)
    this.__setitem__(path_list[-1],value)
    return(external_dict)

def get_dict_items_via_path_list(external_dict,path_list,n2s=0,s2n=0):
    this = external_dict
    for i in range(0,path_list.__len__()):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        this = this.__getitem__(key)
    return(this)

#get_dict_value_from_full_key_path(nhome,"updates/useRmvWithMentions")
def get_dict_value_from_full_key_path(d,full_key_path):
    full_key_path = full_key_path.strip("/")
    if(full_key_path == ''):
        return(d)
    keys = full_key_path.split("/")
    now = d
    klen = keys.__len__()
    for i in range(0,klen):
        try:
            now = now.__getitem__(keys[i])
        except Exception as err:
            now = now.__getitem__(int(keys[i]))
    return(now)


#get_all_sons_full_key_path
def get_all_sons_full_key_path_list(d,full_key_path):
    all_sons_full_key_path_list = []
    value = get_dict_value_from_full_key_path(d,full_key_path)
    value_type = type(value)
    if(value_type == type([])):
        v_len = value.__len__()
        for i in range(0,v_len):
            kp = ''.join((full_key_path.rstrip("/"),"/",str(i)))
            all_sons_full_key_path_list.append(kp)
    elif(value_type == type({})):
        v_len = value.__len__()
        for each in value:
            kp = ''.join((full_key_path.rstrip("/"),"/",each))
            all_sons_full_key_path_list.append(kp)
    else:
        pass
    return(all_sons_full_key_path_list)



def dict_array_description(dora):
    description_dict = {}
    all_leafs = 0
    unhandled_now = {0:''}
    unhandled_next = {}
    while(all_leafs == 0):
        temp = 0
        description_dict_len = description_dict.__len__()
        description_dict[description_dict_len] = {}
        desc_layer_dict = description_dict[description_dict_len]
        unhandled_now_len = unhandled_now.__len__()
        for i in range(0,unhandled_now_len):
            value = get_dict_value_from_full_key_path(dora,unhandled_now[i])
            value_type = type(value)
            desc_layer_dict_len = desc_layer_dict.__len__()
            desc_layer_dict[desc_layer_dict_len] = unhandled_now[i]
            if( value_type == type([])):
                all_sons_fkp_list = get_all_sons_full_key_path_list(dora,unhandled_now[i])
                llen = all_sons_fkp_list.__len__()
                for i in range(0,llen):
                    unhandled_next_len = unhandled_next.__len__()
                    unhandled_next[unhandled_next_len] = all_sons_fkp_list[i]
                temp = temp | 1
            elif(value_type == type({})):
                all_sons_fkp_list = get_all_sons_full_key_path_list(dora,unhandled_now[i])
                llen = all_sons_fkp_list.__len__()
                for i in range(0,llen):
                    unhandled_next_len = unhandled_next.__len__()
                    unhandled_next[unhandled_next_len] = all_sons_fkp_list[i]
                temp = temp | 1
            else:
                temp = temp | 0
        if(temp == 0):
            all_leafs = 1
        unhandled_now = unhandled_next
        unhandled_next = {}
    return(description_dict)

def get_desc_parent_dict(description_dict):
    desc_len = description_dict.__len__()
    parent_dict = {}
    for i in range(0,desc_len):
        each_level_len = description_dict[i].__len__()
        next_level_cursor = 0
        if(i == 0):
            parent_dict[i] = {}
            parent_dict[i+1] = {}
            next_level_len = description_dict[i+1].__len__()
        elif(i == (desc_len - 1)):
            pass
        else:
            parent_dict[i+1] = {}
            next_level_len = description_dict[i+1].__len__()
        for j in range(0,each_level_len):
            if(i == 0):
                parent_dict[i][j] = -1
            if(i == (desc_len - 1)):
                pass
            else:
                for k in range(next_level_cursor,next_level_len):
                    if(is_parent_path(description_dict[i+1][k],description_dict[i][j])):
                        parent_dict[i+1][k] = j
                        next_level_cursor = next_level_cursor + 1
                    else:
                        break
    return(parent_dict)

def tree_desc(description_dict):
    parent_dict = get_desc_parent_dict(description_dict)
    total_count = 0
    desc_len = description_dict.__len__()
    lvseq_dict = {}
    travel_sign_dict = {}
    for i in range(0,desc_len):
        lvseq_dict[i] = 0
        travel_sign_dict[i] = {}
        each_level_len = description_dict[i].__len__()
        for j in range(0,each_level_len):
            travel_sign_dict[i][j] = 0
            total_count = total_count + 1
    indent = '    '
    text = ''
    prev_level = -1
    prev_seq = -1
    curr_level = 0
    curr_seq = 0
    count = 0
    deep_search_path = []
    while(count < total_count):
        each_level_len = description_dict[curr_level].__len__()
        full_key_path = description_dict[curr_level][curr_seq]
        if(curr_level > prev_level):
            text = ''.join((text,'\n',indent * curr_level,full_key_path))
            curr_location = (curr_level,curr_seq)
            deep_search_path.append(curr_location)
            count = count + 1
            lvseq_dict[curr_level] = curr_seq
            if(get_all_sons_full_key_path_list(nhome,full_key_path) == []):
                travel_sign_dict[curr_level][curr_seq] = 2
                if(curr_seq < (each_level_len - 1)):
                    prev_seq = curr_seq
                    prev_level = curr_level
                    next_seq = curr_seq + 1
                    cond = (parent_dict[curr_level][curr_seq] == parent_dict[curr_level][next_seq])
                    lvseq_dict[curr_level] = curr_seq + 1
                    if(cond):
                        curr_level = curr_level
                        curr_seq = curr_seq + 1
                    else:
                        curr_level = curr_level - 1
                        curr_seq = lvseq_dict[curr_level]
                else:
                    prev_seq = curr_seq
                    prev_level = curr_level
                    curr_level = curr_level - 1
                    curr_seq = lvseq_dict[curr_level]
            else:
                prev_level = curr_level 
                curr_level = curr_level + 1
                prev_seq = curr_seq
                curr_seq = lvseq_dict[curr_level]
                travel_sign_dict[curr_level][curr_seq] = 1
        elif(curr_level == prev_level):
            text = ''.join((text,'\n',indent * curr_level,full_key_path))
            curr_location = (curr_level,curr_seq)
            deep_search_path.append(curr_location)
            count = count + 1
            lvseq_dict[curr_level] = curr_seq
            if(get_all_sons_full_key_path_list(nhome,full_key_path) == []):
                travel_sign_dict[curr_level][curr_seq] = 2
                if(curr_seq < (each_level_len - 1)):
                    prev_seq = curr_seq
                    prev_level = curr_level
                    next_seq = curr_seq + 1
                    cond = (parent_dict[curr_level][curr_seq] == parent_dict[curr_level][next_seq])
                    lvseq_dict[curr_level] = curr_seq + 1
                    if(cond):
                        curr_level = curr_level
                        curr_seq = curr_seq + 1
                    else:
                        curr_level = curr_level - 1
                        curr_seq = lvseq_dict[curr_level]
                else:
                    prev_seq = curr_seq
                    prev_level = curr_level
                    curr_level = curr_level - 1
                    curr_seq = lvseq_dict[curr_level]
            else:
                prev_level = curr_level 
                curr_level = curr_level + 1
                prev_seq = curr_seq
                curr_seq = lvseq_dict[curr_level]
                travel_sign_dict[curr_level][curr_seq] = 1
        else:
            travel_sign_dict[curr_level][curr_seq] = 2
            if(curr_seq < (each_level_len - 1)):
                prev_seq = curr_seq
                prev_level = curr_level
                next_seq = curr_seq + 1
                cond = (parent_dict[curr_level][curr_seq] == parent_dict[curr_level][next_seq])
                lvseq_dict[curr_level] = curr_seq + 1
                if(cond):
                    curr_level = curr_level
                    curr_seq = curr_seq + 1
                else:
                    curr_level = curr_level - 1
                    curr_seq = lvseq_dict[curr_level]
            else:
                prev_seq = curr_seq
                prev_level = curr_level
                curr_level = curr_level - 1
                curr_seq = lvseq_dict[curr_level]
    rslt = {}
    rslt['text'] = text
    rslt['parent_dict'] = parent_dict
    rslt['deep_search_path'] =  deep_search_path
    return(rslt)

def dynamic_indent(deep_search_path,description_dict,full_path_display,fr='',to=''):
    if(fr == ''):
        fr = 0
    text = ''
    dsp_len = deep_search_path.__len__()
    if(to == ''):
        to = dsp_len
    for i in range(0,dsp_len):
        x = deep_search_path[i][0]
        y = deep_search_path[i][1]
        ele = description_dict[x][y]
        if(full_path_display):
            line = ele
        else:
            indent = get_parent_path(ele)
            indent = indent.replace('/','')
            indent = ' ' * indent.__len__()
            rel = get_rel_path(ele)
            line = ''.join((indent,rel))
        if((i >= fr) & (i <= to)):
            text = ''.join((text,'\n',line))
    return(text)

def dict_update_just_intersection(dict1,dict2):
    for key in dict2:
        if(key in dict1):
            dict1[key] = dict2[key]
    return(dict1)



def dict_unique_value(d):
    '''
        >>> 
        >>> d
        {0: 1, 1: 2, 2: 2}
        >>> dict_unique_value(d)
        {0: 1, 1: 2}
        >>> 
    '''
    pt = copy.deepcopy(d)
    seqs_for_del =[]
    vset = set({})
    for k in pt:
        vset.add(pt[k])
    tslen = vset.__len__()
    freq = {}
    for k in pt:
        v = pt[k]
        if(v in freq):
            freq[v] = freq[v] + 1
            seqs_for_del.append(k)
        else:
            freq[v] = 0
    npt = {}
    for k in pt:
        if(k in seqs_for_del):
            pass
        else:
            npt[k] = pt[k]
    pt = npt
    return(npt)


def list_unique_value(l):
    '''
        >>> 
        >>> l
        [1, 2, 2]
        >>> list_unique_value(l)
        [1, 2]
        >>> 
    '''
    pt = copy.deepcopy(l)
    seqs_for_del =[]
    vset = set({})
    for v in pt:
        vset.add(v)
    tslen = vset.__len__()
    freq = {}
    for i in range(0,pt.__len__()):
        v = pt[i]
        if(v in freq):
            freq[v] = freq[v] + 1
            seqs_for_del.append(i)
        else:
            freq[v] = 0
    npt = []
    for i in range(0,pt.__len__()):
        if(i in seqs_for_del):
            pass
        else:
            npt.append(pt[i])
    pt = npt
    return(npt)



def list_comprise(list1,list2,**kwargs):
    '''
        >>> 
        >>> list_comprise([1,2,3,4,5],[2,3,4],strict=0)
        True
        >>> list_comprise([1,2,3,4,5],[2,3,4])
        True
        >>> list_comprise([1,2,3,4,5],[2,3,4],strict=1)
        False
        >>> list_comprise([1,2,3,4,5],[1,2,3,4],strict=1)
        True
        >>> 
    '''
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 0
    len_1 = list1.__len__()
    len_2 = list2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        if(strict):
            if(list2 == list1[:len_2]):
                return(True)
            else:
                return(False)
        else:
            end = len_1 - len_2
            for i in range(0,end+1):
                if(list2 == list1[i:(i+len_2)]):
                    return(True)
                else:
                    pass
    return(False)

def dict_comprise(dict1,dict2,**kwargs):
    '''
        >>> 
        >>> dict_comprise({'a':1,'b':2,'c':3,'d':4},{'b':2,'c':3})
        True
        >>> 
    '''
    len_1 = dict1.__len__()
    len_2 = dict2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        for k2 in dict2:
            v2 = dict2[k2]
            if(k2 in dict1):
                v1 = dict1[k2]
                if(v1 == v2):
                    return(True)
                else:
                    return(False)
            else:
                return(False)


def max_wordwidth_in_dict(myDict):
    maxValueWidth = 0
    for each in myDict:
        eachValueWidth = myDict[each].__len__()
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)


def max_display_width_in_dict(myDict):
    maxValueWidth = 0
    for each in myDict:
        eachValueWidth = string_display_width(myDict[each])
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)


    
# char encode decode

def pack_unicode_char_str(char_str):
    '''
        >>> print('a')
        a
        >>> print(ord('a'))
        97
        >>> print(hex(97))
        0x61
        >>> '\x00'
        '\x00'
        >>> print('\x61')
        a
        >>> print('\u0061')
        a
        >>> pack_unicode_char_str('a')
        b'\x00a'
        >>> 
        >>> 
        >>> 
        >>> print('问')
        问
        >>> print(ord('问'))
        38382
        >>> print(hex(38382))
        0x95ee
        >>> print('\x95')
        
        >>> print('\xee')
        î
        >>> print('\u95ee')
        问
        >>> pack_unicode_char_str('问')
        b'\x95\xee'
        >>>
    '''
    u = char_str.encode('raw_unicode_escape')
    u = u.decode('utf-8') 
    if(u.__len__() == 1):
        u = b'\x00' + bytes(u,'latin-1')
    else:
        u = u[2:]
        uh = int(u[0:2],16)
        ul = int(u[2:],16)
        u = bytes((chr(uh)+chr(ul)),'latin-1')
    return(u)


def unpack_unicode_char_bytes(two_bytes):
    '''
        >>> unpack_unicode_char_bytes(b'\x00a')
        'a'
        >>> unpack_unicode_char_bytes(b'\x95\xee')
        '问'
        >>> print('\u0061')
        a
        >>> print('\u95ee')
        问
        >>> 
    '''
    h,l = struct.unpack('BB',two_bytes)
    h = '{0:0>2}'.format(hex(h).lstrip('0x'))
    l = '{0:0>2}'.format(hex(l).lstrip('0x'))
    u = ''.join(('\\u',h,l))
    u = bytes(u,'utf-8')
    s = u.decode('raw_unicode_escape')
    return(s)


def pack_unicode_str(str):
    '''
        >>> pack_unicode_str('abcdefg')
        b'\x00a\x00b\x00c\x00d\x00e\x00f\x00g'
        >>> 
        >>> pack_unicode_str('你们好')
        b'O`N\xecY}'
        >>> 
    '''
    len = str.__len__()
    B = b''
    for i in range(0,len):
        B = B + pack_unicode_char_str(str[i])
    return(B)


def unpack_unicode_bytes_stream(Bs):
    '''
        >>> unpack_unicode_bytes_stream(b'\x00a\x00b\x00c\x00d\x00e\x00f\x00g')
        'abcdefg'
        >>> unpack_unicode_bytes_stream(b'O`N\xecY}')
        '你们好'
        >>> 
    '''
    len = Bs.__len__()
    pairs = len // 2
    t = struct.unpack('{0}B'.format(len),Bs)
    U = ''
    for i in range(0,pairs):
        h = t[2*i]
        l = t[2*i+1]
        h = '{0:0>2}'.format(hex(h).lstrip('0x'))
        l = '{0:0>2}'.format(hex(l).lstrip('0x'))
        u = ''.join(('\\u',h,l))
        u = bytes(u,'utf-8')
        u = u.decode('raw_unicode_escape')
        U = ''.join((U,u))
    return(U)


def char_to_slash_u_str(ch,with_slash_u=1):
    '''
        >>> char_to_slash_u_str('a')
        '\\u0061'
        >>> char_to_slash_u_str('你')
        '\\u4f60'
    '''
    if(ord(ch)<256):
        bs = hex(ord(ch)).replace('0x','\\u00')
        if(with_slash_u):
            return(bs)
        else:
            return(bs[2:])
    else:
        bs = ch.encode('raw_unicode_escape')
        if(with_slash_u):
            return(bs.__str__()[3:-1])
        else:
            return(bs.__str__()[5:-1])


def slash_u_str_to_char(slash_u_str):
    '''
        >>> slash_u_str_to_char('\\u0061')
        'a'
        >>> slash_u_str_to_char('0061')
        'a'
        >>> slash_u_str_to_char('\\u4f60')
        '你'
        >>> slash_u_str_to_char('4f60')
        '你'
        >>> 
    '''
    if(slash_u_str[:2]=='\\u'):
        slash_u_str = slash_u_str[2:]
    else:
        pass
    one = chr(int(slash_u_str[0:2],16))
    two = chr(int(slash_u_str[2:],16))
    pk = ''.join((one,two))
    bs = bytes(pk,'latin-1')
    return(unpack_unicode_char_bytes(bs)) 

def str_to_slash_u_str(a_string,with_slash_u=1):
    '''
        >>> str_to_slash_u_str('你们好',0)
        '4f604eec597d'
        >>> str_to_slash_u_str('你们好',1)
        '\\u4f60\\u4eec\\u597d'
        >>> str_to_slash_u_str('abc',0)
        '006100620063'
        >>> str_to_slash_u_str('abc',1)
        '\\u0061\\u0062\\u0063'
        >>> 
    '''
    rslt = ''
    for i in range(0,a_string.__len__()):
        ch = a_string[i]
        rslt = ''.join((rslt,char_to_slash_u_str(ch,with_slash_u)))
    return(rslt)

def slash_u_str_to_str(slash_us):
    '''
        >>> slash_u_str_to_str('4f604eec597d')
        '你们好'
        >>> slash_u_str_to_str('\\u4f60\\u4eec\\u597d')
        '你们好'
        >>> slash_u_str_to_str('006100620063')
        'abc'
        >>> slash_u_str_to_str('\\u0061\\u0062\\u0063')
        'abc'
        >>> 
    '''
    rslt = ''
    slash_us = slash_us.replace('\\u','')
    for i in range(0,slash_us.__len__(),4):
        slash_u_str = slash_us[i:i+4]
        rslt = ''.join((rslt,slash_u_str_to_char(slash_u_str)))
    return(rslt)

def char_str_to_unicode_num(char_str):
    '''
        >>> 
        >>> char_str_to_unicode_num('a')
        97
        >>> chr(97)
        'a'
        >>> char_str_to_unicode_num('你')
        20320
        >>> chr(20320)
        '你'
    '''
    s = char_to_slash_u_str(char_str,with_slash_u=0)
    num = int(s,16)
    return(num)
    
def unicode_num_to_char_str(unicode_num):
    '''
        >>> unicode_num_to_char_str(97)
        'a'
        >>> unicode_num_to_char_str(20320)
        '你'
        >>> 
    '''
    h = hex(unicode_num)
    h = h[2:]
    prepend = "0" * (4 - h.__len__())
    h = ''.join((prepend,h))
    ch = slash_u_str_to_char(h)
    return(ch)

def str_to_unicode_num_array(a_string):
    '''
        >>> str_to_unicode_num_array('abc')
        [97, 98, 99]
        >>> str_to_unicode_num_array('你们好')
        [20320, 20204, 22909]
        >>> 
    '''
    rslt = []
    for i in range(0,a_string.__len__()):
        ch = a_string[i]
        num = char_str_to_unicode_num(ch)
        rslt.append(num)
    return(rslt)

def unicode_num_array_to_str(num_arr):
    '''
        >>> unicode_num_array_to_str([97, 98, 99])
        'abc'
        >>> unicode_num_array_to_str([20320, 20204, 22909])
        '你们好'
        >>> 
    '''
    rslt = ''
    for i in range(0,num_arr.__len__()):
        ch = unicode_num_to_char_str(num_arr[i])
        rslt = ''.join((rslt,ch))
    return(rslt)

# bitmap
def bitmaplist_to_num(bitmaplist):
    num = 0
    for i in range(0,bitmaplist.__len__()):
        num = num + 2 **i * bitmaplist[i]
    return(num)

def num_to_bitmaplist(num,bitmap_size):
    bitmaplist = []
    s = bin(num)[2:]
    s_len = s.__len__() 
    for i in range(0,s_len):
        b = s[s_len-i-1]
        bitmaplist.append(int(b))
    for i in range(s_len,bitmap_size):
        bitmaplist.append(0)
    return(bitmaplist)

def bitmaplist_bitsum(bitmaplist):
    sum = 0
    for i in range(0,bitmaplist.__len__()):
        sum = sum + bitmaplist[i]
    return(sum)

def subset_bitmap(n,k):
    rslt = {}
    size = bin(2**n-1).__len__() - 2
    seq = 0 
    for i in range(0,2**n):
        bitmaplist = num_to_bitmaplist(i,size)
        sum = bitmaplist_bitsum(bitmaplist)
        if(sum == k):
            rslt[seq] = bitmaplist
            seq = seq + 1
        else:
            pass
    return(rslt)

def bitmap_contain(bm1,bm2):
    bm3 = list(map(lambda x,y:(x|y),bm1,bm2))
    if(bm3 == bm1):
        return(True)
    else:
        return(False)

