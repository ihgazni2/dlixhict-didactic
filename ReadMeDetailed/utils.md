##object type judgement
-----------------------------------------------------------------------------------------------------------------------
1. is_list(obj) 
2. is_tuple(obj)
3. is_dict(obj)
4. is_set(obj)
5. is_str(obj)
6. is_int(obj)
7. is_float(obj)
8. is_number(obj)
9. is_bool(obj)
10. is_none(obj)
11. is_recursive_type(obj)
12. is_module(obj)
13. is_non_buildin_function(obj)
14. is_buildin_function(obj)
15. is_function(obj)
16. is_type(obj)
17. is_customer_defined_type(obj)
18. is_hashable_type(obj)
19. is_unhashable_type(obj)
20. is_json(obj,strict=False)
21. is_bytes(obj)
22. is_int_str(s)
23. is_float_str(s)
24. is_number_str(s)
25. get_obj_type_name(obj)
-----------------------------------------------------------------------------------------------------------------------

##path string
-----------------------------------------------------------------------------------------------------------------------
1. path_string_is_slash_end(path_string,delimiter='/')  

        >>> from xdict.utils import *  
        >>> path_string_is_slash_end('a/b/c')
        False
        >>> path_string_is_slash_end('a/b/c/')
        True
        >>> path_string_is_slash_end('a#b#c#',delimiter='#')
        True
        >>> 

2. path_string_get_head(path_string,delimiter='/')  

        >>> from xdict.utils import *
        >>> path_string_get_head('a/b/c')
        'a/b/'
        >>> path_string_get_head('/a/b/c')
        '/a/b/'
        >>> path_string_get_head('a/b/c/')
        'a/b/'
        >>> path_string_get_head('/a/b/c/')
        '/a/b/'

3. path_string_get_tail(path_string,delimiter='/')  

        >>> from xdict.utils import *
        >>> path_string_get_tail('a/b/c')
        'c'
        >>> path_string_get_tail('/a/b/c')
        'c'
        >>> path_string_get_tail('a/b/c/')
        'c/'
        >>> path_string_get_tail('/a/b/c/')
        'c/'


4. path_string_to_path_list(path_str,**kwargs)  

        >>> from xdict.utils import *
        >>> path_string_to_path_list('/a/b/c/')
        ['', 'a', 'b', 'c', '']
        >>> path_string_to_path_list('#a#b#c#',delimiter = '#')
        ['', 'a', 'b', 'c', '']
        >>> path_string_to_path_list('/a/b/c/',keep_begin_sp=0)
        ['a', 'b', 'c', '']
        >>> path_string_to_path_list('/a/b/c/',keep_end_sp=0)
        ['', 'a', 'b', 'c']
        >>> path_string_to_path_list('/a/b/c/',keep_begin_sp=0,keep_end_sp=0)
        ['a', 'b', 'c']



5. path_string_is_parent(parent,son,**kwargs)  

        >>> from xdict.utils import *
        >>> path_string_is_parent('a/b/','a/b/c')
        0
        >>> path_string_is_parent('a/b/','a/b/c/')
        0
        >>> path_string_is_parent('a/b/','a/b/c/d')
        0
        >>> path_string_is_parent('a/b/','a/b/c/d/')
        0
        >>> 
        >>> path_string_is_parent('/a/b','a/b/c')
        0
        >>> path_string_is_parent('/a/b','a/b/c/')
        0
        >>> path_string_is_parent('/a/b','a/b/c/d')
        0
        >>> path_string_is_parent('/a/b','a/b/c/d/')
        0
        >>> 
        >>> path_string_is_parent('a/b','a/b/c')
        1
        >>> path_string_is_parent('a/b','a/b/')
        1
        >>> path_string_is_parent('a/b','a/b/c/')
        0
        >>> path_string_is_parent('a/b','a/b/c/d')
        0
        >>> path_string_is_parent('a/b','a/b/c/d/')
        0
        >>> 
        >>> path_string_is_parent('a/b','/a/b/c')
        0
        >>> path_string_is_parent('a/b','/a/b/c/')
        0
        >>> path_string_is_parent('a/b','/a/b/c/d')
        0
        >>> path_string_is_parent('a/b','/a/b/c/d/')
        0

6. path_string_is_son(son,parent,**kwargs)

        >>> from xdict.utils import *
        >>> path_string_is_son('a/b/c','a/b/')
        0
        >>> path_string_is_son('a/b/c/','a/b/')
        0
        >>> path_string_is_son('a/b/c/d','a/b/')
        0
        >>> path_string_is_son('a/b/c/d/','a/b/')
        0
        >>> 
        >>> path_string_is_son('a/b/c','/a/b')
        0
        >>> path_string_is_son('a/b/c/','/a/b')
        0
        >>> path_string_is_son('a/b/c/d','/a/b')
        0
        >>> path_string_is_son('a/b/c/d/','/a/b')
        0
        >>> 
        >>> path_string_is_son('a/b/c','a/b')
        1
        >>> path_string_is_son('a/b/','a/b')
        1
        >>> path_string_is_son('a/b/c/','a/b')
        0
        >>> path_string_is_son('a/b/c/d','a/b')
        0
        >>> path_string_is_son('a/b/c/d/','a/b')
        0
        >>> 
        >>> path_string_is_son('/a/b/c','a/b')
        0
        >>> path_string_is_son('/a/b/c/','a/b')
        0
        >>> path_string_is_son('/a/b/c/d','a/b')
        0
        >>> path_string_is_son('/a/b/c/d/','a/b')
        0

7. path_string_is_sibling(sib1,sib2,**kwargs)

        >>> 
        >>> from xdict.utils import *
        >>> path_string_is_sibling('a/b/c','a/b/d')
        1
        >>> path_string_is_sibling('a/b/c','a/b/e')
        1
        >>> path_string_is_sibling('a/b/c','a/b/d/')
        0
        >>> path_string_is_sibling('a/b/c','a/e/d')
        0


8. path_string_is_leaf(leaf,path_str,**kwargs)  

        >>> from xdict.utils import *
        >>> path_string_is_leaf('c','a/b/c')
        1
        >>> path_string_is_leaf('/c','a/b/c')
        0
        >>> path_string_is_leaf('','a/b/c')
        0
        >>> path_string_is_leaf('c/','a/b/c/')
        0
        >>> path_string_is_leaf('','a/b/c/')
        1

9. path_string_is_ancestor(ances,des,**kwargs)

        >>> from xdict.utils import *
        >>> path_string_is_ancestor('a/b','a/b')
        False
        >>> path_string_is_ancestor('a/b','a/b/')
        True
        >>> path_string_is_ancestor('a/b','a/b/c')
        True
        >>> path_string_is_ancestor('a/b','a/b/c/d')
        True
        >>> path_string_is_ancestor('a/b','a/b/c/d/')
        True



10. path_string_is_descedant(des,ances,**kwargs)  

        >>> from xdict.utils import *
        >>> path_string_is_descedant('a/b','a/b')
        False
        >>> path_string_is_descedant('a/b/','a/b')
        True
        >>> path_string_is_descedant('a/b/c','a/b')
        True
        >>> path_string_is_descedant('a/b/c/d','a/b')
        True
        >>> path_string_is_descedant('a/b/c/d/','a/b')
        True



11. path_string_get_parent(son,**kwargs)  

        >>> from xdict.utils import *
        >>> path_string_get_parent('a/b/c')
        'a/b'
        >>> path_string_get_parent('a/b/c/')
        'a/b/c'
        >>> path_string_get_parent('/a/b/c')
        '/a/b'
        >>> path_string_get_parent('/a/b/c/')
        '/a/b/c'
        >>> path_string_get_parent('c')
        ''
        >>> 

12. path_string_get_leaf(absp,**kwargs)  

        >>> from xdict.utils import *
        >>> path_string_get_leaf('a/b/c')
        'c'
        >>> path_string_get_leaf('a/b/c/')
        ''
        >>> path_string_get_leaf('/a/b/c')
        'c'
        >>> path_string_get_leaf('/a/b/c/')
        ''
        >>> path_string_get_leaf('c')
        'c'
        >>> path_string_get_leaf('')
        ''
13. path_string_get_ancestors(des,**kwargs) 

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> ancestors = path_string_get_ancestors('a/b/c/d')
        >>> pobj(ancestors)
        [
        'a', 
        'a/b', 
         'a/b/c'
        ]
        >>> ancestors = path_string_get_ancestors('/a/b/c/d')
        >>> pobj(ancestors)
        [
         '', 
         '/a', 
         '/a/b', 
         '/a/b/c'
        ]
        >>> 



-----------------------------------------------------------------------------------------------------------------------

