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

>├── [cmdline](ReadMeDetailed/cmdline.md)    
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



## Part1. [cmdline](ReadMeDetailed/cmdline.md)  

__1. init__  
-----------
            from xdict import cmdline
            from xdict.jprint import pobj
            currd = {'AutoPauseSpeed': 0, 'HRLimitLow': 125, 'Activity': 6, 'UseHRLimits': False, 'SpeedLimitLow': None, 'UseHRBelt': False, 'Id': 13336645, 'Ordinal': 2, 'SpeedLimitHigh': None, 'GPSInterval': 0, 'UseAutolap': True, 'Interval1Time': None, 'Interval2Time': None, 'BacklightMode': None, 'TapFunctionality': None, 'AutolapDistanceFootPOD': None, 'UseIntervals': False, 'AutolapDistanceSpeedPOD': None, 'AutoscrollDelay': 10, 'AutolapDistanceBikePOD': None, 'Interval2Distance': None, 'UseFootPOD': False, 'AltiBaroMode': 1, 'UseCadencePOD': None, 'UseInDevice': True, 'Name': 'Pool swimming', 'HRLimitHigh': 165, 'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], '__type': 'Suunto.BLL.CustomMode', 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125], 'RecordingInterval': 1, 'Display': None, 'IntervalRepetitions': 0, 'UsePowerPOD': False, 'Interval1Distance': None, 'UseAccelerometer': False, 'UseBikePOD': False, 'UseAutoscroll': False, 'AutolapDistance': 100, 'ShowNavigationSelection': 0, 'Tones': None}
            
            cmdt = cmdline.cmdict(dict=currd)

![](ReadMeDetailed/Images/cmdline.cmdict.__init__.1.png) 
![](ReadMeDetailed/Images/cmdline.cmdict.__init__.2.png) 


__2. cmdt[keys]__
-----------------
            cmdt
            # use cmd seperated by space as keys sequence:
            cmdt['Displays 6 Views 0 Row']
            cmdt['Displays 6 Views 0']
            cmdt['Displays 6 Views']
            cmdt['Displays 6']
            cmdt['Displays']  
	    
![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.1.png)
![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.2.png)

            # use paths list as keys sequence:
            cmdt[['Displays',6,'Views',0,'Row']]
            cmdt[['Displays',6,'Views',0]]
            cmdt[['Displays',6,'Views']]
            cmdt[['Displays',6]]
            cmdt[['Displays']]

![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.3.png)  

            # use traditional keys sequence:
            cmdt.dict['Displays'][6]['Views'][0]['Row']
            cmdt.dict['Displays'][6]['Views'][0]
            cmdt.dict['Displays'][6]['Views']
            cmdt.dict['Displays'][6]
            cmdt.dict['Displays']
            
![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.4.png)

            # search most similiar key:
            cmdt['isplays 1']
            cmdt['RuleID']
            cmdt['LoggedRuleIDs']
            cmdt['LoggedRuleIDs 0']
            cmdt['LoggedRuleIDs 1']
            cmdt['LoggedRuleIDs 2']
	    
![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.5.png)
![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.6.png)
![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.7.png)

            # give prompt indication for exact key,
            # for example: wrongly input 0 as '0':
            cmdt[['Displays',6,'Views','0','Row']]
            
            cmdt[['Displays', 6, 'Views', 0, 'Row']]
            cmdt.dict['Displays'][6]['Views'][0]['Row']
	    
![](ReadMeDetailed/Images/cmdline.cmdict.__getitem__.8.png)

--------------------------------------------------------


## Part2. [crtable](ReadMeDetailed/CrtableReadMe/crtable.md)
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

__2. crtb[keys]__
-----------------  
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


__16. crtb[keys]=values__
-------------------------
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




__26. del crtb[keys]__
----------------------
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
		
__38. crtb = crtb1 * crtb2__
----------------------------
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

		
__40. crtb = crtb1 + crtb2__
----------------------------
		import xdict.CrtableLib.crtable as xcr
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
		crtb = crtb1 + crtb2
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__add__.png)


