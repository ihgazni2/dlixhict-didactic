# dlixhict-didactic
>transform and converting between html,json,python-dict,command-line,dir-path  
# install
>

# INTRODUCE:

for detailed usage and functions please refer to:
-------------------------------------------------
				ReadMeDetailed/
				├── console_color.md
				├── CrtableReadMe
				│   └── crtable.md
				├── hdict_cmdline.md
				├── hdict_object.md
				├── hdict_xml.md
				├── jprint.md
				├── ltdict.md
				├── TestReadMe
				│   └── genrand.md
				├── tuple_list.md
				└── utils.md


1. Definition:  

>1.1.  list\_tuple\_dict   
>>for example:  
array = ['a','b','c','d','e'];  
the corresponding list\_tuple\_dict of this array is :  
>>>{  
>>>>0: 'a',  
1: 'b',  
2: 'c',  
3: 'd',  
4: 'e'  

>>>}  

>1.2.  html\_dict  
			
				{   #a  <html\_dict>  is a dict with the following format:
					0 : <element>,  
					1 : <element>,  
					......,  
					n : <element>
				}

>> element  

				{    #each <element> is a dict with the follwing format:
					'depth': 2,   
					'orig_obj_path': ['html','body','Error'],  
					'siblings_seq': 1,  
					'path': [0,'children',1,'children',1], 
					'attrib': {  
						'type': 'NoneType'  
					},  
					'tag': 'Error',  
					'breadth': 2,  
					'text': "Timeout!!!",  
					'children': <html_dict>
  				  }  
>>>1.2.1 the meaning of each key in element:  
take a simple html structure for explaining:  

					<html>  
						<head>  
							<meta>  
							</meta>  
						</head>  
						<body>
							<Success>  
							</Success>
							<Error type="NoneType">  
								Timeout!!!
							</Error>  
						</body>  
					</html>
>>>>'depth' :  which hierarchy
>>>>>html depth = 0 ;  
head depth = 1, body depth = 1;  
meta depth =2, Success depth =2,Error depth =2;  

>>>>'breadth' :  the position of the element hierarchy
>>>>>html breadth = 0 ;  
head breadth = 0, body breadth = 1;  
meta breadth = 0, Success breadth =1,Error breadth =2;  

>>>>'siblings_seq' :  the position of the element in its siblings
>>>>>html siblings_seq = 0 ;  
head siblings_seq = 0, body siblings_seq = 1;  
meta siblings_seq = 0, Success siblings_seq =0,Error siblings_seq =1; 

>>>>'orig\_obj\_path': the absolute path consist of tags splited into a array,just like the ancestors-and-self chain in html  
>>>>>Error orig\_obj\_path = ['html','body','Error']  

>>>>'path': the absolute path consist of siblings\_seq and 'children' splited into a array  
>>>>>html path = [0] ;  
head path = [0,'children',0], body path = [0,'children',1];  
meta path = [0,'children',0,'children',0], Success path =[0,'children',1,'children',0],Error path =[0,'children',1,'children',1];  

>>>>'tag' :  tag names when convered a html\_dict back to a dict, tag will be used as key  

>>>>'attrib': a dict stores the attributes , just like the html attributes, when convert a dict to a html\_dict, it will store the data type of the original  in element['attrib']['type']

>>>>'children': just like the descendants tree in html;if the children = {},which means this is a non-recursive leaf, the string fromat of leaf value will be stored in element['text'],the type of leaf value will be stored in element['attrib']['type']  

>>>>'text':just like the text in html;if the children = {},which means this is a non-recursive leaf, the string fromat of leaf value will be stored in element['text'],the type of leaf value will be stored in element['attrib']['type']; if the children != {}, the element['text'] will be None.  

>>list/array and tuple not exist in html\_dict,when converting a dict a html\_dict, list/array and tuple will be convert to the following formats(it use the element['attrib']['type'] to in dicate the original type):  
  
>>>the original key:value pair:  
>>>>"Pair": ('swimming','cadence')  
key = "Pair"  
 value = ('swimming','cadence')  

>>>the correspoding element of the key:value pair:  

					{  
						'depth': 3,  
						'orig_obj_path': ['Value', 'RuleInfo', 'Rule', 'Pair'],  
						'siblings_seq': 0,  
						'path': [0, 'children', 2, 'children', 1, 'children', 0],  
						'attrib': {  
							'type': 'tuple'#-----indicate the type of the value in the original key:value pair  
						},  
						'tag': 'Pair', #----the key name in the original key:value pair  
						'breadth': 0,  
						'text': None,  
						'children': {  
							0: {  
								'depth': 4,  
								'orig_obj_path': ['Value', 'RuleInfo', 'Rule', 'Pair', 0],  
								'siblings_seq': 0,  
								'path': [0, 'children', 2, 'children', 1, 'children', 0, 'children', 0],  
								'attrib': {  
									'type': 'str' #-----the 'swimming' of value tuple ('swimming','cadence')[0]  
								},  
								'tag': 0,  
								'breadth': 0,  
								'text': 'swimming',#------the 0st in the original value tuple  
								'children': {}  
							},  
							1: {  
								'depth': 4,  
								'orig_obj_path': ['Value', 'RuleInfo', 'Rule', 'Pair', 1],  
								'siblings_seq': 1,  
								'path': [0, 'children', 2, 'children', 1, 'children', 0, 'children', 1],  
								'attrib': {  
									'type': 'str'  
								},  
								'tag': 1,  
								'breadth': 1,  
								'text': 'cadence',#------the 1st in the original value tuple  
								'children': {}  
							 }  
						 }  
					}  