##path list
-----------------------------------------------------------------------------------------------------------------------
1. path_list_get_head(path_list)  

        >>> from xdict.utils import *
        >>> path_list_get_head(['a','b','c'])
        ['a', 'b', '']
        >>> path_list_get_head(['','a','b','c'])
        ['', 'a', 'b', '']
        >>> path_list_get_head(['a','b','c',''])
        ['a', 'b', '']
        >>> path_list_get_head(['','a','b','c',''])
        ['', 'a', 'b', '']

2. path_list_get_tail(path_list)  

        >>> from xdict.utils import *
        >>> path_list_get_tail(['a','b','c'])
        ['c']
        >>> path_list_get_tail(['','a','b','c'])
        ['c']
        >>> path_list_get_tail(['a','b','c',''])
        ['c', '']
        >>> path_list_get_tail(['','a','b','c',''])
        ['c', '']


3. path_list_get_parent(pathlist)  

        >>> from xdict.utils import *
        >>> path_list_get_parent(['a','b','c'])
        ['a', 'b']
        >>> path_list_get_parent(['a','b','c',''])
        ['a', 'b', 'c']
        >>> path_list_get_parent(['a','b','c'])
        ['a', 'b']
        >>> path_list_get_parent(['','a','b','c',''])
        ['', 'a', 'b', 'c']
        >>> path_list_get_parent(['c'])
        []


4. path_list_get_ancestors(des_pl,**kwargs)  

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> ancestors = path_list_get_ancestors(['a','b','c','d'])
        >>> pobj(ancestors,fixed_indent=1)
        [
            ['a'],
            ['a', 'b'],
            ['a', 'b', 'c']
        ]
        >>> ancestors = path_list_get_ancestors(['a','b','c','d'])
        >>> pobj(ancestors,fixed_indent=1)
        [
           ['a'],
            ['a', 'b'],
            ['a', 'b', 'c']
        ]


5. path_list_to_path_string(path_list,**kwargs)  

        >>> from xdict.utils import *
        >>> path_list_to_path_string(['a','b','c',''])
        'a/b/c/'
        >>> path_list_to_path_string(['a','b','c',''],delimiter = '#')
        'a#b#c#'
        >>> path_list_to_path_string(['','a','b','c',''],keep_begin_sp=0)
        'a/b/c/'
        >>> path_list_to_path_string(['','a','b','c',''],keep_end_sp=0)
        '/a/b/c'
        >>> path_list_to_path_string(['','a','b','c',''],keep_begin_sp=0,keep_end_sp=0)
        'a/b/c'


6. path_list_is_parent(parent_pl,son_pl)  

        >>> from xdict.utils import *
        >>> path_list_is_parent(['a','b',''],['a','b','c'])
        False
        >>> path_list_is_parent(['a','b',''],['a','b','c',''])
        False
        >>> path_list_is_parent(['a','b',''],['a','b','c','d'])
        False
        >>> path_list_is_parent(['a','b',''],['a','b','c','d',''])
        False
        >>> 
        >>> path_list_is_parent(['','a','b'],['a','b','c'])
        False
        >>> path_list_is_parent(['','a','b'],['a','b','c',''])
        False
        >>> path_list_is_parent(['','a','b'],['a','b','c','d'])
        False
        >>> path_list_is_parent(['','a','b'],['a','b','c','d',''])
        False
        >>> 
        >>> path_list_is_parent(['a','b'],['a','b','c'])
        True
        >>> path_list_is_parent(['a','b'],['a','b',''])
        True
        >>> path_list_is_parent(['a','b'],['a','b','c',''])
        False
        >>> path_list_is_parent(['a','b'],['a','b','c','d'])
        False
        >>> path_list_is_parent(['a','b'],['a','b','c','d',''])
        False
        >>> 
        >>> path_list_is_parent(['a','b'],['a','b','c'])
        True
        >>> path_list_is_parent(['a','b'],['a','b','c',''])
        False
        >>> path_list_is_parent(['a','b'],['a','b','c','d'])
        False
        >>> path_list_is_parent(['a','b'],['a','b','c','d',''])
        False


7. path_list_is_son(son_pl,parent_pl)  

        >>> from xdict.utils import *
        >>> path_list_is_son(['a','b','c'],['a','b',''])
        False
        >>> path_list_is_son(['a','b','c',''],['a','b',''])
        False
        >>> path_list_is_son(['a','b','c','d'],['a','b',''])
        False
        >>> path_list_is_son(['a','b','c','d',''],['a','b',''])
        False
        >>> 
        >>> path_list_is_son(['a','b','c'],['','a','b'])
        False
        >>> path_list_is_son(['a','b','c',''],['','a','b'])
        False
        >>> path_list_is_son(['a','b','c','d'],['','a','b'])
        False
        >>> path_list_is_son(['a','b','c','d',''],['','a','b'])
        False
        >>> 
        >>> path_list_is_son(['a','b','c'],['a','b'])
        True
        >>> path_list_is_son(['a','b',''],['a','b'])
        True
        >>> path_list_is_son(['a','b','c',''],['a','b'])
        False
        >>> path_list_is_son(['a','b','c','d'],['a','b'])
        False
        >>> path_list_is_son(['a','b','c','d',''],['a','b'])
        False
        >>> 
        >>> path_list_is_son(['a','b','c'],['a','b'])
        True
        >>> path_list_is_son(['a','b','c',''],['a','b'])
        False
        >>> path_list_is_son(['a','b','c','d'],['a','b'])
        False
        >>> path_list_is_son(['a','b','c','d',''],['a','b'])
        False

8. path_list_is_sibling(sib1,sib2,**kwargs)  

        >>> from xdict.utils import *
        >>> path_list_is_sibling(['a','b','c'],['a','b','d'])
        1
        >>> path_list_is_sibling(['a','b','c'],['a','b','e'])
        1
        >>> path_list_is_sibling(['a','b','c'],['a','b','d',''])
        0
        >>> path_list_is_sibling(['a','b','c'],['a','e','d'])
        0

9. path_list_is_leaf(leaf,pathlist,**kwargs)  

        >>> from xdict.utils import *
        >>> path_list_is_leaf(['c'],['a','b','c'])
        1
        >>> path_list_is_leaf(['','c'],['a','b','c'])
        0
        >>> path_list_is_leaf([''],['a','b','c'])
        0
        >>> path_list_is_leaf(['c',''],['a','b','c',''])
        0
        >>> path_list_is_leaf([''],['a','b','c',''])
        1

10. path_list_is_ancestor(ances_pl,des_pl)  

        >>> from xdict.utils import *
        >>> path_list_is_ancestor(['a','b'],['a','b'])
        False
        >>> path_list_is_ancestor(['a','b'],['a','b',''])
        True
        >>> path_list_is_ancestor(['a','b'],['a','b','c'])
        True
        >>> path_list_is_ancestor(['a','b'],['a','b','c','d'])
        True
        >>> path_list_is_ancestor(['a','b'],['a','b','c','d',''])
        True

11. path_list_is_descedant(des_pl,ances_pl)  

        >>> from xdict.utils import *
        >>> path_list_is_descedant(['a','b'],['a','b'])
        False
        >>> path_list_is_descedant(['a','b',''],['a','b'])
        True
        >>> path_list_is_descedant(['a','b','c'],['a','b'])
        True
        >>> path_list_is_descedant(['a','b','c','d'],['a','b'])
        True
        >>> path_list_is_descedant(['a','b','c','d',''],['a','b'])
        True


12. path_list_to_getitem_string(path_list)  

        >>> path_list_to_getitem_string([1, '1', 2])
            "[1]['1'][2]"
        >>> 


-----------------------------------------------------------------------------------------------------------------------

##string
1. str_to_bool(s,**kwargs)

        >>> from xdict.utils import *
        >>> str_to_bool('False')
        False
        >>> str_to_bool('false')
        False
        >>> str_to_bool('True')
        True
        >>> str_to_bool('true')
        True

2. str_lstrip(s,char,count)

        >>> from xdict.utils import *
        >>> str_lstrip('sssa','s',0)
        'sssa'
        >>> str_lstrip('sssa','s',1)
        'ssa'
        >>> str_lstrip('sssa','s',2)
        'sa'
        >>> str_lstrip('sssa','s',3)
        'a'
        >>> str_lstrip('sssa','s',4)
        'a'

3. str_rstrip(s,char,count)

        >>> from xdict.utils import *
        >>> str_rstrip('asss','s',0)
        'asss'
        >>> str_rstrip('asss','s',1)
        'ass'
        >>> str_rstrip('asss','s',2)
        'as'
        >>> str_rstrip('asss','s',3)
        'a'
        >>> str_rstrip('asss','s',4)
        'a'

4. str_prepend(s,char,n)

        >>> from xdict.utils import *
        >>> str_prepend('a','s',3)
        'sssa'

5. str_apppend(s,char,n)

        >>> from xdict.utils import *
        >>> str_append('a','s',3)
        'asss'


