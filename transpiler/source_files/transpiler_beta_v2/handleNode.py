##custom imports
from anytree import AnyNode, RenderTree, search
import json

CONSTANTS_TREE = None
CONSTANTS_parent = None
SETUP_TREE = None
SETUP_parent = None
LOOP_TREE = None
LOOP_parent = None

TRANSPILED_LINES = []

methods_dict = {"ON()":"digitalWrite({},HIGH);",\
                "OFF()":"digitalWrite({},LOW);",\
                "GETDISTANCE()":"getUsonDistance({},{})",\
                "READVAL()":"digitalRead({})",\
                "STATE()":"digitalRead({})",\
                "READTEMP()":"readTemp({})"}


rel_op_dict = {"<":"<", ">":">", "=":"=="}
dtype_dict = {"integer":"int", "number":"float"}

def initTree():
    ##runs before every transpilation
    global CONSTANTS_TREE, SETUP_TREE, LOOP_TREE
    global CONSTANTS_parent, SETUP_parent, LOOP_parent
    global TRANSPILED_LINES

    ##setup tress
    CONSTANTS_TREE = AnyNode(nodename="const_root")
    SETUP_TREE = AnyNode(nodename="setup_root")
    LOOP_TREE = AnyNode(nodename="loop_root")
    ##setup parent nodes
    CONSTANTS_parent = CONSTANTS_TREE
    SETUP_parent = SETUP_TREE
    LOOP_parent = LOOP_TREE
    ##emptying previous lines
    TRANSPILED_LINES = []

def addNodeOutput(variable):
    ##output node only allowed in loop_tree
    global LOOP_parent
    n = AnyNode(parent = LOOP_parent, nodename="output", variable=variable)


def addNodeEnd():
    global LOOP_parent
    if len(LOOP_parent.ancestors) >= 1:
        ##end of some block, so moving up in the tree
        LOOP_parent = LOOP_parent.ancestors[-1]
    ##all ocurences of end are to be replaces with closing bracket
    n = AnyNode(parent = LOOP_parent, nodename="end")

def addNodeElse():
    ##else appears only in loop part
    global LOOP_parent
    LOOP_parent = LOOP_parent.ancestors[-1]
    n = AnyNode(parent = LOOP_parent, nodename = "else")
    ##updating parent with this node
    LOOP_parent = n

def addIf(val1, val2, rel):
    global LOOP_parent
    n = AnyNode(parent = LOOP_parent, nodename = "if", val1 = val1, val2 = val2, rel = rel)
    ##updating parent with this node
    LOOP_parent = n

def addDecl(dtype, var):
    ##declarationss are only allowed in loop part
    global LOOP_parent
    n = AnyNode(parent = LOOP_parent, nodename = "decl", dtype = dtype, var = var)

def addAssign(var, value, lib, funs):
    ##assigment allowed in only loop part
    global LOOP_parent
    if lib is None:
        ##normal assigment
        n = AnyNode(parent = LOOP_parent, nodename = "assgn", var = var, value = value, lib_ist = None)
    else:
        ##assignment has function involded
        n = AnyNode(parent = LOOP_parent, nodename = "assgn", var = var, lib_ist = lib, funs = funs)

def addBoth(dtype, var, val, lib, funs):
    ##declaration and assignment only allowed in loop
    global LOOP_parent
    if lib is None:
        ##normal declaration and assignment
        n = AnyNode(parent = LOOP_parent, nodename="dNa", dtype=dtype, var=var, value=val, lib_ist = None)
    else:
        ##assignment is a function call
        n = AnyNode(parent = LOOP_parent, nodename="dNa", dtype=dtype, var=var, lib_ist=lib, funs=funs)

##Section LED: begin

def addLED(ins_name, pin):
    ##add pin number to constants
    ##add varname to setup, set it as output
    global CONSTANTS_parent, SETUP_parent
    ##adding to constant_tree
    n = AnyNode(parent = CONSTANTS_parent, var=ins_name, value=pin)
    ##adding to setup tree
    n = AnyNode(parent = SETUP_parent, ins_name=ins_name, functype="OUTPUT", lib="LED")

def turnLedOn(ins_name):
    ##led can be controlled in loop part only(i.e from inside action Main)
    global LOOP_parent
    n = AnyNode(parent=LOOP_parent, nodename="func", ins_name=ins_name, funcdoes="ON()")

def turnLedOff(ins_name):
    ##led can be controlled in loop part only(i.e from inside action Main)
    global LOOP_parent
    n = AnyNode(parent=LOOP_parent, nodename="func", ins_name=ins_name, funcdoes="OFF()")

##Section LED: end

