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
def is_bytes(obj):
    if(type(obj)==type(b'x')):
        return(True)
    else:
        return(False)
def is_int_str(old_index):
    try:
        int(old_index)
    except:
        return(False)
    else:
        if('.' in s):
            return(False)
        else:
            return(True)
def is_float_str(s):
    try:
        float(s)
    except:
        return(False)
    else:
        if('.' in s):
            return(True)
        else:
            return(False)
def is_number_str(s):
    return(is_int_str(s)|is_float_str(s))
def get_obj_type_name(obj):
    class_str = str(type(obj))
    regex = re.compile('\'(.*)\'')
    m = regex.search(class_str)
    return(m.group(1))


#------------------------------------------------------------------#
#path string
#path_string : path_str

#path_string_leaf: path_str_leaf


# head + <the last delimiter> + leaf-tail   
# or 
# head(include the second last delimiter) + non-leaf-tail(include the last delimiter)
#path_string_head:   path_str_head '/a/b/c'.head() = '/a/b/'
#path_string_tail:   path_str_tail '/a/b/c/'.head() = 'c/'

# parent + <the last delimiter> + leaf
#path_string_parent: path_str_parent '/a/b/c'.parent()= '/a/b'
#                                     '/a/b/c/'.parent()='/a/b/c'
 
def path_string_is_slash_end(path_string,delimiter='/'):
    '''
        from xdict.utils import *
        path_string_is_slash_end('a/b/c')
        path_string_is_slash_end('a/b/c/')
        path_string_is_slash_end('a#b#c#',delimiter='#')
    '''
    if(path_string == ''):
        return(False)
    if(path_string[-1] == delimiter):
        return(True)
    else:
        return(False)

def path_string_get_head(path_string,delimiter='/'):
    '''
        from xdict.utils import *
        path_string_get_head('a/b/c')
        path_string_get_head('/a/b/c')
        path_string_get_head('a/b/c/')
        path_string_get_head('/a/b/c/')
    '''
    if(path_string == ''):
        return('')
    path_len = path_string.__len__()
    last_index = path_len - 1
    if(path_string_is_slash_end(path_string,delimiter)):
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

def path_string_get_tail(path_string,delimiter='/'):
    '''
        from xdict.utils import *
        path_string_get_tail('a/b/c')
        path_string_get_tail('/a/b/c')
        path_string_get_tail('a/b/c/')
        path_string_get_tail('/a/b/c/')
    '''
    if(path_string == ''):
        return('')
    path_len = path_string.__len__()
    last_index = path_len - 1
    if(path_string_is_slash_end(path_string,delimiter)):
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

def path_string_to_path_list(path_str,**kwargs):
    '''
        from xdict.utils import *
        path_string_to_path_list('/a/b/c/')
        path_string_to_path_list('#a#b#c#',delimiter = '#')
        path_string_to_path_list('/a/b/c/',keep_begin_sp=0)
        path_string_to_path_list('/a/b/c/',keep_end_sp=0)
        path_string_to_path_list('/a/b/c/',keep_begin_sp=0,keep_end_sp=0)
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('keep_begin_sp' in kwargs):
        keep_begin_sp = kwargs['keep_begin_sp']
    else:
        keep_begin_sp = 1
    if('keep_end_sp' in kwargs):
        keep_end_sp = kwargs['keep_end_sp']
    else:
        keep_end_sp = 1
    if(keep_begin_sp):
        path_str = path_str
    else:
        path_str = str_lstrip(path_str,delimiter,1)
    if(keep_end_sp):
        path_str = path_str
    else:
        path_str = str_rstrip(path_str,delimiter,1)
    sps = path_str.split(delimiter)
    return(sps)

def path_string_is_parent(parent,son,**kwargs):
    ''' 
        from xdict.utils import *
        path_string_is_parent('a/b/','a/b/c')
        path_string_is_parent('a/b/','a/b/c/')
        path_string_is_parent('a/b/','a/b/c/d')
        path_string_is_parent('a/b/','a/b/c/d/')

        path_string_is_parent('/a/b','a/b/c')
        path_string_is_parent('/a/b','a/b/c/')
        path_string_is_parent('/a/b','a/b/c/d')
        path_string_is_parent('/a/b','a/b/c/d/')

        path_string_is_parent('a/b','a/b/c')
        path_string_is_parent('a/b','a/b/')
        path_string_is_parent('a/b','a/b/c/')
        path_string_is_parent('a/b','a/b/c/d')
        path_string_is_parent('a/b','a/b/c/d/')
        
        path_string_is_parent('a/b','/a/b/c')
        path_string_is_parent('a/b','/a/b/c/')
        path_string_is_parent('a/b','/a/b/c/d')
        path_string_is_parent('a/b','/a/b/c/d/')
        
        
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('head_tail_strip' in kwargs):
        head_tail_strip = kwargs['head_tail_strip']
    else:
        head_tail_strip = 0
    if(head_tail_strip):
        parent = str_lstrip(parent,delimiter,1)
        parent = str_rstrip(parent,delimiter,1)
        son = str_lstrip(son,delimiter,1)
        son = str_rstrip(son,delimiter,1)
    else:
       pass
    sks = son.split(delimiter)
    pks = parent.split(delimiter)
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

def path_string_is_son(son,parent,**kwargs):
    ''' 
        from xdict.utils import *
        path_string_is_son('a/b/c','a/b/')
        path_string_is_son('a/b/c/','a/b/')
        path_string_is_son('a/b/c/d','a/b/')
        path_string_is_son('a/b/c/d/','a/b/')

        path_string_is_son('a/b/c','/a/b')
        path_string_is_son('a/b/c/','/a/b')
        path_string_is_son('a/b/c/d','/a/b')
        path_string_is_son('a/b/c/d/','/a/b')

        path_string_is_son('a/b/c','a/b')
        path_string_is_son('a/b/','a/b')
        path_string_is_son('a/b/c/','a/b')
        path_string_is_son('a/b/c/d','a/b')
        path_string_is_son('a/b/c/d/','a/b')
        
        path_string_is_son('/a/b/c','a/b')
        path_string_is_son('/a/b/c/','a/b')
        path_string_is_son('/a/b/c/d','a/b')
        path_string_is_son('/a/b/c/d/','a/b')
        
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('head_tail_strip' in kwargs):
        head_tail_strip = kwargs['head_tail_strip']
    else:
        head_tail_strip = 0
    if(head_tail_strip):
        parent = str_lstrip(parent,delimiter,1)
        parent = str_rstrip(parent,delimiter,1)
        son = str_lstrip(son,delimiter,1)
        son = str_rstrip(son,delimiter,1)
    else:
       pass
    sks = son.split(delimiter)
    pks = parent.split(delimiter)
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

def path_string_is_sibling(sib1,sib2,**kwargs):
    ''' 
        from xdict.utils import *
        path_string_is_sibling('a/b/c','a/b/d')
        path_string_is_sibling('a/b/c','a/b/e')
        path_string_is_sibling('a/b/c','a/b/d/')
        path_string_is_sibling('a/b/c','a/e/d')
        
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('head_tail_strip' in kwargs):
        head_tail_strip = kwargs['head_tail_strip']
    else:
        head_tail_strip = 0
    if(head_tail_strip):
        sib1 = str_lstrip(sib1,delimiter,1)
        sib1 = str_rstrip(sib1,delimiter,1)
        sib2 = str_lstrip(sib2,delimiter,1)
        sib2 = str_rstrip(sib2,delimiter,1)
    else:
       pass
    s1s = sib1.split(delimiter)
    s2s = sib2.split(delimiter)
    if(s1s.__len__() != s2s.__len__()):
        return(0)
    else:
        s1p = s1s[:-1]
        s2p = s2s[:-1]
        if(s1p==s2p):
            return(1)
        else:
            return(0)

def path_string_is_leaf(leaf,path_str,**kwargs):
    ''' 
        from xdict.utils import *
        path_string_is_leaf('c','a/b/c')
        path_string_is_leaf('/c','a/b/c')
        path_string_is_leaf('','a/b/c')
        path_string_is_leaf('c/','a/b/c/')
        path_string_is_leaf('','a/b/c/')
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    pks = path_str.split(delimiter)
    if(pks[-1] == leaf):
        return(1)
    else:
        return(0)

def path_string_is_ancestor(ances,des,**kwargs):
    '''
        from xdict.utils import *
        path_string_is_ancestor('a/b','a/b')
        path_string_is_ancestor('a/b','a/b/')
        path_string_is_ancestor('a/b','a/b/c')
        path_string_is_ancestor('a/b','a/b/c/d')
        path_string_is_ancestor('a/b','a/b/c/d/')
        
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    ances_pl = ances.split(delimiter)
    des_pl = des.split(delimiter)
    return(path_list_is_ancestor(ances_pl,des_pl))

