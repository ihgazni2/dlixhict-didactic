import re


def creat_regexes_array(chars_arr):
    '''
        >>> creat_regexes_array(['"',"'",'<','>'])
        [re.compile('["]'), re.compile("[']"), re.compile('[<]'), re.compile('[>]')]
        >>> 
    '''
    regex_chars_arr = []
    for i in range(0,chars_arr.__len__()):
        regex_str = ''.join(('[',chars_arr[i],']'))
        regex = re.compile(regex_str)
        regex_chars_arr.append(regex)
    return(regex_chars_arr)



def creat_regexes_not_array(chars_arr):
    '''
        >>> creat_regexes_not_array(['"',"'",'<','>'])
        [re.compile('[^"]'), re.compile("[^']"), re.compile('[^<]'), re.compile('[^>]')]
        >>>
    '''
    regex_chars_arr = []
    for i in range(0,chars_arr.__len__()):
        regex_str = ''.join(('[^',chars_arr[i],']'))
        regex = re.compile(regex_str)
        regex_chars_arr.append(regex)
    return(regex_chars_arr)


def creat_regex_from_arr(chars_arr):
    '''
        >>> creat_regex_from_arr(['"',"'",'<','>'])
        re.compile('["\'<>]')
        >>> 
    '''
    regex_str = '['
    for i in range(0,chars_arr.__len__()):
        regex_str = ''.join((regex_str,chars_arr[i]))
    regex_str = ''.join((regex_str,']'))
    return(re.compile(regex_str))



def creat_regex_not_from_arr(chars_arr):
    '''
        >>> creat_regex_not_from_arr(['"',"'",'<','>'])
        re.compile('[^"\'<>]')
        >>> 
    '''
    regex_str = '[^'
    for i in range(0,chars_arr.__len__()):
        regex_str = ''.join((regex_str,chars_arr[i]))
    regex_str = ''.join((regex_str,']'))
    return(re.compile(regex_str))



class FSM():
    def __init__(self,**kwargs):
        self.action_returned = None
        if('fsm_dict' in kwargs):
            self.fsm_dict = kwargs['fsm_dict']
        else:
            self.fsm_dict = {}
        if('do_action' in kwargs):
            self.do_action = kwargs['do_action']
        else:
            self.do_action = True
        if('enable_debug' in kwargs):
            self.enable_debug = kwargs['enable_debug']
        else:
            self.enable_debug = False
    def help(self):
        print("curr_state is the FSM CURRENT STATE")
        print("input_symbol is the INPUT")
        print("trigger_checker is ised to check the INPUT,if passed checked goto the CORRESPONDING NEXT STATE")
        print("next_state is the FSM NEXT STATE if be triggered")
    def __repr__(self):    
        for key in self.fsm_dict:
            curr_state, trigger_checker = key
            action,next_state = self.fsm_dict[key]
            print("curr_state: "+curr_state)
            print("trigger_checker: "+trigger_checker.__str__())
            if(action == None):
                print("action: None")
            else:
                print("action: "+action.__qualname__)
            print("next_state: "+next_state)
        return("")
    def modify(self,*args):
        if((args[0],args[1]) in self.fsm_dict):
            self.fsm_dict[(args[0],args[1])] = (args[2],args[3])
            return(True)
        else:
            print((args[0],args[1]),end='')
            print("not in fsm_dict,use .add")
            return(False)

    def modify_by_name(self,**kwargs):
        if('curr_state' in kwargs):
            curr_state = kwargs['curr_state']
        else:
            curr_state = None
        if('trigger_checker' in kwargs):
            trigger_checker = kwargs['trigger_checker']
        else:
            trigger_checker = None
        if('action' in kwargs):
            action = kwargs['action']
        else:
            action = None
        if('next_state' in kwargs):
            next_state = kwargs['next_state']
        else:
            next_state = None
        if((curr_state,trigger_checker) in self.fsm_dict):
            self.fsm_dict[(curr_state,trigger_checker)] = (action,next_state)
            return(True)
        else:
            print((curr_state,trigger_checker),end='')
            print("not in fsm_dict, use .add_by_name ")
            return(False) 

  
    def add(self,*args):
        if((args[0],args[1]) in self.fsm_dict):
            print((args[0],args[1]),end='')
            print("already in fsm_dict, use .modify ") 
            return(False)
        else:
            self.fsm_dict[(args[0],args[1])] = (args[2],args[3]) 
            return(True)


    def add_by_name(self,**kwargs):
        if('curr_state' in kwargs):
            curr_state = kwargs['curr_state']
        else:
            curr_state = None
        if('trigger_checker' in kwargs):
            trigger_checker = kwargs['trigger_checker']
        else:
            trigger_checker = None
        if('action' in kwargs):
            action = kwargs['action']
        else:
            action = None
        if('next_state' in kwargs):
            next_state = kwargs['next_state']
        else:
            next_state = None
        if((curr_state,trigger_checker) in fsm_dict):
            print((curr_state,trigger_checker),end='')
            print("already in fsm_dict, use .modify_by_name ")
            return(False)
        else:
            self.fsm_dict[(curr_state,trigger_checker)] = (action,next_state)
            return(True)
               
    def remove(self,*args):
        del self.fsm_dict[(args[0],args[1])]

    def remove_by_name(self,**kwargs):
        if('curr_state' in kwargs):
            curr_state = kwargs['curr_state']
        else:
            curr_state = None
        if('trigger_checker' in kwargs):
            trigger_checker = kwargs['trigger_checker']
        else:
            trigger_checker = None
        del self.fsm_dict[(curr_state,trigger_checker)]

    def search(self,curr_state,input_symbol,*action_args):
        for key in self.fsm_dict:
            if(key[0] == curr_state):
                if(key[1].search(input_symbol)):
                    action,next_state = self.fsm_dict[key]
                    if(self.enable_debug):
                        print("curr_state: "+curr_state)
                        print("trigger_checker: "+trigger_checker.__str__())
                        print("input_symbol: "+input_symbol.__str__())
                        if(action == None):
                            print("action: None")
                        else:
                            print("action: "+action.__qualname__)
                        print("    params: ")
                        print("        ",end='')
                        print(*action_args)
                        print("next_state: "+next_state)
                    else:
                        pass
                    if(self.do_action):
                        if(action == None):
                            pass
                        else:
                            self.action_returned = action.__call__(*action_args)    
                    else:
                        pass
                    return(self.fsm_dict[key])
                else:
                    pass
            else:
                pass
        return((None,None))

     


