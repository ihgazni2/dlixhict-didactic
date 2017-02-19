# dlixhict-didactic
>transform and converting between html,json,python-dict,command-line,dir-path  

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
>>a  <html\_dict>  is a dict with the following format:  

				{   
					0 : <element>,  
					1 : <element>,  
					......,  
					n : <element>
				}

>>each <element> is a dict with the follwing format:  

				{    
					'depth': 2,   
					'external_path': ['html','body','Error'],  
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
>>>1.2.1 the meaning of each key in <element>:  
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

>>>>'breadth' :  the position of the <element> hierarchy
>>>>>html breadth = 0 ;  
head breadth = 0, body breadth = 1;  
meta breadth = 0, Success breadth =1,Error breadth =2;  

>>>>'siblings_seq' :  the position of the <element> in its siblings
>>>>>html siblings_seq = 0 ;  
head siblings_seq = 0, body siblings_seq = 1;  
meta siblings_seq = 0, Success siblings_seq =0,Error siblings_seq =1; 

>>>>'external\_path': the absolute path consist of tags splited into a array,just like the ancestors chain in html  
>>>>>Error external\_path = ['html','body','Error']  

>>>>'path': the absolute path consist of siblings\_seq and 'children' splited into a array  
>>>>>html path = [0] ;  
head path = [0,'children',0], body path = [0,'children',1];  
meta path = [0,'children',0,'children',0], Success path =[0,'children',1,'children',0],Error path =[0,'children',1,'children',1];  

>>>>'tag' :  tag names when convered a html\_dict back to a dict, tag will be used as key  

>>>>'attrib': a dict stores the attributes , just like the html attributes, when convert a dict to a html\_dict, it will store the data type of the original  in <element>['attrib']['type']

>>>>'children': just like the descendants tree in html;if the children = {},which means this is a non-recursive leaf, the string fromat of leaf value will be stored in <element>['text'],the type of leaf value will be stored in <element>['attrib']['type']  

>>>>'text':just like the text in html;if the children = {},which means this is a non-recursive leaf, the string fromat of leaf value will be stored in <element>['text'],the type of leaf value will be stored in <element>['attrib']['type']; if the children != {}, the <element>['text'] will be None.  

>>list/array and tuple not exist in <html_dict>,when converting a dict a html\_dict, list/array and tuple will be convert to the following formats(it use the <element>['attrib']['type'] to in dicate the original type):  
  
>>>the original key:value pair:  
>>>>"Pair": ('swimming','cadence')  
key = "Pair"  
 value = ('swimming','cadence')  

>>>the correspoding <element> of the key:value pair:  

					{  
						'depth': 3,  
						'external_path': ['Value', 'RuleInfo', 'Rule', 'Pair'],  
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
								'external_path': ['Value', 'RuleInfo', 'Rule', 'Pair', 0],  
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
								'external_path': ['Value', 'RuleInfo', 'Rule', 'Pair', 1],  
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

>>>the <desciption> is a dict with the following format:  

				{  
					'external_path': ['html', 'body', 'Error'],#the same meaning as external_path explained in 1.2.1
					'breadth_external_path': [0, 1, 0], #the array after poping all 'children's of internal_path
					'internal_path': [0, 'children', 1, 'children', 0]#the same meaning as path explained in 1.2.1
				 }
		


				{  
					0: {  # this mean the 0st  hierarchy
						 0: {  # this mean the 0st in the 0st hierarchy
							'external_path': ['html'],  
							'breadth_external_path': [0],  
							'internal_path': [0]  
						}  
					}  
					1: {  # this mean the 1st  hierarchy
						0: {  # this mean the 0st in 1st the hierarchy
							'external_path': ['html', 'head'],  
							'breadth_external_path': [0, 0],  
							'internal_path': [0, 'children', 0]  
						},  
						1: {  # this mean the 1st in the 1st hierarchy
							'external_path': ['html', 'body'],  
							'breadth_external_path': [0, 1],  
							 'internal_path': [0, 'children', 1]  
						}  
					},  
					2: {  # this mean the 2st  hierarchy
						0: {  # this mean the 0st in the 2st hierarchy
							'external_path': ['html', 'head', 'meta'],  								'breadth_external_path': [0, 0, 0],  									'internal_path': [0, 'children', 0, 'children', 0]  
						},  
						1: {  # this mean the 1st in the 2st hierarchy
							'external_path': ['html', 'body', 'Error'],
							'breadth_external_path': [0, 1, 0],
							'internal_path': [0, 'children', 1, 'children', 0]
						 },
						2: {  # this mean the 2st in the 2st hierarchy
							'external_path': ['html', 'body', 'Success'],  
							'breadth_external_path': [0, 1, 1],  
							'internal_path': [0, 'children', 1, 'children', 1]  
						 }  
					}  
				}  




		

