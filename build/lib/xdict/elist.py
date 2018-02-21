import re
import struct
import copy

def list_intlize(l):
    return(list(map(lambda ele:int(ele),l)))

def list_strlize(l):
    return(list(map(lambda ele:str(ele),l)))

def list_diff_nonrecur(l1,l2):
    rslt = []
    for i in range(0,l1.__len__()):
        if(l1[i]!=l2[i]):
            print(i)
            rslt.append(i)
    return(rslt)

def list_shift(l):
    return(l.pop(0))

def list_prepend(l,ele):
    '''this will open a new list'''
    nl = [ele] + l
    return(nl)

def list_samemem_prepend(l,*args):
    '''this will on the same list
    '''
    length = l.__len__()
    args_len = args.__len__()
    for i in range(0,args_len):
        l.append(None)
    for i in range(length-1,-1,-1):
        l[i+args_len] = l[i]
    for i in range(0,args_len):
        l[i] = args[i]
    return(l)

list_unshift = list_samemem_prepend


def list_creat_default_with_len(len,default_element=None):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        l = list_creat_default_with_len(5)
        pobj(l)
    '''
    rslt = []
    for i in range(0,len):
        rslt.append(default_element)
    return(rslt)


list_setitem_via_path_list = dict_setitem_via_path_list
        # list_setitem_via_path_list(l,path_list,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b']]
        # path_list = [1,0]
        # list_setitem_via_path_list(l,path_list,'x')
        # pobj(l)
list_getitem_via_path_list = dict_getitem_via_path_list
        # list_getitem_via_path_list(l,path_list,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b']]
        # path_list = [1,0]
        # list_getitem_via_path_list(l,path_list)
        # pobj(l)
def list_getitem_via_cmd(l,cmd_str,**kwargs):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        l = ['a',['b']]
        cmd = '1 0'
        list_getitem_via_cmd(l,cmd)
        pobj(l)
    '''
    if('cmd_sp' in kwargs):
        cmd_sp = kwargs['cmd_sp']
    else:
        cmd_sp = ' '
    return(dict_getitem_via_cmd(l,cmd_str,s2n=1,n2s=0,cmd_sp=cmd_sp))

list_delitem_via_path_list = dict_delitem_via_path_list
        # list_getitem_via_path_list(l,path_list,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b']]
        # path_list = [1,0]
        # list_getitem_via_path_list(l,path_list)
        # pobj(l)
def list_getitem_via_pathstr(l,pathstr,**kwargs):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        l = ['a',['b']]
        pathstr = '1/0'
        list_getitem_via_pathstr(l,pathstr)
        pobj(l)
    '''
    if('delimiter' in kwargs):
        delimiter = kwargs['delimiter']
    else:
        delimiter = '/'
    return(dict_getitem_via_pathstr(l,pathstr,s2n=1))

list_get_all_sons_pathstrs = dict_get_all_sons_pathstrs
        # list_get_all_sons_pathstrs(l,full_key_path,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b',['x','y']],'c']
        # list_get_all_sons_pathstrs(l,'')
        # list_get_all_sons_pathstrs(l,'1')
        # list_get_all_sons_pathstrs(l,'1/1')

list_include_pathlist = dict_include_pathlist
        # list_include_pathlist(l,path_list,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b',['x','y']],'c']
        # list_include_pathlist(l,[1,1,1])

list_find_keys_via_value = dict_find_keys_via_value
        # list_find_keys_via_value(l,value,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b',['x','b']],'b']
        # list_find_keys_via_value(l,'b')

def list_non_recursive_find_keys_via_value(l,v):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        l = ['a',['b',['x','b']],'b']
        list_find_keys_via_value_non_recursive(l,'b')
    '''
    rslt = []
    for i in range(0,l.__len__()):
        if(l[i] == v):
            rslt.append(i)
    return(rslt)


list_get_pathstr_hierachy_description = dict_get_pathstr_hierachy_description
        # list_get_pathstr_hierachy_description(l,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b',['x','b']],'b']
        # desc = list_get_pathstr_hierachy_description(l)
        # pobj(desc)