def path_string_is_descedant(des,ances,**kwargs):
    '''
        from xdict.utils import *
        path_string_is_descedant('a/b','a/b')
        path_string_is_descedant('a/b/','a/b')
        path_string_is_descedant('a/b/c','a/b')
        path_string_is_descedant('a/b/c/d','a/b')
        path_string_is_descedant('a/b/c/d/','a/b')
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    ances_pl = ances.split(delimiter)
    des_pl = des.split(delimiter)
    return(path_list_is_descedant(des_pl,ances_pl))

def path_string_get_parent(son,**kwargs):
    ''' 
        from xdict.utils import *
        path_string_get_parent('a/b/c')
        path_string_get_parent('a/b/c/')
        path_string_get_parent('/a/b/c')
        path_string_get_parent('/a/b/c/')
        path_string_get_parent('c')
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if(not(delimiter in son)):
        son = delimiter
    else:
        pass
    regex_str = ''.join(('(.*)',delimiter,'(.*?)'))
    regex = re.compile(regex_str)
    m = regex.search(son)
    return(m.group(1))

def path_string_get_leaf(absp,**kwargs):
    ''' 
        from xdict.utils import *
        path_string_get_leaf('a/b/c')
        path_string_get_leaf('a/b/c/')
        path_string_get_leaf('/a/b/c')
        path_string_get_leaf('/a/b/c/')
        path_string_get_leaf('c')
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if(not(delimiter in absp)):
        return(absp)
    else:
        pass
    regex_str = ''.join(('(.*)',delimiter,'([^/]*)'))
    if(absp == ''):
        absp = delimiter
    if(not(delimiter in absp)):
        absp = delimiter
    else:
        pass
    regex = re.compile(regex_str)
    m = regex.search(absp)
    return(m.group(2))

def path_string_get_ancestors(des,**kwargs):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        ancestors = path_string_get_ancestors('a/b/c/d')
        pobj(ancestors)
        ancestors = path_string_get_ancestors('/a/b/c/d')
        pobj(ancestors)
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    des_pl = des.split(delimiter)
    rslt = []
    
    for ei in range(0,des_pl.__len__()-1):
        ances_pl = copy.deepcopy(des_pl[:(ei+1)])
        ances = path_list_to_path_string(ances_pl,delimiter = delimiter)
        rslt.append(ances)
    return(rslt)


class pathstr(str):
    '''
        from xdict import utils
        from xdict.jprint import pobj
        ps = utils.pathstr('/a/b/c')
        ps.head()
        ps.tail()
        ps.leaf()
        ps.parent()
        ps.ancestors()
        
        ps = utils.pathstr('/a/b/c')
        ps.is_parent_of('/a/b/c/d')
        ps = utils.pathstr('d')
        ps.is_leaf_of('/a/b/c/d')
        ps = utils.pathstr('/a/b/c/d')
        ps.is_son_of('/a/b/c')
        ps = utils.pathstr('a/b/c')
        ps.is_sibling_of('/a/b/d')
        
        ps.pathlist()
        
        ps = utils.pathstr('a/b')
        ps.is_ancestor_of('a/b/c')
        ps.is_ancestor_of('a/b/c/')
        ps.is_ancestor_of('a/b/c/d')
        ps.is_ancestor_of('a/b/c/d/')
        
        ps = utils.pathstr('a/b/c/d')
        ps.is_descedant_of('a/b/c')
        ps.is_descedant_of('a/b/c/')
        ps.is_descedant_of('a/b')
        ps.is_descedant_of('a/b/')
        ps.is_descedant_of('a')
        ps.is_descedant_of('a/')
        ps.is_descedant_of('')
        ps.is_descedant_of('/')
    '''
    def head(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_get_head(self,delimiter=delimiter))
    def tail(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_get_tail(self,delimiter=delimiter))
    def leaf(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_get_leaf(self,delimiter=delimiter))
    def parent(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_get_parent(self,delimiter=delimiter))
    def ancestors(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_get_ancestors(self,delimiter=delimiter))
    def pathlist(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        if('keep_begin_sp' in kwargs):
            keep_begin_sp = kwargs['keep_begin_sp']
        else:
            keep_begin_sp = 1
        if('keep_begin_sp' in kwargs):
            keep_end_sp = kwargs['keep_end_sp']
        else:
            keep_end_sp = 1
        return(path_string_to_path_list(self,delimiter=delimiter,keep_begin_sp=keep_begin_sp,keep_end_sp=keep_end_sp))
    def is_parent_of(self,pathstr_2,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_is_parent(self,pathstr_2,delimiter=delimiter))
    def is_son_of(self,pathstr_2,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_is_son(self,pathstr_2,delimiter=delimiter))
    def is_sibling_of(self,pathstr_2,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_is_sibling(self,pathstr_2,delimiter=delimiter))
    def is_leaf_of(self,pathstr_2,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_is_leaf(self,pathstr_2,delimiter=delimiter))
    def is_ancestor_of(self,pathstr_2,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_is_ancestor(self,pathstr_2,delimiter=delimiter))
    def is_descedant_of(self,pathstr_2,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_string_is_descedant(self,pathstr_2,delimiter=delimiter))


def path_list_get_head(path_list):
    '''
        from xdict.utils import *
        path_list_get_head(['a','b','c'])
        path_list_get_head(['','a','b','c'])
        path_list_get_head(['a','b','c',''])
        path_list_get_head(['','a','b','c',''])
    '''
    path_str = path_list_to_path_string(path_list)
    head = path_string_get_head(path_str)
    return(path_string_to_path_list(head))

def path_list_get_tail(path_list):
    '''
        from xdict.utils import *
        path_list_get_tail(['a','b','c'])
        path_list_get_tail(['','a','b','c'])
        path_list_get_tail(['a','b','c',''])
        path_list_get_tail(['','a','b','c',''])
    '''
    path_str = path_list_to_path_string(path_list)
    tail = path_string_get_tail(path_str)
    return(path_string_to_path_list(tail))

def path_list_get_parent(pathlist):
    ''' 
        from xdict.utils import *
        path_list_get_parent(['a','b','c'])
        path_list_get_parent(['a','b','c',''])
        path_list_get_parent(['a','b','c'])
        path_list_get_parent(['','a','b','c',''])
        path_list_get_parent(['c'])
    '''
    pl = copy.deepcopy(pathlist)
    return(pl[:-1])


def path_list_get_ancestors(des_pl,**kwargs):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        ancestors = path_list_get_ancestors(['a','b','c','d'])
        pobj(ancestors,fixed_indent=1)
        ancestors = path_list_get_ancestors(['a','b','c','d'])
        pobj(ancestors,fixed_indent=1)
    '''
    rslt = []
    for ei in range(0,des_pl.__len__()-1):
        ances_pl = copy.deepcopy(des_pl[:(ei+1)])
        rslt.append(ances_pl)
    return(rslt)