6. str_at_begin_of_str(str1,str2)

        >>> from xdict.utils import *
        >>> str_at_begin_of_str('abc','abcd')
        True


7. str_at_end_of_str(str1,str2)

        >>> from xdict.utils import *
        >>> str_at_end_of_str('abcd','bcd')
        False

8. str_display_width(s)

        >>> from xdict.utils import *
        >>> str_display_width('a')
        1
        >>> str_display_width('去')
        2

9. str_prepend_spaces_basedon_displaywidth(s,width)

        >>> from xdict.utils import *
        >>> str_prepend_basedon_displaywidth('a',4,padding='x')
        'xxxa'
        >>> str_prepend_basedon_displaywidth('去',4,padding='x')
        'xx去'

10. str_append_basedon_displaywidth(s,width,**kwargs)

        >>> from xdict.utils import *
        >>> str_append_basedon_displaywidth('a',4,padding='x')
        'xxxa'
        >>> str_append_basedon_displaywidth('去',4,padding='x')
        'xx去'



-------------------------------------------------------------------------------------------------------------------------

## char encode decode  
1. unpack_unicode_char_bytes(two_bytes)  
![](/Images/utils.unpack_unicode_char_bytes.png)  

2. pack_unicode_char_str(char_str)  
![](/Images/utils.pack_unicode_char_str.png)  

3. unpack_unicode_bytes_stream(Bs)  
![](/Images/utils.unpack_unicode_bytes_stream.png)  

4. pack_unicode_str(str)  
![](/Images/utils.pack_unicode_str.png) 

5. char_to_slash_u_str(ch,with_slash_u=1)  
![](/Images/utils.char_to_slash_u_str.png) 

6. slash_u_str_to_char(slash_u_str)  
![](/Images/utils.slash_u_str_to_char.png) 

7. str_to_slash_u_str(a_string,with_slash_u=1)  
![](/Images/utils.str_to_slash_u_str.png)

8. slash_u_str_to_str(slash_us)  
![](/Images/utils.slash_u_str_to_str.png)

9. char_str_to_unicode_num(char_str)  
![](/Images/utils.char_str_to_unicode_num.png)

10. unicode_num_to_char_str(unicode_num)  
![](/Images/utils.unicode_num_to_char_str.png)

11. str_to_unicode_num_array(a_string)  
![](/Images/utils.str_to_unicode_num_array.png)

12. unicode_num_array_to_str(num_arr)  
![](/Images/utils.unicode_num_array_to_str.png)

--------------------------------------------------------------------------------------------------------------------------------


## dict

1. dict_setdefault_via_path_list(external_dict,path_list,**kwargs)

        from xdict.utils import *
        >>> y = {}
        >>> path_list = ['c','b']
        >>> dict_setdefault_via_path_list(y,path_list)
        {'c': {'b': {}}}

2. dict_setitem_via_path_list(external_dict,path_list,value,**kwargs)  

        from xdict.utils import *
        >>> y = {'c': {'b': {}}}
        >>> dict_setitem_via_path_list(y,['c','b'],200)
        {'c': {'b': 200}}
        >>> 

3. dict_getitem_via_path_list(external_dict,path_list,**kwargs)  

        from xdict.utils import *
        >>> y = {'c': {'b': 200}}
        >>> dict_getitem_via_path_list(y,['c','b'])
        200


4. dict_getitem_via_cmd(external_dict,cmd_str,**kwargs)  

        from xdict.utils import *
        >>> y = {'c': {'b': 200}}
        >>> dict_getitem_via_cmd(y,'c b')
        200

5. dict_getitem_via_pathstr(d,full_key_path,**kwargs)  

        from xdict.utils import *
        >>> y = {'c': {'b': 200}}
        >>> dict_getitem_via_pathstr(y,'c/b')
        200

6. dict_delitem_via_path_list(external_dict,path_list,**kwargs)

        from xdict.utils import *
        >>> y = {'c': {'b': 200}}
        >>> dict_delitem_via_path_list(y,['c','b'])
        {'c': {}}
        >>> 

7. dict_delitem_via_path_list(external_dict,path_list,**kwargs)

        from xdict.utils import *
        >>> y = {'c': {'b': 200}}
        >>> dict_delitem_via_path_list(y,['c','b'])
        {'c': {}}

8. dict_delitem_via_pathstr(external_dict,pathstr,**kwargs)

        >>> y = {'c': {'b': 200}}
        >>> dict_delitem_via_pathstr(y,'c/b')
        {'c': {}}
        >>> 
        
9. dict_delitem_via_cmd(external_dict,cmd_str,**kwargs)

        from xdict.utils import *
        >>> y = {'c': {'b': 200}}
        >>> dict_delitem_via_cmd(y,'c b')
        {'c': {}}

11. dict_get_all_sons_pathstrs(d,full_key_path,**kwargs)  

        >>> from xdict.utils import *
        >>> dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'')
        ['1', '2']
        >>> dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'2')
        ['2/x']
        >>> dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'2/x')
        []

        
        >>> dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'',keep_indicator=1)
        ['/1', '/2/']
        >>> dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'2',keep_indicator=1)
        ['/2/x']
        >>> dict_get_all_sons_pathstrs({1:'a',2:{'x':'b'}},'2/x',keep_indicator=1)
        []
        >>> 


12. dict_include_pathlist(external_dict,path_list,**kwargs)

        >>> from xdict.utils import *
        >>> y = {'a':
        ...         {'x':88},
        ...     'b':
        ...         {
        ...             'x':
        ...                 {'c':66}
        ...         }
        ... }
        >>> dict_include_pathlist(y,['a'])
        True
        >>> dict_include_pathlist(y,['a','x'])
        True
        >>> dict_include_pathlist(y,['b','x','c'])
        True

13. dict_find_keys_via_value(dlts,v,**kwargs)

        >>> from xdict.utils import *
        >>> dlts = {1:'a',2:{3:'a'}}
        >>> dict_find_keys_via_value(dlts,'a')
        [[1], [2, 3]]
        >>> dict_find_keys_via_value(dlts,'a')
        [[1], [2, 3]]
        >>>
        

14. dict_non_recursive_find_keys_via_value(d,v)

        >>> from xdict.utils import *
        >>> dlts = {1:'a',2:{3:'a'}}
        >>> dict_non_recursive_find_keys_via_value(dlts,'a')
        [1]
        

