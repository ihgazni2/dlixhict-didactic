# Introduce
>two-dimension ltdict  used as a multi-keys/multi-values  dict  
or used as a light-weight small database  
	
>for example:

		+++++++++++++++++++++++++++++++++++++++++++
		+++|  size|    color| language|    expire |
		+++++++++++++++++++++++++++++++++++++++++++
		+++|     0|        1|        2|       3   |
		+++++++++++++++++++++++++++++++++++++++++++
		+ 0|   500|    green|  espanol|2018-dec-01|
		+++++++++++++++++++++++++++++++++++++++++++
		+ 1|    74|    green|  chinese|2017-oct-01|
		+++++++++++++++++++++++++++++++++++++++++++
		+ 2|   300|darkblack|  spanish|2017-oct-01|
		+++++++++++++++++++++++++++++++++++++++++++
		+ 3|100000|     blue|  english|2018-dec-01|
		+++++++++++++++++++++++++++++++++++++++++++
		+ 4|   500|    green|  english|2017-oct-01|
		+++++++++++++++++++++++++++++++++++++++++++  

>the upper  table will be stored in a two-dimensiton ltdict as below:

    >>> table[0]
    {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
    >>> table[1]
    {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
    >>> table[2]
    {0: 300, 1: 'darkblack', 2: 'spanish', 3: '2017-oct-01'}
    >>> table[3]
    {0: 100000, 1: 'blue', 2: 'english', 3: '2018-dec-01'}
    >>> table[4]
    {0: 500, 1: 'green', 2: 'english', 3: '2017-oct-01'}
    >>>
 
>for each row :each column is a attrib, all columns are called attribs:
>>attribs: {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}  
attribnames: size,color,language,expire  
each attribname must be string  
attribindexes:0,1,2,3  
each attribindex must be int  
attrib\_name\_index\_mirror\_dict: animd  

	{
		0: 'size', 
		1: 'color', 
		2: 'language', 
		3: 'expire', 
		'size': 0, 
		'language': 2, 
		'color': 1, 
		'expire': 3
	}

>keys are a subset of attribs: {1:'green',2:'espanol'},    
values are a subset of attribs: {0:'500',3:'2018-dec-01'},    
keys have no intersection with values,  
attribs consist of keys and values: {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'},       
>>keynames: color,language  
each keyname must be string  
keyindexes:1,2  
each keyindex must be int  
valunames: size,expire  
each valuename must be string  
valueindexes:0,3  
each valueindex must be int  
key\_name\_index\_mirror\_dict: knimd  

		{
			1: 'color', 
			2: 'language', 
			'language': 2, 
			'color': 1
		}

>>value\_name\_index\_mirror_dict: vnimd  

		{
			0: 'size', 
			3: 'expire', 
			'size': 0, 
			'expire': 3
		}  
  
  
> crtable is a dict as below: 

	crtable = {  
			'table': {...two-dimension ltdict...}, 
			'animd': {...attrib_name_index_mirror_dict...},  
			'knimd': {...key_name_index_mirror_dict...},    
			'vnimd': {...value_name_index_mirror_dict...}  
		}




# QuickStart
1.
2.
3.
4.
5.
6.

# Functions  
## part_1: name_index_mirror_dict
__1. is_name_index_mirror_dict(name_index_mirror_dict)__  
-------------------------------------------------------- 
![](Images/crtable.is_name_index_mirror_dict.png) 

__2. creat_mirror_dict(refdict):__
----------------------------------
![](Images/crtable.creat_mirror_dict_1.png)
![](Images/crtable.creat_mirror_dict_2.png)  
![](Images/crtable.creat_mirror_dict_3.png)


__3. get_indexonly_refdict(refdict,**kwargs)__
----------------------------------------------  
__4. get_nameonly_refdict(refdict,**kwargs)__
---------------------------------------------
![](Images/crtable.get_nameonly_refdict.png)  

__5. get_mirror_dict_via_indexeslist(indexes_list,attribs_name_index_mirror_dict)__
---------------------------------------------------------------------------- 
![](Images/crtable.get_mirror_dict_via_indexeslist.png)  

__6. get_mirror_dict_via_nameslist(names_list,attribs_name_index_mirror_dict)__
------------------------------------------------------------------------
![](Images/crtable.get_mirror_dict_via_nameslist.png)  

__7. get_the_other_mirror_dict_via_indexeslist(indexes_list,attribs_name_index_mirror_dict)__
--------------------------------------------------------------------------------------  
![](Images/crtable.get_the_other_mirror_dict_via_indexeslist.png)  

__8. get_the_other_mirror_dict_via_nameslist(names_list,attribs_name_index_mirror_dict)__
----------------------------------------------------------------------------------
![](Images/crtable.get_the_other_mirror_dict_via_nameslist.png)  

__9. get_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict)__
---------------------------------------------------------------------------------
__10. get_names_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)__
------------------------------------------------------------------------------------
__11. get_the_other_indexes_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)__
------------------------------------------------------------------------------------------------
__12. get_the_other_indexes_list_via_names_list(names_list,attribs_name_index_mirror_dict)__
--------------------------------------------------------------------------------------------
__13. get_the_other_names_list_via_indexes_list(indexes_list,attribs_name_index_mirror_dict)__
----------------------------------------------------------------------------------------------
__14. get_the_other_names_list_via_names_list(names_list,attribs_name_index_mirror_dict)__
------------------------------------------------------------------------------------------
![](Images/crtable.get_the_other_names_list_via_names_list.png)  

