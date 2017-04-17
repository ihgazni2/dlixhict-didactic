# dlixhict-didactic
>__1. transform and converting between html,json,python-dict,command-line,dir-path__  
__2. dict, list, tuple, toolset__

# install
>__pip3 install xdict__

# INTRODUCE:

for detailed usage and functions please refer to:
-------------------------------------------------

----------------------------------------------------------
>├── [console_color](ReadMeDetailed/console_color.md)      
├── CrtableReadMe  
>>>>├── [crtable](ReadMeDetailed/CrtableReadMe/crtable.md)  

>├── [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)    
├── [hdict_object](ReadMeDetailed/hdict_object.md)   
├── [hdict_xml](ReadMeDetailed/hdict_xml.md)  
├── [jprint](ReadMeDetailed/jprint.md)  
├── [ltdict](ReadMeDetailed/ltdict.md)  
├── [structure](ReadMeDetailed/structure.md)  
├── TestReadMe  
>>>>├── [genrand](ReadMeDetailed/genrand.md)  

>├── [tuple_list](ReadMeDetailed/tuple_list.md)  
└── [utils](ReadMeDetailed/utils.md)

-------------------------------------------------------


## Part1. [crtable](ReadMeDetailed/CrtableReadMe/crtable.md)
__1. init__  
-----------
		import xdict.CrtableLib.crtable as xcr
		colnameslist = ['size','color','language','expire']
		keynameslist = ['size','language']
		table = {}
		table[0] = {0: 500, 1: 'green', 2: 'espanol', 3: '2018-dec-01'}
		table[1] = {0: 74, 1: 'green', 2: 'chinese', 3: '2017-oct-01'}
		table[2] = {0: 74, 1: 'green', 2: 'espanol', 3: '2017-oct-01'}
		crtb = xcr.crtable(colnameslist = colnameslist,table=table,keynameslist = keynameslist)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__init__.png) 

__2. getitem__
--------------  
		from xdict.jprint import pobj
		keys_1 = {'language':'espanol','color':'green'}
		values_1 = crtb[keys_1]
		keys_2 = {'color':'green'}
		values_2 = crtb[keys_2]
		values_1
		pobj(values_1)
		values_2
		pobj(values_2)  

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__getitem__.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__getitem__.2.png)  

__3. .select_rownums(keysorvalues)__  
------------------------------------
		crtb
		keysorvalues = {'color':'green'}
		rownums = crtb.select_rownums(keysorvalues)
		rownums
		keysorvalues = {'language':'espanol'}
		rownums = crtb.select_rownums(keysorvalues)
		rownums  

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.select_rownums.png) 


__4. .select_attribs(keysorvalues)__
------------------------------------
		crtb
		keysorvalues = {'color':'green'}
		attribs = crtb.select_attribs(keysorvalues)
		pobj(attribs)
		keysorvalues = {'language':'espanol'}
		attribs = crtb.select_attribs(keysorvalues)
		pobj(attribs)  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.select_attribs.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.select_attribs.2.png)
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.select_attribs.3.png)  


__5. .select_values(keys)__
---------------------------
		crtb
		keys = {'language':'espanol'}
		values = crtb.select_values(keys)
		pobj(values)
		keys = {'language':'espanol','size':74}
		values = crtb.select_values(keys)
		pobj(values)  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.select_values.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.select_values.2.png)  


__6. .choose_cols(colslist)__
-----------------------------
		crtb
		colslist = [0,2]
		subcols = crtb.choose_cols(colslist)
		xcr.show_crtable(subcols)
		colslist = ['size','color']
		subcols = crtb.choose_cols(colslist)
		xcr.show_crtable(subcols)  

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.choose_cols.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.choose_cols.2.png)  


__7. .choose_rows(rownumslist)__
--------------------------------
		crtb
		rownumslist = [1,2]
		subrows = crtb.choose_rows(rownumslist)
		xcr.show_crtable(subrows)  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.choose_rows.png) 


__8. .append_row(row)__
-----------------------
		crtb
		row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
		crtb.append_row(row)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.append_row.png)


__9. .append_rows(rows)__
-------------------------
		crtb
		rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
		        {'size': 555, 'color': 'yellow', 'language': 'korean'}]
		crtb.append_rows(rows)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.append_rows.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.append_rows.2.png)



__10. .prepend_row(row)__
-------------------------
		crtb
		row = {'size': 700, 'color': 'pink', 'language': 'espanol'}
		crtb.prepend_row(row)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.prepend_row.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.prepend_row.2.png)


__11. .prepend_rows(rows)__
---------------------------
		crtb
		rows = [{'size': 555, 'color': 'yellow', 'language': 'chinese'},
		        {'size': 555, 'color': 'yellow', 'language': 'korean'}]
		crtb.prepend_rows(rows)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.prepend_rows.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.prepend_rows.2.png)


__12. .append_col(col)__
------------------------
		crtb
		col = {'owner':['dli','dli','dli','dli']}
		crtb.append_col(col)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.append_col.png)  



__13. .append_cols(cols)__
--------------------------
		crtb
		cols = [{'id':['2271','2272','2273','2274']},
        		{'tid':['t1','t2','t3','t4']}]
		crtb.append_cols(cols)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.append_cols.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.append_cols.2.png)

__14. .prepend_col(col)__
-------------------------
		crtb
		col = {'owner':['dli','dli','dli','dli']}
		crtb.prepend_col(col)
		crtb 
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.prepend_col.png)  


__15. .prepend_cols(cols)__
---------------------------
		crtb
		cols = [{'nickname':['kk','vv','tt','dd']},
		        {'uid':['u1','u2','u3','u4']}]

		crtb.prepend_cols(cols)
		crtb  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.prepend_cols.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.prepend_cols.2.png)