def path_list_to_path_string(path_list,**kwargs):
    '''
        from xdict.utils import *
        path_list_to_path_string(['a','b','c',''])
        path_list_to_path_string(['a','b','c',''],delimiter = '#')
        path_list_to_path_string(['','a','b','c',''],keep_begin_sp=0)
        path_list_to_path_string(['','a','b','c',''],keep_end_sp=0)
        path_list_to_path_string(['','a','b','c',''],keep_begin_sp=0,keep_end_sp=0)
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('keep_begin_sp' in kwargs):
        keep_begin_sp = kwargs['keep_begin_sp']
    else:
        keep_begin_sp = 1
    if('keep_end_sp' in kwargs):
        keep_end_sp = kwargs['keep_end_sp']
    else:
        keep_end_sp = 1
    if(keep_begin_sp):
        path_list = path_list
    else:
        path_list = copy.deepcopy(path_list[1:])
    if(keep_end_sp):
        path_list = path_list
    else:
        path_list = copy.deepcopy(path_list[:path_list.__len__()-1])
    
    path_str = ''.join((path_list[0],delimiter))
    for i in range(1,path_list.__len__()):
        path_str=''.join((path_str,str(path_list[i]),delimiter))
    path_str = str_rstrip(path_str,delimiter,1)
    return(path_str)

def path_list_is_parent(parent_pl,son_pl):
    ''' 
        from xdict.utils import *
        path_list_is_parent(['a','b',''],['a','b','c'])
        path_list_is_parent(['a','b',''],['a','b','c',''])
        path_list_is_parent(['a','b',''],['a','b','c','d'])
        path_list_is_parent(['a','b',''],['a','b','c','d',''])

        path_list_is_parent(['','a','b'],['a','b','c'])
        path_list_is_parent(['','a','b'],['a','b','c',''])
        path_list_is_parent(['','a','b'],['a','b','c','d'])
        path_list_is_parent(['','a','b'],['a','b','c','d',''])

        path_list_is_parent(['a','b'],['a','b','c'])
        path_list_is_parent(['a','b'],['a','b',''])
        path_list_is_parent(['a','b'],['a','b','c',''])
        path_list_is_parent(['a','b'],['a','b','c','d'])
        path_list_is_parent(['a','b'],['a','b','c','d',''])

        path_list_is_parent(['a','b'],['a','b','c'])
        path_list_is_parent(['a','b'],['a','b','c',''])
        path_list_is_parent(['a','b'],['a','b','c','d'])
        path_list_is_parent(['a','b'],['a','b','c','d',''])
    '''
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

def path_list_is_son(son_pl,parent_pl):
    ''' 
        from xdict.utils import *
        path_list_is_son(['a','b','c'],['a','b',''])
        path_list_is_son(['a','b','c',''],['a','b',''])
        path_list_is_son(['a','b','c','d'],['a','b',''])
        path_list_is_son(['a','b','c','d',''],['a','b',''])

        path_list_is_son(['a','b','c'],['','a','b'])
        path_list_is_son(['a','b','c',''],['','a','b'])
        path_list_is_son(['a','b','c','d'],['','a','b'])
        path_list_is_son(['a','b','c','d',''],['','a','b'])

        path_list_is_son(['a','b','c'],['a','b'])
        path_list_is_son(['a','b',''],['a','b'])
        path_list_is_son(['a','b','c',''],['a','b'])
        path_list_is_son(['a','b','c','d'],['a','b'])
        path_list_is_son(['a','b','c','d',''],['a','b'])

        path_list_is_son(['a','b','c'],['a','b'])
        path_list_is_son(['a','b','c',''],['a','b'])
        path_list_is_son(['a','b','c','d'],['a','b'])
        path_list_is_son(['a','b','c','d',''],['a','b'])
    '''
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

# ------------------------------------------------
def path_list_is_sibling(sib1,sib2,**kwargs):
    ''' 
        from xdict.utils import *
        path_list_is_sibling(['a','b','c'],['a','b','d'])
        path_list_is_sibling(['a','b','c'],['a','b','e'])
        path_list_is_sibling(['a','b','c'],['a','b','d',''])
        path_list_is_sibling(['a','b','c'],['a','e','d'])
        
    '''
    s1s = sib1
    s2s = sib2
    if(s1s.__len__() != s2s.__len__()):
        return(0)
    else:
        s1p = s1s[:-1]
        s2p = s2s[:-1]
        if(s1p==s2p):
            return(1)
        else:
            return(0)


def path_list_is_leaf(leaf,pathlist,**kwargs):
    ''' 
        from xdict.utils import *
        path_list_is_leaf(['c'],['a','b','c'])
        path_list_is_leaf(['','c'],['a','b','c'])
        path_list_is_leaf([''],['a','b','c'])
        path_list_is_leaf(['c',''],['a','b','c',''])
        path_list_is_leaf([''],['a','b','c',''])
    '''
    pks = pathlist
    if(pks[-1] == leaf[0]):
        return(1)
    else:
        return(0)

def path_list_is_ancestor(ances_pl,des_pl):
    '''
        from xdict.utils import *
        path_list_is_ancestor(['a','b'],['a','b'])
        path_list_is_ancestor(['a','b'],['a','b',''])
        path_list_is_ancestor(['a','b'],['a','b','c'])
        path_list_is_ancestor(['a','b'],['a','b','c','d'])
        path_list_is_ancestor(['a','b'],['a','b','c','d',''])
    '''
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

def path_list_is_descedant(des_pl,ances_pl):
    '''
        from xdict.utils import *
        path_list_is_descedant(['a','b'],['a','b'])
        path_list_is_descedant(['a','b',''],['a','b'])
        path_list_is_descedant(['a','b','c'],['a','b'])
        path_list_is_descedant(['a','b','c','d'],['a','b'])
        path_list_is_descedant(['a','b','c','d',''],['a','b'])
    '''
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

def path_list_to_getitem_string(path_list):
    '''
        >>> path_list_to_getitem_string([1, '1', 2])
            "[1]['1'][2]"
        >>> 
    '''
    t1 = path_list.__repr__()
    t1 = t1.lstrip('[')
    t1 = t1.rstrip(']')
    t2 = t1.split(", ")
    s = ''
    for i in range(0,t2.__len__()):
        s = ''.join((s,'[',t2[i],']'))
    return(s)

class pathlist(list):
    '''
        from xdict import utils
        pl = utils.pathlist(['','a','b','c'])
        pl.head()
        pl.tail()
        pl.leaf()
        pl.parent()
        pl.ancestors()
        pobj(pl.ancestors(),fixed_indent=1)
    
        pl.pathstr()
    
        pl = utils.pathlist(['a','b','c'])
        pl.is_parent_of(['a','b','c','d'])
        pl = utils.pathlist(['d'])
        pl.is_leaf_of(['a','b','c','d'])
        pl = utils.pathlist(['a','b','c','d'])
        pl.is_son_of(['a','b','c'])
        pl = utils.pathlist(['a','b','c'])
        pl.is_sibling_of(['a','b','d'])
    
        pl = utils.pathlist(['a','b'])
        pl.is_ancestor_of(['a','b','c'])
        pl.is_ancestor_of(['a','b','c',''])
        pl.is_ancestor_of(['a','b','c','d'])
        pl.is_ancestor_of(['a','b','c','d',''])
    
        pl = utils.pathlist(['a','b','c','d'])
        pl.is_descedant_of(['a','b','c'])
        pl.is_descedant_of(['a','b','c',''])
        pl.is_descedant_of(['a','b'])
        pl.is_descedant_of(['a','b',''])
        pl.is_descedant_of(['a'])
        pl.is_descedant_of(['a',''])
        pl.is_descedant_of([''])
        pl.is_descedant_of(['',''])
    '''
    def head(self):
        pl = copy.deepcopy(self)
        return(path_list_get_head(self))
    def tail(self):
        return(path_list_get_tail(self))
    def leaf(self):
        return([self[-1]])
    def parent(self):
        p = copy.deepcopy(self)
        p.pop(-1)
        return(p)
    def ancestors(self):
        return(path_list_get_ancestors(self))
    def pathstr(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(path_list_to_path_string(self,delimiter=delimiter))
    def is_parent_of(self,pl2):
        return(path_list_is_parent(self,pl2))
    def is_son_of(self,pl2):
        return(path_list_is_son(self,pl2))
    def is_sibling_of(self,pl2):
        return(path_list_is_sibling(self,pl2))
    def is_leaf_of(self,pl2):
        return(path_list_is_leaf(self,pl2))
    def is_ancestor_of(self,pl2):
        return(path_list_is_ancestor(self,pl2))
    def is_descedant_of(self,pl2):
        return(path_list_is_ancestor(self,pl2))
    def getitem_string(self):
        return(path_list_to_getitem_string(self))


#string

def str_to_bool(s,**kwargs):
    '''
        from xdict.utils import *
        str_to_bool('False')
        str_to_bool('false')
        str_to_bool('True')
        str_to_bool('true')
    '''
    if('strict' in kwargs):
        strict = kwargs['strict']
    else:
        strict = 0
    if(strict):
        if(s == 'False'):
            return(False)
        elif(s == 'True'):
            return(True)
        else:
            return(None)
    else:
        if((s == 'False') | (s == 'false')):
            return(False)
        elif((s == 'True') | (s == 'true')):
            return(True)
        else:
            return(None)


def str_lstrip(s,char,count):
    '''
        from xdict.utils import *
        str_lstrip('sssa','s',0)
        str_lstrip('sssa','s',1)
        str_lstrip('sssa','s',2)
        str_lstrip('sssa','s',3)
        str_lstrip('sssa','s',4)
    '''
    c = 0
    for i in range(0,s.__len__()):
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
        return(s[c:])

def str_rstrip(s,char,count):
    '''
        from xdict.utils import *
        str_rstrip('asss','s',0)
        str_rstrip('asss','s',1)
        str_rstrip('asss','s',2)
        str_rstrip('asss','s',3)
        str_rstrip('asss','s',4)
    '''
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
        ei = s.__len__() - c
        return(s[:ei])

def str_prepend(s,char,n):
    '''
        from xdict.utils import *
        str_prepend('a','s',3)
    '''
    prepend = ''
    for i in range(1,n+1):
        prepend = ''.join((prepend,char))
    return(''.join((prepend,s)))

def str_append(s,char,n):
    '''
        from xdict.utils import *
        str_append('a','s',3)
    '''
    append = ''
    for i in range(1,n+1):
        append = ''.join((append,char))
    return(''.join((s,append)))

def str_at_begin_of_str(str1,str2):
    '''
        from xdict.utils import *
        str_at_begin_of_str('abc','abcd')
    '''
    len1 = str1.__len__()
    begin = str2[:len1]
    if(str1 == begin):
        return(True)
    else:
        return(False)

def str_at_end_of_str(str1,str2):
    '''
        from xdict.utils import *
        str_at_end_of_str('abcd','bcd')
    '''
    len1 = str1.__len__()
    len2 = str2.__len__()
    end = str2[(len2-len1):]
    if(str1 == end):
        return(True)
    else:
        return(False)

def str_display_width(s):
    '''
        from xdict.utils import *
        str_display_width('a')
        str_display_width('去')
    '''
    s= str(s)
    width = 0
    len = s.__len__()
    for i in range(0,len):
        sublen = s[i].encode().__len__()
        sublen = int(sublen/2 + 1/2)
        width = width + sublen
    return(width)

def str_prepend_basedon_displaywidth(s,width,**kwargs):
    '''
        from xdict.utils import *
        str_prepend_basedon_displaywidth('a',4,padding='x')
        str_prepend_basedon_displaywidth('去',4,padding='x')
    '''
    if('padding' in kwargs):
        padding = kwargs['padding']
    else:
        padding = ' '
    s = str(s)
    w = str_display_width(s)
    space_Len = width - w
    new_S = ''
    for i in range(0,space_Len):
        new_S = ''.join((padding, new_S))
    new_S = ''.join((new_S,s))
    return(new_S)

def str_append_basedon_displaywidth(s,width,**kwargs):
    '''
        from xdict.utils import *
        str_append_basedon_displaywidth('a',4,padding='x')
        str_append_basedon_displaywidth('去',4,padding='x')
    '''
    if('padding' in kwargs):
        padding = kwargs['padding']
    else:
        padding = ' '
    s = str(s)
    w = str_display_width(s)
    space_Len = width - w
    new_S = padding * space_Len
    new_S = ''.join((new_S,s))
    return(new_S)




# char encode decode

def pack_char_using_unicode(char_str):
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
        >>> pack_char_using_unicode('a')
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
        >>> pack_char_using_unicode('问')
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

def unpack_twobytes_using_unicode(two_bytes):
    '''
        >>> unpack_twobytes_using_unicode(b'\x00a')
        'a'
        >>> unpack_twobytes_using_unicode(b'\x95\xee')
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

