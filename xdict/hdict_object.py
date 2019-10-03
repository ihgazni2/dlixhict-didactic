# obj - obj_to_hdict ->hdict,sdict,prdict 
# hdict - hdict_get_paths_relationship -> prdict
# hdict sdict(internal state),prdict - hdict_fullfill_sdict -> sdict
# hdict - get_sdict_and_prdict_from_hdict -> sdict,prdict
# any_kind_of_path  - prdict -> breadth_path - breadth_path_to_sdict_location -> sdict_location
# hdict,sdict,prdict - hdict_to_obj -> obj 



import copy
import json
import cgi
from xdict import utils
import ltdict.ltdict as ltdict

def obj_to_hdict(obj,**kwargs):
    def add_dict_tree_entry(hdict,path,value,n2s=0,s2n=0):
        utils.dict_setdefault_via_path_list(hdict,path,n2s=n2s,s2n=s2n)
        utils.dict_setitem_via_path_list(hdict,path,value,n2s=n2s,s2n=s2n)
    if('debug' in kwargs):
        debug = kwargs['debug']
    else:
        debug = 0
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if('save' in kwargs):
        save = kwargs['save']
    else:
        save = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('json' in kwargs):
        js = kwargs['json']
    else:
        js = 0
    if('get_sdict' in kwargs):
        get_sdict = kwargs['get_sdict']
    else:
        get_sdict =1
    if('sdict' in kwargs):
        sdict = kwargs['sdict']
    else:
        sdict = {}
    hdict = {}
    if(deepcopy):
        new_obj = copy.deepcopy(obj)
    else:
        new_obj = obj
    if(debug):
        print("root:{0}".format(new_obj))
    else:
        pass
    unhandled = []
    if(utils.is_list(new_obj)|utils.is_tuple(new_obj)):
        for i in range(0,new_obj.__len__()):
            unhandled.append({'node':new_obj[i],'path':[i],'tag':i,'siblings_seq':i,'breadth':i,'depth':0,'orig_obj_path':[i],'breadth_path':[i]})
    elif(utils.is_set(new_obj)):
        i = 0
        for ele in new_obj:
            unhandled.append({'node':ele,'path':[i],'tag':i,'siblings_seq':i,'breadth':i,'depth':0,'orig_obj_path':[i],'breadth_path':[i],'orig_obj_path_loose':[]})
            i = i + 1
    elif(utils.is_dict(new_obj)):
        seq = 0
        for key in new_obj:
            unhandled.append({'node':new_obj[key],'path':[seq],'tag':key,'siblings_seq':seq,'breadth':seq,'depth':0,'orig_obj_path':[key],'breadth_path':[seq]})
            seq = seq + 1
    else:
        hdict[0] = {}
        hdict[0]['tag'] = ''
        hdict[0]['attrib'] = {}
        hdict[0]['attrib']['type'] = utils.get_obj_type_name(new_obj)
        hdict[0]['text'] = str(new_obj)
        hdict[0]['depth'] = 0
        hdict[0]['breadth'] = 0
        hdict[0]['breadth_path'] = 0
        hdict[0]['siblings_seq'] = 0
        hdict[0]['path'] = [0]
        hdict[0]['children'] = {}
        return(hdict)
    depth = 0
    while(unhandled.__len__()>0):
        if(debug):
            print("--------------depth:{0}---------------------".format(depth))
        else:
            pass
        next_unhandled = []
        sdict[depth] = {}
        for i in range(0,unhandled.__len__()):
            parent = unhandled[i]
            parent_path = unhandled[i]['path']
            parent_path_path = copy.copy(parent_path)
            parent_path_path.append('path')
            add_dict_tree_entry(hdict,parent_path_path,parent_path,s2n=s2n,n2s=n2s)
            parent_orig_obj_path_path = copy.copy(parent_path)
            parent_orig_obj_path_path.append('orig_obj_path')
            add_dict_tree_entry(hdict,parent_orig_obj_path_path,parent['orig_obj_path'],s2n=s2n,n2s=n2s)
            parent_tag_path = copy.copy(parent_path)
            parent_tag_path.append('tag')
            add_dict_tree_entry(hdict,parent_tag_path,parent['tag'],s2n=s2n,n2s=n2s)
            parent_attrib_path = copy.copy(parent_path)
            parent_attrib_path.append('attrib')
            parent_attrib = {}
            parent_attrib['type'] = utils.get_obj_type_name(parent['node'])
            add_dict_tree_entry(hdict,parent_attrib_path,parent_attrib,s2n=s2n,n2s=n2s)
            parent_depth_path = copy.copy(parent_path)
            parent_depth_path.append('depth')
            add_dict_tree_entry(hdict,parent_depth_path,unhandled[i]['depth'],s2n=s2n,n2s=n2s)
            parent_text_path = copy.copy(parent_path)
            parent_text_path.append('text')
            if(utils.is_recursive_type(unhandled[i]['node']) | utils.is_set(unhandled[i]['node'])):
                text_temp = None
            else:
                text_temp = unhandled[i]['node']
            add_dict_tree_entry(hdict,parent_text_path,text_temp,s2n=s2n,n2s=n2s)
            parent_siblings_seq_path = copy.copy(parent_path)
            parent_siblings_seq_path.append('siblings_seq')
            add_dict_tree_entry(hdict,parent_siblings_seq_path,unhandled[i]['siblings_seq'],s2n=s2n,n2s=n2s)
            parent_breadth_path = copy.copy(parent_path)
            parent_breadth_path.append('breadth')
            add_dict_tree_entry(hdict,parent_breadth_path,unhandled[i]['breadth'],s2n=s2n,n2s=n2s)
            #
            parent_bps_path = copy.copy(parent_path)
            parent_bps_path.append('breadth_path')
            add_dict_tree_entry(hdict,parent_bps_path,unhandled[i]['breadth_path'],s2n=s2n,n2s=n2s)
            #
            parent_children_path = copy.copy(parent_path)
            parent_children_path.append('children')
            utils.dict_setdefault_via_path_list(hdict,parent_children_path)
            children = parent['node']
            if(debug):
                print("children:{0}:  {1}".format(i,children))
            else:
                pass
            if(get_sdict):
                siblings_seq_path = hdict_path_to_siblings_seq_path(parent_path)
                sdict[depth][unhandled[i]['breadth']] = {}
                sdict[depth][unhandled[i]['breadth']]['text'] = text_temp
                sdict[depth][unhandled[i]['breadth']]['attrib'] = parent_attrib
                sdict[depth][unhandled[i]['breadth']]['breadth_path'] = parent['breadth_path']
                sdict[depth][unhandled[i]['breadth']]['hdict_path'] = parent_path
                sdict[depth][unhandled[i]['breadth']]['siblings_seq_path'] = siblings_seq_path
                sdict[depth][unhandled[i]['breadth']]['orig_obj_path'] = parent['orig_obj_path']
                if(utils.is_recursive_type(children)|utils.is_set(children)):
                    sdict[depth][unhandled[i]['breadth']]['leaf'] = False
                    sdict[depth][unhandled[i]['breadth']]['html_tag_lines'] = 2
                else:
                    sdict[depth][unhandled[i]['breadth']]['leaf'] = True
                    sdict[depth][unhandled[i]['breadth']]['html_tag_lines'] = 3
                if('type' in parent_attrib):
                    sdict[depth][unhandled[i]['breadth']]['type'] = parent_attrib['type']
                else:
                    sdict[depth][unhandled[i]['breadth']]['type'] = None
            else:
                pass
            if(utils.is_list(children)|utils.is_tuple(children)):
                for j in range(0,children.__len__()):
                    child = children[j]
                    breadth = next_unhandled.__len__()
                    siblings_seq = j
                    parent_path = copy.copy(unhandled[i]['path'])
                    parent_path.append('children')
                    parent_path.append(siblings_seq)
                    path = parent_path
                    parent_orig_obj_path = copy.copy(parent['orig_obj_path'])
                    parent_orig_obj_path.append(siblings_seq)
                    parent_bps_path = copy.copy(parent['breadth_path'])
                    parent_bps_path.append(breadth)
                    next_unhandled.append({'node':child,'path':path,'tag':siblings_seq,'siblings_seq':siblings_seq,'breadth':breadth,'depth':(depth+1),'orig_obj_path':parent_orig_obj_path,'breadth_path':parent_bps_path})
            elif(utils.is_set(children)):
                temp_seq = 0
                for ele in children:
                    child = ele
                    breadth = next_unhandled.__len__()
                    siblings_seq = temp_seq
                    parent_path = copy.copy(unhandled[i]['path'])
                    parent_path.append('children')
                    parent_path.append(siblings_seq)
                    path = parent_path
                    parent_orig_obj_path = copy.copy(parent['orig_obj_path'])
                    parent_orig_obj_path_loose = parent_orig_obj_path
                    parent_orig_obj_path.append(siblings_seq)
                    parent_bps_path = copy.copy(parent['breadth_path'])
                    parent_bps_path.append(breadth)
                    next_unhandled.append({'node':child,'path':path,'tag':siblings_seq,'siblings_seq':siblings_seq,'breadth':breadth,'depth':(depth+1),'orig_obj_path':parent_orig_obj_path,'breadth_path':parent_bps_path,'orig_obj_path_loose':parent_orig_obj_path_loose})
                    temp_seq = temp_seq + 1
            elif(utils.is_dict(children)):
                seq = 0
                for key in children:
                    child = children[key]
                    breadth = next_unhandled.__len__()
                    siblings_seq = seq
                    parent_path = copy.copy(unhandled[i]['path'])
                    parent_path.append('children')
                    parent_path.append(siblings_seq)
                    path = parent_path
                    parent_orig_obj_path = copy.copy(parent['orig_obj_path'])
                    parent_orig_obj_path.append(key)
                    parent_bps_path = copy.copy(parent['breadth_path'])
                    parent_bps_path.append(breadth)
                    next_unhandled.append({'node':child,'path':path,'tag':key,'siblings_seq':siblings_seq,'breadth':breadth,'depth':(depth+1),'orig_obj_path':parent_orig_obj_path,'breadth_path':parent_bps_path})
                    seq = seq + 1
            else:
                pass
        unhandled = next_unhandled
        depth = depth + 1
    next_unhandled = None
    unhandled = None
    #now sdict is in internal state
    if(js):
        hdict_str = json.dumps(hdict,sort_keys=True,indent=4)
        #json.dumps will convert number key to str key 
        #json.dumps({0:'a',1:'b'})
        #'{"0": "a", "1": "b"}'
        hdict = json.loads(hdict_str)
        # json.loads Expecting property name enclosed in double quotes:
        # json.loads('{0:"a",1:"b"}') ERROR
        # json.loads('{"0":"a","1":"b"}') OK 
    else:
        hdict_str = hdict.__str__()
    if(save):
        fd = open(kwargs['fn'],kwargs['op'])
        fd.write(hdict_str)
        fd.close()
    else:
        pass
    prdict = hdict_get_paths_relationship(hdict)
    #get final sdict
    sdict = hdict_fullfill_sdict(sdict,hdict,prdict)
    return({'hdict':hdict,'sdict':sdict,'prdict':prdict})