__16. .__setitem__(keys,values)__
---------------------------------
		crtb
		keys = {'size':88,'language':'korean'}
		values = {'color':'azure'}
		crtb[keys] = values
		crtb
		keys = {'language':'espanol'}
		values = {'color':'darkblack'}
		crtb[keys] = values
		crtb  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__setitem__.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__setitem__.2.png)
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__setitem__.3.png)


__17. .modify_first_row(keys)__
---------------------------------
		crtb
		keys = {'size':74}
		values = {'color':'purple'}
		crtb.modify_first_row(keys,values)
		crtb  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_first_row.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_first_row.2.png)


__18. .modify_last_row(keys)__
------------------------------
		crtb
		keys = {'size':74}
		values = {'color':'purple'}
		crtb.modify_last_row(keys,values)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_first_row.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_first_row.2.png)


__19. .modify_specific_row(keys)__
----------------------------------
		crtb
		keys = {'color':'green'}
		values = {'language':'korean'}
		crtb.modify_specific_row(keys,values,1)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_specific_row.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_specific_row.2.png)


__20. .modify_all_rows(keys)__
------------------------------
		crtb
		keys = {'color':'green'}
		values = {'language':'korean'}
		crtb.modify_all_rows(keys,values)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_all_rows.png) 

__21. .modify_col(colnum_or_colname,col)__
------------------------------------------
		crtb
		col = {0:50,1:50,2:50}
		crtb.modify_col(0,col)
		crtb
		col = {0:60,1:60}
		crtb.modify_col('size',col)
		crtb


![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_col.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_col.2.png)
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.modify_col.3.png) 



__22. .insert_col(colnum,col)__
-------------------------------
		crtb
		col = {'owner':['dli','dlx','dly','dlz']}
		crtb.insert_col(1,col)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_col.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_col.2.png)


__23. .insert_cols(colnumlist,cols)__
-------------------------------------
		crtb
		cols = [
		    {'owner':['dli','dlx','dly','dlz']},
		    {'uid':['ua','ub','uc','ud']}
		]
		colnumlist = [1,3]
		crtb.insert_cols(colnumlist,cols)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_cols.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_cols.2.png)


__24. .insert_row(rownum,row)__
-------------------------------
		crtb
		row = {'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'}
		crtb.insert_row(1,row)
		crtb
		

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_row.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_row.2.png)


__25. .insert_rows(rownumlist,rows)__
-------------------------------------
		crtb
		rows = [{'size': 8888, 'color': 'blue', 'language': 'russian', 'expire': '2018-dec-01'},
		        {'size': 666, 'color': 'azure', 'language': 'russian', 'expire': '2017-dec-01'}]
		rownumlist = [0,2]
		crtb.insert_rows(rownumlist,rows)
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_rows.1.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.insert_rows.2.png)




__26. .__delitem__(keys)__
---------------------------
		crtb
		keys =  {'language':'espanol'}
		del crtb[keys]
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__delitem__.png) 


__27. .delete_first_row(keys)__
-------------------------------
		crtb
		keys =  {'language':'espanol'}
		crtb.delete_first_row(keys)
		crtb
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.del_first_row.png)


__28. .delete_last_row(keys)__
------------------------------
		crtb
		keys =  {'language':'espanol'}
		crtb.delete_last_row(keys)
		crtb
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.delete_last_row.png)


__29. .delete_specific_row(keys,whichrow)__
-------------------------------------------
		crtb
		keys =  {'language':'espanol'}
		crtb.delete_specific_row(keys,1)
		crtb
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.delete_specific_row.png)


__30. .delete_all_rows(keys)__
------------------------------
		crtb
		keys =  {'language':'espanol'}
		crtb.delete_all_rows(keys)
		crtb
		

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.delete_all_rows.png)


__31. .del_col(colnum_or_colname)__
-----------------------------------
		crtb
		crtb.del_col('language')
		crtb
		crtb.del_col(0)
		crtb
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.del_col.1.png)
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.del_col.2.png)

__32. del_cols(colnum_or_colname)__
-----------------------------------
		crtb
		crtb.del_cols(['size','language'])
		crtb
		crtb
		crtb.del_cols([0,3])
		crtb  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.del_cols.1.png)
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.del_cols.2.png)



__33. .keys()__
---------------
		crtb
		crtb.keys()

__34. .values()__
-----------------
		crtb
		crtb.values()

__35. .items()__
----------------
		crtb
		crtb.items()

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.keysvaluesitems.png)


__36. .clear()__
----------------
		crtb
		crtb.clear()
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.clear.png)



__37. .copy()__
---------------
		crtb
		crtb.copy()
		
__38. "*"__
-----------
		table_1 = {
		              0: {0: 'a1', 1: 'b1'}, 
		              1: {0: 'a1', 1: 'b2'} 
		          }
		table_2 = {
		              0: {0: 'a1', 1: 'b2'}, 
		              1: {0: 'a1', 1: 'b3'} 
		          }
		colnameslist = ['A','B']
		keynameslist = ['A']
		crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
		crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
		crtb = crtb1 * crtb2
		crtb
		

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__mul__.png)


__39. .project(crtb2)__
-----------------------
		crtb
		colnameslist = ['color','language']
		crtb.project(colnameslist)
		crtb
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.project.png)

		
__40. "+"__
------------
		table_1 = {
		              0: {0: 'a1', 1: 'b1'}, 
		              1: {0: 'a1', 1: 'b2'} 
		          }
		table_2 = {
		              0: {0: 'a1', 1: 'b2'}, 
		              1: {0: 'a1', 1: 'b3'} 
		          }
		colnameslist = ['A','B']
		keynameslist = ['A']
		crtb1 = crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
		crtb2 = crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
		crtb = crtb1 + crtb2
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__add__.png)






























		