def pack_str_using_unicode(str):
    '''
        >>> pack_str_using_unicode('abcdefg')
        b'\x00a\x00b\x00c\x00d\x00e\x00f\x00g'
        >>> 
        >>> pack_str_using_unicode('你们好')
        b'O`N\xecY}'
        >>> 
    '''
    len = str.__len__()
    B = b''
    for i in range(0,len):
        B = B + pack_char_using_unicode(str[i])
    return(B)

def unpack_bytes_stream_using_unicode(Bs):
    '''
        >>> unpack_bytes_stream_using_unicode(b'\x00a\x00b\x00c\x00d\x00e\x00f\x00g')
        'abcdefg'
        >>> unpack_bytes_stream_using_unicode(b'O`N\xecY}')
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
    return(unpack_twobytes_using_unicode(bs)) 

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

class estr(str):
    '''
        from xdict.utils import *
        es = estr('true')
        es.boolize()
        es = estr('sssa')
        es.elstrip('s',2)
        es = estr('asss')
        es.erstrip('s',2)
        es = estr('ssass')
        es.estrip('s',2)
        es = estr('abc')
        es.prepend('x',2)
        es.append('x',2)
        es = estr('abc')
        es.at_begin('abcd')
        es = estr('bcd')
        es.at_end('abcd')
        es = estr('我我我')
        es.display_width()
        
        es = estr('我')
        es.prepend_basedon_displaywidth(4,padding='a')
        es = estr('我')
        es.append_basedon_displaywidth(4,padding='a')
        es = estr('abcdefg')
        es.pack()
        es = estr('你们好')
        es.pack()
        es = estr('你们好')
        es.unicode()
        es.unicode(with_slash_u=0)
        es = estr('abc')
        es.unicode()
        es.unicode(with_slash_u=0)
        es = estr('你们好')
        es.unicode_num_array()
        es = estr('abc')
        es.unicode_num_array()
    '''
    def boolize(self,**kwargs):
        if('strict' in kwargs):
            strict = kwargs['strict']
        else:
            strict = 0
        return(str_to_bool(self,strict=strict))
    def elstrip(self,char,count):
        return(str_lstrip(self,char,count))
    def erstrip(self,char,count):
        return(str_rstrip(self,char,count))
    def estrip(self,char,count):
        s = str_lstrip(self,char,count)
        return(str_rstrip(s,char,count))
    def prepend(self,char,count):
        return(str_prepend(self,char,count))
    def append(self,char,count):
        return(str_append(self,char,count))
    def at_begin(self,str2):
        return(str_at_begin_of_str(self,str2))
    def at_end(self,str2):
        return(str_at_end_of_str(self,str2))
    def display_width(self):
        return(str_display_width(self))
    def prepend_basedon_displaywidth(self,width,**kwargs):
        if('padding' in kwargs):
            padding = kwargs['padding']
        else:
            padding = ' '
        return(str_prepend_basedon_displaywidth(self,width,padding=padding))
    def append_basedon_displaywidth(self,width,**kwargs):
        if('padding' in kwargs):
            padding = kwargs['padding']
        else:
            padding = ' '
        return(str_append_basedon_displaywidth(self,width,padding=padding))
    def pack(self):
        return(pack_str_using_unicode(self))
    def unicode(self,**kwargs):
        if('with_slash_u' in kwargs):
            with_slash_u = kwargs['with_slash_u']
        else:
            with_slash_u = 1
        return(str_to_slash_u_str(self,with_slash_u=with_slash_u))
    def unicode_num_array(self):
        return(str_to_unicode_num_array(self))

        
class eunicode():
    '''
        from xdict.utils import *
        eu = eunicode([97, 98, 99])
        eu.str
        eu.bytes
        eu.nums
        eu.unicode
        
        eu = eunicode('abc')
        eu.str
        eu.bytes
        eu.nums
        eu.unicode
        
        eu = eunicode(b'\x00a\x00b\x00c')
        eu.str
        eu.bytes
        eu.nums
        eu.unicode
        
        eu = eunicode([20320, 20204, 22909])
        eu.str
        eu.bytes
        eu.nums
        eu.unicode
        
        eu = eunicode('你们好')
        eu.str
        eu.bytes
        eu.nums
        eu.unicode
        
        eu = eunicode(b'O`N\xecY}')
        eu.str
        eu.bytes
        eu.nums
        eu.unicode
    '''
    def __init__(self,u,**kwargs):
        if('with_slash_u' in kwargs):
            with_slash_u = kwargs['with_slash_u']
        else:
            with_slash_u = 1
        if(is_list(u)):
            self.nums = u
            self.str = unicode_num_array_to_str(self.nums)
            self.unicode = str_to_slash_u_str(self.str,with_slash_u=with_slash_u)
            self.bytes = pack_str_using_unicode(self.str)
        elif(is_bytes(u)):
            self.bytes = u
            self.str = unpack_bytes_stream_using_unicode(self.bytes)
            self.unicode = str_to_slash_u_str(self.str,with_slash_u=with_slash_u)
            self.nums = str_to_unicode_num_array(self.str)
        else:
            self.str = u
            self.unicode = str_to_slash_u_str(self.str,with_slash_u=with_slash_u)
            self.nums = str_to_unicode_num_array(self.str)
            self.bytes = pack_str_using_unicode(self.str)




#dict

def dict_setdefault_via_path_list(external_dict,path_list,**kwargs):
    '''
        #if path_list already in external_dict, will do nothing
        y = {}
        path_list = ['c','b']
        dict_setdefault_via_path_list(y,path_list)
    
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('default_element' in kwargs):
        default_element = kwargs['default_element']
    else:
        default_element = {}
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
                # necessary ,when default_element = {} or []
                de = copy.deepcopy(default_element)
                this.__setitem__(key,de)
            except:
                return(external_dict)
            else:
                pass
            this = this.__getitem__(key)
        else:
            this = this.__getitem__(key)
    return(external_dict)

