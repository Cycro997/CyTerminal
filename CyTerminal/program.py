print("Welcome! Type g.help for a list of commands.")
print("Note: command must be lowercase")
import time
import random
import os
v1,v2,v3 = 0,0,0
#Functions
def add(a, b, *c): 
    try:
        try:
            print(float(a)+float(b)+float(c[0]))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
    except IndexError:
        try:
            print(float(a)+float(b))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
def multiply(a, b, *c):
    try:
        try:
            print(float(a)*float(b)*float(c[0]))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
    except IndexError:
        try:
            print(float(a)*float(b))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
def subtract(a, b, *c):
    try:
        try:
            print(float(a)-float(b)-float(c[0]))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
    except IndexError:
        try:
            print(float(a)-float(b))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
def divide(a, b, *c):
    try:
        try:
            print(float(a)/float(b)/float(c[0]))
        except ValueError:
            print("One of the arguments isn't a number")
        except ZeroDivisionError:
            print("cannot divide by 0")
        except OverflowError:
            print("The result is too large")
    except IndexError:
        try:
            print(float(a)/float(b))
        except ValueError:
            print("One of the arguments isn't a number")
        except ZeroDivisionError:
            print("cannot divide by 0")
        except OverflowError:
            print("The result is too large")
def exponentiate(a, b, *c):
    try:
        try:
            print(float(a)**float(b)**float(c[0]))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
    except IndexError:
        try:
            print(float(a)**float(b))
        except ValueError:
            print("One of the arguments isn't a number")
        except OverflowError:
            print("The result is too large")
def randomn(a,b):
    print(random.randrange(a,b))
def comparevar(a,b,c):
    if a == "v1":
        lv1=v1
    elif a == "v2":
        lv1=v2
    elif a == "v3":
        lv1=v3
    else:
        print("Invalid variable")
        lv2="unknown"
    if b == "v1":
        lv2=v1
    elif b == "v2":
        lv2=v2
    elif b == "v3":
        lv2=v3
    else:
        lv2="unknown"
    if c == "=":
        try:
            print(float(lv1)==float(lv2))
        except ValueError:
            print("Invalid variable or variable type")
    elif c == "<":
        try:
            print(float(lv1)<float(lv2))
        except ValueError:
            print("Invalid variable or variable type")
    elif c == ">":
        try:
            print(float(lv1)>float(lv2))
        except ValueError:
            print("Invalid variable or variable type")
    else:
        print("Invalid comparison operator")
def getvartype(a):
    lNoError=True
    if a == "v1":
        lv1=v1
    elif a == "v2":
        lv1=v2
    elif a == "v3":
        lv1=v3
    else:
        print("Invalid variable")
        lNoError=False
    if lNoError == True:
        if type(lv1) == str:
            return "String"
        elif type(lv1) == int:
            return "Integer"
        elif type(lv1) == float:
            return "Float"
        elif type(lv1) == list:
            return "List"
        elif type(lv1) == tuple:
            return "Tuple"
        elif type(lv1) == set:
            return "Set"
        elif type(lv1) == dict:
            return "Dictionary"
