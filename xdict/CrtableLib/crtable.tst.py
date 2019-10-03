

import xdict.CrtableLib.crtable as xcr
colnameslist = ['name','chapter','sentence','startloc','endloc']
keynameslist = ['name']
table = {}
table[0] = ['姜维', 98, '姜维', 3215, 3217]
table[1] = ['姜维', 100, '姜维', 2476, 2478]
table[2] = ['姜维', 101, '姜维', 1699, 1701]
crtb = xcr.crtable(colnameslist = colnameslist,table=table,keynameslist = keynameslist)
print(crtb.__str__())


#+++++++++++++++++++++++++++++++++++++++
#|name|chapter|sentence|startloc|endloc|
#+++++++++++++++++++++++++++++++++++++++
#|姜维|     98|    姜维|    3215|  3217|
#+++++++++++++++++++++++++++++++++++++++
#|姜维|    100|    姜维|    2476|  2478|
#+++++++++++++++++++++++++++++++++++++++
#|姜维|    101|    姜维|    1699|  1701|
#+++++++++++++++++++++++++++++++++++++++


import xdict.CrtableLib.crtable as xcr

ROWs = {
         0: {0: 'TBqESO', 1: 'jVymZLRRhj', 2: 'VlWVOMszE'},
         1: {0: 'apxjPB', 1: 'iSdHTH', 2: 'WuqefeO'},
         2: {0: 'alYhP', 1: 'lOST', 2: 'anQOLA'}
        }

display_COLs = xcr.display_table_via_rows(ROWs,returned=True)


colormatrix = {
      0: {0: 'yellow', 1: 'green', 2: 'blue'},
      1: {0: 'red', 1: 'yellow', 2: 'green'},
      2: {0: 'blue', 1: 'yellow', 2: 'green'}
     }

COLs = xcr.rows_to_cols(ROWs)


xcr.display_table_via_rows(ROWs,colormatrix=colormatrix,returned=True)


m = [
    [1,2,3,4,5],
    [2,2,2,2,2],
    [55,6,7,7,8]
]

import xdict.CrtableLib.crtable as xcr
xcr.shmat(m)

#s =''
#color_sec ={}
#cursor = 0
#for j in range(0,COLs.__len__()):
#    s = s + display_COLs[j][i]
#    length = display_COLs[j][i].__len__()
#    color_sec[j+1] = (cursor,cursor+length-1,colormatrix[i][j])
#    cursor = cursor+length

#boundary = '+' * len(s)
#s = s +'\n'+boundary
#color_sec[COLs.__len__()+1] = (cursor,cursor+boundary.__len__(),"white")
#console.paint(s,color_sec=color_sec)