list_get_partent_pathstr_hierachy_description_from_description_dict = dict_get_partent_pathstr_hierachy_description_from_description_dict
        # list_get_partent_pathstr_hierachy_description_from_description_dict(desc)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b',['x','b']],'b']
        # desc = list_get_pathstr_hierachy_description(l)
        # pobj(desc)
        # ppdesc = list_get_partent_pathstr_hierachy_description_from_description_dict(desc)
        # pobj(ppdesc)
list_get_tree_pathstr_hierachy_description = dict_get_tree_pathstr_hierachy_description
        # list_get_tree_pathstr_hierachy_description(l,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b',['x','b']],'b']
        # desc = list_get_tree_pathstr_hierachy_description(l)
        # pobj(desc)

def list_get_value_indexes_description(l):
    '''
        from xdict.utils import *
        from xdict.jprint import pobj
        l = ['a','b','b','a','c','b']
        list_get_value_indexes_description(l)
    '''
    pt = copy.deepcopy(l)
    desc = {}
    vset = set({})
    for v in pt:
        vset.add(v)
    for v in vset:
        desc[v] = []
    for i in range(0,l.__len__()):
        desc[l[i]].append(i)
    return(desc)

list_print_tree_pathstr_with_dynamic_indent = dict_print_tree_pathstr_with_dynamic_indent
        # list_print_tree_pathstr_with_dynamic_indent(l,**kwargs)
        # from xdict.utils import *
        # from xdict.jprint import pobj
        # l = ['a',['b',['x','b']],'b']
        # s = list_print_tree_pathstr_with_dynamic_indent(l)
        # print(s)