15. dict_get_pathstr_hierachy_description(dora,**kwargs)

        from xdict.utils import *
        from xdict.jprint import pobj
        >>> pobj(currd)
        {
        'Activity': 6, 
        'Interval1Time': None, 
        'RecordingInterval': 1, 
        'UseAccelerometer': False, 
        'Interval2Distance': None, 
        'UseHRLimits': False, 
        'UsePowerPOD': False, 
        'HRLimitLow': 125, 
        'UseBikePOD': False, 
        'AutolapDistanceBikePOD': None, 
        'UseAutolap': True, 
        'Interval2Time': None, 
        'Ordinal': 2, 
        'SpeedLimitLow': None, 
        'UseSpeedLimits': None, 
        'LoggedRuleIDs': 
                        [
                        11516163, 
                        11516164, 
                        11516125
                        ], 
        'AutomaticLogRecording': None, 
        '__type': 'Suunto.BLL.CustomMode', 
        'IntervalRepetitions': 0, 
        'SpeedLimitHigh': None, 
        'HRLimitHigh': 165, 
        'Id': 13336645, 
        'AutolapDistanceSpeedPOD': None, 
        'ShowNavigationSelection': 0, 
        'BacklightMode': None, 
        'UseIntervals': False, 
        'AutoPauseSpeed': 0, 
        'Tones': None, 
        'AutolapDistance': 100, 
        'Displays': 
                    [
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': 11516125, 
                                'Row': None
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': 11516163, 
                                'Row': None
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 37
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 41
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 40
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 39
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 68
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 10
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 38
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 49
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 50
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 48
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 52
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 53
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 51
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 56
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 57
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 54
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 59
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 12
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 58
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 4
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 20
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': 11516164, 
                                'Row': None
                            }
                    }
                    ], 
        'RuleIDs': 
                    [
                    11516125, 
                    11516163, 
                    11516164
                    ], 
        'UseCadencePOD': None, 
        'AutoscrollDelay': 10, 
        'UseInDevice': True, 
        'UseFootPOD': False, 
        'AutoPause': None, 
        'Interval1Distance': None, 
        'TapFunctionality': None, 
        'UseAutoscroll': False, 
        'AltiBaroMode': 1, 
        'Display': None, 
        'Name': 'Pool swimming', 
        'AutolapDistanceFootPOD': None, 
        'GPSInterval': 0, 
        'UseHRBelt': False
        }
        
        desc_dict = dict_get_pathstr_hierachy_description(currd)
        >>>pobj(desc_dict)
        {
        0: 
            {
            0: ''
            }, 
        1: 
            {
            0: 'Activity', 
            1: 'Interval1Time', 
            2: 'RecordingInterval', 
            3: 'UseAccelerometer', 
            4: 'Interval2Distance', 
            5: 'UseHRLimits', 
            6: 'UsePowerPOD', 
            7: 'HRLimitLow', 
            8: 'UseBikePOD', 
            9: 'AutolapDistanceBikePOD', 
            10: 'UseAutolap', 
            11: 'Interval2Time', 
            12: 'Ordinal', 
            13: 'SpeedLimitLow', 
            14: 'UseSpeedLimits', 
            15: 'LoggedRuleIDs', 
            16: 'AutomaticLogRecording', 
            17: '__type', 
            18: 'IntervalRepetitions', 
            19: 'SpeedLimitHigh', 
            20: 'HRLimitHigh', 
            21: 'Id', 
            22: 'AutolapDistanceSpeedPOD', 
            23: 'ShowNavigationSelection', 
            24: 'BacklightMode', 
            25: 'UseIntervals', 
            26: 'AutoPauseSpeed', 
            27: 'Tones', 
            28: 'AutolapDistance', 
            29: 'Displays', 
            30: 'RuleIDs', 
            31: 'UseCadencePOD', 
            32: 'AutoscrollDelay', 
            33: 'UseInDevice', 
            34: 'UseFootPOD', 
            35: 'AutoPause', 
            36: 'Interval1Distance', 
            37: 'TapFunctionality', 
            38: 'UseAutoscroll', 
            39: 'AltiBaroMode', 
            40: 'Display', 
            41: 'Name', 
            42: 'AutolapDistanceFootPOD', 
            43: 'GPSInterval', 
            44: 'UseHRBelt'
            }, 
        2: 
            {
            0: 'LoggedRuleIDs/0', 
            1: 'LoggedRuleIDs/1', 
            2: 'LoggedRuleIDs/2', 
            3: 'Displays/0', 
            4: 'Displays/1', 
            5: 'Displays/2', 
            6: 'Displays/3', 
            7: 'Displays/4', 
            8: 'Displays/5', 
            9: 'Displays/6', 
            10: 'Displays/7', 
            11: 'RuleIDs/0', 
            12: 'RuleIDs/1', 
            13: 'RuleIDs/2'
            }, 
        3: 
            {
            0: 'Displays/0/Type', 
            1: 'Displays/0/Row2', 
            2: 'Displays/0/RequiresHRBelt', 
            3: 'Displays/0/Views', 
            4: 'Displays/0/Row1', 
            5: 'Displays/1/Type', 
            6: 'Displays/1/Row2', 
            7: 'Displays/1/RequiresHRBelt', 
            8: 'Displays/1/Views', 
            9: 'Displays/1/Row1', 
            10: 'Displays/2/Type', 
            11: 'Displays/2/Row2', 
            12: 'Displays/2/RequiresHRBelt', 
            13: 'Displays/2/Views', 
            14: 'Displays/2/Row1', 
            15: 'Displays/3/Type', 
            16: 'Displays/3/Row2', 
            17: 'Displays/3/RequiresHRBelt', 
            18: 'Displays/3/Views', 
            19: 'Displays/3/Row1', 
            20: 'Displays/4/Type', 
            21: 'Displays/4/Row2', 
            22: 'Displays/4/RequiresHRBelt', 
            23: 'Displays/4/Views', 
            24: 'Displays/4/Row1', 
            25: 'Displays/5/Type', 
            26: 'Displays/5/Row2', 
            27: 'Displays/5/RequiresHRBelt', 
            28: 'Displays/5/Views', 
            29: 'Displays/5/Row1', 
            30: 'Displays/6/Type', 
            31: 'Displays/6/Row2', 
            32: 'Displays/6/RequiresHRBelt', 
            33: 'Displays/6/Views', 
            34: 'Displays/6/Row1', 
            35: 'Displays/7/Type', 
            36: 'Displays/7/Row2', 
            37: 'Displays/7/RequiresHRBelt', 
            38: 'Displays/7/Views', 
            39: 'Displays/7/Row1'
            }, 
        4: 
            {
            0: 'Displays/0/Row2/RuleID', 
            1: 'Displays/0/Row2/Row', 
            2: 'Displays/0/Views/0', 
            3: 'Displays/0/Row1/RuleID', 
            4: 'Displays/0/Row1/Row', 
            5: 'Displays/1/Row2/RuleID', 
            6: 'Displays/1/Row2/Row', 
            7: 'Displays/1/Views/0', 
            8: 'Displays/1/Row1/RuleID', 
            9: 'Displays/1/Row1/Row', 
            10: 'Displays/2/Row2/RuleID', 
            11: 'Displays/2/Row2/Row', 
            12: 'Displays/2/Views/0', 
            13: 'Displays/2/Row1/RuleID', 
            14: 'Displays/2/Row1/Row', 
            15: 'Displays/3/Row2/RuleID', 
            16: 'Displays/3/Row2/Row', 
            17: 'Displays/3/Views/0', 
            18: 'Displays/3/Row1/RuleID', 
            19: 'Displays/3/Row1/Row', 
            20: 'Displays/4/Row2/RuleID', 
            21: 'Displays/4/Row2/Row', 
            22: 'Displays/4/Views/0', 
            23: 'Displays/4/Row1/RuleID', 
            24: 'Displays/4/Row1/Row', 
            25: 'Displays/5/Row2/RuleID', 
            26: 'Displays/5/Row2/Row', 
            27: 'Displays/5/Views/0', 
            28: 'Displays/5/Row1/RuleID', 
            29: 'Displays/5/Row1/Row', 
            30: 'Displays/6/Row2/RuleID', 
            31: 'Displays/6/Row2/Row', 
            32: 'Displays/6/Views/0', 
            33: 'Displays/6/Row1/RuleID', 
            34: 'Displays/6/Row1/Row', 
            35: 'Displays/7/Row2/RuleID', 
            36: 'Displays/7/Row2/Row', 
            37: 'Displays/7/Views/0', 
            38: 'Displays/7/Row1/RuleID', 
            39: 'Displays/7/Row1/Row'
            }, 
        5: 
            {
            0: 'Displays/0/Views/0/RuleID', 
            1: 'Displays/0/Views/0/Row', 
            2: 'Displays/1/Views/0/RuleID', 
            3: 'Displays/1/Views/0/Row', 
            4: 'Displays/2/Views/0/RuleID', 
            5: 'Displays/2/Views/0/Row', 
            6: 'Displays/3/Views/0/RuleID', 
            7: 'Displays/3/Views/0/Row', 
            8: 'Displays/4/Views/0/RuleID', 
            9: 'Displays/4/Views/0/Row', 
            10: 'Displays/5/Views/0/RuleID', 
            11: 'Displays/5/Views/0/Row', 
            12: 'Displays/6/Views/0/RuleID', 
            13: 'Displays/6/Views/0/Row', 
            14: 'Displays/7/Views/0/RuleID', 
            15: 'Displays/7/Views/0/Row'
            }
        }