def hdict_get_paths_relationship(hdict):
    r = {}
    r['h:b'] = {():[]}
    r['b:h'] = {():[]}
    r['o:h'] = {():[]}
    r['h:o'] = {():[]}
    unhandled = []
    for i in range(0,hdict.__len__()):
        unhandled.append(hdict[i])
    while(unhandled.__len__()>0):
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            e = unhandled[i]
            h = e['path']
            b = e['breadth_path']
            o = e['orig_obj_path']
            try:
                t = e['attrib']['type']
            except:
                t = None
            else:
                pass
            r['h:b'][tuple(h)] = b
            r['b:h'][tuple(b)] = h
            r['h:o'][tuple(h)] = o
            r['o:h'][tuple(o)] = h
            if(e['children'].__len__() == 0):
                pass
            else:
                child = e['children']
                for j in range(0,child.__len__()):
                    next_unhandled.append(child[j])
        unhandled = next_unhandled
    return(r)

#----------------obdseleted-----------------------
def obseleted_hdict_fullfill_sdict(sdict,hdict,prdict):
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range(r.__len__()-1,-1,-1):
            d = r[j]
            d['leaf_sons'] = 0
            d['non_leaf_sons']= 0
            d['leaf_descendants']= 0
            d['non_leaf_descendants']= 0
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range(r.__len__()-1,-1,-1):
            d = r[j]
            if(d['breadth_path'].__len__()>1):
                parent_breadth = d['breadth_path'][-2]
                if('leaf_sons' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_sons'] = sdict[i-1][parent_breadth]['leaf_sons'] + 1
                    else:
                        pass
                else:
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_sons'] = 1
                    else:
                        pass
                if('non_leaf_sons' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        pass
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_sons'] = sdict[i-1][parent_breadth]['non_leaf_sons'] + 1
                else:
                    if(d['leaf']):
                        pass
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_sons'] = 1
                if('leaf_descendants' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_descendants'] = sdict[i-1][parent_breadth]['leaf_descendants']+d['leaf_descendants'] + 1
                    else:
                        sdict[i-1][parent_breadth]['leaf_descendants'] = sdict[i-1][parent_breadth]['leaf_descendants']+d['leaf_descendants']
                else:
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_descendants'] = d['leaf_descendants'] + 1
                    else:
                        sdict[i-1][parent_breadth]['leaf_descendants'] = d['leaf_descendants']
                if('non_leaf_descendants' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['non_leaf_descendants'] = sdict[i-1][parent_breadth]['non_leaf_descendants']+d['non_leaf_descendants'] 
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_descendants'] = sdict[i-1][parent_breadth]['non_leaf_descendants']+d['non_leaf_descendants'] + 1
                else:
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['non_leaf_descendants'] = d['non_leaf_descendants'] 
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_descendants'] = d['non_leaf_descendants'] + 1
            else:
                pass
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range(r.__len__()-1,-1,-1):
            d = r[j]
            d['hdict_parent_path'] = copy.copy(d['hdict_path'])
            d['hdict_parent_path'].pop(-1)
            d['orig_parent_path'] = copy.copy(d['orig_obj_path'])
            d['orig_parent_path'].pop(-1)
            d['hdict_lsib_path'] = hdict_lsib_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_lsib_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_lsib_path'])
            d['hdict_rsib_path'] = hdict_rsib_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_rsib_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_rsib_path'])
            d['hdict_lcin_path'] = hdict_lcin_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_lcin_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_lcin_path'])
            d['hdict_rcin_path'] = hdict_rcin_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_rcin_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_rcin_path'])
    return(sdict)

#--------------------------------------------------------



#---------------------

def hdict_fullfill_sdict(sdict,hdict,prdict):
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range(r.__len__()-1,-1,-1):
            d = r[j]
            d['leaf_sons'] = 0
            d['non_leaf_sons']= 0
            d['leaf_descendants']= 0
            d['non_leaf_descendants']= 0
            #################################
            d['leaf_son_pathlists'] = []
            d['non_leaf_son_pathlists']= []
            d['leaf_descendant_pathlists']= []
            d['non_leaf_descendant_pathlists']= []
            ##################################
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range(r.__len__()-1,-1,-1):
            d = r[j]
            if(d['breadth_path'].__len__()>1):
                parent_breadth = d['breadth_path'][-2]
                if('leaf_sons' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_sons'] = sdict[i-1][parent_breadth]['leaf_sons'] + 1
                        ########################
                        sdict[i-1][parent_breadth]['leaf_son_pathlists'].append(d['orig_obj_path'])
                        ########################
                    else:
                        pass
                else:
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_sons'] = 1
                        ########################
                        sdict[i-1][parent_breadth]['leaf_son_pathlists'].append(d['orig_obj_path'])
                        ########################
                    else:
                        pass
                if('non_leaf_sons' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        pass
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_sons'] = sdict[i-1][parent_breadth]['non_leaf_sons'] + 1
                        ########################
                        sdict[i-1][parent_breadth]['non_leaf_son_pathlists'].append(d['orig_obj_path'])
                        ########################
                else:
                    if(d['leaf']):
                        pass
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_sons'] = 1
                        ########################
                        sdict[i-1][parent_breadth]['non_leaf_son_pathlists'].append(d['orig_obj_path'])
                        ########################
                if('leaf_descendants' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_descendants'] = sdict[i-1][parent_breadth]['leaf_descendants']+d['leaf_descendants'] + 1
                        ##################################
                        sdict[i-1][parent_breadth]['leaf_descendant_pathlists'] = sdict[i-1][parent_breadth]['leaf_descendant_pathlists']+d['leaf_descendant_pathlists']
                        sdict[i-1][parent_breadth]['leaf_descendant_pathlists'].append(d['orig_obj_path'])
                        ##################################
                    else:
                        sdict[i-1][parent_breadth]['leaf_descendants'] = sdict[i-1][parent_breadth]['leaf_descendants']+d['leaf_descendants']
                        ##################################
                        sdict[i-1][parent_breadth]['leaf_descendant_pathlists'] = sdict[i-1][parent_breadth]['leaf_descendant_pathlists']+d['leaf_descendant_pathlists']
                        ###############################@@##
                        ###############################@@##
                else:
                    if(d['leaf']):
                        sdict[i-1][parent_breadth]['leaf_descendants'] = d['leaf_descendants'] + 1
                        ##################################
                        sdict[i-1][parent_breadth]['leaf_descendant_pathlists'] = d['leaf_descendant_pathlistss']
                        sdict[i-1][parent_breadth]['leaf_descendant_pathlists'].append(d['orig_obj_path'])
                        ##################################
                    else:
                        sdict[i-1][parent_breadth]['leaf_descendants'] = d['leaf_descendants']
                        ##################################
                        sdict[i-1][parent_breadth]['leaf_descendant_pathlists'] = d['leaf_descendant_pathlistss']
                        ##################################
                if('non_leaf_descendants' in sdict[i-1][parent_breadth]):
                    if(d['leaf']):
                        pass
                        ##################################
                        ##################################
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_descendants'] = sdict[i-1][parent_breadth]['non_leaf_descendants']+d['non_leaf_descendants'] + 1
                        ##################################
                        sdict[i-1][parent_breadth]['non_leaf_descendant_pathlists'] =  sdict[i-1][parent_breadth]['non_leaf_descendant_pathlists']+d['non_leaf_descendant_pathlists']
                        sdict[i-1][parent_breadth]['non_leaf_descendant_pathlists'].append(d['orig_obj_path'])
                        ##################################
                else:
                    if(d['leaf']):
                        pass
                        ##################################
                    else:
                        sdict[i-1][parent_breadth]['non_leaf_descendants'] = d['non_leaf_descendants'] + 1
                        ##################################
                        sdict[i-1][parent_breadth]['non_leaf_descendant_pathlists'] = d['non_leaf_descendant_pathlists']
                        sdict[i-1][parent_breadth]['non_leaf_descendant_pathlists'].append(d['orig_obj_path'])
                        ##################################
            else:
                pass
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range(r.__len__()-1,-1,-1):
            d = r[j]
            d['hdict_parent_path'] = copy.copy(d['hdict_path'])
            d['hdict_parent_path'].pop(-1)
            d['orig_parent_path'] = copy.copy(d['orig_obj_path'])
            d['orig_parent_path'].pop(-1)
            d['hdict_lsib_path'] = hdict_lsib_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_lsib_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_lsib_path'])
            d['hdict_rsib_path'] = hdict_rsib_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_rsib_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_rsib_path'])
            d['hdict_lcin_path'] = hdict_lcin_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_lcin_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_lcin_path'])
            d['hdict_rcin_path'] = hdict_rcin_path(hdict,sdict,prdict,d['hdict_path'])
            d['orig_rcin_path'] = hdict_path_to_orig_obj_path(prdict,d['hdict_rcin_path'])
    return(sdict)












#--------------------




def hdict_get_value(hdict,path_list_or_path_string,**kwargs):
    if('prdict' in kwargs):
        prdict = kwargs['prdict']
    else:
        prdict = hdict_get_paths_relationship(hdict)
    if('method' in kwargs):
        method = kwargs['method']
    else:
        method = 'orig_obj_path'
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if(utils.is_list(path_list_or_path_string)):
        pl = path_list_or_path_string
    else:
        pl = path_list_or_path_string.split(sp)
    if(method == 'hdict_path'):
        pass
    if(method == 'siblings_seq_path'):
        pl = siblings_seq_path_to_hdict_path(pl,sp=sp)
    if(method == 'breadth_path'):
        pl = breadth_path_to_hdict_path(prdict,pl,sp=sp)
    if(method == 'orig_obj_path'):
        pl = orig_obj_path_to_hdict_path(prdict,pl,sp=sp)
    rslt = utils.dict_getitem_via_path_list(hdict,pl,s2n=1)
    return(rslt)

def get_sdict_and_prdict_from_hdict(hdict,**kwargs):
    if('disable_type' in kwargs):
        disable_type = kwargs['disable_type']
    else:
        disable_type = 0
    sdict = {}
    unhandled = []
    depth = 0
    for i in range(0,hdict.__len__()):
        unhandled.append(hdict[i])
    while(unhandled.__len__()>0):
        sdict[depth] = {}
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            e = unhandled[i]
            sdict[depth][e['breadth']] = {}
            sdict[depth][e['breadth']]['text'] = e['text']
            sdict[depth][e['breadth']]['breadth_path'] = e['breadth_path']
            sdict[depth][e['breadth']]['hdict_path'] = e['path']
            sdict[depth][e['breadth']]['siblings_seq_path'] = hdict_path_to_siblings_seq_path(e['path'])
            sdict[depth][e['breadth']]['orig_obj_path'] = e['orig_obj_path']
            #
            sdict[depth][e['breadth']]['attrib'] = e['attrib']
            #
            if(disable_type):
                sdict[depth][e['breadth']]['type'] = None
            else:
                if('type' in e['attrib']):
                    sdict[depth][e['breadth']]['type'] = e['attrib']['type']
                else:
                    sdict[depth][e['breadth']]['type'] = None
            if(e['children'].__len__() == 0):
                sdict[depth][e['breadth']]['leaf'] = True
                sdict[depth][e['breadth']]['html_tag_lines'] = 3
            else:
                sdict[depth][e['breadth']]['leaf'] = False
                sdict[depth][e['breadth']]['html_tag_lines'] = 2
                children = e['children']
                for j in range(0,children.__len__()):
                    next_unhandled.append(children[j])
        unhandled = next_unhandled
        depth = depth + 1
    prdict = hdict_get_paths_relationship(hdict)
    #now sdict is internal state
    sdict = hdict_fullfill_sdict(sdict,hdict,prdict)
    #final state sdict
    return({'sdict':sdict,'prdict':prdict})

def get_path_list(path_list_or_path_string,sp):
    if(ltdict.is_ltdict(path_list_or_path_string)):
        path_list = ltdict.ltdict2list(path_list_or_path_string)
    elif(utils.is_list(path_list_or_path_string)):
        path_list = path_list_or_path_string
    else:
        path_list = path_list_or_path_string.split(sp)
    return(path_list)

def hdict_path_to_siblings_seq_path(path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    siblings_seq_path = []
    for i in range(0,path_list.__len__()):
        if(path_list[i] == 'children'):
            pass
        else:
            siblings_seq_path.append(path_list[i])
    return(siblings_seq_path)

def siblings_seq_path_to_hdict_path(path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    hdict_path = []
    for i in range(0,path_list.__len__()):
        hdict_path.append(path_list[i])
        hdict_path.append('children')
    hdict_path.pop(-1)
    return(hdict_path)

def hdict_path_to_breadth_path(hdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    temp = utils.dict_getitem_via_path_list(hdict,path_list,s2n=1)
    breadth_path = copy.copy(temp['breadth_path'])
    return(breadth_path)

def breadth_path_to_hdict_path(prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    hdict_path = prdict['b:h'][tuple(path_list)]
    return(hdict_path)

def orig_obj_path_to_hdict_path(prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    hdict_path = prdict['o:h'][tuple(path_list)]
    return(hdict_path)

def hdict_path_to_orig_obj_path(prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    orig_obj_path = prdict['h:o'][tuple(path_list)]
    return(orig_obj_path)

def breadth_path_to_sdict_location(path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    r = path_list.__len__() - 1
    if(r<0):
        c = -1
    else:
        c = path_list[-1]
    return(r,c)

def get_siblings_number_from_breadth_path(sdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    breadth_path = get_path_list(path_list_or_path_string,sp)
    parent_breadth_path = copy.copy(breadth_path)
    parent_breadth_path.pop(-1)
    if(parent_breadth_path.__len__()==0):
        siblings_number = 0
    else:
        r,c = breadth_path_to_sdict_location(parent_breadth_path,sp=sp)
        siblings_number = sdict[r][c]['leaf_sons'] + sdict[r][c]['non_leaf_sons']
    return(siblings_number)

def get_cousins_number_from_breadth_path(sdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    breadth_path = get_path_list(path_list_or_path_string,sp)
    depth = breadth_path.__len__() - 1
    cousins_number = sdict[depth].__len__()
    return(cousins_number)

def hdict_parent_path(hdict,pl,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl = get_path_list(pl,sp)
    pl = copy.copy(p1)
    p1 = p1[:-2]
    return(pl)

def hdict_lsib_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs): 
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    siblings_seq_path = hdict_path_to_siblings_seq_path(path_list,sp=sp)
    siblings_seq_path[-1] = siblings_seq_path[-1] - 1
    lsib_siblings_seq_path = siblings_seq_path
    if(lsib_siblings_seq_path[-1]<0):
        return([])
    else:
        lsib_hdict_path = siblings_seq_path_to_hdict_path(lsib_siblings_seq_path,sp=sp)
        return(lsib_hdict_path)

def hdict_rsib_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    breadth_path = hdict_path_to_breadth_path(hdict,path_list,sp=sp)
    max_siblings_seq = get_siblings_number_from_breadth_path(sdict,breadth_path,sp=sp) - 1
    siblings_seq_path = hdict_path_to_siblings_seq_path(path_list,sp=sp)
    siblings_seq_path[-1] = siblings_seq_path[-1] + 1
    rsib_siblings_seq_path = siblings_seq_path
    if(rsib_siblings_seq_path[-1]>max_siblings_seq):
        return([])
    else:
        rsib_hdict_path = siblings_seq_path_to_hdict_path(rsib_siblings_seq_path,sp=sp)
        return(rsib_hdict_path)

def hdict_lcin_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs): 
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    breadth_path = hdict_path_to_breadth_path(hdict,path_list,sp=sp)
    max_cousin_seq = get_cousins_number_from_breadth_path(sdict,breadth_path,sp=sp)
    r = breadth_path.__len__() - 1
    c = breadth_path[-1] - 1
    if(c<0):
        return([])
    else:
        siblings_seq_path = hdict_path_to_siblings_seq_path(path_list,sp=sp)
        siblings_seq_path[-1] = siblings_seq_path[-1] - 1
        lsib_siblings_seq_path = siblings_seq_path
        if(lsib_siblings_seq_path[-1]<0):
            lcin_breadth_path = sdict[r][c]['breadth_path']
            lcin_hdict_path = breadth_path_to_hdict_path(prdict,lcin_breadth_path,sp=sp)
        else:
            return([])
        return(lcin_hdict_path)

def hdict_rcin_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    breadth_path = hdict_path_to_breadth_path(hdict,path_list,sp=sp)
    max_cousin_seq = get_cousins_number_from_breadth_path(sdict,breadth_path,sp=sp) - 1
    max_siblings_seq = get_siblings_number_from_breadth_path(sdict,breadth_path,sp=sp) - 1
    r = breadth_path.__len__() - 1
    c = breadth_path[-1] + 1
    if(c>max_cousin_seq):
        return([])
    else:
        siblings_seq_path = hdict_path_to_siblings_seq_path(path_list,sp=sp)
        siblings_seq_path[-1] = siblings_seq_path[-1] + 1
        rsib_siblings_seq_path = siblings_seq_path
        if(rsib_siblings_seq_path[-1]>max_siblings_seq):
            rcin_breadth_path = sdict[r][c]['breadth_path']
            rcin_hdict_path = breadth_path_to_hdict_path(prdict,rcin_breadth_path,sp=sp)
        else:
            return([])
    return(rcin_hdict_path)

def orig_parent_path(hdict,pl,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl = get_path_list(pl,sp)
    pl = copy.copy(p1)
    p1 = p1[:-1]
    return(pl)

def orig_lsib_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    lsib_hdict_path = hdict_lsib_path(hdict,sdict,prdict,pl,sp=sp)
    orig_lsib_path = hdict_path_to_orig_obj_path(prdict,lsib_hdict_path,sp=sp)
    return(orig_lsib_path)

def orig_rsib_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    rsib_hdict_path = hdict_rsib_path(hdict,sdict,prdict,pl,sp=sp)
    orig_rsib_path = hdict_path_to_orig_obj_path(prdict,rsib_hdict_path,sp=sp)
    return(orig_rsib_path)

def orig_lcin_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    lcin_hdict_path = hdict_lcin_path(hdict,sdict,prdict,pl,sp=sp)
    orig_lcin_path = hdict_path_to_orig_obj_path(prdict,lcin_hdict_path,sp=sp)
    return(orig_lcin_path)

def orig_rcin_path(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    rcin_hdict_path = hdict_rcin_path(hdict,sdict,prdict,pl,sp=sp)
    orig_rcin_path = hdict_path_to_orig_obj_path(prdict,rcin_hdict_path,sp=sp)
    return(orig_rcin_path)

def hdict_relationship(pl1,pl2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl1 = get_path_list(pl2,sp)
    bp1 = hdict_path_to_breadth_path(hdict,pl1,sp=sp)
    bp2 = hdict_path_to_breadth_path(hdict,pl2,sp=sp)
    len1 = bp1.__len__()
    len2 = bp2.__len__()
    i = 0
    while((i<len1) & (i<len2)):
        if(bp1[i] == bp2[i]):
            i = i + 1
        else:
            break
    if((i==len1)|(i==len2)):
        nearest_ancestor = []
    else:
        nearest_ancestor = []
        for j in range(0,i):
            nearest_ancestor.append(bp1[j])
    dist = len1 - nearest_ancestor.__len__() + len2 - nearest_ancestor.__len__()
    nearest_ancestor = breadth_path_to_hdict_path(prdict,nearest_ancestor,sp=sp)
    l = nearest_ancestor.__len__()
    ancestor_to_x = copy.copy(pl1)[i:]
    ancestor_to_y = copy.copy(pl2)[i:]
    rel = {}
    rel['dist'] = dist
    rel['nearest_ancestor'] = nearest_ancestor
    rel['ancestor_to_x'] = ancestor_to_x
    rel['ancestor_to_y'] = ancestor_to_y
    return(rel)

def hdict_is_ancestor(pl1,pl2):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    pl1 = hdict_path_to_breadth_path(pl1)
    pl2 = hdict_path_to_breadth_path(pl2)
    if(pl1.__len__()<pl2.__len__()):
        if(pl1[:pl1.__len__()] == pl2[:pl1.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def hdict_is_parent(pl1,pl2):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    pl1 = hdict_path_to_breadth_path(pl1)
    pl2 = hdict_path_to_breadth_path(pl2)
    if(pl1.__len__()==(pl2.__len__()-1)):
        if(pl1[:pl1.__len__()] == pl2[:pl1.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def hdict_is_decesdant(pl1,pl2):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    pl1 = hdict_path_to_breadth_path(pl1)
    pl2 = hdict_path_to_breadth_path(pl2)
    if(pl1.__len__()>pl2.__len__()):
        if(pl1[:pl2.__len__()] == pl2[:pl2.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def hdict_is_son(pl1,pl2):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    pl1 = hdict_path_to_breadth_path(pl1)
    pl2 = hdict_path_to_breadth_path(pl2)
    if(pl1.__len__()==(pl2.__len__()+1)):
        if(pl1[:pl2.__len__()] == pl2[:pl2.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def hdict_is_lsib(pl1,pl2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    lsibp = hdict_lsib_path(hdict,sdict,prdict,pl2,sp=sp)
    if(lsibp == pl1):
        return(True)
    else:
        return(False)

def hdict_is_rsib(pl1,pl2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    rsibp = hdict_rsib_path(hdict,sdict,prdict,pl2,sp=sp)
    if(rsibp == pl1):
        return(True)
    else:
        return(False)

def hdict_is_lcin(pl1,pl2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    lcinp = hdict_lcin_path(hdict,sdict,prdict,pl2,sp=sp)
    if(lcinp == pl1):
        return(True)
    else:
        return(False)

def hdict_is_rcin(pl1,pl2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    pl1 = get_path_list(pl1,sp)
    pl2 = get_path_list(pl2,sp)
    rcinp = hdict_rcin_path(hdict,sdict,prdict,pl2,sp=sp)
    if(rcinp == pl1):
        return(True)
    else:
        return(False)

def orig_relationship(ol1,ol2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    len1 = ol1.__len__()
    len2 = ol2.__len__()
    i = 0
    while((i<len1) & (i<len2)):
        if(ol1[i] == ol2[i]):
            i = i + 1
        else:
            break
    if((i==len1)|(i==len2)):
        nearest_ancestor = []
    else:
        nearest_ancestor = []
        for j in range(0,i):
            nearest_ancestor.append(ol1[j])
    dist = len1 - nearest_ancestor.__len__() + len2 - nearest_ancestor.__len__()
    l = nearest_ancestor.__len__()
    ancestor_to_x = copy.copy(ol1)[i:]
    ancestor_to_y = copy.copy(ol2)[i:]
    rel = {}
    rel['dist'] = dist
    rel['nearest_ancestor'] = nearest_ancestor
    rel['ancestor_to_x'] = ancestor_to_x
    rel['ancestor_to_y'] = ancestor_to_y
    return(rel)

def orig_is_ancestor(ol1,ol2,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if(ol1.__len__()<ol2.__len__()):
        if(ol1[:ol1.__len__()] == ol2[:ol1.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def orig_is_parent(ol1,ol2,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if(ol1.__len__()==(ol2.__len__()-1)):
        if(ol1[:ol1.__len__()] == ol2[:ol1.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def orig_is_decesdant(ol1,ol2,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if(ol1.__len__()>ol2.__len__()):
        if(ol1[:ol2.__len__()] == ol2[:ol2.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def orig_is_son(ol1,ol2,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    if(ol1.__len__()==(ol2.__len__()+1)):
        if(ol1[:ol2.__len__()] == ol2[:ol2.__len__()]):
            return(True)
        else:
            return(False)
    else:
        return(False)

def orig_is_lsib(ol1,ol2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol1 = get_path_list(ol1,sp)
    ol2 = get_path_list(ol2,sp)
    lsibp = orig_lsib_path(hdict,sdict,prdict,ol2,sp=sp)
    if(lsibp == ol1):
        return(True)
    else:
        return(False)

def orig_is_rsib(ol1,ol2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol1 = get_path_list(ol1,sp)
    ol2 = get_path_list(ol2,sp)
    rsibp = orig_rsib_path(hdict,sdict,prdict,ol2,sp=sp)
    if(rsibp == ol1):
        return(True)
    else:
        return(False)

def orig_is_lcin(ol1,ol2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol1 = get_path_list(ol1,sp)
    ol2 = get_path_list(ol2,sp)
    lcinp = orig_lcin_path(hdict,sdict,prdict,ol2,sp=sp)
    if(lcinp == ol1):
        return(True)
    else:
        return(False)

def orig_is_rcin(ol1,ol2,hdict,sdict,prdict,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol1 = get_path_list(ol1,sp)
    ol2 = get_path_list(ol2,sp)
    rcinp = orig_rcin_path(hdict,sdict,prdict,ol2,sp=sp)
    if(rcinp == ol1):
        return(True)
    else:
        return(False)

def hdict_parent(hdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    ppl = hdict_parent_path(hdict,path_list,sp=sp)
    rslt = hdict_get_value(hdict,ppl,method='hdict_path')
    return(rslt)

def hdict_lsib(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    lsibpl = hidct_lsib_path(hdict,sdict,prdict,path_list,sp=sp)
    rslt = hdict_get_value(hdict,lsibpl,method='hdict_path')
    return(rslt)

def hdict_rsib(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    rsibpl = hidct_rsib_path(hdict,sdict,prdict,path_list,sp=sp)
    rslt = hdict_get_value(hdict,rsibpl,method='hdict_path')
    return(rslt)

def hdict_lcin(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    lcinpl = hidct_lcin_path(hdict,sdict,prdict,path_list,sp=sp)
    rslt = hdict_get_value(hdict,lcinpl,method='hdict_path')
    return(rslt)

def hdict_rcin(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    path_list = get_path_list(path_list_or_path_string,sp)
    rcinpl = hidct_rcin_path(hdict,sdict,prdict,path_list,sp=sp)
    rslt = hdict_get_value(hdict,rcinpl,method='hdict_path')
    return(rslt)

def orig_parent(obj,hdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    ppl = hidct_parent_path(hdict,pl,sp=sp)
    pol = hdict_path_to_orig_obj_path(prdict,ppl,sp=sp)
    rslt = utils.dict_getitem_via_path_list(obj,pol,s2n=1)
    return(rslt)

def orig_lsib(obj,hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    lsibpl = hdict_lsib_path(hdict,sdict,prdict,pl,sp=sp)
    lsibol = hdict_path_to_orig_obj_path(prdict,lsibpl,sp=sp)
    rslt = utils.dict_getitem_via_path_list(obj,lsibol,s2n=1)
    return(rslt)

def orig_rsib(hdict,sdict,prdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    rsibpl = hdict_rsib_path(hdict,sdict,prdict,pl,sp=sp)
    rsibol = hdict_path_to_orig_obj_path(prdict,rsibpl,sp=sp)
    rslt = utils.dict_getitem_via_path_list(obj,rsibol,s2n=1)
    return(rslt)

def orig_lcin(hdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    lcinpl = hdict_lcin_path(hdict,sdict,prdict,pl,sp=sp)
    lcinol = hdict_path_to_orig_obj_path(prdict,lcinpl,sp=sp)
    rslt = utils.dict_getitem_via_path_list(obj,lcinol,s2n=1)
    return(rslt)

def orig_rcin(hdict,path_list_or_path_string,**kwargs):
    if('sp' in kwargs):
        sp = kwargs['sp']
    else:
        sp = '/'
    ol = get_path_list(path_list_or_path_string,sp)
    pl = orig_obj_path_to_hdict_path(prdict,ol,sp=sp)
    rcinpl = hdict_rcin_path(hdict,sdict,prdict,pl,sp=sp)
    rcinol = hdict_path_to_orig_obj_path(prdict,rcinpl,sp=sp)
    rslt = utils.dict_getitem_via_path_list(obj,rcinol,s2n=1)
    return(rslt)

def hdict_to_obj(hdict,sdict,prdict,**kwargs):
    def add_dict_tree_entry(obj,path,value,n2s=0,s2n=0):
        utils.dict_setdefault_via_path_list(obj,path,n2s=n2s,s2n=s2n)
        utils.dict_setitem_via_path_list(obj,path,value,n2s=n2s,s2n=s2n)
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('check_type' in kwargs):
        check_type = kwargs['check_type']
    else:
        check_type = 1
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if(deepcopy):
        newh = copy.copy(hdict)
    else:
        newh = hdict
    obj = {}
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range (0,r.__len__()):
            c = r[j]
            path = c['orig_obj_path']
            if(c['leaf']):
                if((c['type']== '') | (c['type']=='dict') ):
                    value = {}
                elif((c['type']== 'list')):
                    value = []
                elif((c['type']== 'tuple')):
                    value =()
                elif((c['type']== 'set')):
                    value = set({})
                elif((c['type']== 'str')):
                    value = utils.dict_getitem_via_path_list(newh,c['hdict_path'],n2s=n2s,s2n=s2n)
                    value = value['text']
                    value = str(value)
                elif((c['type']== 'int')):
                    value = utils.dict_getitem_via_path_list(newh,c['hdict_path'],n2s=n2s,s2n=s2n)
                    value = value['text']
                    value = int(value)
                elif((c['type']== 'float')):
                    value = utils.dict_getitem_via_path_list(newh,c['hdict_path'],n2s=n2s,s2n=s2n)
                    value = value['text']
                    value = float(value)
                else:
                    value = utils.dict_getitem_via_path_list(newh,c['hdict_path'],n2s=n2s,s2n=s2n)
                    value = value['text']
                add_dict_tree_entry(obj,path,value,n2s=n2s,s2n=s2n)
            else:
                if((c['type']== '') | (c['type']=='dict') ):
                    pass
                elif((c['type']== 'list')):
                    value = utils.dict_getitem_via_path_list(obj,path,n2s=n2s,s2n=s2n)
                    new_value = []
                    for k in range(0,value.__len__()):
                        new_value.append(value[k])
                    utils.dict_setitem_via_path_list(obj,path,new_value,n2s=n2s,s2n=s2n)
                elif((c['type']== 'tuple')):
                    value = utils.dict_getitem_via_path_list(obj,path,n2s=n2s,s2n=s2n)
                    new_value = []
                    for k in range(0,value.__len__()):
                        new_value.append(value[k])
                    new_value = tuple(new_value)
                    utils.dict_setitem_via_path_list(obj,path,new_value,n2s=n2s,s2n=s2n)
                elif((c['type']== 'set')):
                    value = utils.dict_getitem_via_path_list(obj,path,n2s=n2s,s2n=s2n)
                    new_value = []
                    for k in range(0,value.__len__()):
                        new_value.append(value[k])
                    new_value = set(new_value)
                    utils.dict_setitem_via_path_list(obj,path,new_value,n2s=n2s,s2n=s2n)
                else:
                    pass
    return(obj)

def xml_indent_prepend(path_list_or_path_string,**kwargs):
    if('fixed_indent' in kwargs):
        fixed_indent = kwargs['fixed_indent']
    else:
        fixed_indent = 0
    if('indent' in kwargs):
        indent = kwargs['indent']
    else:
        indent = 4
    if('path_sp' in kwargs):
        path_sp = kwargs['path_sp']
    else:
        path_sp = '/'
    pl = get_path_list(path_list_or_path_string,path_sp)
    if(fixed_indent):
        prepend = ' '*4*pl.__len__()
    else:
        c = 0
        for i in range(0,pl.__len__()):
           c = c + str(pl[i]).__len__()+2
        prepend = ' '*c
    return(prepend)

def attrib_dict_to_str(attrib):
    s = ''
    for key in attrib:
        if(attrib[key]):
            s = ''.join((s,' ',key,'=','"',str(attrib[key]),'"'))
        else:
            s = ''.join((s,' ',key))
    return(s)

def creat_xml_tag_line_label(sdict,**kwargs):
    if('noattrib' in kwargs):
        noattrib = kwargs['noattrib']
    else:
        noattrib = 0
    if('clear' in kwargs):
        clear = kwargs['clear']
    else:
        clear = 1
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 0
    if(deepcopy):
        sdict = copy.deepcopy(sdict)
    else:
        pass
    if(clear):
        for i in range(sdict.__len__()-1,-1,-1):
            r = sdict[i]
            for j in range(r.__len__()-1,-1,-1):
                d = r[j]
                d['html_tag_lines'] = 0
                d['start_tagn'] = 0
                d['end_tagn'] = 0
                if(d['leaf']):
                    d['html_tag_lines'] = 3
                else:
                    d['html_tag_lines'] = 2
    else:
        pass
    for i in range(sdict.__len__()-1,-1,-1):
        r = sdict[i]
        for j in range(r.__len__()-1,-1,-1):
            d = r[j]
            pbp = copy.copy(d['breadth_path'])
            pbp.pop(-1)
            h,v = breadth_path_to_sdict_location(pbp)
            if((h==-1)|(v==-1)):
                pass
            else:
                sdict[h][v]['html_tag_lines'] = sdict[h][v]['html_tag_lines']+d['html_tag_lines']
    for i in range(0,sdict.__len__()):
        r = sdict[i]
        for j in range(0,r.__len__()):
            d = r[j]
            if((j==0)&(i==0)):
                cursor = 0
            ssp = copy.copy(d['siblings_seq_path'])
            sibn = ssp.pop(-1)
            if(sibn == 0):
                pbp = copy.copy(d['breadth_path'])
                pbp.pop(-1)
                h,v = breadth_path_to_sdict_location(pbp)
                if((h==-1)&(v==-1)):
                    pass
                else:
                    p = sdict[h][v]
                    cursor = p['start_tagn'] + 1
            else:
                pass
            d['start_tagn'] = cursor
            d['end_tagn'] = cursor + d['html_tag_lines'] -1
            cursor = d['end_tagn'] + 1
    html_lines = {}
    for i in range(0,sdict.__len__()):
        r = sdict[i]
        for j in range(0,r.__len__()):
            d = r[j]
            pol = copy.copy(d['orig_obj_path'])
            tag = pol.pop(-1)
            prepend = xml_indent_prepend(pol)
            if(noattrib):
                attrib =''
            else:
                attrib = attrib_dict_to_str(d['attrib'])
            html_lines[d['start_tagn']] = ''.join((prepend,'<',str(tag),attrib,'>'))
            html_lines[d['end_tagn']] = ''.join((prepend,'</',str(tag),'>'))
            #
            d['start_html_line'] = html_lines[d['start_tagn']]
            d['end_html_line'] = html_lines[d['end_tagn']]
            #
            if(d['leaf']):
                ol = copy.copy(d['orig_obj_path'])
                prepend = xml_indent_prepend(ol)
                #
                if(None == d['text']):
                    html_text = ''
                    prepend = ''
                else:
                    html_text = cgi.escape(str(d['text']))
                #
                html_lines[d['start_tagn']+1] = ''.join((prepend,html_text))
                #
                d['text_html_line'] = html_lines[d['start_tagn']+1]
                #
            else:
                #
                d['text_html_line'] = None
                #
    return({'sdict':sdict,'html_lines':html_lines})

def hdict_to_xml(hdict,**kwargs):
    if('disable_type' in kwargs):
        disable_type = kwargs['disable_type']
    else:
        disable_type = 0
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    temp = get_sdict_and_prdict_from_hdict(hdict,disable_type = disable_type)
    sdict = temp['sdict']
    prdict = temp['prdict']
    tmp = creat_xml_tag_line_label(sdict)
    sdict = tmp['sdict']
    tag_lines = tmp['html_lines']
    rslt = ''
    for i in range(0,tag_lines.__len__()):
        if(tag_lines[i] == ''):
            pass
        else:
            rslt = ''.join((rslt,tag_lines[i],line_sp))
    rslt = utils.str_rstrip(rslt,line_sp,1)
    return(rslt)


def hspr_to_xml(hspr,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    sdict = hspr['sdict']
    prdict = hspr['prdict']
    tmp = creat_xml_tag_line_label(sdict)
    sdict = tmp['sdict']
    tag_lines = tmp['html_lines']
    rslt = ''
    for i in range(0,tag_lines.__len__()):
        if(tag_lines[i] == ''):
            pass
        else:
            rslt = ''.join((rslt,tag_lines[i],line_sp))
    rslt = utils.str_rstrip(rslt,line_sp,1)
    return(rslt)





def obj_to_xml(obj,**kwargs):
    if('line_sp' in kwargs):
        line_sp = kwargs['line_sp']
    else:
        line_sp = '\n'
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    temp = obj_to_hdict(obj,s2n=s2n,n2s=n2s)
    sdict = temp['sdict']
    hdict = temp['hdict']
    prdict = temp['prdict']
    if('disable_type' in kwargs):
        disable_type = kwargs['disable_type']
    else:
        disable_type = 0
    rslt = hdict_to_xml(hdict,line_sp =line_sp,disable_type = disable_type)
    return(rslt)

def path_list_to_console_key_str(pl):
    rslt = ''
    for i in range(0,pl.__len__()):
        temp = pl[i]
        if(utils.is_int(temp)):
            temp = str(temp)
        else:
            temp = ''.join(('"',temp,'"'))
        rslt = ''.join((rslt,'[',temp,']'))
    return(rslt)
    
