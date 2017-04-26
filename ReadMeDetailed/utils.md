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
22. is_number_str(old_index):
23. get_obj_type_name(obj)
-----------------------------------------------------------------------------------------------------------------------

##path string
-----------------------------------------------------------------------------------------------------------------------
1. path_string_is_slash_end(path_string,delimiter='/')
2. path_string_get_head(path_string,delimiter='/')
3. path_string_get_tail(path_string,delimiter='/')
4. path_string_to_path_list(path_str,**kwargs)
5. path_string_is_parent(parent,son,**kwargs)
6. path_string_is_leaf(leaf,path_str,**kwargs)
7. path_string_get_parent(son,**kwargs)
8. path_string_get_leaf(absp,**kwargs)
-----------------------------------------------------------------------------------------------------------------------

##path list
-----------------------------------------------------------------------------------------------------------------------
1. path_list_to_path_string(path_list,**kwargs)
2. path_list_is_parent(parent_pl,son_pl)
3. path_list_is_son(son_pl,parent_pl)
4. path_list_is_ancestor(ances_pl,des_pl)
5. path_list_is_descedant(des_pl,ances_pl)
6. path_list_to_getitem_string(path_list)
-----------------------------------------------------------------------------------------------------------------------

##string
1. str_to_bool(s,**kwargs):
2. str_lstrip(s,char,count):
3. str_rstrip(s,char,count):
4. str_prepend(s,char,n):
5. str_apppend(s,char,n):
6. str_at_begin_of_str(str1,str2):
7. str_at_end_of_str(str1,str2):
8. str_display_width(s):
9. str_prepend_spaces_basedon_displaywidth(s,width):

-------------------------------------------------------------------------------------------------------------------------

##dict list tuple
1. creat_default_list_with_len(len,element=None)  
2. set_default_dict_items_via_path_list(external_dict,path_list,n2s=0,s2n=0)  
3. path_list_in_dict(external_dict,path_list,n2s=0,s2n=0)  
4. set_dict_items_via_path_list(external_dict,path_list,value,n2s=0,s2n=0)  
5. get_dict_items_via_path_list(external_dict,path_list,n2s=0,s2n=0)  
6. get_dict_value_from_full_key_path(d,full_key_path)  
7. get_all_sons_full_key_path_list(d,full_key_path)  
8. dict_array_description(dora)
9. get_desc_parent_dict(description_dict)
10. tree_desc(description_dict)
11. dynamic_indent(deep_search_path,description_dict,full_path_display,fr='',to='')
12. dict_update_just_intersection(dict1,dict2)
13. dict_unique_value(d)  
14. list_unique_value(l)  
15. list_comprise(list1,list2,**kwargs) 
16. dict_comprise(dict1,dict2,**kwargs)  
17. max_wordwidth_in_dict(myDict) 
18. max_display_width_in_dict(myDict)
19. dict_extend(dict1,dict2,**kwargs)
20. get_dict_value_via_cmd(external_dict,cmd_str,**kwargs)  
21. non_recursive_dict_find_keys_via_value(d,v)  
22. dict_find_keys_via_value(dlts,v,**kwargs)
23. del_dict_items_via_path_list(external_dict,path_list,n2s=0,s2n=0)


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

## bitmap
1. bitmaplist_to_num(bitmaplist)
2. num_to_bitmaplist(num,bitmap_size)
3. bitmaplist_bitsum(bitmaplist)
4. subset_bitmap(n,k)  
5. bitmap_contain(bm1,bm2)  