def dict_setitem_via_path_list(external_dict,path_list,value,**kwargs):
    '''
        y = {'c': {'b': {}}}
        dict_setitem_via_path_list(y,['c','b'],200)
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
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

def dict_getitem_via_path_list(external_dict,path_list,**kwargs):
    '''
        y = {'c': {'b': 200}}
        dict_getitem_via_path_list(y,['c','b'])
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
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

def dict_getitem_via_cmd(external_dict,cmd_str,**kwargs):
    '''
        y = {'c': {'b': 200}}
        dict_getitem_via_cmd(y,'c b')
    '''
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    regex_str = ''.join(('[',cmd_sp,']','+'))
    regex = re.compile(regex_str)
    cmd_str = re.sub(regex,cmd_sp,cmd_str)
    cmd_str = str_rstrip(cmd_str,cmd_sp,1)
    cmd_str = str_lstrip(cmd_str,cmd_sp,1)  
    path_list = cmd_str.split(cmd_sp)
    return(dict_getitem_via_path_list(external_dict,path_list,n2s=n2s,s2n=s2n))

def dict_getitem_via_pathstr(d,full_key_path,**kwargs):
    '''
        y = {'c': {'b': 200}}
        dict_getitem_via_pathstr(y,'c/b')
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('strip_head_sp' in kwargs):
        strip_head_sp = kwargs['strip_head_sp']
    else:
        strip_head_sp = 0
    if('strip_tail_sp' in kwargs):
        strip_tail_sp = kwargs['strip_tail_sp']
    else:
        strip_tail_sp = 0
    if(strip_head_sp):
        full_key_path = str_lstrip(full_key_path,delimiter,1)
    else:
        pass
    if(strip_tail_sp):
        full_key_path = str_rstrip(full_key_path,delimiter,1)
    else:
        pass
    if(full_key_path == ''):
        return(d)
    keys = full_key_path.split(delimiter)
    now = d
    klen = keys.__len__()
    for i in range(0,klen):
        try:
            now = now.__getitem__(keys[i])
        except Exception as err:
            now = now.__getitem__(int(keys[i]))
    return(now)

def dict_delitem_via_path_list(external_dict,path_list,**kwargs):
    '''
        y = {'c': {'b': 200}}
        dict_delitem_via_path_list(y,['c','b'])
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
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
    this.__delitem__(path_list[-1])
    return(external_dict)

def dict_delitem_via_pathstr(external_dict,pathstr,**kwargs):
    '''
        y = {'c': {'b': 200}}
        dict_delitem_via_pathstr(y,'c/b')
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('strip_head_sp' in kwargs):
        strip_head_sp = kwargs['strip_head_sp']
    else:
        strip_head_sp = 0
    if('strip_tail_sp' in kwargs):
        strip_tail_sp = kwargs['strip_tail_sp']
    else:
        strip_tail_sp = 0
    if(strip_head_sp):
        pathstr = str_lstrip(pathstr,delimiter,1)
    else:
        pass
    if(strip_tail_sp):
        pathstr = str_rstrip(pathstr,delimiter,1)
    else:
        pass
    pathlist = pathstr.split(delimiter)
    return(dict_delitem_via_path_list(external_dict,pathlist,s2n=s2n,n2s=n2s,strip_head_sp=strip_head_sp,strip_tail_sp=strip_tail_sp))

def dict_delitem_via_cmd(external_dict,cmd_str,**kwargs):
    '''
        from xdict.utils import *
        y = {'c': {'b': 200}}
        dict_delitem_via_cmd(y,'c b')
    '''
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('strip_head_sp' in kwargs):
        strip_head_sp = kwargs['strip_head_sp']
    else:
        strip_head_sp = 0
    if('strip_tail_sp' in kwargs):
        strip_tail_sp = kwargs['strip_tail_sp']
    else:
        strip_tail_sp = 0
    if(strip_head_sp):
        pathstr = str_lstrip(pathstr,delimiter,1)
    else:
        pass
    if(strip_tail_sp):
        pathstr = str_rstrip(pathstr,delimiter,1)
    else:
        pass
    regex_str = ''.join(('[',cmd_sp,']','+'))
    regex = re.compile(regex_str)
    cmd_str = re.sub(regex,cmd_sp,cmd_str)
    cmd_str = str_rstrip(cmd_str,cmd_sp,1)
    cmd_str = str_lstrip(cmd_str,cmd_sp,1)
    pathlist = cmd_str.split(cmd_sp)
    return(dict_delitem_via_path_list(external_dict,pathlist,s2n=s2n,n2s=n2s,strip_head_sp=strip_head_sp,strip_tail_sp=strip_tail_sp))

def dict_get_all_sons_pathstrs(d,full_key_path,**kwargs):
    '''
        dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'')
        dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'2')
        dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'2/x')
    ''' 
    
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('strip_head_sp' in kwargs):
        strip_head_sp = kwargs['strip_head_sp']
    else:
        strip_head_sp = 0
    if('strip_tail_sp' in kwargs):
        strip_tail_sp = kwargs['strip_tail_sp']
    else:
        strip_tail_sp = 0
    if('keep_indicator' in kwargs):
        keep_indicator = kwargs['keep_indicator']
    else:
        keep_indicator = 0
    if(strip_head_sp):
        full_key_path = str_lstrip(full_key_path,delimiter,1)
    else:
        pass
    if(strip_tail_sp):
        full_key_path = str_rstrip(full_key_path,delimiter,1)
    else:
        pass
    if(full_key_path  == delimiter):
        full_key_path = ''
    else:
        pass
    all_sons_full_key_path_list = []
    value = dict_getitem_via_pathstr(d,full_key_path,strip_head_sp=strip_head_sp,strip_tail_sp=strip_tail_sp)
    value_type = type(value)
    if(value_type == type([])):
        v_len = value.__len__()
        for i in range(0,v_len):
            kp = ''.join((full_key_path,delimiter,str(i)))
            if(is_dict(value[i])|is_list(value[i])|is_tuple(value[i])|is_set(value[i])):
                kp = ''.join((kp,delimiter))
            else:
                pass
            if(full_key_path == ''):
                pass
            else:
                kp = ''.join((delimiter,kp))
            if(keep_indicator):
                pass
            else:
                kp = str_lstrip(kp,delimiter,1)
                kp = str_rstrip(kp,delimiter,1)
            all_sons_full_key_path_list.append(kp)
    elif(value_type == type({})):
        v_len = value.__len__()
        for each in value:
            kp = ''.join((full_key_path,delimiter,str(each)))
            if(is_dict(value[each])|is_list(value[each])|is_tuple(value[each])|is_set(value[each])):
                kp = ''.join((kp,delimiter))
            else:
                pass
            if(full_key_path == ''):
                pass
            else:
                kp = ''.join((delimiter,kp))
            if(keep_indicator):
                pass
            else:
                kp = str_lstrip(kp,delimiter,1)
                kp = str_rstrip(kp,delimiter,1)
            all_sons_full_key_path_list.append(kp)
    else:
        pass
    return(all_sons_full_key_path_list)

def dict_include_pathlist(external_dict,path_list,**kwargs):
    '''
        y = {
            'a':
                {'x':88},
            'b':
                {
                    'x':
                        {'c':66}
                }
        }
        dict_include_pathlist(y,['a'])
        dict_include_pathlist(y,['a','x'])
        dict_include_pathlist(y,['b','x','c'])
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
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


