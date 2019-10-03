from xdict import utils
from xdict import jprint
from xdict import cmdline
from xdict import hdict_object
from xdict import hdict_xml


class description():
    def __init__(self,**kwargs):
        if('readable_path' in kwargs):
            self.readable_path = kwargs['readable_path']
        else:
            self.readable_path = None
        if('pathlist' in kwargs):
            self.pathlist = kwargs['pathlist']
        else:
            self.pathlist = None
        if('depth' in kwargs):
            self.depth = kwargs['depth']
        else:
            self.depth = None
        if('breadth' in kwargs):
            self.breadth = kwargs['breadth']
        else:
            self.breadth = None
        if('siblings_seq' in kwargs):
            self.siblings_seq = kwargs['siblings_seq']
        else:
            self.siblings_seq = None
        if('tag' in kwargs):
            self.tag = kwargs['tag']
        else:
            self.tag = None
        if('attrib' in kwargs):
            self.attrib = kwargs['attrib']
        else:
            self.attrib = None
        if('text' in kwargs):
            self.text = kwargs['text']
        else:
            self.text = None
        if('type' in kwargs):
            self.type = kwargs['type']
        else:
            self.type = None
        if('leaf' in kwargs):
            self.leaf = kwargs['leaf']
        else:
            self.leaf = None
        if('leaf_sons' in kwargs):
            self.leaf_sons = kwargs['leaf_sons']
        else:
            self.leaf_sons = None
        if('nonleaf_sons' in kwargs):
            self.nonleaf_sons = kwargs['nonleaf_sons']
        else:
            self.nonleaf_sons = None
        if('leaf_descendants' in kwargs):
            self.leaf_descendants = kwargs['leaf_descendants']
        else:
            self.leaf_descendants = None
        if('nonleaf_descendants' in kwargs):
            self.nonleaf_descendants = kwargs['nonleaf_descendants']
        else:
            self.nonleaf_descendants = None
    def __dir__(self):
        l = ['readable_path','pathlist','depth','breadth','siblings_seq','tag','attrib','text','type','leaf','leaf_sons','nonleaf_sons','leaf_descendants','nonleaf_descendants']
        jprint.pobj(l)
        return(l)
    def __repr__(self):
        printed_str = ''
        l = ['readable_path','pathlist','depth','breadth','siblings_seq','tag','attrib','text','type','leaf','leaf_sons','nonleaf_sons','leaf_descendants','nonleaf_descendants']
        for i in range(0,l.__len__()):
            s = '{0} : {1}'.format(l[i],str(self.__getattribute__(l[i])))
            printed_str = ''.join((printed_str,s,'\n'))
        return(printed_str)