##Section Ultrasonic: begin
def addUsonTrig(ins_name, trig_pin):
    global CONSTANTS_parent, SETUP_parent
    ##add new constant
    n = AnyNode(parent = CONSTANTS_parent, var = ins_name + "_trig", value = trig_pin)
    ##check if theres a a node for this instance
    if search.find_by_attr(SETUP_parent, name="ins_name", value=ins_name) is None:
        ##add new node, while transpiling set pinModes
        n = AnyNode(parent = SETUP_parent, ins_name = ins_name, trig_p = trig_pin, echo_p = -1, lib="USON")
    else:
        ##update trig_p propert of the node
        ##print("updaing trig pin of {}".format(ins_name))
        search.find_by_attr(SETUP_parent, name="ins_name", value=ins_name).trig_p = trig_pin

def addUsonEcho(ins_name, echo_pin):
    global CONSTANTS_parent, SETUP_parent
    ##add new constant
    ##check if theres a a node for this instance
    n = AnyNode(parent = CONSTANTS_parent, var = ins_name + "_echo", value = echo_pin)
    if search.find_by_attr(SETUP_parent, name="ins_name", value=ins_name) is None:
        ##add new node, while transpiling set pinModes
        n = AnyNode(parent = SETUP_parent, ins_name = ins_name, echo_p = echo_pin, trig_p = -1, lib="USON")
    else:
        ##update echo_p propert of the node
        ##print("updating echo pin of {}".format(ins_name))
        search.find_by_attr(SETUP_parent, name="ins_name", value=ins_name).echo_p = echo_pin

def readUsonDist(ins_name):
    ##add this line in loop, since read is done in loop
    global LOOP_parent
    n = AnyNode(parent = LOOP_parent, nodename = "func", ins_name = ins_name, funcdoes="GETDISTANCE()")
    ##define helper methods later

##Section Ultrasonic : end
##Section Infrared : begin

def addIRED(ins_name, pin):
    global SETUP_parent, CONSTANTS_parent
    ##add in constant
    n = AnyNode(parent = CONSTANTS_parent, var = ins_name, value = pin)
    ##add in setup
    n = AnyNode(parent = SETUP_parent, ins_name = ins_name, functype="INPUT", lib="IRED")

def readIRED(ins_name):
    global LOOP_parent
    n = AnyNode(parent=LOOP_parent, nodename="func", ins_name = ins_name, funcdoes="READVAL()")

##Section IRED: end
##Section BUTTON: begin

def addButton(ins_name, pin):
    global SETUP_parent, CONSTANTS_parent
    ##add constant
    n = AnyNode(parent=CONSTANTS_parent, var=ins_name, value=pin)
    ##add to setup
    n = AnyNode(parent=SETUP_parent, ins_name = ins_name, functype="INPUT", lib="BUTTON")

def readBtnState(ins_name):
    global LOOP_parent
    n = AnyNode(parent = LOOP_parent, nodename="func", ins_name = ins_name, funcdoes="STATE()")

##Section BUTTON: end
##Section LMTEMP: begin

def addLMTEMP(ins_name, pin):
    global SETUP_parent, CONSTANTS_parent
    ##add constant
    n = AnyNode(parent=CONSTANTS_parent, var=ins_name, value=pin)
    ##add to setup
    n = AnyNode(parent=SETUP_parent, ins_name = ins_name, functype="INPUT", lib="LMTMP")

def readLMTemp(ins_name):
    global LOOP_parent
    n = AnyNode(parent = LOOP_parent, nodename="func", ins_name = ins_name, funcdoes="READTEMP()")

##Section LMTEMP: end
def printTree():
    global CONSTANTS_TREE, SETUP_TREE, LOOP_TREE
    print(RenderTree(CONSTANTS_TREE))
    print(RenderTree(SETUP_TREE))
    print(RenderTree(LOOP_TREE))

def constructCode(lib_name):
    ccode = []
    if lib_name == "uson":
        ccode.append("//returns distance in cms")
        ccode.append("int getUsonDistance(int tpin, int epin){")
        ccode.append("\tlong duration;")
        ccode.append("\tint distance;")
        ccode.append("\t//clearing trig pin")
        ccode.append("\tdigitalWrite(tpin, LOW);")
        ccode.append("\tdelayMicroseconds(2);")
        ccode.append("\t//Set trigger pin high for 10 Microseconds")
        ccode.append("\tdigitalWrite(tpin, HIGH);")
        ccode.append("\tdelayMicroseconds(10);")
        ccode.append("\tdigitalWrite(tpin, LOW);")
        ccode.append("\t//Reads the echo pin, returns the sound wave travel time in microseconds")
        ccode.append("\tduration = pulseIn(epin, HIGH);")
        ccode.append("\t//Calculating distance")
        ccode.append("\tdistance = duration * 0.034 / 2;")
        ccode.append("\treturn distance;")
        ccode.append("}")
    elif lib_name == "lmtmp":
        ccode.append("//returns temperature in celsius")
        ccode.append("float getTemp(int pin){")
        ccode.append("\tfloat val = analogRead(pin);")
        ccode.append("\tfloat mv = ( val/1024.0 )*5000;")
        ccode.append("\tfloat cel = mv/10;")
        ccode.append("\treturn cel;")
        ccode.append("}")

    return ccode

