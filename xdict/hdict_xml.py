import copy
from lxml import etree
from xdict import utils
from xdict import hdict_object

def get_lxml_etree_root_type():
    html_text='<html><boby></body></html>'
    root = etree.HTML(html_text)
    return(type(root))

def attrib_str_to_dict(attrib_str):
    html_text = ''
    html_text = ''.join(('<div ',attrib_str,'>','\n','</div>'))
    root = etree.HTML(html_text)
    child = root.getchildren()[0]
    child = child.getchildren()[0]
    return(child.attrib)

def html_to_hdict(**kwargs):
    if('html_file_path' in kwargs):
        html_file_path = kwargs['html_file_path']
        fd = open(html_file_path,'r') 
        html_text = fd.read()
        fd.close()
        root = etree.HTML(html_text)
    elif('html_text' in kwargs):
        html_text = kwargs['html_text']
        root = etree.HTML(html_text)
    else:
        root = kwargs['root']
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('s2n' in kwargs):
        s2n = kwargs['n2s']
    else:
        s2n = 0
    if('get_sdict' in kwargs):
        get_sdict = kwargs['get_sdict']
    else:
        get_sdict =1
    if('sdict' in kwargs):
        sdict = kwargs['sdict']
    else:
        sdict = {}
    def add_dict_tree_entry(hdict,path,value={},n2s=0,s2n=0):
        utils.dict_setdefault_via_path_list(hdict,path,n2s=n2s,s2n=s2n)
        if(value == {}):
            # necessary to avoid Ellipsis ISSUE, unknown reason
            pass
        else:
            utils.dict_setitem_via_path_list(hdict,path,value,n2s=n2s,s2n=s2n)
    hdict = {}
    unhandled = [{'node':root,'path':[0],'tag':root.tag,'siblings_seq':0,'breadth':0,'depth':0,'orig_obj_path':[root.tag],'breadth_path':[0]}]
    depth = 0
    while(unhandled.__len__()>0):
        sdict[depth] = {}
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            parent = unhandled[i]['node']
            parent_path = unhandled[i]['path']
            add_dict_tree_entry(hdict,parent_path)
            parent_path_path = copy.copy(parent_path)
            parent_path_path.append('path')
            add_dict_tree_entry(hdict,parent_path_path,parent_path,s2n=s2n,n2s=n2s)
            parent_tag_path = copy.copy(parent_path)
            parent_tag_path.append('tag')
            add_dict_tree_entry(hdict,parent_tag_path,parent.tag)
            parent_attrib_path = copy.copy(parent_path)
            parent_attrib_path.append('attrib')
            add_dict_tree_entry(hdict,parent_attrib_path,parent.attrib)
            parent_deepth_path = copy.copy(parent_path)
            parent_deepth_path.append('depth')
            add_dict_tree_entry(hdict,parent_deepth_path,unhandled[i]['depth'])
            parent_text_path = copy.copy(parent_path)
            parent_text_path.append('text')
            text_temp = parent.text
            add_dict_tree_entry(hdict,parent_text_path,text_temp)
            parent_siblings_seq_path = copy.copy(parent_path)
            parent_siblings_seq_path.append('siblings_seq')
            add_dict_tree_entry(hdict,parent_siblings_seq_path,unhandled[i]['siblings_seq'])
            parent_breadth_path = copy.copy(parent_path)
            parent_breadth_path.append('breadth')
            add_dict_tree_entry(hdict,parent_breadth_path,unhandled[i]['breadth'])
            #
            parent_orig_obj_path_path = copy.copy(parent_path)
            parent_orig_obj_path_path.append('orig_obj_path')
            add_dict_tree_entry(hdict,parent_orig_obj_path_path,unhandled[i]['orig_obj_path'],s2n=s2n,n2s=n2s)
            parent_bps_path = copy.copy(parent_path)
            parent_bps_path.append('breadth_path')
            add_dict_tree_entry(hdict,parent_bps_path,unhandled[i]['breadth_path'],s2n=s2n,n2s=n2s)
            #
            parent_children_path = copy.copy(parent_path)
            parent_children_path.append('children')
            add_dict_tree_entry(hdict,parent_children_path)
            children = parent.getchildren()
            #
            if(get_sdict):
                siblings_seq_path = hdict_object.hdict_path_to_siblings_seq_path(parent_path)
                sdict[depth][unhandled[i]['breadth']] = {}
                sdict[depth][unhandled[i]['breadth']]['text'] = text_temp
                sdict[depth][unhandled[i]['breadth']]['attrib'] = parent.attrib
                sdict[depth][unhandled[i]['breadth']]['breadth_path'] = unhandled[i]['breadth_path']
                sdict[depth][unhandled[i]['breadth']]['hdict_path'] = parent_path
                sdict[depth][unhandled[i]['breadth']]['siblings_seq_path'] = siblings_seq_path
                sdict[depth][unhandled[i]['breadth']]['orig_obj_path'] = unhandled[i]['orig_obj_path']
                if(children.__len__()>0):
                    sdict[depth][unhandled[i]['breadth']]['leaf'] = False
                    sdict[depth][unhandled[i]['breadth']]['html_tag_lines'] = 2
                else:
                    sdict[depth][unhandled[i]['breadth']]['leaf'] = True
                    sdict[depth][unhandled[i]['breadth']]['html_tag_lines'] = 3
                #xml to hdict not use type , type is used when obj to type 
                sdict[depth][unhandled[i]['breadth']]['type'] = None
            else:
                pass
            #
            for j in range(0,children.__len__()):
                child = children[j]
                breadth = next_unhandled.__len__()
                siblings_seq = j
                parent_path = copy.copy(unhandled[i]['path'])
                parent_path.append('children')
                parent_path.append(siblings_seq)
                path = parent_path
                parent_bps_path = copy.copy(unhandled[i]['breadth_path'])
                parent_bps_path.append(breadth)
                parent_orig_obj_path = copy.copy(unhandled[i]['orig_obj_path'])
                parent_orig_obj_path.append(child.tag)
                next_unhandled.append({'node':child,'path':path,'tag':child.tag,'siblings_seq':siblings_seq,'breadth':breadth,'depth':(depth+1),'orig_obj_path':parent_orig_obj_path,'breadth_path':parent_bps_path})
        unhandled = next_unhandled
        depth = depth + 1
    next_unhandled = None
    unhandled = None
    prdict = hdict_object.hdict_get_paths_relationship(hdict)
    #get final sdict
    sdict = hdict_object.hdict_fullfill_sdict(sdict,hdict,prdict)
    rslt = {'hdict':hdict,'sdict':sdict,'prdict':prdict}
    if('save' in kwargs):
       if(kwargs['save']==1):
           fd = open(kwargs['fn'],kwargs['op'])
           fd.write(rslt.__str__())
           fd.close()
    else:
       pass
    return(rslt)