16. dict_get_partent_pathstr_hierachy_description_from_description_dict(description_dict)

        from xdict.utils import *
        from xdict.jprint import pobj
        >>> currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
        >>> pobj(currd)
        {
        'Activity': 6, 
        'Interval1Time': None, 
        'RecordingInterval': 1, 
        'UseAccelerometer': False, 
        'Interval2Distance': None, 
        'UseHRLimits': False, 
        'UsePowerPOD': False, 
        'HRLimitLow': 125, 
        'UseBikePOD': False, 
        'AutolapDistanceBikePOD': None, 
        'UseAutolap': True, 
        'Interval2Time': None, 
        'Ordinal': 2, 
        'SpeedLimitLow': None, 
        'UseSpeedLimits': None, 
        'LoggedRuleIDs': 
                        [
                        11516163, 
                        11516164, 
                        11516125
                        ], 
        'AutomaticLogRecording': None, 
        '__type': 'Suunto.BLL.CustomMode', 
        'IntervalRepetitions': 0, 
        'SpeedLimitHigh': None, 
        'HRLimitHigh': 165, 
        'Id': 13336645, 
        'AutolapDistanceSpeedPOD': None, 
        'ShowNavigationSelection': 0, 
        'BacklightMode': None, 
        'UseIntervals': False, 
        'AutoPauseSpeed': 0, 
        'Tones': None, 
        'AutolapDistance': 100, 
        'Displays': 
                    [
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': 11516125, 
                                'Row': None
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': 11516163, 
                                'Row': None
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 37
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 41
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 40
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 39
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 68
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 10
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 38
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 49
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 50
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 48
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 52
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 53
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 51
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 56
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 57
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 54
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 59
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 12
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': None, 
                                'Row': 58
                            }
                    }, 
                    {
                    'Type': 5, 
                    'Row2': 
                            {
                                'RuleID': None, 
                                'Row': 4
                            }, 
                    'RequiresHRBelt': None, 
                    'Views': 
                                [
                                {
                                'RuleID': None, 
                                'Row': 20
                                }
                                ], 
                    'Row1': 
                            {
                                'RuleID': 11516164, 
                                'Row': None
                            }
                    }
                    ], 
        'RuleIDs': 
                    [
                    11516125, 
                    11516163, 
                    11516164
                    ], 
        'UseCadencePOD': None, 
        'AutoscrollDelay': 10, 
        'UseInDevice': True, 
        'UseFootPOD': False, 
        'AutoPause': None, 
        'Interval1Distance': None, 
        'TapFunctionality': None, 
        'UseAutoscroll': False, 
        'AltiBaroMode': 1, 
        'Display': None, 
        'Name': 'Pool swimming', 
        'AutolapDistanceFootPOD': None, 
        'GPSInterval': 0, 
        'UseHRBelt': False
        }
        >>> phd = dict_get_pathstr_hierachy_description(currd)
        >>> pphd = dict_get_partent_pathstr_hierachy_description_from_description_dict(phd)
        >>> pobj(pphd)
        {
        0: 
            {
            0: -1
            }, 
        1: 
            {
            0: 0, 
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0, 
            7: 0, 
            8: 0, 
            9: 0, 
            10: 0, 
            11: 0, 
            12: 0, 
            13: 0, 
            14: 0, 
            15: 0, 
            16: 0, 
            17: 0, 
            18: 0, 
            19: 0, 
            20: 0, 
            21: 0, 
            22: 0, 
            23: 0, 
            24: 0, 
            25: 0, 
            26: 0, 
            27: 0, 
            28: 0, 
            29: 0, 
            30: 0, 
            31: 0, 
            32: 0, 
            33: 0, 
            34: 0, 
            35: 0, 
            36: 0, 
            37: 0, 
            38: 0, 
            39: 0, 
            40: 0, 
            41: 0, 
            42: 0, 
            43: 0, 
            44: 0
            }, 
        2: 
            {
            0: 15, 
            1: 15, 
            2: 15, 
            3: 29, 
            4: 29, 
            5: 29, 
            6: 29, 
            7: 29, 
            8: 29, 
            9: 29, 
            10: 29, 
            11: 30, 
            12: 30, 
            13: 30
            }, 
        3: 
            {
            0: 3, 
            1: 3, 
            2: 3, 
            3: 3, 
            4: 3, 
            5: 4, 
            6: 4, 
            7: 4, 
            8: 4, 
            9: 4, 
            10: 5, 
            11: 5, 
            12: 5, 
            13: 5, 
            14: 5, 
            15: 6, 
            16: 6, 
            17: 6, 
            18: 6, 
            19: 6, 
            20: 7, 
            21: 7, 
            22: 7, 
            23: 7, 
            24: 7, 
            25: 8, 
            26: 8, 
            27: 8, 
            28: 8, 
            29: 8, 
            30: 9, 
            31: 9, 
            32: 9, 
            33: 9, 
            34: 9, 
            35: 10, 
            36: 10, 
            37: 10, 
            38: 10, 
            39: 10
            }, 
        4: 
            {
            0: 1, 
            1: 1, 
            2: 3, 
            3: 4, 
            4: 4, 
            5: 6, 
            6: 6, 
            7: 8, 
            8: 9, 
            9: 9, 
            10: 11, 
            11: 11, 
            12: 13, 
            13: 14, 
            14: 14, 
            15: 16, 
            16: 16, 
            17: 18, 
            18: 19, 
            19: 19, 
            20: 21, 
            21: 21, 
            22: 23, 
            23: 24, 
            24: 24, 
            25: 26, 
            26: 26, 
            27: 28, 
            28: 29, 
            29: 29, 
            30: 31, 
            31: 31, 
            32: 33, 
            33: 34, 
            34: 34, 
            35: 36, 
            36: 36, 
            37: 38, 
            38: 39, 
            39: 39
            }, 
        5: 
            {
            0: 2, 
            1: 2, 
            2: 7, 
            3: 7, 
            4: 12, 
            5: 12, 
            6: 17, 
            7: 17, 
            8: 22, 
            9: 22, 
            10: 27, 
            11: 27, 
            12: 32, 
            13: 32, 
            14: 37, 
            15: 37
            }
        }
        >>> 