def dict_find_keys_via_value(dlts,v,**kwargs):
    '''
        from xdict.utils import *
        dlts = {1:'a',2:{3:'a'}}
        dict_find_keys_via_value(dlts,'a')
        dict_find_keys_via_value(dlts,'a')
    '''
    rslt = []
    unhandled = [dlts]
    parents   = [[]]
    while(unhandled.__len__()>0):
        next_unhandled = []
        next_parents = []
        for i in range(0,unhandled.__len__()):
            curr = unhandled[i]
            p = parents[i]
            if(is_dict(curr)):
                if(curr == v):
                    rslt.append(p)
                for key in curr:
                    np = copy.deepcopy(p)
                    np.append(key)
                    next_parents.append(np)
                    next_unhandled.append(curr[key])
            elif(is_list(curr)):
                if(curr == v):
                    rslt.append(p)
                for key in range(0,curr.__len__()):
                    np = copy.deepcopy(p)
                    np.append(key)
                    next_parents.append(np)
                    next_unhandled.append(curr[key])
            else:
                if(curr == v):
                    rslt.append(p)
        unhandled = next_unhandled
        parents = next_parents
    return(rslt)

def dict_non_recursive_find_keys_via_value(d,v):
    '''
        from xdict.utils import *
        dlts = {1:'a',2:{3:'a'}}
        dict_non_recursive_find_keys_via_value(dlts,'a')
    '''
    rslt = []
    for key in d:
        if(d[key] == v):
            rslt.append(key)
    return(rslt)

def dict_get_pathstr_hierachy_description(dora,**kwargs):
    '''
        could be used to handle dict/list embeded hierachy structure
        the  more complicated structure such as with mixed tuple/set/dict/list
        please use hdict module functions
        
        from xdict.utils import *
        from xdict.jprint import pobj
        currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
        pobj(currd)
        desc_dict = dict_get_pathstr_hierachy_description(currd)
        pobj(desc_dict)
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    if('strip_head_sp' in kwargs):
        strip_head_sp = kwargs['strip_head_sp']
    else:
        strip_head_sp = 0
    if('strip_tail_sp' in kwargs):
        strip_tail_sp = kwargs['strip_tail_sp']
    else:
        strip_tail_sp = 0
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
            value = dict_getitem_via_pathstr(dora,unhandled_now[i],strip_head_sp=strip_head_sp,strip_tail_sp=strip_tail_sp)
            value_type = type(value)
            desc_layer_dict_len = desc_layer_dict.__len__()
            desc_layer_dict[desc_layer_dict_len] = unhandled_now[i]
            if( value_type == type([])):
                all_sons_fkp_list = dict_get_all_sons_pathstrs(dora,unhandled_now[i],delimiter=delimiter)
                llen = all_sons_fkp_list.__len__()
                for i in range(0,llen):
                    unhandled_next_len = unhandled_next.__len__()
                    unhandled_next[unhandled_next_len] = all_sons_fkp_list[i]
                temp = temp | 1
            elif(value_type == type({})):
                all_sons_fkp_list = dict_get_all_sons_pathstrs(dora,unhandled_now[i],delimiter=delimiter)
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


def dict_get_partent_pathstr_hierachy_description_from_description_dict(description_dict):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
        pobj(currd)
        phd = dict_get_pathstr_hierachy_description(currd)
        pphd = dict_get_partent_pathstr_hierachy_description_from_description_dict(phd)
        pobj(pphd)
    '''
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
                    if(path_string_is_parent(description_dict[i][j],description_dict[i+1][k],head_tail_strip=1)):
                        parent_dict[i+1][k] = j
                        next_level_cursor = next_level_cursor + 1
                    else:
                        break
    if(1 in parent_dict):
        for seq in description_dict[1]:
            parent_dict[1][seq] = [0][0]
    else:
        pass
    return(parent_dict)

def dict_get_tree_pathstr_hierachy_description(currd,**kwargs):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
        hierachy_desc = dict_get_tree_pathstr_hierachy_description(currd)
        hierachy_desc.keys()
        print(hierachy_desc['text'])
        pobj(hierachy_desc['parent_dict'])
        pobj(hierachy_desc['description_dict'])
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    description_dict = dict_get_pathstr_hierachy_description(currd,delimiter=delimiter)
    parent_dict = dict_get_partent_pathstr_hierachy_description_from_description_dict(description_dict)
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
            if(dict_get_all_sons_pathstrs(currd,full_key_path) == []):
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
            if(dict_get_all_sons_pathstrs(currd,full_key_path) == []):
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
    rslt['description_dict'] = description_dict
    return(rslt)


def dict_update_just_intersection(dict1,dict2):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        dict1 = {1:'a',2:'b',3:'c',4:'d'}
        dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        dict_update_just_intersection(dict1,dict2)
        pobj(dict1)
        pobj(dict2)
    '''
    for key in dict2:
        if(key in dict1):
            dict1[key] = dict2[key]
    return(dict1)



def dict_uniqualize(d):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        dict1 = {1:'a',2:'b',3:'c',4:'b'}
        dict_uniqualize(dict1)
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
    
    

def dict_extend(dict1,dict2,**kwargs):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        dict1 = {1:'a',2:'b',3:'c',4:'d'}
        dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        dict_extend(dict1,dict2)
        pobj(dict1)
        pobj(dict2)
        dict1 = {1:'a',2:'b',3:'c',4:'d'}
        dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        dict_extend(dict1,dict2,overwrite=1)
        pobj(dict1)
        pobj(dict2)
    '''
    if('deepcopy' in kwargs):
        deepcopy=kwargs['deepcopy']
    else:
        deepcopy=1
    if('overwrite' in kwargs):
        overwrite=kwargs['overwrite']
    else:
        overwrite=0
    if(deepcopy):
        dict1 = copy.deepcopy(dict1)
        dict2 = copy.deepcopy(dict2)
    else:
        pass
    d = dict1
    for key in dict2:
        if(key in dict1):
            if(overwrite):
                d[key] = dict2[key]
            else:
                pass
        else:
            d[key] = dict2[key]
    return(d)

    


def dict_comprise(dict1,dict2):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        dict1 = {'a':1,'b':2,'c':3,'d':4}
        dict2 = {'b':2,'c':3}
        dict_comprise(dict1,dict2)
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


def dict_get_value_keys_description(d):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        dict1 = {'a':1,'b':2,'c':2,'d':4}
        dict_get_value_keys_description(dict1)
    '''
    pt = copy.deepcopy(d)
    seqs_for_del =[]
    vset = set({})
    for k in pt:
        vset.add(pt[k])
    desc = {}
    for v in vset:
        desc[v] = []
    for k in pt:
        desc[pt[k]].append(k)
    return(desc)



def dict_print_tree_pathstr_with_dynamic_indent(currd,**kwargs):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
        s = dict_print_tree_pathstr_with_dynamic_indent(currd)
        print(s)
    '''
    
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'

    tree_pathstr_hierachy_description = dict_get_tree_pathstr_hierachy_description(currd,delimiter = delimiter)
    deep_search_path = tree_pathstr_hierachy_description['deep_search_path'] 
    description_dict = tree_pathstr_hierachy_description['description_dict']
    
    if('from' in kwargs):
        fr = kwargs['from']
    else:
        fr = 0
    text = ''
    dsp_len = deep_search_path.__len__()
    if('to' in kwargs):
        to = kwargs['to']
    else:
        to = dsp_len
    if('full_path_display' in kwargs):
        full_path_display = kwargs['full_path_display']
    else:
        full_path_display = 0
    for i in range(0,dsp_len):
        x = deep_search_path[i][0]
        y = deep_search_path[i][1]
        ele = description_dict[x][y]
        if(full_path_display):
            line = ele
        else:
            if(ele == ''):
                pass
            else:
                if(ele[-1] == delimiter):
                    ele = str_rstrip(ele,delimiter,1)
                else:
                    pass
            indent = path_string_get_parent(ele)
            indent = indent.replace(delimiter,'')
            indent = ' ' * indent.__len__()
            rel = path_string_get_leaf(ele)
            line = ''.join((indent,rel))
        if((i >= fr) & (i <= to)):
            text = ''.join((text,'\n',line))
    return(text)

def dict_get_max_wordwidth(myDict):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        currd = {0:'AutoPauseSpeed', 125:'HRLimitLow', 6:'Activity'}
        dict_get_max_wordwidth(currd)
    '''
    maxValueWidth = 0
    for each in myDict:
        eachValueWidth = myDict[each].__len__()
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)

def dict_get_max_word_displaywidth(myDict):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        currd = {0:'你们大家好', 125:'ABCDE', 6:'1234567'}
        dict_get_max_word_displaywidth(currd)
    '''
    maxValueWidth = 0
    for each in myDict:
        eachValueWidth = str_display_width(myDict[each])
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)

