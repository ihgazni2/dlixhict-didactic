#https://github.com/ihgazni2/dlixhict-didactic/blob/master/utils.md
import re
import struct

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