17. dict_get_tree_pathstr_hierachy_description(currd,**kwargs)

        from xdict.utils import *
        from xdict.jprint import pobj
        currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
        hierachy_desc = dict_get_tree_pathstr_hierachy_description(currd)
        hierachy_desc.keys()
        print(hierachy_desc['text'])
        pobj(hierachy_desc['parent_dict'])
        pobj(hierachy_desc['description_dict'])
        
        
        
        >>> print(hierachy_desc['text'])
        
        
            UseHRLimits
            UseSpeedLimits
            LoggedRuleIDs
                LoggedRuleIDs/0
                LoggedRuleIDs/1
                LoggedRuleIDs/2
            Interval1Distance
            UseAutoscroll
            Id
            Ordinal
            UseAutolap
            SpeedLimitHigh
            Displays
                Displays/0
                    Displays/0/RequiresHRBelt
                    Displays/0/Row2
                        Displays/0/Row2/RuleID
                        Displays/0/Row2/Row
                    Displays/0/Views
                        Displays/0/Views/0
                            Displays/0/Views/0/RuleID
                            Displays/0/Views/0/Row
                    Displays/0/Row1
                        Displays/0/Row1/RuleID
                        Displays/0/Row1/Row
                    Displays/0/Type
                Displays/1
                    Displays/1/RequiresHRBelt
                    Displays/1/Row2
                        Displays/1/Row2/RuleID
                        Displays/1/Row2/Row
                    Displays/1/Views
                        Displays/1/Views/0
                            Displays/1/Views/0/RuleID
                            Displays/1/Views/0/Row
                    Displays/1/Row1
                        Displays/1/Row1/RuleID
                        Displays/1/Row1/Row
                    Displays/1/Type
                Displays/2
                    Displays/2/RequiresHRBelt
                    Displays/2/Row2
                        Displays/2/Row2/RuleID
                        Displays/2/Row2/Row
                    Displays/2/Views
                        Displays/2/Views/0
                            Displays/2/Views/0/RuleID
                            Displays/2/Views/0/Row
                    Displays/2/Row1
                        Displays/2/Row1/RuleID
                        Displays/2/Row1/Row
                    Displays/2/Type
                Displays/3
                    Displays/3/RequiresHRBelt
                    Displays/3/Row2
                        Displays/3/Row2/RuleID
                        Displays/3/Row2/Row
                    Displays/3/Views
                        Displays/3/Views/0
                            Displays/3/Views/0/RuleID
                            Displays/3/Views/0/Row
                    Displays/3/Row1
                        Displays/3/Row1/RuleID
                        Displays/3/Row1/Row
                    Displays/3/Type
                Displays/4
                    Displays/4/RequiresHRBelt
                    Displays/4/Row2
                        Displays/4/Row2/RuleID
                        Displays/4/Row2/Row
                    Displays/4/Views
                        Displays/4/Views/0
                            Displays/4/Views/0/RuleID
                            Displays/4/Views/0/Row
                    Displays/4/Row1
                        Displays/4/Row1/RuleID
                        Displays/4/Row1/Row
                    Displays/4/Type
                Displays/5
                    Displays/5/RequiresHRBelt
                    Displays/5/Row2
                        Displays/5/Row2/RuleID
                        Displays/5/Row2/Row
                    Displays/5/Views
                        Displays/5/Views/0
                            Displays/5/Views/0/RuleID
                            Displays/5/Views/0/Row
                    Displays/5/Row1
                        Displays/5/Row1/RuleID
                        Displays/5/Row1/Row
                    Displays/5/Type
                Displays/6
                    Displays/6/RequiresHRBelt
                    Displays/6/Row2
                        Displays/6/Row2/RuleID
                        Displays/6/Row2/Row
                    Displays/6/Views
                        Displays/6/Views/0
                            Displays/6/Views/0/RuleID
                            Displays/6/Views/0/Row
                    Displays/6/Row1
                        Displays/6/Row1/RuleID
                        Displays/6/Row1/Row
                    Displays/6/Type
                Displays/7
                    Displays/7/RequiresHRBelt
                    Displays/7/Row2
                        Displays/7/Row2/RuleID
                        Displays/7/Row2/Row
                    Displays/7/Views
                        Displays/7/Views/0
                            Displays/7/Views/0/RuleID
                            Displays/7/Views/0/Row
                    Displays/7/Row1
                        Displays/7/Row1/RuleID
                        Displays/7/Row1/Row
                    Displays/7/Type
            UseIntervals
            GPSInterval
            __type
            AutolapDistanceSpeedPOD
            AutoPauseSpeed
            UseInDevice
            TapFunctionality
            UseCadencePOD
            HRLimitLow
            ShowNavigationSelection
            UseAccelerometer
            HRLimitHigh
            SpeedLimitLow
            Interval2Time
            Interval1Time
            AutomaticLogRecording
            AutoPause
            UseHRBelt
            UseFootPOD
            UseBikePOD
            AutolapDistanceFootPOD
            Interval2Distance
            AutoscrollDelay
            BacklightMode
            Activity
            RuleIDs
                RuleIDs/0
                RuleIDs/1
                RuleIDs/2
            Display
            Name
            RecordingInterval
            AltiBaroMode
            UsePowerPOD
            Tones
            AutolapDistanceBikePOD
            IntervalRepetitions
            AutolapDistance
        >>>



        >>> pobj(hierachy_desc['parent_dict'])
        {
        0: 
            {
            0: -1
            }, 
        1: 
            {
            0: 0, 
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0, 
            7: 0, 
            8: 0, 
            9: 0, 
            10: 0, 
            11: 0, 
            12: 0, 
            13: 0, 
            14: 0, 
            15: 0, 
            16: 0, 
            17: 0, 
            18: 0, 
            19: 0, 
            20: 0, 
            21: 0, 
            22: 0, 
            23: 0, 
            24: 0, 
            25: 0, 
            26: 0, 
            27: 0, 
            28: 0, 
            29: 0, 
            30: 0, 
            31: 0, 
            32: 0, 
            33: 0, 
            34: 0, 
            35: 0, 
            36: 0, 
            37: 0, 
            38: 0, 
            39: 0, 
            40: 0, 
            41: 0, 
            42: 0, 
            43: 0, 
            44: 0
            }, 
        2: 
            {
            0: 2, 
            1: 2, 
            2: 2, 
            3: 9, 
            4: 9, 
            5: 9, 
            6: 9, 
            7: 9, 
            8: 9, 
            9: 9, 
            10: 9, 
            11: 35, 
            12: 35, 
            13: 35
            }, 
        3: 
            {
            0: 3, 
            1: 3, 
            2: 3, 
            3: 3, 
            4: 3, 
            5: 4, 
            6: 4, 
            7: 4, 
            8: 4, 
            9: 4, 
            10: 5, 
            11: 5, 
            12: 5, 
            13: 5, 
            14: 5, 
            15: 6, 
            16: 6, 
            17: 6, 
            18: 6, 
            19: 6, 
            20: 7, 
            21: 7, 
            22: 7, 
            23: 7, 
            24: 7, 
            25: 8, 
            26: 8, 
            27: 8, 
            28: 8, 
            29: 8, 
            30: 9, 
            31: 9, 
            32: 9, 
            33: 9, 
            34: 9, 
            35: 10, 
            36: 10, 
            37: 10, 
            38: 10, 
            39: 10
            }, 
        4: 
            {
            0: 1, 
            1: 1, 
            2: 2, 
            3: 3, 
            4: 3, 
            5: 6, 
            6: 6, 
            7: 7, 
            8: 8, 
            9: 8, 
            10: 11, 
            11: 11, 
            12: 12, 
            13: 13, 
            14: 13, 
            15: 16, 
            16: 16, 
            17: 17, 
            18: 18, 
            19: 18, 
            20: 21, 
            21: 21, 
            22: 22, 
            23: 23, 
            24: 23, 
            25: 26, 
            26: 26, 
            27: 27, 
            28: 28, 
            29: 28, 
            30: 31, 
            31: 31, 
            32: 32, 
            33: 33, 
            34: 33, 
            35: 36, 
            36: 36, 
            37: 37, 
            38: 38, 
            39: 38
            }, 
        5: 
            {
            0: 2, 
            1: 2, 
            2: 7, 
            3: 7, 
            4: 12, 
            5: 12, 
            6: 17, 
            7: 17, 
            8: 22, 
            9: 22, 
            10: 27, 
            11: 27, 
            12: 32, 
            13: 32, 
            14: 37, 
            15: 37
            }
        }
        >>> 




        >>> hierachy_desc['deep_search_path']
        [(0, 0), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 3), (3, 0), (3, 1), (4, 0), (4, 1), (3, 2), (4, 2), (5, 0), (5, 1), (3, 3), (4, 3), (4, 4), (3, 4), (2, 4), (3, 5), (3, 6), (4, 5), (4, 6), (3, 7), (4, 7), (5, 2), (5, 3), (3, 8), (4, 8), (4, 9), (3, 9), (2, 5), (3, 10), (3, 11), (4, 10), (4, 11), (3, 12), (4, 12), (5, 4), (5, 5), (3, 13), (4, 13), (4, 14), (3, 14), (2, 6), (3, 15), (3, 16), (4, 15), (4, 16), (3, 17), (4, 17), (5, 6), (5, 7), (3, 18), (4, 18), (4, 19), (3, 19), (2, 7), (3, 20), (3, 21), (4, 20), (4, 21), (3, 22), (4, 22), (5, 8), (5, 9), (3, 23), (4, 23), (4, 24), (3, 24), (2, 8), (3, 25), (3, 26), (4, 25), (4, 26), (3, 27), (4, 27), (5, 10), (5, 11), (3, 28), (4, 28), (4, 29), (3, 29), (2, 9), (3, 30), (3, 31), (4, 30), (4, 31), (3, 32), (4, 32), (5, 12), (5, 13), (3, 33), (4, 33), (4, 34), (3, 34), (2, 10), (3, 35), (3, 36), (4, 35), (4, 36), (3, 37), (4, 37), (5, 14), (5, 15), (3, 38), (4, 38), (4, 39), (3, 39), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (1, 26), (1, 27), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (1, 33), (1, 34), (1, 35), (2, 11), (2, 12), (2, 13), (1, 36), (1, 37), (1, 38), (1, 39), (1, 40), (1, 41), (1, 42), (1, 43), (1, 44)]
        >>> 


        >>> pobj(hierachy_desc['description_dict'])
        {
        0: 
            {
            0: ''
            }, 
        1: 
            {
            0: 'UseHRLimits', 
            1: 'UseSpeedLimits', 
            2: 'LoggedRuleIDs', 
            3: 'Interval1Distance', 
            4: 'UseAutoscroll', 
            5: 'Id', 
            6: 'Ordinal', 
            7: 'UseAutolap', 
            8: 'SpeedLimitHigh', 
            9: 'Displays', 
            10: 'UseIntervals', 
            11: 'GPSInterval', 
            12: '__type', 
            13: 'AutolapDistanceSpeedPOD', 
            14: 'AutoPauseSpeed', 
            15: 'UseInDevice', 
            16: 'TapFunctionality', 
            17: 'UseCadencePOD', 
            18: 'HRLimitLow', 
            19: 'ShowNavigationSelection', 
            20: 'UseAccelerometer', 
            21: 'HRLimitHigh', 
            22: 'SpeedLimitLow', 
            23: 'Interval2Time', 
            24: 'Interval1Time', 
            25: 'AutomaticLogRecording', 
            26: 'AutoPause', 
            27: 'UseHRBelt', 
            28: 'UseFootPOD', 
            29: 'UseBikePOD', 
            30: 'AutolapDistanceFootPOD', 
            31: 'Interval2Distance', 
            32: 'AutoscrollDelay', 
            33: 'BacklightMode', 
            34: 'Activity', 
            35: 'RuleIDs', 
            36: 'Display', 
            37: 'Name', 
            38: 'RecordingInterval', 
            39: 'AltiBaroMode', 
            40: 'UsePowerPOD', 
            41: 'Tones', 
            42: 'AutolapDistanceBikePOD', 
            43: 'IntervalRepetitions', 
            44: 'AutolapDistance'
            }, 
        2: 
            {
            0: 'LoggedRuleIDs/0', 
            1: 'LoggedRuleIDs/1', 
            2: 'LoggedRuleIDs/2', 
            3: 'Displays/0', 
            4: 'Displays/1', 
            5: 'Displays/2', 
            6: 'Displays/3', 
            7: 'Displays/4', 
            8: 'Displays/5', 
            9: 'Displays/6', 
            10: 'Displays/7', 
            11: 'RuleIDs/0', 
            12: 'RuleIDs/1', 
            13: 'RuleIDs/2'
            }, 
        3: 
            {
            0: 'Displays/0/RequiresHRBelt', 
            1: 'Displays/0/Row2', 
            2: 'Displays/0/Views', 
            3: 'Displays/0/Row1', 
            4: 'Displays/0/Type', 
            5: 'Displays/1/RequiresHRBelt', 
            6: 'Displays/1/Row2', 
            7: 'Displays/1/Views', 
            8: 'Displays/1/Row1', 
            9: 'Displays/1/Type', 
            10: 'Displays/2/RequiresHRBelt', 
            11: 'Displays/2/Row2', 
            12: 'Displays/2/Views', 
            13: 'Displays/2/Row1', 
            14: 'Displays/2/Type', 
            15: 'Displays/3/RequiresHRBelt', 
            16: 'Displays/3/Row2', 
            17: 'Displays/3/Views', 
            18: 'Displays/3/Row1', 
            19: 'Displays/3/Type', 
            20: 'Displays/4/RequiresHRBelt', 
            21: 'Displays/4/Row2', 
            22: 'Displays/4/Views', 
            23: 'Displays/4/Row1', 
            24: 'Displays/4/Type', 
            25: 'Displays/5/RequiresHRBelt', 
            26: 'Displays/5/Row2', 
            27: 'Displays/5/Views', 
            28: 'Displays/5/Row1', 
            29: 'Displays/5/Type', 
            30: 'Displays/6/RequiresHRBelt', 
            31: 'Displays/6/Row2', 
            32: 'Displays/6/Views', 
            33: 'Displays/6/Row1', 
            34: 'Displays/6/Type', 
            35: 'Displays/7/RequiresHRBelt', 
            36: 'Displays/7/Row2', 
            37: 'Displays/7/Views', 
            38: 'Displays/7/Row1', 
            39: 'Displays/7/Type'
            }, 
        4: 
            {
            0: 'Displays/0/Row2/RuleID', 
            1: 'Displays/0/Row2/Row', 
            2: 'Displays/0/Views/0', 
            3: 'Displays/0/Row1/RuleID', 
            4: 'Displays/0/Row1/Row', 
            5: 'Displays/1/Row2/RuleID', 
            6: 'Displays/1/Row2/Row', 
            7: 'Displays/1/Views/0', 
            8: 'Displays/1/Row1/RuleID', 
            9: 'Displays/1/Row1/Row', 
            10: 'Displays/2/Row2/RuleID', 
            11: 'Displays/2/Row2/Row', 
            12: 'Displays/2/Views/0', 
            13: 'Displays/2/Row1/RuleID', 
            14: 'Displays/2/Row1/Row', 
            15: 'Displays/3/Row2/RuleID', 
            16: 'Displays/3/Row2/Row', 
            17: 'Displays/3/Views/0', 
            18: 'Displays/3/Row1/RuleID', 
            19: 'Displays/3/Row1/Row', 
            20: 'Displays/4/Row2/RuleID', 
            21: 'Displays/4/Row2/Row', 
            22: 'Displays/4/Views/0', 
            23: 'Displays/4/Row1/RuleID', 
            24: 'Displays/4/Row1/Row', 
            25: 'Displays/5/Row2/RuleID', 
            26: 'Displays/5/Row2/Row', 
            27: 'Displays/5/Views/0', 
            28: 'Displays/5/Row1/RuleID', 
            29: 'Displays/5/Row1/Row', 
            30: 'Displays/6/Row2/RuleID', 
            31: 'Displays/6/Row2/Row', 
            32: 'Displays/6/Views/0', 
            33: 'Displays/6/Row1/RuleID', 
            34: 'Displays/6/Row1/Row', 
            35: 'Displays/7/Row2/RuleID', 
            36: 'Displays/7/Row2/Row', 
            37: 'Displays/7/Views/0', 
            38: 'Displays/7/Row1/RuleID', 
            39: 'Displays/7/Row1/Row'
            }, 
        5: 
            {
            0: 'Displays/0/Views/0/RuleID', 
            1: 'Displays/0/Views/0/Row', 
            2: 'Displays/1/Views/0/RuleID', 
            3: 'Displays/1/Views/0/Row', 
            4: 'Displays/2/Views/0/RuleID', 
            5: 'Displays/2/Views/0/Row', 
            6: 'Displays/3/Views/0/RuleID', 
            7: 'Displays/3/Views/0/Row', 
            8: 'Displays/4/Views/0/RuleID', 
            9: 'Displays/4/Views/0/Row', 
            10: 'Displays/5/Views/0/RuleID', 
            11: 'Displays/5/Views/0/Row', 
            12: 'Displays/6/Views/0/RuleID', 
            13: 'Displays/6/Views/0/Row', 
            14: 'Displays/7/Views/0/RuleID', 
            15: 'Displays/7/Views/0/Row'
            }
        }
        >>> 
        

