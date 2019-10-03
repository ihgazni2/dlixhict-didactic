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