## part_2:attribs_keys_values
__1. nameattribs_to_indexattribs(attribs,attribs_name_index_mirror_dict)__
--------------------------------------------------------------------------
__2. indexattribs_to_nameattribs(attribs,attribs_name_index_mirror_dict)__
--------------------------------------------------------------------------
![](Images/crtable.indexattribs_to_nameattribs.png) 

__3. format_attribs_indexdominant(attribs,attribs_name_index_mirror_dict)__
---------------------------------------------------------------------------
__4. format_keys_indexdominant(keys,attribs_name_index_mirror_dict)__
---------------------------------------------------------------------
__5. format_values_indexdominant(values,attribs_name_index_mirror_dict)__
-------------------------------------------------------------------------
![](Images/crtable.format_attribs_indexdominant.png)  

__6. format_attribs_namedominant(attribs,attribs_name_index_mirror_dict)__
--------------------------------------------------------------------------
__7. format_keys_namedominant(keys,attribs_name_index_mirror_dict)__
--------------------------------------------------------------------
__8. format_values_namedominant(values,attribs_name_index_mirror_dict)__
------------------------------------------------------------------------
![](Images/crtable.format_attribs_indexdominant.png) 

__9. format_attribs_to_indexkeyonly(attribs,attribs_name_index_mirror_dict,**kwargs)__
--------------------------------------------------------------------------------------
__10. format_keys_to_indexkeyonly(keys,attribs_name_index_mirror_dict)__
------------------------------------------------------------------------
__11. format_values_to_indexkeyonly(values,attribs_name_index_mirror_dict)__
----------------------------------------------------------------------------
![](Images/crtable.format_attribs_to_indexkeyonly.png)  

__12. format_attribs_to_namekeyonly(attribs,attribs_name_index_mirror_dict,**kwargs)__
--------------------------------------------------------------------------------------
__13. format_keys_to_namekeyonly(keys,attribs_name_index_mirror_dict)__
-----------------------------------------------------------------------
__14. format_values_to_namekeyonly(values,attribs_name_index_mirror_dict)__
---------------------------------------------------------------------------
![](Images/crtable.format_attribs_to_namekeyonly.png)  

## part_3: basic_select

__1. get_seqslist_via_attribs(attribs,crtable)__
------------------------------------------------
![](Images/crtable.get_seqslist_via_attribs.png)  

__2. get_seqslist_via_keys(keys,crtable)__
------------------------------------------
__3. get_seqslist_via_values(values,crtable)__
----------------------------------------------
![](Images/crtable.get_seqslist_via_keys.png)  