18. dict_update_just_intersection(dict1,dict2)
        
        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> dict1 = {1:'a',2:'b',3:'c',4:'d'}
        >>> dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        >>> dict_update_just_intersection(dict1,dict2)
        {1: 'a', 2: 'v', 3: 'w', 4: 'd'}
        >>> pobj(dict1)
        {
        1: 'a', 
        2: 'v', 
        3: 'w', 
        4: 'd'
        }
        >>> pobj(dict2)
        {
        2: 'v', 
        3: 'w', 
        5: 'u', 
        6: 'x', 
        7: 'y'
        }
        >>> 

19. dict_uniqualize(d)

        >>> 
        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> dict1 = {1:'a',2:'b',3:'c',4:'b'}
        >>> dict_uniqualize(dict1)
        {1: 'a', 2: 'b', 3: 'c'}
        >>> 
        
20. dict_extend(dict1,dict2,**kwargs)


         >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> dict1 = {1:'a',2:'b',3:'c',4:'d'}
        >>> dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        >>> dict_extend(dict1,dict2)
        {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'u', 6: 'x', 7: 'y'}
        >>> pobj(dict1)
        {
        1: 'a', 
        2: 'b', 
        3: 'c', 
        4: 'd'
        }
        >>> pobj(dict2)
        {
        2: 'v', 
        3: 'w', 
        5: 'u', 
        6: 'x', 
        7: 'y'
        }
        >>> dict1 = {1:'a',2:'b',3:'c',4:'d'}
        >>> dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        >>> dict_extend(dict1,dict2,overwrite=1)
        {1: 'a', 2: 'v', 3: 'w', 4: 'd', 5: 'u', 6: 'x', 7: 'y'}
        >>> pobj(dict1)
        {
        1: 'a', 
        2: 'b', 
        3: 'c', 
        4: 'd'
        }
        >>> pobj(dict2)
        {
        2: 'v', 
        3: 'w', 
        5: 'u', 
        6: 'x', 
        7: 'y'
        }
        >>>
       

21. dict_comprise(dict1,dict2)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> dict1 = {'a':1,'b':2,'c':3,'d':4}        
        >>> dict2 = {'b':2,'c':3}
        >>> dict_comprise(dict1,dict2)
        True
        >>> 

 22.dict_get_value_keys_description(d)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> dict1 = {'a':1,'b':2,'c':2,'d':4}
        >>> dict_get_value_keys_description(dict1)
        {1: ['a'], 2: ['b', 'c'], 4: ['d']}
        >>> 

23. dict_print_tree_pathstr_with_dynamic_indent(currd,**kwargs)  

        >>> 
        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
        >>> s = dict_print_tree_pathstr_with_dynamic_indent(currd)
        >>> print(s)
        
        
        Display
        Interval2Distance
        Id
        UseBikePOD
        SpeedLimitLow
        UseAccelerometer
        Displays
                0
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
                1
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
                2
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
                3
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
                4
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
                5
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
                6
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
                7
                Views
                    0
                    Row
                    RuleID
                RequiresHRBelt
                Row2
                    Row
                    RuleID
                Row1
                    Row
                    RuleID
                Type
        UseInDevice
        HRLimitLow
        UseAutoscroll
        Interval2Time
        Interval1Distance
        AutolapDistanceSpeedPOD
        Interval1Time
        AutolapDistance
        UseHRLimits
        UseSpeedLimits
        GPSInterval
        UsePowerPOD
        AutoscrollDelay
        RuleIDs
            0
            1
            2
        AutomaticLogRecording
        Tones
        __type
        AutoPause
        BacklightMode
        Activity
        RecordingInterval
        IntervalRepetitions
        Name
        UseHRBelt
        UseAutolap
        ShowNavigationSelection
        SpeedLimitHigh
        AutolapDistanceBikePOD
        Ordinal
        LoggedRuleIDs
                    0
                    1
                    2
        AutolapDistanceFootPOD
        HRLimitHigh
        TapFunctionality
        UseIntervals
        UseFootPOD
        AutoPauseSpeed
        UseCadencePOD
        AltiBaroMode
        >>> 

24. dict_get_max_wordwidth(myDict)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> currd = {0:'AutoPauseSpeed', 125:'HRLimitLow', 6:'Activity'}
        >>> dict_get_max_wordwidth(currd)
        14
        >>> 
        
25. dict_get_max_word_displaywidth(myDict)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> currd = {0:'你们大家好', 125:'ABCDE', 6:'1234567'}
        >>> dict_get_max_word_displaywidth(currd)
        10
        >>> 




## list  

1. list_creat_default_with_len(len,default_element=None)  

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = list_creat_default_with_len(5)
        >>> pobj(l)
        [
        None, 
        None, 
        None, 
        None, 
        None
        ]
        >>> 