def startTranspiling():
    global CONSTANTS_TREE, SETUP_TREE, LOOP_TREE
    global methods_dict, rel_op_dict, dtype_dict
    global TRANSPILED_LINES

    skipped_first = False
    c = ""
    ##stores if any extra functions need to be added
    extras = []
    transplied = []
    ##handle constant here
    for pre, fill, node in RenderTree(CONSTANTS_TREE):
        if not skipped_first:
            skipped_first = True
            continue
        c = "const int {} = {};".format(node.var, node.value)
        transplied.append(c)

    ##handle setup here
    skipped_first = False
    transplied.append("void setup(){")
    for pre, fill, node in RenderTree(SETUP_TREE):
        if not skipped_first:
            skipped_first = True
            continue
        if node.lib == "USON":
            c = "\tpinMode({},{});".format(node.ins_name + "_trig", "OUTPUT")
            transplied.append(c)
            c = "\tpinMode({},{});".format(node.ins_name + "_echo", "INPUT")
            transplied.append(c)
        else:
            c = "\tpinMode({},{});".format(node.ins_name, node.functype)
            transplied.append(c)
    transplied.append("\tSerial.begin(9600);")
    transplied.append("}")

    ##handle loop here
    skipped_first = False
    transplied.append("void loop(){")
    tab_count = 1
    for pre, fill, node in RenderTree(LOOP_TREE):
        if not skipped_first:
            skipped_first = True
            continue
        if node.nodename == "output":
            c = "\t"*tab_count + "Serial.println({});".format(node.variable)
        elif node.nodename == "end":
            tab_count = tab_count - 1 if tab_count > 1 else 1
            c = "\t"*tab_count + "}"
        elif node.nodename == "if":
            c = "\t"*tab_count + "if( {} {} {} )".format(node.val1, rel_op_dict[node.rel], node.val2) + "{"
            tab_count = 1 + tab_count
        elif node.nodename == "else":
            tab_count = tab_count - 1 if tab_count > 1 else 1
            ##close the previous code block
            transplied.append("\t"*tab_count + "}")
            c = "\t"*tab_count + "else{"
            ##increase tab count
            tab_count = 1 + tab_count
        elif node.nodename == "decl":
            c = "\t"*tab_count + "{} {};".format(dtype_dict[node.dtype], node.var)
        elif node.nodename == "assgn":
            if node.lib_ist == None:
                ##normal assignment
                c = "\t"*tab_count + "{} = {};".format(node.var, node.value)
            else:
                if node.funs == "GETDISTANCE()":
                    c = "\t"*tab_count + "{} = getUsonDistance({},{});".format(node.var, node.lib_ist + "_trig", node.lib_ist + "_echo")
                    if not "uson" in extras:
                        extras.append("uson")
                elif node.funs =="READTEMP()":
                    c = "\t"*tab_count + "{} = getTemp({});".format(node.var, node.lib_ist)
                    if not "lmtmp" in extras:
                        extras.append("lmtmp")
                else:
                    c = "\t"*tab_count + "{} = {};".format(node.var, methods_dict[node.funs].format(node.lib_ist))
        elif node.nodename == "dNa":
            if node.lib_ist == None:
                ##normal declaration and assignment
                c = "\t"*tab_count + "{} {} = {};".format(dtype_dict[node.dtype], node.var, node.value)
            else:
                if node.funs == "GETDISTANCE()":
                    c = "\t"*tab_count + "{} {} = getUsonDistance({},{});".format(dtype_dict[node.dtype], node.var, node.lib_ist + "_trig", node.lib_ist + "_echo")
                    if not "uson" in extras:
                        extras.append("uson")
                elif node.funs =="READTEMP()":
                    c = "\t"*tab_count + "{} {} = getTemp({});".format(dtype_dict[node.dtype], node.var, node.lib_ist)
                    if not "lmtmp" in extras:
                        extras.append("lmtmp")
                else:
                    c = "\t"*tab_count + "{} {} = {};".format(dtype_dict[node.dtype], node.var, methods_dict[node.funs].format(node.lib_ist))
        elif node.nodename == "func":
            ##only led on and off will be applicable here
            ##since others return a particular value
            ##they'll be either handled by assgn or dNa
            c = "\t"*tab_count + "{}".format(methods_dict[node.funcdoes].format(node.ins_name))
        transplied.append(c)
    ##remove last two end transpilation
    transplied.pop(-1)
    transplied.pop(-1)
    ##add final closing
    transplied.append("}")
    for extra in extras:
        transplied.extend(constructCode(extra))

    print(RenderTree(CONSTANTS_TREE))
    print(RenderTree(SETUP_TREE))
    print(RenderTree(LOOP_TREE))

    for line in transplied:
        print(line)

    TRANSPILED_LINES = transplied

def getLines():
    global TRANSPILED_LINES
    return TRANSPILED_LINES