>>>when converting  a html\_dict back to a dict, list/array and tuple will be convert back to list\_tuple\_dict 

>1.3.  structure\_description\_dict  

>>for example,theoriginal\_dict:  

				original_dict = {  
					'html': {  
						'head': {
							'meta': None  
						} , 
						'body': {  
							'Success': None,  
							'Error': 'Timeout!!!'  
						 }  
					}  
				}  

>>the corresponding html:  

		<html>  
			<head>  
				<meta>  
				</meta>  
			</head>
			<body>  
				<Success>  
				</Success>  
				<Error>  
					Timeout!!!  
				</Error>  
			</body>  
		</html>  

>>the corresponding structure\_description\_dict is a two dimension dict with the format:  

				{  
					0:  { 0:<description>,1:<description>......L1:<description>},  
					1:  {0:<description,1:<description>......L2:<description>},  
					......  
					n:  {0:<description>,1:<description>......Ln:<description>}  
				}  

>>>the desciption is a dict with the following format:  

				{  
					'orig_obj_path': ['html', 'body', 'Error'],#the same meaning as orig_obj_path explained in 1.2.1
					'breadth_path': [0, 1, 0], #the array after poping all 'children's of hdict_path
					'hdict_path': [0, 'children', 1, 'children', 0],#the same meaning as path explained in 1.2.1  
					'leaf':True,
					'leaf_sons':0,
					'non_leaf_sons':0,
					'leaf_descendants':0,
					'non_leaf_descendants':0,  
					'hdict_lsib_path': [], #the hdict_path of the left sibling  
					'hdict_lcin_path': [0.'children',0,'children',0], #the hdict_path of the left cousin (non-common parent)
					'hdict_rsib_path': [0, 'children', 1, 'children', 1], #the hdict_path of the right sibling
					'hdict_rcin_path': [], #the hdict_path of the right cousin (non-common parent)  
					'orig_lsib_path': [], #the orig_obj_path of the left sibling
					'orig_lcin_path': ['html','head','meta'], #the orig_obj_path of the left cousin (non-common parent)
					'orig_rsib_path': ['html','body','Success'], #the orig_obj_path of the right sibling
					'orig_rcin_path': [], #the orig_obj_path of the right cousin (non-common parent)  
				 }
		


				{  
					0: {  # this mean the 0st  hierarchy
						 0: {  # this mean the 0st in the 0st hierarchy
							'orig_obj_path': ['html'],  
							'breadth_path': [0],  
							'hdict_path': [0],  
							'leaf':False,
							'leaf_sons':0,
							'non_leaf_sons':2,
							'leaf_descendants':3,
							'non_leaf_descendants':2,
							'hdict_lsib_path':[],
							'hdict_rsib_path':[],
							'hdict_lcin_path':[],
							'hdict_rcin_path':[],
							'orig_lsib_path':[],
							'orig_rsib_path':[],
							'orig_lcin_path':[],
							'orig_rcin_path':[]
							
						}  
					}  
					1: {  # this mean the 1st  hierarchy
						0: {  # this mean the 0st in 1st the hierarchy
							'orig_obj_path': ['html', 'head'],  
							'breadth_path': [0, 0],  
							'hdict_path': [0, 'children', 0],  
							'leaf':False,
							'leaf_sons':1,
							'non_leaf_sons':0,
							'leaf_descendants':1,
							'non_leaf_descendants':0,
							'hdict_lsib_path':[],
							'hdict_rsib_path':[0,'children',1],
							'hdict_lcin_path':[],
							'hdict_rcin_path':[],
							'orig_lsib_path':[],
							'orig_rsib_path':['html','body'],
							'orig_lcin_path':[],
							'orig_rcin_path':[],
						},  
						1: {  # this mean the 1st in the 1st hierarchy
							'external_path': ['html', 'body'],  
							'breadth_external_path': [0, 1],
							'internal_path': [0, 'children', 1],
							'leaf':False,
							'leaf_sons':2,
							'non_leaf_sons':0,
							'leaf_descendants':2,
							'non_leaf_descendants':0,
							'hdict_lsib_path':[0, 'children', 0],
							'hdict_rsib_path':[],
							'hdict_lcin_path':[],
							'hdict_rcin_path':[],
							'orig_lsib_path':['html','head'],
							'orig_rsib_path':[],
							'orig_lcin_path':[],
							'orig_rcin_path':[]
						}  
					},  
					2: {  # this mean the 2st  hierarchy
						0: {  # this mean the 0st in the 2st hierarchy
							'orig_obj_path': ['html', 'head', 'meta'],  
							'breadth_path': [0, 0, 0],  
							'hdict_path': [0, 'children', 0, 'children', 0],  
							'leaf':True,
							'leaf_sons':0,
							'non_leaf_sons':0,
							'leaf_descendants':0,
							'non_leaf_descendants':0,
							'hdict_lsib_path':[],
							'hdict_rsib_path':[],
							'hdict_lcin_path':[],
							'hdict_rcin_path':[0,'children',1,'children',0],
							'orig_lsib_path':[],
							'orig_rsib_path':[],
							'orig_lcin_path':[],
							'orig_rcin_path':['html','body','Error']
						},  
						1: {  # this mean the 1st in the 2st hierarchy
							'orig_obj_path': ['html', 'body', 'Error'],
							'breadth_path': [0, 1, 0],
							'hdict_path': [0, 'children', 1, 'children', 0],
							'leaf':True,
							'leaf_sons':0,
							'non_leaf_sons':0,
							'leaf_descendants':0,
							'non_leaf_descendants':0,
							'hdict_lsib_path':[],
							'hdict_rsib_path':[0,'children',1,'children',1],
							'hdict_lcin_path':[0,'children',0,'children',0],
							'hdict_rcin_path':[],
							'orig_lsib_path':[],
							'orig_rsib_path':['html','body','Success'],
							'orig_lcin_path':['html','head','meta'],
							'orig_rcin_path':[]
						 },
						2: {  # this mean the 2st in the 2st hierarchy
							'orig_obj_path': ['html', 'body', 'Success'],  
							'breadth_path': [0, 1, 1],  
							'hdict_path': [0, 'children', 1, 'children', 1],  
							'leaf':True,
							'leaf_sons':0,
							'non_leaf_sons':0,
							'leaf_descendants':0,
							'non_leaf_descendants':0,
							'hdict_lsib_path':[0, 'children', 1, 'children', 0],
							'hdict_rsib_path':[],
							'hdict_lcin_path':[],
							'hdict_rcin_path':[],
							'orig_lsib_path':['html','body','Error'],
							'orig_rsib_path':[],
							'orig_lcin_path':[],
							'orig_rcin_path':[]
						 }  
					}  
				}  


  
