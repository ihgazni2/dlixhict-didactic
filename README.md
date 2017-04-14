# dlixhict-didactic
>__transform and converting between html,json,python-dict,command-line,dir-path__  
# install
>__pip3 install xdict__

# INTRODUCE:

for detailed usage and functions please refer to:
-------------------------------------------------
ReadMeDetailed/  
   ├── [console_color](ReadMeDetailed/console_color.md)      
   ├── CrtableReadMe  
   │    └── [crtable](ReadMeDetailed/CrtableReadMe/crtable.md)    
   ├── [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)    
   ├── [hdict_object](ReadMeDetailed/hdict_object.md)   
   ├── [hdict_xml](ReadMeDetailed/hdict_xml.md)  
   ├── [jprint](ReadMeDetailed/jprint.md)  
   ├── [ltdict](ReadMeDetailed/ltdict.md)  
   ├── [structure](ReadMeDetailed/structure.md)  
   ├── TestReadMe  
   │    └── [genrand](ReadMeDetailed/genrand.md)  
   ├── [tuple_list](ReadMeDetailed/tuple_list.md)  
   └── [utils](ReadMeDetailed/utils.md)


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

![](ReadMeDetailed/CrtableReadMe/Images/crtable.__init__.png) 
