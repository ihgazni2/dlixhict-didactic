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

3. dict_getitem_via_path_list(external_dict,path_list,**kwargs)

4. dict_getitem_via_cmd(external_dict,cmd_str,**kwargs)

5. dict_getitem_via_pathstr(d,full_key_path,**kwargs)

6. dict_delitem_via_path_list(external_dict,path_list,**kwargs)


## list

## bitmap
1. bitmaplist_to_num(bitmaplist)
2. num_to_bitmaplist(num,bitmap_size)
3. bitmaplist_bitsum(bitmaplist)
4. subset_bitmap(n,k)  
5. bitmap_contain(bm1,bm2)  