__41. .crtb = crtb1 - crtb2__
------------------------------

		import xdict.CrtableLib.crtable as xcr
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
		crtb = crtb1 - crtb2
		crtb

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__sub__.png)



__42. .crtb = crtb1 / crtb2__
-----------------------------

		import xdict.CrtableLib.crtable as xcr
		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
		              1: {0: 'a2', 1: 'b3', 2: 'c7'},
		              2: {0: 'a3', 1: 'b4', 2: 'c6'},
		              3: {0: 'a1', 1: 'b2', 2: 'c3'},
		              4: {0: 'a4', 1: 'b6', 2: 'c6'}, 
		              5: {0: 'a2', 1: 'b2', 2: 'c3'},
		              6: {0: 'a1', 1: 'b2', 2: 'c1'}
		          }
		table_2 = {
		              0: {0: 'b1', 1: 'c2', 2: 'd1'}, 
		              1: {0: 'b2', 1: 'c1', 2: 'd1'},
		              2: {0: 'b2', 1: 'c3', 2: 'd2'}
		          }
		colnameslist1 =['A','B','C']
		colnameslist2 =['B','C','D']
		keynameslist1 = ['A']
		keynameslist2 = ['B','C']
		crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
		crtb = crtb1 / crtb2
		crtb
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__truediv__.png)


__43. .unique()__
-----------------

		crtb
		crtb.unique()
		crtb 
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.unique.png)  



__44. .naturalize()__
---------------------

		#no need to call this ,this will be auto executed
		crtb
		crtb.naturalize()
		crtb
		

__45. .intersec(crtb2)__
------------------------

		import xdict.CrtableLib.crtable as xcr
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
		crtb1
		crtb2
		crtb = crtb1.intersec(crtb2)
		crtb


![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.intersec.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.intersec.2.png) 


__46. crtb1 == crtb2__
----------------------
		import xdict.CrtableLib.crtable as xcr
		table_1 = {
		              0: {0: 'a1', 1: 'b1'}, 
		              1: {0: 'a1', 1: 'b2'} 
		          }
		table_2 = {
		              0: {0: 'a1', 1: 'b1'}, 
		              1: {0: 'a1', 1: 'b2'} 
 		         }
		colnameslist = ['A','B']
		keynameslist = ['A']
		crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
		crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
		crtb1 == crtb2


__47. crtb1 != crtb2__
----------------------

		import xdict.CrtableLib.crtable as xcr
		table_1 = {
		              0: {0: 'a1', 1: 'b1'}, 
		              1: {0: 'a1', 1: 'b2'} 
		          }
		table_2 = {
		              0: {0: 'a1', 1: 'b1'}, 
 		             1: {0: 'a1', 1: 'b2'} 
			}
		colnameslist = ['A','B']
		keynameslist = ['A']
		crtb1 = xcr.crtable(colnameslist = colnameslist,table=table_1,keynameslist = keynameslist)
		crtb2 = xcr.crtable(colnameslist = colnameslist,table=table_2,keynameslist = keynameslist)
		crtb1 != crtb2

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.eqne.png) 
		
__48. crtb2 in crtb1__
----------------------

		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
		              1: {0: 'a2', 1: 'b3', 2: 'c7'},  
			      2: {0: 'a3', 1: 'b4', 2: 'c6'},  
			      3: {0: 'a1', 1: 'b2', 2: 'c3'}  
			  }
		table_2 = {  
				0: {0: 'b3', 1: 'c7'}, 
              			1: {0: 'b4', 1: 'c6'},
              			2: {0: 'b2', 1: 'c3'}
          		}
		colnameslist1 =['A','B','C']
		colnameslist2 =['B','C']
		keynameslist1 = ['A']
		keynameslist2 = ['B']
		crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
		crtb2 in crtb1
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.__contains__.png)


