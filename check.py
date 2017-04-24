
import sys
import os
import subprocess
import shlex

def pipe_shell_cmds(shell_CMDs):
    '''
        shell_CMDs = {}
        shell_CMDs[1] = 'netstat -n'
        shell_CMDs[2] = "awk {'print $6'}"
    '''
    len = shell_CMDs.__len__()
    p = {}
    p[1] = subprocess.Popen(shlex.split(shell_CMDs[1]), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for i in range(2,len):
        p[i] = subprocess.Popen(shlex.split(shell_CMDs[i]), stdin=p[i-1].stdout, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if(len > 1):
        p[len] = subprocess.Popen(shlex.split(shell_CMDs[len]), stdin=p[len-1].stdout, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result = p[len].communicate()
    if(len > 1):
        for i in range(2,len+1):
            returncode = p[i].wait()
    else:
        returncode = p[len].wait()
    return(result)

def check(fname):
    fl = []
    fl.append('cat ./xdict/console_color.py')
    fl.append('cat ./xdict/CrtableLib/crtable.py ')
    fl.append('cat ./xdict/CrtableLib/__init__.py ')
    fl.append('cat ./xdict/cmdline.py ' )
    fl.append('cat ./xdict/hdict_object.py ')
    fl.append('cat ./xdict/hdict_xml.py' )
    fl.append('cat ./xdict/__init__.py ')
    fl.append('cat ./xdict/jprint.py ' )
    fl.append('cat ./xdict/ltdict.py  ' )
    fl.append('cat ./xdict/TestLib/genrand.py ')
    fl.append('cat ./xdict/TestLib/__init__.py ' )
    fl.append('cat ./xdict/tuple_list.py')
    fl.append('cat ./xdict/utils.py')
    for cmd in fl:
        shell_CMDs = {}
        shell_CMDs[1] = cmd
        shell_CMDs[2] = "egrep " + '"' + fname + '"'
        rslt = pipe_shell_cmds(shell_CMDs)
        if(rslt == (b'', b'')):
            pass
        else:
            print(cmd)
            print(rslt)

check(sys.argv[1])