class edict(dict):
    def setdefault_via_pathlist(self,pathlist,**kwargs):
        '''
            edict1 = edict({})
            edict1
            path_list = ['c','b']
            edict1.setdefault_via_pathlist(path_list)
            edict1
        '''
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        if('default_element' in kwargs):
            default_element = kwargs['default_element']
        else:
            default_element = {}
        return(dict_setdefault_via_path_list(self,pathlist,s2n=s2n,n2s=n2s,default_element=default_element))
    
    def setitem_via_pathlist(self,pathlist,value,**kwargs):
        '''
            edict1 = edict({})
            edict1
            
            path_list = ['c','b']
            edict1.setitem_via_pathlist(path_list,'i am ok')
            edict1
            
            
            path_list = ['c']
            edict1.setitem_via_pathlist(path_list,{})
            edict1
            
            path_list = ['c','b']
            edict1.setitem_via_pathlist(path_list,'i am ok')
            edict1
        '''
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(dict_setitem_via_path_list(self,pathlist,value,s2n=s2n,n2s=n2s))
    
    def getitem_via_pathlist(self,pathlist,**kwargs):
        '''
            edict1 = edict({'c':{'b':'x'}})
            edict1
            
            path_list = ['c','b']
            edict1.getitem_via_pathlist(path_list)
            
        '''
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(dict_getitem_via_path_list(self,pathlist,s2n=s2n,n2s=n2s))
    
    def getitem_via_cmd(self,cmd_str,**kwargs):
        '''
            edict1 = edict({'c':{'b':'x'}})
            edict1
            
            cmd = 'c b'
            edict1.getitem_via_cmd(cmd)
            
        '''
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        if('cmd_sp' in kwargs):
            cmd_sp = kwargs['cmd_sp']
        else:
            cmd_sp = ' '
        return(dict_getitem_via_cmd(self,cmd_str,s2n=s2n,n2s=n2s,cmd_sp=cmd_sp))

    def getitem_via_pathstr(self,pathstr,**kwargs):
        '''
            edict1 = edict({'c':{'b':'x'}})
            edict1
            
            pathstr = 'c/b'
            edict1.getitem_via_pathstr(pathstr)
            
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        if('strip_head_sp' in kwargs):
            strip_head_sp = kwargs['strip_head_sp']
        else:
            strip_head_sp = 0
        if('strip_tail_sp' in kwargs):
            strip_tail_sp = kwargs['strip_tail_sp']
        else:
            strip_tail_sp = 0
        return(dict_getitem_via_pathstr(self,pathstr,delimiter = delimiter,strip_head_sp =strip_head_sp,strip_tail_sp = strip_tail_sp))

    def delitem_via_pathlist(self,pathlist,**kwargs):
        '''
            edict1 = edict({'c':{'b':'x'}})
            edict1
            
            pathlist = ['c','b']
            edict1.delitem_via_pathlist(pathlist)
            
        '''
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(dict_delitem_via_path_list(self,pathlist,s2n=s2n,n2s=n2s))

    def sons_pathstrs(self,parent_pathstr,**kwargs):
        '''
            edict1 = edict({1:'a',2:{'x':'b'}})
            edict1
            
            edict1.sons_pathstrs('')
            edict1.sons_pathstrs('2')
            edict1.sons_pathstrs('2/x')
            
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(dict_get_all_sons_pathstrs(self,parent_pathstr,delimiter = delimiter))

    def include_pathlist(self,pathlist,**kwargs):
        '''
            edict1 = edict({1:'a',2:{'x':'b'}})
            edict1
            
            pathlist = [2,'x']
            edict1.include_pathlist(pathlist)
        '''
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(dict_include_pathlist(self,pathlist,s2n=s2n,n2s=n2s))

    def keys_via_value(self,value):
        '''
            edict1 = edict({1:'a',2:{'mm':'a'}})
            edict1
            edict1.keys_via_value('a')
        '''
        return(dict_find_keys_via_value(self,value,strict=strict))

    def keys_via_value_non_recursive(self,value):
        '''
            edict1 = edict({1:'a',2:{'mm':'a'}})
            edict1
            edict1.keys_via_value_non_recursive('a')
        '''
        return(dict_non_recursive_find_keys_via_value(self,value))

    def pathstr_hierachy_description(self,**kwargs):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            currd = { 'HRLimitHigh': 165, 'RuleIDs': [11516125, 11516163, 11516164], 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}}]}
            edict1 = edict(currd)
            desc_desc = edict1.pathstr_hierachy_description()
            pobj(desc_dict)
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(dict_get_pathstr_hierachy_description(self,delimiter = delimiter))

    def tree_pathstr_hierachy_description(self,**kwargs):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            currd = { 'HRLimitHigh': 165, 'RuleIDs': [11516125, 11516163, 11516164], 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}}]}
            edict1 = edict(currd)
            hierachy_desc = edict1.tree_pathstr_hierachy_description()
            hierachy_desc.keys()
            print(hierachy_desc['text'])
            pobj(hierachy_desc['parent_dict'])
            pobj(hierachy_desc['description_dict'])
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(dict_get_tree_pathstr_hierachy_description(self,delimiter = delimiter))

    def update_just_intersection(self,dict2):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            edict1 = edict({1:'a',2:'b',3:'c',4:'d'})
            edict2 = edict({5:'u',2:'v',3:'w',6:'x',7:'y'})
            edict1.update_just_intersection(edict1,edict2)
            pobj(edict1)
            pobj(edict2)
        '''
        return(dict_update_just_intersection(self,dict2))

    def uniqualize(self):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            edict1 = edict({1:'a',2:'b',3:'c',4:'b'})
            edict1.uniqualize()
            pobj(edict1)
        '''
        return(dict_uniqualize(self))

    def xextend(self,dict2,**kwargs):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            edict1 = edict({1:'a',2:'b',3:'c',4:'d'})
            edict2 = edict({5:'u',2:'v',3:'w',6:'x',7:'y'})
            edict1.xextend(edict2)
            pobj(edict1)
            pobj(edict2)
            edict1 = edict({1:'a',2:'b',3:'c',4:'d'})
            edict2 = edict({5:'u',2:'v',3:'w',6:'x',7:'y'})
            edict1.xextend(edict2,overwrite=1)
            pobj(edict1)
        '''
        if('deepcopy' in kwargs):
            deepcopy=kwargs['deepcopy']
        else:
            deepcopy=1
        if('overwrite' in kwargs):
            overwrite=kwargs['overwrite']
        else:
            overwrite=0
        if(deepcopy):
            dict1 = copy.deepcopy(self)
            dict2 = copy.deepcopy(dict2)
        else:
            pass
        return(dict_extend(dict1,dict2,deepcopy=deepcopy,overwrite=overwrite))

    def comprise(self,dict2):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            edict1 = edict({'a':1,'b':2,'c':3,'d':4})
            edict2 = edict({'b':2,'c':3})
            edict1.comprise(edict2)
        '''
        return((dict_comprise(self,dict2)))

    def value_keys_description(self):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            edict1 = edict({'a':1,'b':2,'c':2,'d':4})
            edict1.value_keys_description()
        '''
        return((dict_get_value_keys_description(self)))

    def tree_pathstr_with_dynamic_indent(self,**kwargs):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            currd = { 'HRLimitHigh': 165, 'RuleIDs': [11516125, 11516163, 11516164], 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}}]}
            edict1 = edict(currd)
            s = edict1.tree_pathstr_with_dynamic_indent()
            print(s)
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        if('from' in kwargs):
            fr = kwargs['from']
        else:
            fr = 0
        dsp_len = deep_search_path.__len__()
        if('to' in kwargs):
            to = kwargs['to']
        else:
            to = dsp_len
        return(dict_print_tree_pathstr_with_dynamic_indent(self,delimiter =delimiter,fr=fr,to=to))

    def max_wordwidth(self):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            currd = {0:'AutoPauseSpeed', 125:'HRLimitLow', 6:'Activity'}
            edict1 = edict(currd)
            edict1.get_max_wordwidth()
        '''
        return(dict_get_max_wordwidth(self))

    def max_word_displaywidth(self):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            currd = {0:'你们大家好', 125:'ABCDE', 6:'1234567'}
            edict1 = edict(currd)
            edict1.get_max_word_displaywidth()
        '''
        return(dict_get_max_word_displaywidth(self))


#list

def list_creat_default_with_len(len,default_element=None):
    rslt = []
    for i in range(0,len):
        rslt.append(default_element)
    return(rslt)

list_setdefault_via_path_list = dict_setdefault_via_path_list
list_setitem_via_path_list = dict_setitem_via_path_list
list_getitem_via_path_list = dict_getitem_via_path_list
list_getitem_via_cmd = dict_getitem_via_cmd
list_delitem_via_path_list = dict_delitem_via_path_list
list_getitem_via_pathstr = dict_getitem_via_pathstr
list_get_all_sons_pathstrs = dict_get_all_sons_pathstrs
list_include_pathlist = dict_include_pathlist
list_find_keys_via_value = dict_find_keys_via_value

def list_non_recursive_find_keys_via_value(l,v):
    rslt = []
    for i in range(0,l.__len__()):
        if(l[i] == v):
            rslt.append(i)
    return(rslt)

list_get_pathstr_hierachy_description = dict_get_pathstr_hierachy_description
list_get_partent_pathstr_hierachy_description_from_description_dict = dict_get_partent_pathstr_hierachy_description_from_description_dict
list_get_tree_pathstr_hierachy_description = dict_get_tree_pathstr_hierachy_description

def list_get_value_indexes_description(l):
    pt = copy.deepcopy(l)
    vset = set({})
    for v in pt:
        vset.add(v)
    for v in vset:
        desc[v] = []
    for i in range(0,l.__len__()):
        desc[l[i]].append(i)
    return(desc)

list_print_tree_pathstr_with_dynamic_indent = dict_print_tree_pathstr_with_dynamic_indent

def list_uniqualize(l):
    '''
        >>> 
        >>> l
        [1, 2, 2]
        >>> list_uniqualize(l)
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


