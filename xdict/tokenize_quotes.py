from xdict.prepare_quotes_token_machine  import prepare_quotes_token_machine


def tokenize_quotes(machine):
    curr_state = "INIT"
    rslt = ''
    for i in range(0,machine.orig_str.__len__()):
        input_symbol = machine.orig_str[i]
        action,next_state,trigger_checker = machine.search(curr_state,input_symbol)
        #print('----------')
        #print(curr_state,trigger_checker,input_symbol,action,next_state)
        if(action == machine.do_replace):
            ch = action(input_symbol)
            #print(ch)
        elif(action == machine.do_throw):
            ch = ''
            action(curr_state,trigger_checker,input_symbol)
        else:
            ch = input_symbol
        #rslt = ''.join((rslt,ch))
        rslt = rslt +ch
        curr_state = next_state
    return(rslt)



#######################
def convert_token_in_quote(j_str,**kwargs):
    '''
        #1. use html.escape  to  escape all quote-operators appeared in single-quote or double-quote
        #2. use html.escape  to  escape all paired-operators appeared in single-quote or double-quote : such as  "{,},[,],(,)"
        #3. use html.escape  to  escape all other operators appeared in single-quote or double-quote : such as : ':',','
        #4. use html_escape  to  escape seperators-operators appeared in single-quote or double-quote: such as '\n'

        >>> from xdict.jprint import convert_token_in_quote
        >>> from xdict.jprint import help
        >>>
        >>> convert_token_in_quote('"a b":"cd"')
        '"a&#32;b":"cd"'
        >>> import html
        >>> html.unescape('"a&#32;b":"cd"')
        '"a b":"cd"'
        >>> convert_token_in_quote('"a b":cd')
        '"a&#32;b":cd'
        >>>
        >>> #help(convert_token_in_quote)
        convert_token_in_quote('<a b>:"cd"',quotes_pairs_dict={1: ('"', '"'), 2: ("<", ">")})
        '<a&#32;b>:"cd"'
    '''
    machine = prepare_quotes_token_machine(j_str,**kwargs)
    rslt = tokenize_quotes(machine)
    return(rslt)