#Commands
while 1:
    inp=input("Enter command ")
    inpsplit=inp.split(" ")
    if inpsplit[0]=="g.help":
        if len(inpsplit) == 1:
            file = open("data\\cmdinfo\\cmdlist.txt")
            print(file.read())
        elif len(inpsplit) == 2:
            #Types
            if inpsplit[1] == "category" or inpsplit[1] == "categories":
                file = open("data\\cmdinfo\\t;ctg.help.txt")
                print(file.read())
            if inpsplit[1] == "subcategory" or inpsplit[1] == "subcategories":
                file = open("data\\cmdinfo\\t;sct.help.txt")
                print(file.read())
            elif inpsplit[1] == "command" or inpsplit[1] == "commands":
                file = open("data\\cmdinfo\\t;cmd.help.txt")
                print(file.read())
            elif inpsplit[1] == "subcommand" or inpsplit[1] == "subcommands":
                file = open("data\\cmdinfo\\t;scm.help.txt")
                print(file.read())
            #Categories
            elif inpsplit[1] == "g" or inpsplit[1] == "general":
                file = open("data\\cmdinfo\\g.help.txt")
                print(file.read())
            elif inpsplit[1]=="m" or inpsplit[1] == "math":
                file = open("data\\cmdinfo\\m.help.txt")
                print(file.read())
            elif inpsplit[1]=="d" or inpsplit[1] == "data":
                file = open("data\\cmdinfo\\d.help.txt")
                print(file.read())
            #Subcategories
            elif inpsplit[1] == "d,var":
                file = open("data\\cmdinfo\\d,var.help.txt")
                print(file.read())
            elif inpsplit[1] == "d,file":
                file = open("data\\cmdinfo\\d,file.help.txt")
                print(file.read())
            #Commands
            elif inpsplit[1]=="g.help" or inpsplit[1] == "g.hlp":
                file = open("data\\cmdinfo\\g.hlp.help.txt")
                print(file.read())
            elif inpsplit[1]=="g.exit" or inpsplit[1] == "g.ext":
                file = open("data\\cmdinfo\\g.ext.help.txt")
                print(file.read())
            elif inpsplit[1]=="g.echo" or inpsplit[1] == "g.ech":
                file = open("data\\cmdinfo\\g.ech.help.txt")
                print(file.read())
            elif inpsplit[1]=="g.timer" or inpsplit[1] == "g.tmr":
                file = open("data\\cmdinfo\\g.tmr.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.add" or inpsplit[1] == "m.ad":
                file = open("data\\cmdinfo\\m.ad.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.multiply" or inpsplit[1] == "m.mu":
                file = open("data\\cmdinfo\\m.mu.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.subtract" or inpsplit[1] == "m.su":
                file = open("data\\cmdinfo\\m.su.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.divide" or inpsplit[1] == "m.di":
                file = open("data\\cmdinfo\\m.di.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.exponentiate" or inpsplit[1] == "m.ex":
                file = open("data\\cmdinfo\\m.ex.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.set" or inpsplit[1] == "d,var.st":
                file = open("data\\cmdinfo\\d,var.st.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.display" or inpsplit[1] == "d,var.dsp":
                file = open("data\\cmdinfo\\d,var.dsp.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.type" or inpsplit[1] == "d,var.tp":
                file = open("data\\cmdinfo\\d,var.tp.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.random" or inpsplit[1] == "m.ran":
                file = open("data\\cmdinfo\\m.ran.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.append" or inpsplit[1] == "d,var.apd":
                file = open("data\\cmdinfo\\d,var.apd.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.compare" or inpsplit[1] == "d,var.cmp":
                file = open("data\\cmdinfo\\d,var.cmp.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.len" or inpsplit[1] == "d,var.ln":
                file = open("data\\cmdinfo\\d,var.ln.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.settype" or inpsplit[1] == "d,var.stp":
                file = open("data\\cmdinfo\\d,var.stp.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.addsetitem" or inpsplit[1] == "d,var.asi":
                file = open("data\\cmdinfo\\d,var.asi.help.txt")
                print(file.read())
            elif inpsplit[1]=="g.version" or inpsplit[1] == "g.ver":
                file = open("data\\cmdinfo\\g.ver.help.txt")
                print(file.read())
            elif inpsplit[1]=="g.changelog" or inpsplit[1] == "g.chlg":
                file = open("data\\cmdinfo\\g.chlg.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,var.adddictitem" or inpsplit[1] == "d,var.adi":
                file = open("data\\cmdinfo\\d,var.adi.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,file.read" or inpsplit[1] == "d,file.r":
                file = open("data\\cmdinfo\\d,var.r.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,file.delete" or inpsplit[1] == "d,file.d":
                file = open("data\\cmdinfo\\d,var.d.help.txt")
                print(file.read())
            elif inpsplit[1]=="d,file.readtovar" or inpsplit[1] == "d,file.rtv":
                file = open("data\\cmdinfo\\d,var.rtv.help.txt")
                print(file.read())
            #Subcommands
            elif inpsplit[1]=="m.ad.succeed" :
                file = open("data\\cmdinfo\\m.ad.succeed.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.mu.double" :
                file = open("data\\cmdinfo\\m.mu.double.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.su.precede" :
                file = open("data\\cmdinfo\\m.su.precede.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.di.half":
                file = open("data\\cmdinfo\\m.di.half.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.ex.square" :
                file = open("data\\cmdinfo\\m.ex.square.help.txt")
                print(file.read())
            #Invalid
            else:
                print("Invalid argument")
        else:
            print("You need from 0 to 1 arguments to run to runt this command")         
    elif inpsplit[0]=="g.exit":
        if len(inpsplit) == 1:
            exit()
        else:
            print("You need only 0 arguments to run this command")
    elif inpsplit[0]=="m.add":
        if len(inpsplit)==4:
            add(inpsplit[1],inpsplit[2],inpsplit[3])
        elif len(inpsplit)==3:
            add(inpsplit[1],inpsplit[2])
        else:
            print("You need from 2 to 3 arguments to run this command")
    elif inpsplit[0]=="m.multiply":
        if len(inpsplit)==4:
           multiply(inpsplit[1],inpsplit[2],inpsplit[3])
        elif len(inpsplit)==3:
            multiply(inpsplit[1],inpsplit[2])
        else:
            print("You need from 2 to 3 arguments to run this command")
    elif inpsplit[0]=="m.subtract":
        if len(inpsplit)==4:
            subtract(inpsplit[1],inpsplit[2],inpsplit[3])
        elif len(inpsplit)==3:
            subtract(inpsplit[1],inpsplit[2])
        else:
            print("You need from 2 to 3 arguments to run this command")
    elif inpsplit[0]=="m.divide":
        if len(inpsplit)==4:
            divide(inpsplit[1],inpsplit[2],inpsplit[3])
        elif len(inpsplit)==3:
            divide(inpsplit[1],inpsplit[2])
        else:
            print("You need from 2 to 3 arguments to run this command")
    elif inpsplit[0]=="g.echo":
        if len(inpsplit)>= 1:
            print(" ".join(inpsplit[1:]))
        else:
            print("You need only 1 argument to run this command")
    elif inpsplit[0]=="m.mu.double":
        if len(inpsplit) == 2:
            multiply(2,inpsplit[1])
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="g.timer":
        if len(inpsplit) >= 2:
            try:
                if float(inpsplit[1])<=450:
                    print("Began a %s second timer" % inpsplit[1])
                    time.sleep(float(inpsplit[1]))
                    if len(inpsplit)>2:
                        print(" ".join(inpsplit[2:]))
                    else:
                        print("time's up!")
                else:
                    print("Time cannot exceed 7 minutes and 30 seconds")
            except ValueError:
                if inpsplit[1]=="tnsec":
                    print("Began a 10 second timer")
                    time.sleep(10)
                    if len(inpsplit)>2:
                        print(" ".join(inpsplit[2:]))
                    else:
                        print("time's up!")
                elif inpsplit[1]=="twnsec":
                    print("Began a 20 second timer")
                    time.sleep(20)
                    if len(inpsplit)>2:
                        print(" ".join(inpsplit[2:]))
                    else:
                        print("time's up!")
                elif inpsplit[1]=="hlmin":
                    print("Began a 30 second timer")
                    time.sleep(30)
                    if len(inpsplit)>2:
                        print(" ".join(inpsplit[2:]))
                    else:
                        print("time's up!")
                elif inpsplit[1]=="min":
                    print("Began a 1 minute timer")
                    time.sleep(60)
                    if len(inpsplit)>2:
                        print(" ".join(inpsplit[2:]))
                    else:
                        print("time's up!")
                elif inpsplit[1]=="fimin":
                    print("Began a 5 minute timer")
                    time.sleep(300)
                    if len(inpsplit)>2:
                        print(" ".join(inpsplit[2:]))
                    else:
                        print("time's up!")
                else:
                    print("The specified time is invalid")
        else:
            print("You need 1 or 2 arguments to run this command")
    elif inpsplit[0]=="m.di.half":
        if len(inpsplit) == 2:
            divide(inpsplit[1], 2)
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="m.exponentiate":
        if len(inpsplit)==4:
            exponentiate(inpsplit[1],inpsplit[2],inpsplit[3])
        elif len(inpsplit)==3:
            exponentiate(inpsplit[1],inpsplit[2])
        else:
            print("You need from 2 to 3 arguments to run this command")
    elif inpsplit[0]=="m.ex.square":
        if len(inpsplit) == 2:
            exponentiate(inpsplit[1], 2)
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="m.ad.succeed":
        if len(inpsplit) == 2:
            try:
                add(int(inpsplit[1]), 1)
            except ValueError:
                print("Number must be an integer")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="m.su.precede":
        if len(inpsplit) == 2:
            try:
                subtract(int(inpsplit[1]), 1)
            except ValueError:
                print("Number must be an integer")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="d,var.set":
        if len(inpsplit)>=4:
            if inpsplit[1] == "str":
                if inpsplit[2] == "v1":
                    v1=" ".join(inpsplit[3:])
                elif inpsplit[2] == "v2":
                    v2=" ".join(inpsplit[3:])
                elif inpsplit[2] == "v3":
                    v3=" ".join(inpsplit[3:])
                elif inpsplit[2]=="all":
                    v1=v2=v3=" ".join(inpsplit[3:])
                else:
                    print("invalid variable")
            elif inpsplit[1] == "int":
                if len(inpsplit)==4:
                    if inpsplit[2] == "v1":
                        try:
                            v1=int(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    elif inpsplit[2] == "v2":
                        try:
                            v2=int(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    elif inpsplit[2] == "v3":
                        try:
                            v3=int(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    elif inpsplit[2]=="all":
                        try:
                            v1=v2=v3=int(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    else:
                        print("invalid variable")
                else:
                    print("3rd argument must be 1 word long")
            elif inpsplit[1] == "flt":
                if len(inpsplit)==4:
                    if inpsplit[2] == "v1":
                        try:
                           v1=float(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    elif inpsplit[2] == "v2":
                        try:
                            v2=float(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    elif inpsplit[2] == "v3":
                        try:
                            v3=float(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    elif inpsplit[2]=="all":
                        try:
                            v1=v2=v3=float(inpsplit[3])
                        except ValueError:
                            print("invalid value")
                    else:
                        print("invalid variable")
                else:
                    print("3rd argument must be 1 word long")
            elif inpsplit[1] == "set":
                if inpsplit[2] == "v1":
                    v1=set(inpsplit[3:])
                elif inpsplit[2] == "v2":
                    v2=set(inpsplit[3:])
                elif inpsplit[2] == "v3":
                    v3=set(inpsplit[3:])
                elif inpsplit[2]=="all":
                    v1=v2=v3=set(inpsplit[3:])
                else:
                    print("invalid variable")
            elif inpsplit[1] == "tpl":
                if inpsplit[2] == "v1":
                    v1=tuple(inpsplit[3:])
                elif inpsplit[2] == "v2":
                    v2=tuple(inpsplit[3:])
                elif inpsplit[2] == "v3":
                    v3=tuple(inpsplit[3:])
                elif inpsplit[2]=="all":
                    v1=v2=v3=tuple(inpsplit[3:])
                else:
                    print("invalid variable")
            elif inpsplit[1] == "lst":
                if inpsplit[2] == "v1":
                    v1=inpsplit[3:]
                elif inpsplit[2] == "v2":
                    v2=inpsplit[3:]
                elif inpsplit[2] == "v3":
                    v3=inpsplit[3:]
                elif inpsplit[2]=="all":
                    v1=v2=v3=inpsplit[3:]
                else:
                    print("invalid variable")
            elif inpsplit[1] == "dict":
                if len(inpsplit)>=5:
                    if inpsplit[2] == "v1":
                        v1={
                            inpsplit[3] : " ".join(inpsplit[4:])
                        }
                    elif inpsplit[2] == "v2":
                        v2={
                            inpsplit[3] : " ".join(inpsplit[4:])
                        }
                    elif inpsplit[2] == "v3":
                        v3={
                            inpsplit[3] : " ".join(inpsplit[4:])
                        }
                    elif inpsplit[2]=="all":
                        v1=v2=v3={
                            inpsplit[3] : " ".join(inpsplit[4:])
                        }
                    else:
                        print("invalid variable")
                else:
                    print("3rd argument must be atleast 2 words long")
            else:
                print("invalid datatype")
        else:
            print("You need 3 arguments to run this command")
    elif inpsplit[0]=="d,var.display":
        if len(inpsplit)==2:
            if inpsplit[1]=="v1":
                print(v1)
            elif inpsplit[1]=="v2":
                print(v2)
            elif inpsplit[1]=="v3":
                print(v3)
            elif inpsplit[1]=="all":
                print("v1: %s" % v1)
                print("v2: %s" % v2)
                print("v3: %s" % v3)
            else:
                print("Invalid variable")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="d,var.type":
        if len(inpsplit)==2:
            if inpsplit[1]=="v1":
                print(getvartype("v1"))
            elif inpsplit[1]=="v2":
                print(getvartype("v2"))
            elif inpsplit[1]=="v3":
                print(getvartype("v3"))
            elif inpsplit[1]=="all":
                print("v1: %s" % getvartype("v1"))
                print("v2: %s" % getvartype("v2"))
                print("v3: %s" % getvartype("v3"))
            else:
                print("Invalid variable")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="m.random":
        if len(inpsplit)==3:
            try:
                randomn(int(inpsplit[1]),int(inpsplit[2]))
            except ValueError:
                print("Atleast 1 argument is not an integer or both arguments are identical or the minimum value is greater than the maximum value")
        else:
            print("You need only 2 arguments to run this command")
    elif inpsplit[0]=="d,var.append":
        if len(inpsplit)>=3:
            if inpsplit[1]=="v1":
                try:
                    v1.append(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Variable is not a list")
            elif inpsplit[1]=="v2":
                try:
                    v2.append(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Variable is not a list")
            elif inpsplit[1]=="v3":
                try:
                    v3.append(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Variable is not a list")
            elif inpsplit[1]=="all":
                try:
                    v1.append(" ".join(inpsplit[2:]))
                    v2.append(" ".join(inpsplit[2:]))
                    v3.append(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Atleast 1 variable is not a list")
            else:
                print("Invalid variable")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="d,var.compare":
        if len(inpsplit)==4:
            comparevar(inpsplit[1], inpsplit[2], inpsplit[3])
        else:
            print("You need 3 arguments to run this command")
    elif inpsplit[0]=="d,var.len":
        if len(inpsplit)==2:
            try:
                if inpsplit[1]=="v1":
                    print(len(v1))
                elif inpsplit[1]=="v2":
                    print(len(v2))
                elif inpsplit[1]=="v3":
                    print(len(v3))
                elif inpsplit[1]=="all":
                    print("v1: %s" % len(v1))
                    print("v1: %s" % len(v2))
                    print("v1: %s" % len(v3))
                else:
                    print("invalid variable")
            except TypeError:
                print("Variable has no len()")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="d,var.settype":
        if len(inpsplit)>=3:
            if inpsplit[1] == "str":
                if inpsplit[2] == "v1":
                    v1=str(v1)
                elif inpsplit[2] == "v2":
                    v2=str(v2)
                elif inpsplit[2] == "v3":
                    v3=str(v3)
                elif inpsplit[2]=="all":
                    v1=str(v1)
                    v2=str(v2)
                    v3=str(v3)
                else:
                    print("invalid variable")
            elif inpsplit[1] == "int":
                if len(inpsplit)==4:
                    if inpsplit[2] == "v1":
                        try:
                            v1=int(v1)
                        except ValueError:
                            print("Cannot make the specified variable an integer")
                    elif inpsplit[2] == "v2":
                        try:
                            v2=int(v2)
                        except ValueError:
                            print("Cannot make the specified variable an integer")
                    elif inpsplit[2] == "v3":
                        try:
                            v3=int(v3)
                        except ValueError:
                            print("Cannot make the specified variable an integer")
                    elif inpsplit[2]=="all":
                        try:
                            v1=int(v1)
                            v2=int(v2)
                            v3=int(v3)
                        except ValueError:
                            print("Cannot make atleast 1 variable an integer")
                    else:
                        print("invalid variable")
            elif inpsplit[1] == "flt":
                if len(inpsplit)==4:
                    if inpsplit[2] == "v1":
                        try:
                           v1=float(v1)
                        except ValueError:
                            print("Cannot make the specified variable a floating point number")
                    elif inpsplit[2] == "v2":
                        try:
                            v2=float(v2)
                        except ValueError:
                            print("Cannot make the specified variable a floating point number")
                    elif inpsplit[2] == "v3":
                        try:
                            v3=float(v3)
                        except ValueError:
                            print("Cannot make the specified variable a floating point number")
                    elif inpsplit[2]=="all":
                        try:
                            v1=float(v1)
                            v2=float(v2)
                            v3=float(v3)
                        except ValueError:
                            print("Cannot make atleast 1 variable a floating point number")
                    else:
                        print("invalid variable")
            elif inpsplit[1] == "lst":
                if inpsplit[2] == "v1":
                    v1=list(str(v1))
                elif inpsplit[2] == "v2":
                    v2=list(str(v2))
                elif inpsplit[2] == "v3":
                    v3=list(str(v3))
                elif inpsplit[2]=="all":
                    v1=list(str(v1))
                    v2=list(str(v2))
                    v3=list(str(v3))
                else:
                    print("invalid variable")
            elif inpsplit[1] == "tpl":
                if inpsplit[2] == "v1":
                    v1=tuple(str(v1))
                elif inpsplit[2] == "v2":
                    v2=tuple(str(v2))
                elif inpsplit[2] == "v3":
                    v3=tuple(str(v3))
                elif inpsplit[2]=="all":
                    v1=tuple(str(v1))
                    v2=tuple(str(v2))
                    v3=tuple(str(v3))
                else:
                    print("invalid variable")
            elif inpsplit[1] == "set":
                if inpsplit[2] == "v1":
                    v1=set(str(v1))
                elif inpsplit[2] == "v2":
                    v2=set(str(v2))
                elif inpsplit[2] == "v3":
                    v3=set(str(v3))
                elif inpsplit[2]=="all":
                    v1=set(str(v1))
                    v2=set(str(v2))
                    v3=set(str(v3))
                else:
                    print("invalid variable")
            elif inpsplit[1] == "dict":
                if len(inpsplit)==4:
                    if inpsplit[2] == "v1":
                        try:
                           v1=dict(v1)
                        except ValueError:
                            print("Cannot make the specified variable a dictionary")
                    elif inpsplit[2] == "v2":
                        try:
                            v2=dict(v2)
                        except ValueError:
                            print("Cannot make the specified variable a dictionary")
                    elif inpsplit[2] == "v3":
                        try:
                            v3=dict(v3)
                        except ValueError:
                            print("Cannot make the specified variable a dictionary")
                    elif inpsplit[2]=="all":
                        try:
                            v1=dict(v1)
                            v2=dict(v2)
                            v3=dict(v3)
                        except ValueError:
                            print("Cannot make atleast 1 variable a dictionary")
                    else:
                        print("invalid variable")
            else:
                print("invalid datatype")
        else:
            print("You need 3 arguments to run this command")
    elif inpsplit[0]=="d,var.addsetitem":
        if len(inpsplit)>=3:
            if inpsplit[1]=="v1":
                try:
                    v1.add(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Variable is not a set")
            elif inpsplit[1]=="v2":
                try:
                    v2.add(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Variable is not a set")
            elif inpsplit[1]=="v3":
                try:
                    v3.add(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Variable is not a set")
            elif inpsplit[1]=="all":
                try:
                    v1.add(" ".join(inpsplit[2:]))
                    v2.add(" ".join(inpsplit[2:]))
                    v3.add(" ".join(inpsplit[2:]))
                except AttributeError:
                    print("Atleast 1 variable is not a set")
            else:
                print("Invalid variable")
        else:
            print("You need 2 argument to run this command")
    elif inpsplit[0]=="g.version":
        if len(inpsplit) == 1:
            file = open("data/programinfo/version.txt")
            print(file.read())
        else:
            print("You need 0 arguments to run this commmand")
    elif inpsplit[0]=="g.changelog":
        if len(inpsplit) == 1:
            file = open("data/programinfo/changelog.txt")
            print(file.read())
        else:
            print("You need 0 arguments to run this commmand")
    elif inpsplit[0]=="d,var.adddictitem":
        if len(inpsplit)>=4:
            if inpsplit[1]=="v1":
                try:
                    v1[inpsplit[2]]=(" ".join(inpsplit[3:]))
                except AttributeError:
                    print("Variable is not a dictionary")
            elif inpsplit[1]=="v2":
                try:
                    v2[inpsplit[2]]=(" ".join(inpsplit[3:]))
                except AttributeError:
                    print("Variable is not a dictionary")
            elif inpsplit[1]=="v3":
                try:
                    v3[inpsplit[2]]=(" ".join(inpsplit[3:]))
                except AttributeError:
                    print("Variable is not a dictionary")
            elif inpsplit[1]=="all":
                try:
                    v1[inpsplit[2]]=(" ".join(inpsplit[3:]))
                    v2[inpsplit[2]]=(" ".join(inpsplit[3:]))
                    v3[inpsplit[2]]=(" ".join(inpsplit[3:]))
                except AttributeError:
                    print("Atleast 1 variable is not a dictionary")
            else:
                print("Invalid variable")
        else:
            print("You need 3 arguments to run this command") 
    elif inpsplit[0]=="d,file.read":
        if len(inpsplit)==2:
            try:
                file=open("data//usermadefiles//%s" % inpsplit[1])
                print(file.read())
                file.close
            except FileNotFoundError:
                print("File %s does not exist" % inpsplit[1])
        else:
            print("You need only 1 argument to run this command")
    elif inpsplit[0]=="d,file.write":
        try:
            if len(inpsplit)>=3:
                file=open("data//usermadefiles//%s" % inpsplit[1], "w")
                file.write(" ".join(inpsplit[2:]))
                file.close()
            else:
                print("You need 2 arguments to run this command")
        except FileNotFoundError:
                print("File %s does not exist" % inpsplit[1])
        except PermissionError:
            print("Missing permissions or file is in use")
    elif inpsplit[0]=="d,file.delete":
        try:
            if len(inpsplit)==2:
                os.remove("data//usermadefiles//%s" % inpsplit[1])
            else:
                print("You need 1 argument to run this command")
        except FileNotFoundError:
            print("File %s does not exist" % inpsplit[1])
        except PermissionError:
            print("Missing permissions or file is in use")
    elif inpsplit[0]=="d,file.readtovar":
        if len(inpsplit)==3:
            try:
                file=open("data//usermadefiles//%s" % inpsplit[2])
                if inpsplit[1]=="v1":
                    v1=file.read()
                elif inpsplit[1]=="v2":
                    v2=file.read()
                elif inpsplit[1]=="v3":
                    v3=file.read()
                elif inpsplit[1]=="all":
                    v1=v2=v3=file.read()
                else:
                    print("Invalid variable")
                file.close
            except FileNotFoundError:
                print("File %s does not exist" % inpsplit[1])
        else:
            print("You need 2 arguments to run this command")

    else: #For non-commands
        if inp=="": #No command
            print("Please enter a command")
        elif "." not in inp: #No dot (meaning no prefix)
            print("Did you forget the category prefix?")
        else: #Invalid
            print("Invalid command, perhaps you made a spelling error?")
#Code end