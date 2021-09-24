##custom imports
from anytree import AnyNode, RenderTree
import json

root = AnyNode(nodename='root')
parent = root
specialwords = {'integer':'int', 'number':'float'}
tabs = 1
setup = []
setup.append("void setup(){")
loop = []
loop.append("void loop(){")
con = []
transpiled = []
const_ = AnyNode(nodename="const", parent=root)
setup_ = AnyNode(nodename="setup", parent=root)
loop_ = AnyNode(nodename="loop", parent=root)

def addNodeOutput(variable):
    global parent, tabs
    n = AnyNode(parent=parent, nodename='output',variable=variable)
    loop.append('\t'*tabs + 'printf("%d",{});'.format(variable))

def addNodeEnd():
    global parent, tabs
    if len(parent.ancestors)>=1:
        #print('giving an ancestor')
        parent = parent.ancestors[-1]
    n = AnyNode(parent=parent, nodename='end')
    tabs = tabs - 1
    loop.append('\t'*tabs + '}')

def addNodeElse():
    global parent, tabs
    if len(parent.ancestors)>=1:
        #print('giving an ancestor')
        parent = parent.ancestors[-1]
    n = AnyNode(parent=parent, nodename='else')
    parent = n
    tabs = tabs - 1
    loop.append('\t'*tabs + '}')
    loop.append('\t'*tabs + 'else')
    loop.append('\t'*tabs + '{')
    tabs = 1 + tabs

def addIf(val1, val2, rel):
    global parent, tabs
    n = AnyNode(parent=parent, nodename='if', val1=val1, val2=val2, rel=rel)
    ##update parent to this
    parent = n
    #print('new parent',n)
    loop.append('\t'*tabs + 'if({} {} {})'.format(val1, rel, val2))
    loop.append('\t'*tabs + '{')
    tabs = 1 + tabs

def addDecl(dtype, var_name):
    global parent, specialwords, tabs
    n = AnyNode(parent=parent, nodename='decl', dtype=dtype, var_name=var_name)
    loop.append('\t'*tabs + '{} {};'.format(specialwords.get(dtype), var_name))

def addAssign(var_name, val):
    global parent, tabs
    n = AnyNode(parent=parent, nodename='assign', var_name=var_name, val=val)
    loop.append('\t'*tabs + '{} = {};'.format(var_name, val))

def addBoth(dtype, var_name, val):
    global parent, tabs
    n = AnyNode(parent=parent,nodename='both',dtype=dtype,var_name=var_name,val=val)
    loop.append('\t'*tabs + '{} {} = {};'.format(specialwords.get(dtype),var_name,val))

def addLED(varname, pin):
    global parent, tabs
    n = AnyNode(parent=const_, nodename="const_defn", varname=varname, value=pin)
    con.append("const int {} = {};".format(varname, pin))
    n = AnyNode(parent=setup_, nodename="pinmode", varname=varname, value="OUTPUT")
    setup.append('\t'*tabs + "pinMode({},OUTPUT);".format(varname))

def turnLedOn(varname):
    global parent, tabs
    n = AnyNode(parent=loop_, nodename="led_on", varname=varname)
    loop.append('\t'*tabs + "digitalWrite({},HIGH);".format(varname))

def turnLedOff(varname):
    global parent, tabs
    n = AnyNode(parent=loop_, nodename="led_off", varname=varname)
    loop.append('\t'*tabs + "digitalWrite({},LOW);".format(varname))

def setupEverythin():
    global setup, con, loop, root, parent,tabs,const_, setup_, loop_
    con = []
    setup = ["void setup(){"]
    loop = ["void loop(){"]
    root = AnyNode(nodename='root')
    parent = root
    tabs = 1
    const_ = AnyNode(nodename="const", parent=root)
    setup_ = AnyNode(nodename="setup", parent=root)
    loop_ = AnyNode(nodename="loop", parent=root)

def printTree():
    global root,transpiled
    setup.append("\t"*1 + "Serial.begin(9600);")
    setup.append("}")
    #print(RenderTree(root))
    #print("*"*75)
    transpiled = []
    for c in con:
        ##print(c)
        transpiled.append(c)
    for s in setup:
        ##print(s)
        transpiled.append(s)
    for l in loop[0:-1]:
        ##print(l)
        transpiled.append(l)
    setupEverythin()

def getLines():
    global transpiled
    return transpiled

'''def printTree():
    global root
    print(RenderTree(root))'''