__4. get_values_in_attribs(keys,attribs,attribs_name_index_mirror_dict,**kwargs)__
----------------------------------------------------------------------------------
__5. get_keys_in_attribs(values,attribs,attribs_name_index_mirror_dict,**kwargs)__
----------------------------------------------------------------------------------
![](Images/crtable.get_values_in_attribs.png)  

__6. get_valueslist_via_keys(keys,crtable,**kwargs)__
-----------------------------------------------------
__7. get_keyslist_via_values(values,crtable,**kwargs)__
-------------------------------------------------------
![](Images/crtable.get_valueslist_via_keys.png)  

__8. get_column_via_attribindex(index,crtable)__
------------------------------------------------
__9. get_column_via_attribname(name,crtable)__
----------------------------------------------
![](Images/crtable.get_column_via_attribname.png)  

__10. get_attribslist_of_column_via_attribindex(index,crtable)__
----------------------------------------------------------------
__11. get_attribslist_of_column_via_attribname(name,crtable)__
--------------------------------------------------------------
![](Images/crtable.get_attribslist_of_column_via_attribname.png)

__12. get_seqslist_of_column_via_attribindex(index,crtable)__
-------------------------------------------------------------
__13. get_seqslist_of_column_via_attribname(name,crtable)__
-----------------------------------------------------------
![](Images/crtable.get_seqslist_of_column_via_attribname.png)  

__14. get_domainset_of_column_via_attribindex(index,crtable)__
--------------------------------------------------------------
__15. get_domainset_of_column_via_attribname(name,crtable)__
------------------------------------------------------------
![](Images/crtable.get_domainset_of_column_via_attribname.png)  

## part4: creat,init,add,del,modify

__1. creat_empty_crtable(column_name_dict,**kwargs)__
-----------------------------------------------------
![](Images/crtable.creat_empty_crtable.png) 

__2. expand_part_attribs(attribs,attribs_name_index_mirror_dict,**kwargs)__
---------------------------------------------------------------------------
![](Images/crtable.expand_part_attribs.png) 

__3. add_row(row,crtable)__
---------------------------
![](Images/crtable.add_row.png)

__4. add_col(col,crtable)__
---------------------------
![](Images/crtable.add_col.png)  

__5. add_rows(rows,crtable)__
-----------------------------
![](Images/crtable.add_rows.png) 

__6. add_cols(cols,crtable)__
-----------------------------
![](Images/crtable.add_cols.png) 

__7. del_col_via_colnum(colnum,crtable)__
-----------------------------------------
![](Images/crtable.del_col_via_colnum.png)

__8. del_col_via_colname(colname,crtable)__
-------------------------------------------
![](Images/crtable.del_col_via_colname.png)  

__9. del_cols_via_colnumslist(colnumlist,crtable)__
---------------------------------------------------
![](Images/crtable.del_cols_via_colnumslist.png)  

__10. del_cols_via_colnameslist(colnameslist,crtable)__
-------------------------------------------------------
![](Images/crtable.del_cols_via_colnameslist.png)  

__11. del_rows_via_attribs(attribs,crtable)__
---------------------------------------------
__12. del_rows_via_keys(keys,crtable)__
---------------------------------------
__13. del_rows_via_values(values,crtable)__
-------------------------------------------
![](Images/crtable.del_rows_via_keys.png) 


__14. modify_rows_via_seq(seq,crtable,modified_to)__
----------------------------------------------------
![](Images/crtable.modify_rows_via_seq.png)

__15. modify_rows_via_attribs(attribs,crtable,modified_to)__
-------------------------------------------------------------

__16. modify_rows_via_keys(keys,crtable,modified_to,**kwargs)__
---------------------------------------------------------------

__17. modify_rows_via_values(values,crtable,modified_to,**kwargs)__
-------------------------------------------------------------------
![](Images/crtable.modify_rows_via_keys.png)

__18. modify_col_via_colnum(colnum,crtable,modified_to)__
---------------------------------------------------------

__19. modify_col_via_colname(colname,crtable,modified_to)__
-----------------------------------------------------------
![](Images/crtable. modify_col_via_colname.png) 


## part5: relationship 









