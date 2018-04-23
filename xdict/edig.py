class Dig():
    '''
    '''
    def __init__(self,root,func_is_leaf,get_children,**kwargs):
        self.root = root
        self.gen = dig(root,func_is_leaf,get_children,**kwargs)
    def next(self):
        return(self.gen.__next__())
        

def dig(root,func_is_leaf,get_children,**kwargs):
    '''
    '''
    if('func_is_leaf_args' in kwargs):
        func_is_leaf_args = kwargs['func_is_leaf_args']
    else:
        func_is_leaf_args = []
    if('get_children_args' in kwargs):
        get_children_args = kwargs['get_children_args']
    else:
        get_children_args = []
    unhandled = [root]
    while(unhandled.__len__()>0):
        yield(unhandled)
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            ele = unhandled[i]
            cond = func_is_leaf(ele,*func_is_leaf_args)
            if(cond):
                pass
            else:
                children = get_children(ele,*get_children_args)
                next_unhandled.append(children)
        unhandled = next_unhandled