def list_uniqualize(l):
    '''
        l = [1, 2, 2]
        list_uniqualize(l)
        l
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
        list_comprise([1,2,3,4,5],[2,3,4],strict=0)
        list_comprise([1,2,3,4,5],[2,3,4])
        list_comprise([1,2,3,4,5],[2,3,4],strict=1)
        list_comprise([1,2,3,4,5],[1,2,3,4],strict=1)
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
    '''
        l = ['a','bb','hello','xx','你好吗']
        list_get_max_wordwidth(l)
    '''
    maxValueWidth = 0
    for each in l:
        eachValueWidth = each.__len__()
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)

def list_get_max_word_displaywidth(l):
    '''
        l = ['a','bb','hello','xx','你好吗']
        list_get_max_word_displaywidth(l)
    '''
    maxValueWidth = 0
    for each in l:
        eachValueWidth = str_display_width(each)
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)

#######################################################################
class elist(list):
    def creat_default_with_len(self,len,default_element=None):
        '''
            elist1 = elist([])
            elist1.creat_default_with_len(5)
            elist1
        '''
        return(list_creat_default_with_len(len,default_element))
    def setitem_via_pathlist(self,pathlist,value,**kwargs):
        '''
            elist1 = elist(['a',['b',['x','y'],'u'],'c'])
            pathlist = [1,1,0]
            elist1.setitem_via_pathlist(pathlist,6)
        '''
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
        '''
            elist1 = elist(['a',['b',['x','y'],'u'],'c'])
            pathlist = [1,1,0]
            elist1.getitem_via_pathlist(pathlist)
        '''
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
        '''
            elist1 = elist(['a',['b',['x','y'],'u'],'c'])
            cmd_str = '1 1 0'
            elist1.getitem_via_cmd(cmd_str)
        '''
        if('cmd_sp' in kwargs):
            cmd_sp = kwargs['cmd_sp']
        else:
            cmd_sp = ' '
        return(list_getitem_via_cmd(self,cmd_str,cmd_sp=cmd_sp))
    def getitem_via_pathstr(self,pathstr,**kwargs):
        '''
            elist1 = elist(['a',['b',['x','y'],'u'],'c'])
            pathstr = '1/1/0'
            elist1.getitem_via_pathstr(pathstr)
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        return(list_getitem_via_pathstr(self,pathstr,delimiter = delimiter))
    def delitem_via_pathlist(self,pathlist,**kwargs):
        '''
            elist1 = elist(['a',['b',['x','y'],'u'],'c'])
            pathlist = [1,1,0]
            elist1.delitem_via_pathlist(pathlist)
            elist1
        '''
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
        '''
            elist1 = elist(['a',['b',['x','y'],'u'],'c'])
            elist1.sons_pathstrs('')
            elist1.sons_pathstrs('1')
            elist1.sons_pathstrs('1/1')
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        l = list(self)
        return(list_get_all_sons_pathstrs(l,parent_pathstr,delimiter = delimiter))
    def include_pathlist(self,pathlist,**kwargs):
        '''
            elist1 = elist(['a',['b',['x','y'],'u'],'c'])
            elist1.include_pathlist([1,1,1])
            elist1.include_pathlist([1,1,2])
            elist1.include_pathlist([1,1,3])
        '''
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
        '''
            elist1 = elist(['a',['b',['x','a'],'a'],'c'])
            elist1.keys_via_value('a')
        '''
        l = list(self)
        return(list_find_keys_via_value(l,value))
    def keys_via_value_non_recursive(self,value):
        '''
            elist1 = elist(['a',['b',['x','a'],'a'],'c'])
            elist1.keys_via_value_non_recursive('a')
        '''
        return(list_non_recursive_find_keys_via_value(self,value))
    def pathstr_hierachy_description(self,**kwargs):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            elist1 = elist(['a',['b',['x','b']],'b'])
            desc = elist1.pathstr_hierachy_description()
            pobj(desc)
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        l = list(self)
        return(list_get_pathstr_hierachy_description(l,delimiter = delimiter))
    def tree_pathstr_hierachy_description(self,**kwargs):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            elist1 = elist(['a',['b',['x','b']],'b'])
            desc = elist1.tree_pathstr_hierachy_description()
            pobj(desc['description_dict'])
            pobj(desc['parent_dict'])
            pobj(desc['deep_search_path'],fixed_indent=1)
            print(desc['text'])
        '''
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        l = list(self)
        return(list_get_tree_pathstr_hierachy_description(l,delimiter = delimiter))
    def value_indexes_description(self):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            elist1 = elist(['a','b','b','a','c','b'])
            elist1.value_indexes_description()
        '''
        return(list_get_value_indexes_description(self))
    def tree_pathstr_with_dynamic_indent(self,**kwargs):
        '''
            from xdict.utils import *
            from xdict.jprint import pobj
            elist1 = elist(['a',['b',['x','b']],'b'])
            s = elist1.tree_pathstr_with_dynamic_indent()
            print(s)
        '''
        l = list(self)
        if('delimiter' in kwargs):
            delimiter = kwargs['delimiter']
        else:
            delimiter = '/'
        tree_pathstr_hierachy_description = dict_get_tree_pathstr_hierachy_description(l,delimiter = delimiter)
        deep_search_path = tree_pathstr_hierachy_description['deep_search_path'] 
        description_dict = tree_pathstr_hierachy_description['description_dict']
        if('from' in kwargs):
            fr = kwargs['from']
        else:
            fr = 0
        dsp_len = deep_search_path.__len__()
        if('to' in kwargs):
            to = kwargs['to']
        else:
            to = dsp_len
        return(list_print_tree_pathstr_with_dynamic_indent(l,delimiter =delimiter,fr=fr,to=to))
    def uniqualize(self):
        '''
            elist1 = elist([1, 2, 2])
            elist1.uniqualize()
            elist1
        '''
        return(list_uniqualize(self))
    def comprise(self,list2,**kwargs):
        '''
            elist1 = elist([1,2,3,4,5])
            elist1.comprise([2,3,4],strict=0)
            elist1.comprise([2,3,4])
            elist1.comprise([2,3,4],strict=1)
            elist1.comprise([1,2,3,4],strict=1)
        '''
        if('strict' in kwargs):
            strict = kwargs['strict']
        else:
            strict = 0
        return(list_comprise(self,list2,strict=strict))
    def max_wordwidth(self):
        '''
            elist1 = elist(['a','bb','hello','xx','你好吗'])
            elist1.max_wordwidth()
        '''
        return(list_get_max_wordwidth(self))
    def max_word_displaywidth(self):
        '''
            elist1 = elist(['a','bb','hello','xx','你好吗'])
            elist1.max_word_displaywidth()
        '''
        return(list_get_max_word_displaywidth(self))