>1.4 paths\_relations\_dict:  

>>the paths\_relations\_dict is a two dimension dict with the format:  

		{
			'h:o': { # key = tuple(hdict_path) : value = orig_obj_path
					(0,): ['html'],
					(0, 'children', 0): ['html', 'head'],
					(0, 'children', 1): ['html', 'body'],
					(0, 'children', 0, 'children', 0): ['html', 'head', 'meta'],
					(0, 'children', 1, 'children', 0): ['html', 'body', 'Error'],
					(0, 'children', 1, 'children', 1): ['html', 'body', 'Success']
				},
			'b:h': {# key = tuple(breadth_path) : value = orig_obj_path
					(0,): [0],
					(0,0): [0, 'children', 0],
					(0,1): [0, 'children', 1],
					(0,0,0): [0, 'children', 0, 'children', 0],
					(0,1,1): [0, 'children', 1, 'children', 0],
					(0,1,2): [0, 'children', 1, 'children', 1]
				},
			'o:h': {# key = tuple(orig_obj_path) : value = hdict_path
					('html'): [0],
					('html', 'head'): [0, 'children', 0],
					('html', 'body'): [0, 'children', 1],
					('html', 'head', 'meta'): [0, 'children', 0, 'children', 0],
					('html', 'body', 'Error'): [0, 'children', 1, 'children', 0],
					('html', 'body', 'Success'): [0, 'children', 1, 'children', 1]
				},
			'h:b': {# key = tuple(hdict_path) : value = breadth_path
					(0,): (0,),
					(0, 'children', 0): (0,0),
					(0, 'children', 1): (0,1),
					(0, 'children', 0, 'children', 0): (0,0,0),
					(0, 'children', 1, 'children', 0): (0,1,1),
					(0, 'children', 1, 'children', 1): (0,1,2)
				}
		}



2 . Abbreviations:

>2.1  list\_tuple\_dict :  [ltdict](ReadMeDetailed/ltdict.md)  
2.2   html\_dict: hdict   [hdict_object](ReadMeDetailed/hdict_object.md)  [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)  [hdict_xml](ReadMeDetailed/hdict_xml.md)  
2.3   structure\_description\_dict: sdict  
2.4   paths\_relations\_dict: prdict  
2.5   
>>seperator of command line: cmd_sp  [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)
command line: cmd_str  [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)
command line in list pattern: cmd_pl [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)
cmdlines\_ltdict: clt  [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)
cmdlines\_deep\_ltdict: cdlt [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)
cmdlines\_full\_ltdict: cflt [hdict_cmdline](ReadMeDetailed/hdict_cmdline.md)
     


		

