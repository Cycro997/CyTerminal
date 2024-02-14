print("Welcome! Type g.help for a list of commands.")
print("Note: command must be lowercase")
import time
import random
import os
from functools import reduce
var=0
#Functions
def multiply(a, b):
    try:
        return int(a) * int(b)
    except:
        return "Atleast 1 argument is not a number"
def subtract(a, b, *c):
    try:
        return int(a) - int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"
def divide(a, b, *c):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"
def exponentiate(a, b, *c):
    try:
        return int(a) ** int(b)
    except ValueError:
        return "Atleast 1 argument is not a number"
def randomn(a,b):
    print(random.randrange(a,b))
def specialround(n,d):
    lv1=n/d
    lv2=round(lv1)
    lv3=lv2*d
    return lv3
0
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
            elif inpsplit[1]=="g.freeecho" or inpsplit[1] == "g.fech":
                file = open("data\\cmdinfo\\g.fech.help.txt")
                print(file.read())
            elif inpsplit[1]=="m.round" or inpsplit[1] == "m.rnd":
                file = open("data\\cmdinfo\\m.rnd.help.txt")
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
        if len(inpsplit)>=3:
            try:
                var=[]
                for i in inpsplit[1:]:
                    var.append(int(i))

            except ValueError:
                print("Atleast 1 argument is not an integer")
            else:
                print(sum(var))
        else:
            print("You need atleast 2 arguments to run this command")
    elif inpsplit[0]=="m.multiply":
        if len(inpsplit)>=3:
           print(reduce(multiply, inpsplit[1:]))
        else:
            print("You need atleast 2 arguments to run this command")
    elif inpsplit[0]=="m.subtract":
        if len(inpsplit)>=3:
            print(reduce(subtract, inpsplit[1:]))
        else:
            print("You need atleast 2 arguments to run this command")
    elif inpsplit[0]=="m.divide":
        if len(inpsplit)>=3:
            print(reduce(divide, inpsplit[1:]))
        else:
            print("You need atleast 2 arguments to run this command")
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
        if len(inpsplit)>=3:
            print(reduce(exponentiate, inpsplit[1:]))
        else:
            print("You need atleast 2 arguments to run this command")
    elif inpsplit[0]=="m.ex.square":
        if len(inpsplit) == 2:
            exponentiate(inpsplit[1], 2)
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="m.ad.succeed":
        if len(inpsplit) == 2:
            try:
                sum([int(inpsplit[1]), 1])
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
                code=compile("uservar_%s = \"%s\" " % (inpsplit[2]," ".join(inpsplit[3:])),"test","exec")
                exec(code)
            elif inpsplit[1] == "int":
                if len(inpsplit)==4:
                    try:
                        code=compile("uservar_%s = %s" % (inpsplit[2],int(inpsplit[3])),"test","exec")
                        exec(code)
                    except ValueError:
                        print("Invalid value")
                else:
                    print("3rd argument must be 1 word long")
            elif inpsplit[1] == "flt":
                if len(inpsplit)==4:
                    try:
                        code=compile("uservar_%s = %s" % (inpsplit[2],float(inpsplit[3])),"test","exec")
                        exec(code)
                    except ValueError:
                        print("Invalid value")
                else:
                    print("3rd argument must be 1 word long")
            elif inpsplit[1] == "set":
                code=compile("uservar_%s = %s" % (inpsplit[2],set(inpsplit[3:])),"test","exec")
                exec(code)
            elif inpsplit[1] == "tpl":
                code=compile("uservar_%s = %s" % (inpsplit[2],tuple(inpsplit[3:])),"test","exec")
                exec(code)
            elif inpsplit[1] == "lst":
                code=compile("uservar_%s = %s" % (inpsplit[2],list(inpsplit[3:])),"test","exec")
                exec(code)
            elif inpsplit[1] == "dict":
                if len(inpsplit)>=5:
                    code=compile("uservar_%s = %s" % (inpsplit[2],{inpsplit[3]:inpsplit[4:]}),"test","exec")
                    exec(code)
                else:
                    print("3rd argument must be atleast 2 words long")
            elif inpsplit[1] == "auto":
                try:
                    code=compile("uservar_%s = %s" % (inpsplit[2]," ".join(inpsplit[3:])),"test","exec")
                    exec(code)
                except NameError:
                    print("Name is not defined, did you forget quoration marks (\" \")?")
                except Exception:
                    print("An exception happened")
            else:
                print("invalid datatype")
        else:
            print("You need 3 arguments to run this command")
    elif inpsplit[0]=="d,var.display":
        if len(inpsplit)==2:
            try:
                code=compile("print(uservar_%s)" % (inpsplit[1]),"test","exec")
                exec(code)
            except NameError:
                print("Invalid variabe")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="d,var.type":
        if len(inpsplit)==2:
            try:
                code=compile("""
if type(uservar_%s) == str:
    print('String')
elif type(uservar_%s) == int:
    print('Integer')
elif type(uservar_%s) == float:
    print('Float')
elif type(uservar_%s) == list:
    print('List')
elif type(uservar_%s) == tuple:
    print('Tuple')
elif type(uservar_%s) == set:
    print('Set')
elif type(uservar_%s) == dict:
    print('Dictionary')

else:
    print(type(uservar_%s))

                        """ % (inpsplit[1], inpsplit[1], inpsplit[1], inpsplit[1], inpsplit[1], inpsplit[1], inpsplit[1], inpsplit[1]),"test","exec")
                exec(code)
            except NameError:
                print("Invalid variabe")
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
            try:
                code=compile("uservar_%s.append('%s') " % (inpsplit[1]," ".join(inpsplit[2:])),"test","exec")
                exec(code) 
            except AttributeError:
                print("Variable is not a list")
            except NameError:
                print("Variable forgot to exist")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="d,var.compare":
        if len(inpsplit)==3:
            try:
                code=compile("""
if uservar_%s > uservar_%s:
    print('First variable is greater than the second variable')
elif uservar_%s < uservar_%s:
    print('First variable is smaller than the second variable')
else:
    print('First variable is equal to the second variable')

                        """ % (inpsplit[1], inpsplit[2], inpsplit[1], inpsplit[2]),"test","exec")
                exec(code)
            except NameError:
                print("Invalid variabe")   
            except ValueError or TypeError:
                print("Invalid value")  
        else:
            print("You need 2 arguments to run this command")
    elif inpsplit[0]=="d,var.len":
        if len(inpsplit)==2:
            try:
                code=compile("print(len(uservar_%s))" % (inpsplit[1]),"test","exec")
                exec(code)
            except NameError:
                print("Invalid variabe")
            except TypeError:
                print("Variable has no len()")
        else:
            print("You need 1 argument to run this command")
    elif inpsplit[0]=="d,var.settype":
        if len(inpsplit)>=3:
            if inpsplit[1] == "str":
                try:
                    code=compile("uservar_%s= str(uservar_%s)" % (inpsplit[1], inpsplit[1]),"test","exec")
                    exec(code)
                except NameError:
                    print("Invalid variable")
            elif inpsplit[1] == "int":
                if len(inpsplit)==4:
                    try:
                        code=compile("uservar_%s= int(uservar_%s)" % (inpsplit[1], inpsplit[1]),"test","exec")
                        exec(code)
                    except NameError:
                        print("Invalid variable")
                    except ValueError:
                        print("Operation failed")
            elif inpsplit[1] == "flt":
                if len(inpsplit)==4:
                    try:
                        code=compile("uservar_%s= float(uservar_%s)" % (inpsplit[1], inpsplit[1]),"test","exec")
                        exec(code)
                    except NameError:
                        print("Invalid variable")
                    except ValueError:
                        print("Operation failed")
            elif inpsplit[1] == "tpl":
                try:
                    code=compile("uservar_%s= tuple(str(uservar_%s))" % (inpsplit[1], inpsplit[1]),"test","exec")
                    exec(code)
                except NameError:
                    print("Invalid variable")
            elif inpsplit[1] == "set":
                try:
                    code=compile("uservar_%s= set(str(uservar_%s))" % (inpsplit[1], inpsplit[1]),"test","exec")
                    exec(code)
                except NameError:
                    print("Invalid variable")
            elif inpsplit[1] == "dict":
                if len(inpsplit)==4:
                    try:
                        code=compile("uservar_%s= dict(uservar_%s)" % (inpsplit[1], inpsplit[1]),"test","exec")
                        exec(code)
                    except NameError:
                        print("Invalid variable")
            else:
                print("invalid datatype")
        else:
            print("You need 3 arguments to run this command")
    elif inpsplit[0]=="d,var.addsetitem":
        if len(inpsplit)>=3:
            try:
                code=compile("uservar_%s.add('%s') " % (inpsplit[1]," ".join(inpsplit[2:])),"test","exec")
                exec(code) 
            except AttributeError:
                print("Variable is not a set")
            except NameError:
                print("Variable does not exist")
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
            try:
                code=compile("uservar_%s[%s]='%s' " % (inpsplit[1],inpsplit[2]," ".join(inpsplit[3:])),"test","exec")
                exec(code) 
            except AttributeError:
                print("Variable is not a dictionary")
            except NameError:
                print("Variable may or may not exist...")
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
                code=compile("uservar_%s=%s" % (inpsplit[1],file.read),"test","exec")
                exec(code) 
                file.close
            except FileNotFoundError:
                print("File %s does not exist" % inpsplit[1])
            except NameError:
                print("Variable does not exist.")
        else:
            print("You need 2 arguments to run this command")
    elif inpsplit[0]=="g.freeecho":
        try:
            if len(inpsplit)>= 1:
                code=compile("print(%s)" % ' '.join(inpsplit[1:]),"test","exec")
                exec(code)
            else:
                print("You need only 1 argument to run this command")
        except Exception:
            print("An error occurred")
    elif inpsplit[0]=="m.round":
        try:
            if len(inpsplit)==2:
                print(round(float(inpsplit[1])))
            elif len(inpsplit)==3:
                print(specialround(float(inpsplit[1]),float(inpsplit[2])))
            else:
                print("You need 2 or 3 arguments to run this command")
        except ValueError:
            print("Invalid arguments")
    
    else: #For non-commands
        if inp=="": #No command
            print("Please enter a command")
        elif "." not in inp: #No dot (meaning no prefix)
            print("Did you forget the category prefix?")
        elif inp.startswith("."): #Input starts with a dot
            print("Did you forget the category prefix")
        else: #Invalid
            print("Invalid command, perhaps you made a spelling error?")
#Code end