__49. .include_row(row)__
-------------------------

		table_1 = {
              			0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
              			1: {0: 'a2', 1: 'b3', 2: 'c7'},
              			2: {0: 'a3', 1: 'b4', 2: 'c6'},
              			3: {0: 'a1', 1: 'b2', 2: 'c3'}
          		  }
		colnameslist1 =['A','B','C']
		keynameslist1 = ['A']
		crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		row = {'A': 'a2', 'B': 'b3', 'C': 'c7'}
		crtb.include_row(row)  
		
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.include_row.png)  


__50. .include_col(col)__
-------------------------

		import xdict.CrtableLib.crtable as xcr
		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
		              1: {0: 'a2', 1: 'b3', 2: 'c7'},
		              2: {0: 'a3', 1: 'b4', 2: 'c6'},
 		             3: {0: 'a1', 1: 'b2', 2: 'c3'}
		          }
		colnameslist1 =['A','B','C']
		keynameslist1 = ['A']
		crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		col = {'B': ['b1','b3','b4','b2']}
		crtb.include_col(col)  
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.include_col.png)  


__51. .include_row_slice(part_row)__
------------------------------------

		table_1 = {  
				0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
				1: {0: 'a2', 1: 'b3', 2: 'c7'},  
				2: {0: 'a3', 1: 'b4', 2: 'c6'},  
				3: {0: 'a1', 1: 'b2', 2: 'c3'}  
			}
		colnameslist1 =['A','B','C']
		keynameslist1 = ['A']
		crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		part_row = {'B': 'b3', 'C': 'c7'}
		crtb.include_row_slice(part_row)  
		



__52. .include_col_slice(part_col)__
------------------------------------
		import xdict.CrtableLib.crtable as xcr
		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 'c2'}, 
		              1: {0: 'a2', 1: 'b3', 2: 'c7'},
		              2: {0: 'a3', 1: 'b4', 2: 'c6'},
		              3: {0: 'a1', 1: 'b2', 2: 'c3'}
		          }
		colnameslist1 =['A','B','C']
		keynameslist1 = ['A']
		crtb = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		part_col = {'B': ['b3','b4']}
		crtb.include_col_slice(part_col)  
		

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.include_slice.png)  



__53. .theta_join(crtb2)__
--------------------------
		import xdict.CrtableLib.crtable as xcr
		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 3}, 
		              1: {0: 'a1', 1: 'b2', 2: 6},  
			      2: {0: 'a2', 1: 'b3', 2: 2},  
			      3: {0: 'a2', 1: 'b4', 2: 12}
          		}
		table_2 = {
		              0: {0: 'e1', 1: 3},  
			      1: {0: 'e2', 1: 7},  
			      2: {0: 'e3', 1: 10},  
			      3: {0: 'e3', 1: 2},  
			      4: {0: 'e5', 1: 2}  
			   }
		colnameslist1 =['A','B','C']
		colnameslist2 =['E','C']
		keynameslist1 = ['A']
		keynameslist2 = ['E']
		crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
		def theta_function(subrow_1,subrow_2):
		    k1 = list(subrow_1.keys())[0]
		    k2 = list(subrow_2.keys())[0]
		    if(subrow_1[k1] < subrow_2[k2]):
		        return(True)
		    else:
		        return(False)

		crtb = crtb1.thetajoin(crtb2,theta=theta_function)
		crtb 


		from xdict import ltdict
		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 3}, 
		              1: {0: 'a1', 1: 'b2', 2: 6},
		              2: {0: 'a2', 1: 'b3', 2: 2},  
			      3: {0: 'a2', 1: 'b4', 2: 12}
		          }
		table_2 = {
		              0: {0: 'b1', 1: 3},  
			      1: {0: 'b2', 1: 7},  
			      2: {0: 'b3', 1: 10},  
			      3: {0: 'b3', 1: 2},  
			      4: {0: 'b5', 1: 2}  
			   }
		colnameslist1 =['A','B','C']
		colnameslist2 =['B','C']
		keynameslist1 = ['A']
		keynameslist2 = ['B']
		crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
		def theta_function(subrow_1,subrow_2):
		    subrow_l1 = ltdict.ltdict_naturalize_intkeydict(subrow_1)
		    subrow_l2 = ltdict.ltdict_naturalize_intkeydict(subrow_2)
		    if(subrow_l1 == subrow_l2):
		        return(True)
		    else:
		        return(False)

		crtb = crtb1.thetajoin(crtb2,theta=theta_function)
		crtb 
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.thetajoin.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.thetajoin.2.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.thetajoin.3.png) 
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.thetajoin.4.png) 