class nodedescription():
    def __init__(self,**kwargs):
        if('readable_path' in kwargs):
            self.readable_path = kwargs['readable_path']
        else:
            self.readable_path = None
        if('pathlist' in kwargs):
            self.pathlist = kwargs['pathlist']
        else:
            self.pathlist = None
        if('depth' in kwargs):
            self.depth = kwargs['depth']
        else:
            self.depth = None
        if('breadth' in kwargs):
            self.breadth = kwargs['breadth']
        else:
            self.breadth = None
        if('siblings_seq' in kwargs):
            self.siblings_seq = kwargs['siblings_seq']
        else:
            self.siblings_seq = None
        if('tag' in kwargs):
            self.tag = kwargs['tag']
        else:
            self.tag = None
        if('attrib' in kwargs):
            self.attrib = kwargs['attrib']
        else:
            self.attrib = None
        if('text' in kwargs):
            self.text = kwargs['text']
        else:
            self.text = None
        if('type' in kwargs):
            self.type = kwargs['type']
        else:
            self.type = None
        if('leaf' in kwargs):
            self.leaf = kwargs['leaf']
        else:
            self.leaf = None
        if('leaf_sons' in kwargs):
            self.leaf_sons = kwargs['leaf_sons']
        else:
            self.leaf_sons = None
        if('nonleaf_sons' in kwargs):
            self.nonleaf_sons = kwargs['nonleaf_sons']
        else:
            self.nonleaf_sons = None
        if('leaf_descendants' in kwargs):
            self.leaf_descendants = kwargs['leaf_descendants']
        else:
            self.leaf_descendants = None
        if('nonleaf_descendants' in kwargs):
            self.nonleaf_descendants = kwargs['nonleaf_descendants']
        else:
            self.nonleaf_descendants = None
        if('lsib' in kwargs):
            self.lsib = kwargs['lsib']
        else:
            self.lsib = None
        if('rsib' in kwargs):
            self.rsib = kwargs['rsib']
        else:
            self.rsib = None
        if('lcin' in kwargs):
            self.lcin = kwargs['lcin']
        else:
            self.lcin = None
        if('rcin' in kwargs):
            self.rcin = kwargs['rcin']
        else:
            self.rcin = None
    def __dir__(self):
        l = ['readable_path','pathlist','depth','breadth','siblings_seq','tag','attrib','text','type','leaf','leaf_sons','nonleaf_sons','leaf_descendants','nonleaf_descendants','lsib','rsib','lcin','rcin']
        jprint.pobj(l)
        return(l)
    def __repr__(self):
        printed_str = ''
        l = ['readable_path','pathlist','depth','breadth','siblings_seq','tag','attrib','text','type','leaf','leaf_sons','nonleaf_sons','leaf_descendants','nonleaf_descendants','lsib','rsib','lcin','rcin']
        for i in range(0,l.__len__()):
            s = '{0} : {1}'.format(l[i],str(self.__getattribute__(l[i])))
            printed_str = ''.join((printed_str,s,'\n'))
        return(printed_str)