def list_get_max_wordwidth(l):
    maxValueWidth = 0
    for each in l:
        eachValueWidth = each.__len__()
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)

def list_get_max_word_displaywidth(l):
    maxValueWidth = 0
    for each in l:
        eachValueWidth = str_display_width(each)
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)

#######################################################################
class elist(list):
    def creat_default_with_len(self,len,default_element=None):
        return(list_creat_default_with_len(len,default_element))
    def setdefault_via_pathlist(self,pathlist,**kwargs):
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        if('default_element' in kwargs):
            default_element = kwargs['default_element']
        else:
            default_element = {}
        return(list_setdefault_via_path_list(self,pathlist,s2n=s2n,n2s=n2s,default_element = default_element))
    def setitem_via_pathlist(self,pathlist,value,**kwargs):
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(list_setitem_via_path_list(self,pathlist,value,s2n=s2n,n2s=n2s))
    def getitem_via_pathlist(self,pathlist,**kwargs):
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(list_getitem_via_path_list(self,pathlist,s2n=s2n,n2s=n2s))
    def getitem_via_cmd(self,cmd_str,**kwargs):
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        if('cmd_sp' in kwargs):
            cmd_sp = kwargs['cmd_sp']
        else:
            cmd_sp = ' '
        return(list_getitem_via_cmd(self,cmd_str,s2n=s2n,n2s=n2s,cmd_sp=cmd_sp))
    def getitem_via_pathstr(self,pathstr,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(list_getitem_via_pathstr(self,pathstr,delimiter = delimiter))
    def delitem_via_pathlist(self,pathlist,**kwargs):
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(list_delitem_via_path_list(self,pathlist,s2n=s2n,n2s=n2s))
    def sons_pathstrs(self,parent_pathstr,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(list_get_all_sons_pathstrs(d,parent_pathstr,delimiter = delimiter))
    def include_pathlist(self,pathlist,**kwargs):
        if('s2n' in kwargs):
            s2n = kwargs['s2n']
        else:
            s2n = 0
        if('n2s' in kwargs):
            n2s = kwargs['n2s']
        else:
            n2s = 0
        return(list_include_pathlist(self,pathlist,s2n=s2n,n2s=n2s))
    def keys_via_value(self,value):
        return(list_find_keys_via_value(self,value))
    def keys_via_value_non_recursive(self,value):
        return(list_non_recursive_find_keys_via_value(self,value))
    def pathstr_hierachy_description(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(list_get_pathstr_hierachy_description(self,delimiter = delimiter))
    def tree_pathstr_hierachy_description(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(list_get_tree_pathstr_hierachy_description(self,delimiter = delimiter))
    def value_indexes_description(self):
        return(list_get_value_indexes_description(self))
    def tree_pathstr_with_dynamic_indent(self,**kwargs):
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        if('from' in kwargs):
            fr = kwargs['from']
        else:
            fr = 0
        dsp_len = deep_search_path.__len__()
        if('to' in kwargs):
            to = kwargs['to']
        else:
            to = dsp_len
        return(list_print_tree_pathstr_with_dynamic_indent(self,delimiter =delimiter,fr=fr,to=to))
    def uniqualize(self):
        return(list_uniqualize(self))
    def comprise(self,list2,**kwargs):
        if('strict' in kwargs):
            strict = kwargs['strict']
        else:
            strict = 0
        return(list_comprise(self,list2,strict=strict))
    def max_wordwidth(self):
        return(list_get_max_wordwidth(self))
    def max_word_displaywidth(self):
        return(list_get_max_word_displaywidth(self))


# bitmap
def bitmaplist_to_num(bitmaplist,**kwargs):
    '''
        bitmaplist_to_num([1, 0, 1, 0])
        bitmaplist_to_num([1, 0, 1, 0],bigend=1)
    '''
    if('bigend' in kwargs):
        bigend = kwargs['bigend']
    else:
        bigend = 0
    if(bigend):
        bm = copy.deepcopy(bitmaplist)
        bm.reverse()
    else:
        bm = bitmaplist
    num = 0
    for i in range(0,bm.__len__()):
        num = num + 2 **i * bm[i]
    return(num)

# ----------------------------
def num_to_bitmaplist(num,**kwargs):
    if('size' in kwargs):
        bitmap_size = kwargs['bitmap_size']
    else:
        bitmap_size = bin(num).__len__() - 2
    if('bigend' in kwargs):
        bigend = kwargs['bigend']
    else:
        bigend = 0
    bitmaplist = []
    s = bin(num)[2:]
    s_len = s.__len__() 
    for i in range(0,s_len):
        b = s[s_len-i-1]
        bitmaplist.append(int(b))
    for i in range(s_len,bitmap_size):
        bitmaplist.append(0)
    if(bigend):
        bitmaplist.reverse()
    else:
        pass
    return(bitmaplist)

def bitmaplist_bitsum(bitmaplist):
    sum = 0
    for i in range(0,bitmaplist.__len__()):
        sum = sum + bitmaplist[i]
    return(sum)

def bitmaplist_contain(bm1,bm2):
    bm3 = list(map(lambda x,y:(x|y),bm1,bm2))
    if(bm3 == bm1):
        return(True)
    else:
        return(False)



def subset_bitmap(n,k,**kwargs):
    if('bigend' in kwargs):
        bigend = kwargs['bigend']
    else:
        bigend = 0
    rslt = {}
    size = bin(2**n-1).__len__() - 2
    seq = 0 
    for i in range(0,2**n):
        bitmaplist = num_to_bitmaplist(i,size=size,bigend=bigend)
        sum = bitmaplist_bitsum(bitmaplist)
        if(sum == k):
            rslt[seq] = bitmaplist
            seq = seq + 1
        else:
            pass
    return(rslt)





class bitmap():
    def __init__(self,**kwargs):
        bm = kwargs['bitmap']
        if('size' in kwargs):
            size = kwargs['size']
        else:
            if(is_int(bm)):
                size = bin(num).__len__() - 2
            else:
                size = bm.__len__()
        if('bigend' in kwargs):
            bigend = kwargs['bigend']
        else:
            bigend = 0
        self.bigend = bigend
        if(is_int(bm)):
            self.num = bm
            self.list = num_to_bitmaplist(bm,size=size,bigend=bigend)
            self.size = self.list.__len__()
        elif(is_list(bm)):
            self.list = copy.deepcopy(bm)
            if(size <= bm.__len__()):
                pass
            else:
                if(bigend):
                    size = bm.__len__()
                    self.list = self.list  + [0] * (size)
                else:
                    self.list = [0] * (size) +  self.list 
            self.size = self.list.__len__()
            self.num = bitmaplist_to_num(bm)
        else:
            self.num = -1
            self.list = []
            self.size = 0
    def contain(self,bm2):
        return(bitmaplist_contain(self.list,bm2.list))