__54. .equijoin(crtb2)__
------------------------

		import xdict.CrtableLib.crtable as xcr 
		from xdict import ltdict
		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 3}, 
		              1: {0: 'a1', 1: 'b2', 2: 6},
		              2: {0: 'a2', 1: 'b3', 2: 2},
		              3: {0: 'a2', 1: 'b4', 2: 12}
 		         }
		table_2 = {
		              0: {0: 'b1', 1: 3},  
			      1: {0: 'b2', 1: 7},  
			      2: {0: 'b3', 1: 10},  
			      3: {0: 'b3', 1: 2},  
			      4: {0: 'b5', 1: 2}
			}
		colnameslist1 =['A','B','C']
		colnameslist2 =['B','C']
		keynameslist1 = ['A']
		keynameslist2 = ['B']
		crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
		crtb = crtb1.equijoin(crtb2)
		crtb 
		

![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.equijoin.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.equijoin.2.png) 



__55. .naturaljoin(crtb2)__
---------------------------

		import xdict.CrtableLib.crtable as xcr 
		from xdict import ltdict
		table_1 = {
		              0: {0: 'a1', 1: 'b1', 2: 3},  
			      1: {0: 'a1', 1: 'b2', 2: 6},  
			      2: {0: 'a2', 1: 'b3', 2: 2},  
			      3: {0: 'a2', 1: 'b4', 2: 12}
			}
		table_2 = {
		              0: {0: 'b1', 1: 3},  
			      1: {0: 'b2', 1: 7},  
			      2: {0: 'b3', 1: 10},  
			      3: {0: 'b3', 1: 2},  
			      4: {0: 'b5', 1: 2}
			}
		colnameslist1 =['A','B','C']
		colnameslist2 =['B','C']
		keynameslist1 = ['A']
		keynameslist2 = ['B']
		crtb1 = xcr.crtable(colnameslist = colnameslist1,table=table_1,keynameslist = keynameslist1)
		crtb2 = xcr.crtable(colnameslist = colnameslist2,table=table_2,keynameslist = keynameslist2)
		crtb = crtb1.naturaljoin(crtb2)
		crtb 
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.naturaljoin.1.png)  
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.naturaljoin.2.png) 


__56. .candidates()__
---------------------

		import xdict.CrtableLib.crtable as xcr 
		from xdict import ltdict
		table = {
		    0: {0: 'a1', 1: 'b1', 2: 5, 3: 3}, 
		    1: {0: 'a1', 1: 'b2', 2: 6, 3: 7}, 
		    2: {0: 'a2', 1: 'b3', 2: 8, 3: 10}, 
		    3: {0: 'a2', 1: 'b3', 2: 8, 3: 2}
		}
		colnameslist = ['A','B','C','E']
		keynameslist = ['A']
		crtb = xcr.crtable(colnameslist = colnameslist,table=table,keynameslist = keynameslist)
		crtb.candidates()
		
![](ReadMeDetailed/CrtableReadMe/Images/crtable.crtable.candidates.png) 













		






























		