class hdict():
    '''
        from xdict.HdictLib import hdict
        from xdict.jprint import pobj
        currd = {'UseSpeedLimits': None, 'RuleIDs': [11516125, 11516163, 11516164], 'Displays': [{'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 37, 'RuleID': None}, 'Row2': {'Row': None, 'RuleID': 11516125}, 'Views': [{'Row': None, 'RuleID': 11516163}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 39, 'RuleID': None}, 'Row2': {'Row': 41, 'RuleID': None}, 'Views': [{'Row': 40, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 38, 'RuleID': None}, 'Row2': {'Row': 68, 'RuleID': None}, 'Views': [{'Row': 10, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 48, 'RuleID': None}, 'Row2': {'Row': 49, 'RuleID': None}, 'Views': [{'Row': 50, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 51, 'RuleID': None}, 'Row2': {'Row': 52, 'RuleID': None}, 'Views': [{'Row': 53, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 54, 'RuleID': None}, 'Row2': {'Row': 56, 'RuleID': None}, 'Views': [{'Row': 57, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': 58, 'RuleID': None}, 'Row2': {'Row': 59, 'RuleID': None}, 'Views': [{'Row': 12, 'RuleID': None}]}, {'RequiresHRBelt': None, 'Type': 5, 'Row1': {'Row': None, 'RuleID': 11516164}, 'Row2': {'Row': 4, 'RuleID': None}, 'Views': [{'Row': 20, 'RuleID': None}]}], 'AutomaticLogRecording': None, 'AutoPause': None, 'LoggedRuleIDs': [11516163, 11516164, 11516125]}
        hdict1 = hdict.hdict(object=currd)
        dir(hdict1)
        
        hdict1.depth
        hdict.widths
        print(hdict1.html)
        hdict1.showall()
        hdict1.search('uleIDs')
        
        
    '''
    def __init__(self,**kwargs):
        if('object' in kwargs):
            self.object = kwargs['object']
            hspr = hdict_object.obj_to_hdict(self.object)
            self.cmdt = cmdline.cmdict(dict=self.object)
            self.html = hdict_object.hspr_to_xml(hspr)
            self.orig = 'object'
        elif('html' in kwargs):
            self.html = kwargs['html']
            hspr = hdict_xml.html_to_hdict(html_text=self.html)
            self.cmdt = cmdline.cmdict(html_text=self.html)
            self.object = hdict_object.hdict_to_obj(hspr['hdict'],hspr['sdict'],hspr['prdict'])
            self.orig = 'html'
        elif('cmdline' in kwargs):
            self.cmdt = kwargs['cmdline']
            cmdlines_full_dict = {}
            cmdlines_full_dict['cmds'] = self.cmdt.cmdlines
            cmdlines_full_dict['attribs'] = self.cmdt.attribs
            cmdlines_full_dict['results'] = self.cmdt.results
            #在cmdline.py 中加入代码支持cmds 是 pathlists 的情况
            hspr = cmdline.cmdlines_full_dict_to_hdict(cmdlines_full_dict)
            self.html = hdict_object.hspr_to_xml(hspr)
            self.object = hdict_object.hdict_to_obj(hspr['hdict'],hspr['sdict'],hspr['prdict'])
            self.orig = 'cmdline'
        else:
            raise Exception("Invalid INIT!", kwargs)
        self.hdict = hspr['hdict']
        self.sdict = hspr['sdict']
        self.prdict = hspr['prdict']
        self.depth = self.sdict.__len__()
        self.widths = []
        for i in range(0,self.depth):
            self.widths.append(self.sdict[i].__len__())
    def __dir__(self):
        l = ['depth','widths','node','showall','search','html','object']
        jprint.pobj(l)
        return(l)
    def __repr__(self):
        if(self.orig == 'object'):
            return(self.object.__repr__())
        elif(self.orig == 'html'):
            return(html)
        elif(self.orig == 'cmdline'):
            jprint.pobj(self.cmdt.pathlists,fixed_indent = 1)
            print('\n')
            jprint.pobj(self.cmdt.attribs,fixed_indent = 1)
            print('\n')
            jprint.pobj(self.cmdt.results,fixed_indent = 1)
            print('\n')
            return(self.cmdt.pathlists.__repr__() + self.cmdt.attribs.__repr__() + self.cmdt.results.__repr__())
        else:
            raise Exception("Invalid INIT!",'not object,not html_text,not cmdline')
    def showall(self,**kwargs):
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'readable_path'
        if(mode == 'pathlist'):
            jprint.pobj(self.cmdt.pathlists,fixed_indent = 1)
        elif(mode == 'cmdline'):
            jprint.pobj(self.cmdt.cmdlines,fixed_indent = 1)
        else:
            readables = {}
            for i in range(0,self.cmdt.pathlists.__len__()):
                readable = hdict_object.path_list_to_console_key_str(self.cmdt.pathlists[i])
                readables[i] = readable
            jprint.pobj(readables,fixed_indent = 1)
    def search(self,cmd_str):
        return(self.cmdt.__getitem__(cmd_str))
    def getlsib(self,pathlist):
        hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,pathlist)
        breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,hdict_pathlist)
        depth,breadth = hdict_object.breadth_path_to_sdict_location(breadth_path)
        lsib_pathlist = self.sdict[depth][breadth]['orig_lsib_path']
        if(lsib_pathlist == []):
            lsib_pathlist = None
            lsib_readable_path = None
            lsib_depth = None
            lsib_breadth = None
            lsib_siblings_seq = None
            lsib_tag = None
            lsib_attrib = None
            lsib_text = None
            lsib_type = None
            lsib_leaf = None
            #####
            lsib_leaf_sons = None 
            lsib_nonleaf_sons = None
            lsib_leaf_descendants = None
            lsib_nonleaf_descendants = None
            #####
        else:
            lsib_readable_path = hdict_object.path_list_to_console_key_str(lsib_pathlist)
            lsib_hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,lsib_pathlist)
            lsib_breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,lsib_hdict_pathlist)
            lsib_depth,lsib_breadth = hdict_object.breadth_path_to_sdict_location(lsib_breadth_path)
            lsib_siblings_seq = self.sdict[lsib_depth][lsib_breadth]['siblings_seq_path'][-1]
            lsib_tag = hdict_object.hdict_get_value(self.hdict,lsib_pathlist)['tag']
            lsib_attrib = self.sdict[lsib_depth][lsib_breadth]['attrib']
            lsib_text = self.sdict[lsib_depth][lsib_breadth]['text']
            lsib_type = self.sdict[lsib_depth][lsib_breadth]['type']
            lsib_leaf = self.sdict[lsib_depth][lsib_breadth]['leaf']
            ##########################################
            lsib_leaf_sons = self.sdict[lsib_depth][lsib_breadth]['leaf_son_pathlists']
            lsib_nonleaf_sons = self.sdict[lsib_depth][lsib_breadth]['non_leaf_son_pathlists']
            lsib_leaf_descendants = self.sdict[lsib_depth][lsib_breadth]['leaf_descendant_pathlists']
            lsib_nonleaf_descendants = self.sdict[lsib_depth][lsib_breadth]['non_leaf_descendant_pathlists']
            ###########################################
        desc = description(readable_path=lsib_readable_path,pathlist=lsib_pathlist,depth=lsib_depth,breadth=lsib_breadth,siblings_seq=lsib_siblings_seq,tag=lsib_tag,attrib=lsib_attrib,text=lsib_text,type=lsib_type,leaf=lsib_leaf,leaf_sons=lsib_leaf_sons,nonleaf_sons=lsib_nonleaf_sons,leaf_descendants=lsib_leaf_descendants,nonleaf_descendants=lsib_nonleaf_descendants)
        return(desc)
    def getrsib(self,pathlist):
        hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,pathlist)
        breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,hdict_pathlist)
        depth,breadth = hdict_object.breadth_path_to_sdict_location(breadth_path)
        rsib_pathlist = self.sdict[depth][breadth]['orig_rsib_path']
        if(rsib_pathlist == []):
            rsib_pathlist = None
            rsib_readable_path = None
            rsib_depth = None
            rsib_breadth = None
            rsib_siblings_seq = None
            rsib_tag = None
            rsib_attrib = None
            rsib_text = None
            rsib_type = None
            rsib_leaf = None
            #####
            rsib_leaf_sons = None 
            rsib_nonleaf_sons = None
            rsib_leaf_descendants = None
            rsib_nonleaf_descendants = None
            #####
        else:
            rsib_readable_path = hdict_object.path_list_to_console_key_str(rsib_pathlist)
            rsib_hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,rsib_pathlist)
            rsib_breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,rsib_hdict_pathlist)
            rsib_depth,rsib_breadth = hdict_object.breadth_path_to_sdict_location(rsib_breadth_path)
            rsib_siblings_seq = self.sdict[rsib_depth][rsib_breadth]['siblings_seq_path'][-1]
            rsib_tag = hdict_object.hdict_get_value(self.hdict,rsib_pathlist)['tag']
            rsib_attrib = self.sdict[rsib_depth][rsib_breadth]['attrib']
            rsib_text = self.sdict[rsib_depth][rsib_breadth]['text']
            rsib_type = self.sdict[rsib_depth][rsib_breadth]['type']
            rsib_leaf = self.sdict[rsib_depth][rsib_breadth]['leaf']
            ##########################################
            rsib_leaf_sons = self.sdict[rsib_depth][rsib_breadth]['leaf_son_pathlists']
            rsib_nonleaf_sons = self.sdict[rsib_depth][rsib_breadth]['non_leaf_son_pathlists']
            rsib_leaf_descendants = self.sdict[rsib_depth][rsib_breadth]['leaf_descendant_pathlists']
            rsib_nonleaf_descendants = self.sdict[rsib_depth][rsib_breadth]['non_leaf_descendant_pathlists']
            ###########################################
        desc = description(readable_path=rsib_readable_path,pathlist=rsib_pathlist,depth=rsib_depth,breadth=rsib_breadth,siblings_seq=rsib_siblings_seq,tag=rsib_tag,attrib=rsib_attrib,text=rsib_text,type=rsib_type,leaf=rsib_leaf,leaf_sons=rsib_leaf_sons,nonleaf_sons=rsib_nonleaf_sons,leaf_descendants=rsib_leaf_descendants,nonleaf_descendants=rsib_nonleaf_descendants)
        return(desc)
    def getlcin(self,pathlist):
        hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,pathlist)
        breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,hdict_pathlist)
        depth,breadth = hdict_object.breadth_path_to_sdict_location(breadth_path)
        lcin_pathlist = self.sdict[depth][breadth]['orig_lcin_path']
        if(lcin_pathlist == []):
            lcin_pathlist = None
            lcin_readable_path = None
            lcin_depth = None
            lcin_breadth = None
            lcin_siblings_seq = None
            lcin_tag = None
            lcin_attrib = None
            lcin_text = None
            lcin_type = None
            lcin_leaf = None
            #####
            lcin_leaf_sons = None 
            lcin_nonleaf_sons = None
            lcin_leaf_descendants = None
            lcin_nonleaf_descendants = None
            #####
        else:
            lcin_readable_path = hdict_object.path_list_to_console_key_str(lcin_pathlist)
            lcin_hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,lcin_pathlist)
            lcin_breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,lcin_hdict_pathlist)
            lcin_depth,lcin_breadth = hdict_object.breadth_path_to_sdict_location(lcin_breadth_path)
            lcin_siblings_seq = self.sdict[lcin_depth][lcin_breadth]['siblings_seq_path'][-1]
            lcin_tag = hdict_object.hdict_get_value(self.hdict,lcin_pathlist)['tag']
            lcin_attrib = self.sdict[lcin_depth][lcin_breadth]['attrib']
            lcin_text = self.sdict[lcin_depth][lcin_breadth]['text']
            lcin_type = self.sdict[lcin_depth][lcin_breadth]['type']
            lcin_leaf = self.sdict[lcin_depth][lcin_breadth]['leaf']
            ##########################################
            lcin_leaf_sons = self.sdict[lcin_depth][lcin_breadth]['leaf_son_pathlists']
            lcin_nonleaf_sons = self.sdict[lcin_depth][lcin_breadth]['non_leaf_son_pathlists']
            lcin_leaf_descendants = self.sdict[lcin_depth][lcin_breadth]['leaf_descendant_pathlists']
            lcin_nonleaf_descendants = self.sdict[lcin_depth][lcin_breadth]['non_leaf_descendant_pathlists']
            ###########################################
        desc = description(readable_path=lcin_readable_path,pathlist=lcin_pathlist,depth=lcin_depth,breadth=lcin_breadth,siblings_seq=lcin_siblings_seq,tag=lcin_tag,attrib=lcin_attrib,text=lcin_text,type=lcin_type,leaf=lcin_leaf,leaf_sons=lcin_leaf_sons,nonleaf_sons=lcin_nonleaf_sons,leaf_descendants=lcin_leaf_descendants,nonleaf_descendants=lcin_nonleaf_descendants)
        return(desc)
    def getrcin(self,pathlist):
        hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,pathlist)
        breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,hdict_pathlist)
        depth,breadth = hdict_object.breadth_path_to_sdict_location(breadth_path)
        rcin_pathlist = self.sdict[depth][breadth]['orig_rcin_path']
        if(rcin_pathlist == []):
            rcin_pathlist = None
            rcin_readable_path = None
            rcin_depth = None
            rcin_breadth = None
            rcin_siblings_seq = None
            rcin_tag = None
            rcin_attrib = None
            rcin_text = None
            rcin_type = None
            rcin_leaf = None
            #####
            rcin_leaf_sons = None 
            rcin_nonleaf_sons = None
            rcin_leaf_descendants = None
            rcin_nonleaf_descendants = None
            #####
        else:
            rcin_readable_path = hdict_object.path_list_to_console_key_str(rcin_pathlist)
            rcin_hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,rcin_pathlist)
            rcin_breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,rcin_hdict_pathlist)
            rcin_depth,rcin_breadth = hdict_object.breadth_path_to_sdict_location(rcin_breadth_path)
            rcin_siblings_seq = self.sdict[rcin_depth][rcin_breadth]['siblings_seq_path'][-1]
            rcin_tag = hdict_object.hdict_get_value(self.hdict,rcin_pathlist)['tag']
            rcin_attrib = self.sdict[rcin_depth][rcin_breadth]['attrib']
            rcin_text = self.sdict[rcin_depth][rcin_breadth]['text']
            rcin_type = self.sdict[rcin_depth][rcin_breadth]['type']
            rcin_leaf = self.sdict[rcin_depth][rcin_breadth]['leaf']
            ##########################################
            rcin_leaf_sons = self.sdict[rcin_depth][rcin_breadth]['leaf_son_pathlists']
            rcin_nonleaf_sons = self.sdict[rcin_depth][rcin_breadth]['non_leaf_son_pathlists']
            rcin_leaf_descendants = self.sdict[rcin_depth][rcin_breadth]['leaf_descendant_pathlists']
            rcin_nonleaf_descendants = self.sdict[rcin_depth][rcin_breadth]['non_leaf_descendant_pathlists']
            ###########################################
        desc = description(readable_path=rcin_readable_path,pathlist=rcin_pathlist,depth=rcin_depth,breadth=rcin_breadth,siblings_seq=rcin_siblings_seq,tag=rcin_tag,attrib=rcin_attrib,text=rcin_text,type=rcin_type,leaf=rcin_leaf,leaf_sons=rcin_leaf_sons,nonleaf_sons=rcin_nonleaf_sons,leaf_descendants=rcin_leaf_descendants,nonleaf_descendants=rcin_nonleaf_descendants)
        return(desc)
    def node(self,pathlist):
        hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,pathlist)
        breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,hdict_pathlist)
        depth,breadth = hdict_object.breadth_path_to_sdict_location(breadth_path)
        node_pathlist = self.sdict[depth][breadth]['orig_obj_path']
        if(node_pathlist == []):
            node_pathlist = None
            node_readable_path = None
            node_depth = None
            node_breadth = None
            node_siblings_seq = None
            node_tag = None
            node_attrib = None
            node_text = None
            node_type = None
            node_leaf = None
            #####
            node_leaf_sons = None 
            node_nonleaf_sons = None
            node_leaf_descendants = None
            node_nonleaf_descendants = None
            #####
            node_lsib = None
            node_rsib = None
            node_lcin = None
            node_rcin = None
            #####
        else:
            node_readable_path = hdict_object.path_list_to_console_key_str(node_pathlist)
            node_hdict_pathlist = hdict_object.orig_obj_path_to_hdict_path(self.prdict,node_pathlist)
            node_breadth_path = hdict_object.hdict_path_to_breadth_path(self.hdict,node_hdict_pathlist)
            node_depth,node_breadth = hdict_object.breadth_path_to_sdict_location(node_breadth_path)
            node_siblings_seq = self.sdict[node_depth][node_breadth]['siblings_seq_path'][-1]
            node_tag = hdict_object.hdict_get_value(self.hdict,node_pathlist)['tag']
            node_attrib = self.sdict[node_depth][node_breadth]['attrib']
            node_text = self.sdict[node_depth][node_breadth]['text']
            node_type = self.sdict[node_depth][node_breadth]['type']
            node_leaf = self.sdict[node_depth][node_breadth]['leaf']
            ##########################################
            node_leaf_sons = self.sdict[node_depth][node_breadth]['leaf_son_pathlists']
            node_nonleaf_sons = self.sdict[node_depth][node_breadth]['non_leaf_son_pathlists']
            node_leaf_descendants = self.sdict[node_depth][node_breadth]['leaf_descendant_pathlists']
            node_nonleaf_descendants = self.sdict[node_depth][node_breadth]['non_leaf_descendant_pathlists']
            ###########################################
            #####
            node_lsib = self.getlsib(pathlist)
            node_rsib = self.getrsib(pathlist)
            node_lcin = self.getlcin(pathlist)
            node_rcin = self.getrcin(pathlist)
            #####
        desc = nodedescription(readable_path=node_readable_path,pathlist=node_pathlist,depth=node_depth,breadth=node_breadth,siblings_seq=node_siblings_seq,tag=node_tag,attrib=node_attrib,text=node_text,type=node_type,leaf=node_leaf,leaf_sons=node_leaf_sons,nonleaf_sons=node_nonleaf_sons,leaf_descendants=node_leaf_descendants,nonleaf_descendants=node_nonleaf_descendants,lsib=node_lsib,rsib=node_rsib,lcin=node_lcin,rcin=node_rcin)
        return(desc)