2. list_setitem_via_path_list(l,path_list,**kwargs)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b']]
        >>> path_list = [1,0]
        >>> list_setitem_via_path_list(l,path_list,'x')
        ['a', ['x']]
        >>> pobj(l)
        [
        'a', 
        [
        'x'
        ]
        ]
        >>> 

3. list_getitem_via_path_list(l,path_list,**kwargs)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b']]
        >>> path_list = [1,0]
        >>> list_getitem_via_path_list(l,path_list)
        'b'
        >>> 
        
4. list_getitem_via_cmd(l,cmd,**kwargs)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b']]
        >>> cmd = '1 0'
        >>> list_getitem_via_cmd(l,cmd)
        'b'
        >>> pobj(l)
        [
        'a', 
        [
        'b'
        ]
        ]
        >>> 


5. list_delitem_via_path_list(l,path_list,**kwargs)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b']]
        >>> path_list = [1,0]
        >>> list_delitem_via_path_list(l,path_list)
        ['a', []]
        >>> pobj(l)
        [
        'a', 
        []
        ]
        >>> 

6. list_getitem_via_pathstr(l,pathstr,**kwargs)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b']]
        >>> pathstr = '1/0'
        >>> list_getitem_via_pathstr(l,pathstr)
        'b'
        >>> 

7.  list_get_all_sons_pathstrs(l,full_key_path,**kwargs)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b',['x','y']],'c']
        >>> list_get_all_sons_pathstrs(l,'')
        ['0', '1', '2']
        >>> list_get_all_sons_pathstrs(l,'1')
        ['1/0', '1/1']
        >>> list_get_all_sons_pathstrs(l,'1/1')
        ['1/1/0', '1/1/1']
        >>> 

8.  list_include_pathlist(l,path_list,**kwargs)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b',['x','y']],'c']
        >>> list_include_pathlist(l,[1,1,1])
        True
        >>> 
        

9. list_find_keys_via_value(l,value,**kwargs)
 
        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b',['x','b']],'b']
        >>> list_find_keys_via_value(l,'b')
        [[2], [1, 0], [1, 1, 1]]
        >>> 
        
        
10.  list_find_keys_via_value_non_recursive(l,value,**kwargs)  

                >>> from xdict.utils import *  
                >>> from xdict.jprint import pobj
                >>> l = ['a',['b',['x','b']],'b']
                >>> list_find_keys_via_value_non_recursive(l,'b')
                [[2]]
                >>> 
                
11. list_get_pathstr_hierachy_description(l,**kwargs)  

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b',['x','b']],'b']
        >>> desc = list_get_pathstr_hierachy_description(l)
        >>> pobj(desc)
        {
        0: 
            {
            0: ''
            }, 
        1: 
            {
            0: '0', 
            1: '1', 
            2: '2'
            }, 
        2: 
            {
            0: '1/0', 
            1: '1/1'
            }, 
        3: 
            {
            0: '1/1/0', 
            1: '1/1/1'
            }
        }
        >>> 

12. list_get_partent_pathstr_hierachy_description_from_description_dict(desc)

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b',['x','b']],'b']
        >>> desc = list_get_pathstr_hierachy_description(l)
        >>> pobj(desc)
        {
        0: 
            {
            0: ''
            }, 
        1: 
            {
            0: '0', 
            1: '1', 
            2: '2'
            }, 
        2: 
            {
            0: '1/0', 
            1: '1/1'
            }, 
        3: 
            {
            0: '1/1/0', 
            1: '1/1/1'
            }
        }
        >>> ppdesc = list_get_partent_pathstr_hierachy_description_from_description_dict(desc)
        >>> pobj(ppdesc)
        {
        0: 
            {
            0: -1
            }, 
        1: 
            {
            0: 0, 
            1: 0, 
            2: 0
            }, 
        2: 
            {
            0: 1, 
            1: 1
            }, 
        3: 
            {
            0: 1, 
            1: 1
            }
        }
        >>> 
        
13. list_get_tree_pathstr_hierachy_description(l,**kwargs)

        >>> 
        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b',['x','b']],'b']
        >>> desc = list_get_tree_pathstr_hierachy_description(l)
        >>> desc.keys()
        dict_keys(['parent_dict', 'deep_search_path', 'description_dict', 'text'])
        >>> pobj(desc['parent_dict'])
        {
        0: 
            {
            0: -1
            }, 
        1: 
            {
            0: 0, 
            1: 0, 
            2: 0
            }, 
        2: 
            {
            0: 1, 
            1: 1
            }, 
        3: 
            {
            0: 1, 
            1: 1
            }
        }
        >>> pobj(desc['deep_search_path'],fixed_indent=1)
        [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (1, 2)]
        >>> pobj(desc['description_dict'])
        {
        0: 
            {
            0: ''
            }, 
        1: 
            {
            0: '0', 
            1: '1', 
            2: '2'
            }, 
        2: 
            {
            0: '1/0', 
            1: '1/1'
            }, 
        3: 
            {
            0: '1/1/0', 
            1: '1/1/1'
            }
        }
        >>> print(desc['text'])
        
        
            0
            1
                1/0
                1/1
                    1/1/0
                    1/1/1
            2
        >>> 
        
14. list_get_value_indexes_description(l)  

        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a','b','b','a','c','b']
        >>> list_get_value_indexes_description(l)
        {'a': [0, 3], 'b': [1, 2, 5], 'c': [4]}
        >>> 

15. list_print_tree_pathstr_with_dynamic_indent(l,**kwargs)

        >>> 
        >>> from xdict.utils import *
        >>> from xdict.jprint import pobj
        >>> l = ['a',['b',['x','b']],'b']
        >>> s = list_print_tree_pathstr_with_dynamic_indent(l)
        >>> print(s)
        
        
        0
        1
        0
        1
        0
        1
        2
        >>> 
        
        
 16. list_uniqualize(l)  
                
                >>> l = [1, 2, 2]
                >>> list_uniqualize(l)
                [1, 2]
                >>> l
                [1, 2, 2]
                >>> 
                
17. list_comprise(list1,list2,**kwargs)

        >>> list_comprise([1,2,3,4,5],[2,3,4],strict=0)
        True
        >>> list_comprise([1,2,3,4,5],[2,3,4])
        True
        >>> list_comprise([1,2,3,4,5],[2,3,4],strict=1)
        False
        >>> list_comprise([1,2,3,4,5],[1,2,3,4],strict=1)
        True
        >>> 
        
18. list_get_max_wordwidth(l)

        >>> l = ['a','bb','hello','xx','你好吗']
        >>> list_get_max_wordwidth(l)
        5
        >>> 
        
19. list_get_max_word_displaywidth(l)

        >>> l = ['a','bb','hello','xx','你好吗']
        >>> list_get_max_word_displaywidth(l)
        6
        
        




## bitmap
1. bitmaplist_to_num(bitmaplist)  

        >>> bitmaplist_to_num([1, 0, 1, 0])
        5
        >>> bitmaplist_to_num([1, 0, 1, 0],bigend=1)
        10
        >>> 

2. num_to_bitmaplist(num,bitmap_size)   
 
        >>> 
        >>> num_to_bitmaplist(10)
        [0, 1, 0, 1]
        >>> num_to_bitmaplist(10,size=6)
        [0, 1, 0, 1, 0, 0]
        >>> num_to_bitmaplist(10,bigend=1)
        [1, 0, 1, 0]
        >>> num_to_bitmaplist(10,bigend=1,size=6)

3. bitmaplist_bitsum(bitmaplist)  

        >>> bitmaplist_bitsum([1,0,1])
        2
        >>> bitmaplist_bitsum([1,0,1,0])
        2
        >>> 


4. subset_bitmap(n,k,**kwargs) 

        >>> pobj(subset_bitmap(3,1),fixed_indent=1)
        {
            0: [1, 0, 0],
            1: [0, 1, 0],
            2: [0, 0, 1]
        }
        >>> pobj(subset_bitmap(4,2),fixed_indent=1)
        {
            0: [1, 1, 0, 0],
            1: [1, 0, 1, 0],
            2: [0, 1, 1, 0],
            3: [1, 0, 0, 1],
            4: [0, 1, 0, 1],
            5: [0, 0, 1, 1]
        }
        >>> 


5. bitmap_contain(bm1,bm2)  

        >>> bitmaplist_contain([1,0,1,0],[0,0,0,0])
        True
        >>> bitmaplist_contain([1,0,1,0],[0,0,1,0])
        True
        >>> bitmaplist_contain([1,0,1,0],[1,0,0,0])
        True
        >>> bitmaplist_contain([1,0,1,0],[1,0,1,0])
        True
        >>> bitmaplist_contain([1,0,1,0],[0,0,0,1])
        False
        >>> 




