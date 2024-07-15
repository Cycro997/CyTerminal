import time
import os
from functools import reduce
import tkinter as tk
import datetime
import logging
import json

print("Welcome! Type g.help for a list of commands.")
print("Note: command must be lowercase")

try:
    import data.extracode.CTScript.CTScript as cts
    import data.extracode.PyLib.maths as m
    import data.extracode.PyLib.logic as l
except ModuleNotFoundError:
    print("A custom module is missing, please check /data/extracode")
    time.sleep(3)
    exit()

ctsdb = {}


def getsettings():
    return json.loads(open("data/other/settings.json").read())


def setsettings(new: dict):
    options = {"log": False, "autogui": False}
    options.update(new)
    newoptions = {}
    for i in options:
        if i in ["log", "autogui"]:
            newoptions[i] = options[i]
    file = open("data/other/settings.json", "w")
    file.writelines(json.dumps(newoptions))
    file.close()


def setsetting(option: str, new):
    optiondict = getsettings()
    optiondict.update({option: new})
    setsettings(optiondict)


setsettings(getsettings())


def get_version():
    return "0.6"


logging.basicConfig(format='%(levelname)s:%(message)s', filename="data/other/log.txt", encoding="utf-8",
                    level=logging.DEBUG)

exccount = 1
variables = {}


#Commands
def main():
    global exccount, m, x
    global inp
    global inpsplit
    global exccount
    try:
        if inpsplit[0] == "g.help" or inpsplit[0] == "g.hlp":
            try:
                if len(inpsplit) == 1:
                    file = open("data/cmdinfo/cmdlist.txt")
                    return file.read()
                elif len(inpsplit) == 2:
                    #Types
                    if inpsplit[1] == "category" or inpsplit[1] == "categories":
                        file = open("data/cmdinfo/t;ctg.help.txt")
                        return file.read()
                    if inpsplit[1] == "subcategory" or inpsplit[1] == "subcategories":
                        file = open("data/cmdinfo/t;sct.help.txt")
                        return file.read()
                    elif inpsplit[1] == "command" or inpsplit[1] == "commands":
                        file = open("data/cmdinfo/t;cmd.help.txt")
                        return file.read()
                    elif inpsplit[1] == "subcommand" or inpsplit[1] == "subcommands":
                        file = open("data/cmdinfo/t;scm.help.txt")
                        return file.read()
                    #Categories
                    elif inpsplit[1] == "g" or inpsplit[1] == "general":
                        file = open("data/cmdinfo/g.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m" or inpsplit[1] == "math":
                        file = open("data/cmdinfo/m.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d" or inpsplit[1] == "data":
                        file = open("data/cmdinfo/d.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l" or inpsplit[1] == "logic":
                        file = open("data/cmdinfo/l.help.txt")
                        return file.read()
                    elif inpsplit[1] == "s" or inpsplit[1] == "script":
                        file = open("data/cmdinfo/s.help.txt")
                        return file.read()
                    #Subcategories
                    elif inpsplit[1] == "d,var":
                        file = open("data/cmdinfo/d,var.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,file":
                        file = open("data/cmdinfo/d,file.help.txt")
                        return file.read()
                    #Commands
                    elif inpsplit[1] == "g.help" or inpsplit[1] == "g.hlp":
                        file = open("data/cmdinfo/g.hlp.help.txt")
                        return file.read()
                    elif inpsplit[1] == "g.exit" or inpsplit[1] == "g.ext":
                        file = open("data/cmdinfo/g.ext.help.txt")
                        return file.read()
                    elif inpsplit[1] == "g.echo" or inpsplit[1] == "g.ech":
                        file = open("data/cmdinfo/g.ech.help.txt")
                        return file.read()
                    elif inpsplit[1] == "g.timer" or inpsplit[1] == "g.tmr":
                        file = open("data/cmdinfo/g.tmr.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.add" or inpsplit[1] == "m.ad":
                        file = open("data/cmdinfo/m.ad.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.multiply" or inpsplit[1] == "m.mu":
                        file = open("data/cmdinfo/m.mu.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.subtract" or inpsplit[1] == "m.su":
                        file = open("data/cmdinfo/m.su.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.divide" or inpsplit[1] == "m.di":
                        file = open("data/cmdinfo/m.di.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.exponentiate" or inpsplit[1] == "m.ex":
                        file = open("data/cmdinfo/m.ex.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.set" or inpsplit[1] == "d,var.st":
                        file = open("data/cmdinfo/d,var.st.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.display" or inpsplit[1] == "d,var.dsp":
                        file = open("data/cmdinfo/d,var.dsp.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.type" or inpsplit[1] == "d,var.tp":
                        file = open("data/cmdinfo/d,var.tp.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.random" or inpsplit[1] == "m.ran":
                        file = open("data/cmdinfo/m.ran.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.append" or inpsplit[1] == "d,var.apd":
                        file = open("data/cmdinfo/d,var.apd.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.compare" or inpsplit[1] == "d,var.cmp":
                        file = open("data/cmdinfo/d,var.cmp.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.len" or inpsplit[1] == "d,var.ln":
                        file = open("data/cmdinfo/d,var.ln.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.settype" or inpsplit[1] == "d,var.stp":
                        file = open("data/cmdinfo/d,var.stp.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.addsetitem" or inpsplit[1] == "d,var.asi":
                        file = open("data/cmdinfo/d,var.asi.help.txt")
                        return file.read()
                    elif inpsplit[1] == "g.version" or inpsplit[1] == "g.ver":
                        file = open("data/cmdinfo/g.ver.help.txt")
                        return file.read()
                    elif inpsplit[1] == "g.changelog" or inpsplit[1] == "g.chlg":
                        file = open("data/cmdinfo/g.chlg.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,var.adddictitem" or inpsplit[1] == "d,var.adi":
                        file = open("data/cmdinfo/d,var.adi.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,file.read" or inpsplit[1] == "d,file.r":
                        file = open("data/cmdinfo/d,var.r.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,file.delete" or inpsplit[1] == "d,file.d":
                        file = open("data/cmdinfo/d,var.d.help.txt")
                        return file.read()
                    elif inpsplit[1] == "d,file.readtovar" or inpsplit[1] == "d,file.rtv":
                        file = open("data/cmdinfo/d,var.rtv.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.round" or inpsplit[1] == "m.rnd":
                        file = open("data/cmdinfo/m.rnd.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.deldecimalpoint" or inpsplit[1] == "m.ddp":
                        file = open("data/cmdinfo/m.ddp.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.not" or inpsplit[1] == "l.n":
                        file = open("data/cmdinfo/l.n.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.and" or inpsplit[1] == "l.a":
                        file = open("data/cmdinfo/l.a.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.nand" or inpsplit[1] == "l.na":
                        file = open("data/cmdinfo/l.na.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.or" or inpsplit[1] == "l.o":
                        file = open("data/cmdinfo/l.o.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.nor" or inpsplit[1] == "l.no":
                        file = open("data/cmdinfo/l.no.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.xor" or inpsplit[1] == "l.x":
                        file = open("data/cmdinfo/l.x.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.xnor" or inpsplit[1] == "l.nx":
                        file = open("data/cmdinfo/l.nx.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.is" or inpsplit[1] == "l.i":
                        file = open("data/cmdinfo/l.i.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.nis" or inpsplit[1] == "l.ni":
                        file = open("data/cmdinfo/l.ni.help.txt")
                        return file.read()
                    elif inpsplit[1] == "s.ctscr" or inpsplit[1] == "s.cts":
                        file = open("data/cmdinfo/s.cts.help.txt")
                        return file.read()
                    elif inpsplit[1] == "g.gui" or inpsplit[1] == "g.g":
                        file = open("data/cmdinfo/g.g.help.txt")
                        return file.read()
                    elif inpsplit[1] == "g.datetime" or inpsplit[1] == "g.dt":
                        file = open("data/cmdinfo/g.dt.help.txt")
                        return file.read()
                    elif inpsplit[1] == "l.binary" or inpsplit[1] == "l.b2":
                        file = open("data/cmdinfo/l.b2.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.fibonacci" or inpsplit[1] == "m.fib":
                        file = open("data/cmdinfo/m.fib.help.txt")
                        return file.read()
                    #Subcommands
                    elif inpsplit[1] == "m.ad.succeed":
                        file = open("data/cmdinfo/m.ad.succeed.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.mu.double":
                        file = open("data/cmdinfo/m.mu.double.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.su.precede":
                        file = open("data/cmdinfo/m.su.precede.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.di.half":
                        file = open("data/cmdinfo/m.di.half.help.txt")
                        return file.read()
                    elif inpsplit[1] == "m.ex.square":
                        file = open("data/cmdinfo/m.ex.square.help.txt")
                        return file.read()
                    #Invalid
                    else:
                        return "Invalid argument"
                else:
                    return "You need from 0 to 1 arguments to run to runt this command"
            except FileNotFoundError:
                return "File is missing."
        elif inpsplit[0] == "g.exit" or inpsplit[0] == "g.ext":
            if len(inpsplit) == 1:
                exit()
            else:
                return "You need only 0 arguments to run this command"
        elif inpsplit[0] == "m.add" or inpsplit[0] == "m.ad":
            if len(inpsplit) >= 3:
                try:
                    var = []
                    for i in inpsplit[1:]:
                        var.append(int(i))

                except ValueError:
                    return "Atleast 1 argument is not an integer"
                else:
                    return sum(var)
            else:
                return "You need atleast 2 arguments to run this command"
        elif inpsplit[0] == "m.multiply" or inpsplit[0] == "m.mu":
            if len(inpsplit) >= 3:
                return reduce(m.multiply, inpsplit[1:])
            else:
                return "You need atleast 2 arguments to run this command"
        elif inpsplit[0] == "m.subtract" or inpsplit[0] == "m.su":
            if len(inpsplit) >= 3:
                return reduce(m.subtract, inpsplit[1:])
            else:
                return "You need atleast 2 arguments to run this command"
        elif inpsplit[0] == "m.divide" or inpsplit[0] == "m.di":
            if len(inpsplit) >= 3:
                return reduce(m.divide, inpsplit[1:])
            else:
                return "You need atleast 2 arguments to run this command"
        elif inpsplit[0] == "g.echo" or inpsplit[0] == "g.ech":
            if len(inpsplit) >= 1:
                return " ".join(inpsplit[1:])
            else:
                return "You need only 1 argument to run this command"
        elif inpsplit[0] == "m.mu.double":
            if len(inpsplit) == 2:
                m.multiply(2, inpsplit[1])
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "g.timer" or inpsplit[0] == "g.tmr":
            if len(inpsplit) >= 2:
                try:
                    if float(inpsplit[1]) <= 450:
                        print("Began a %s second timer" % inpsplit[1])
                        time.sleep(float(inpsplit[1]))
                        if len(inpsplit) > 2:
                            return " ".join(inpsplit[2:])
                        else:
                            return "time's up!"
                    else:
                        return "Time cannot exceed 7 minutes and 30 seconds"
                except ValueError:
                    if inpsplit[1] == "tnsec":
                        print("Began a 10 second timer")
                        time.sleep(10)
                        if len(inpsplit) > 2:
                            return " ".join(inpsplit[2:])
                        else:
                            return "time's up!"
                    elif inpsplit[1] == "twnsec":
                        print("Began a 20 second timer")
                        time.sleep(20)
                        if len(inpsplit) > 2:
                            return " ".join(inpsplit[2:])
                        else:
                            return "time's up!"
                    elif inpsplit[1] == "hlmin":
                        print("Began a 30 second timer")
                        time.sleep(30)
                        if len(inpsplit) > 2:
                            return " ".join(inpsplit[2:])
                        else:
                            return "time's up!"
                    elif inpsplit[1] == "min":
                        print("Began a 1 minute timer")
                        time.sleep(60)
                        if len(inpsplit) > 2:
                            return " ".join(inpsplit[2:])
                        else:
                            return "time's up!"
                    elif inpsplit[1] == "fimin":
                        print("Began a 5 minute timer")
                        time.sleep(300)
                        if len(inpsplit) > 2:
                            return " ".join(inpsplit[2:])
                        else:
                            return "time's up!"
                    else:
                        return "The specified time is invalid"
            else:
                return "You need 1 or 2 arguments to run this command"
        elif inpsplit[0] == "m.di.half":
            if len(inpsplit) == 2:
                m.divide(inpsplit[1], 2)
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "m.exponentiate" or inpsplit[0] == "m.ex":
            if len(inpsplit) >= 3:
                return reduce(m.exponentiate, inpsplit[1:])
            else:
                return "You need atleast 2 arguments to run this command"
        elif inpsplit[0] == "m.ex.square":
            if len(inpsplit) == 2:
                m.exponentiate(inpsplit[1], 2)
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "m.ad.succeed":
            if len(inpsplit) == 2:
                try:
                    sum([int(inpsplit[1]), 1])
                except ValueError:
                    return "Number must be an integer"
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "m.su.precede":
            if len(inpsplit) == 2:
                try:
                    m.subtract(int(inpsplit[1]), 1)
                except ValueError:
                    return "Number must be an integer"
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "d,var.set" or inpsplit[0] == "d,var.st":
            if len(inpsplit) >= 4:
                if inpsplit[1] == "str":
                    variables[inpsplit[2]] = " ".join(inpsplit[3:])
                elif inpsplit[1] == "int":
                    if len(inpsplit) == 4:
                        try:
                            variables[inpsplit[2]] = int(inpsplit[3])
                        except ValueError:
                            return "Invalid value"
                    else:
                        return "3rd argument must be 1 word long"
                elif inpsplit[1] == "flt":
                    if len(inpsplit) == 4:
                        try:
                            variables[inpsplit[2]] = float(inpsplit[3])
                        except ValueError:
                            return "Invalid value"
                    else:
                        return "3rd argument must be 1 word long"
                elif inpsplit[1] == "set":
                    variables[inpsplit[2]] = set(inpsplit[3:])
                elif inpsplit[1] == "tpl":
                    variables[inpsplit[2]] = tuple(inpsplit[3:])
                elif inpsplit[1] == "lst":
                    variables[inpsplit[2]] = inpsplit[3:]
                elif inpsplit[1] == "dict":
                    if len(inpsplit) >= 5:
                        variables[inpsplit[2]] = {inpsplit[3], inpsplit[4]}
                    else:
                        return "3rd argument must be atleast 2 words long"
                else:
                    return "invalid datatype"
            else:
                return "You need 3 arguments to run this command"
            return ""
        elif inpsplit[0] == "d,var.display" or inpsplit[0] == "d,var.dsp":
            if len(inpsplit) == 2:
                return variables.get(inpsplit[1], "Invalid variable")
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "d,var.type" or inpsplit[0] == "d,var.tp":
            if len(inpsplit) == 2:
                try:
                    return type(variables[inpsplit[1]]).__name__
                except KeyError:
                    return "Invalid variable"
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "m.random" or inpsplit[0] == "m.ran":
            if len(inpsplit) == 3:
                try:
                    return m.randomn(int(inpsplit[1]), int(inpsplit[2]))
                except ValueError:
                    return (
                        "Atleast 1 argument is not an"
                        " integer or both arguments are identical "
                        "or the minimum value is greater than the maximum value")
            else:
                return "You need only 2 arguments to run this command"
        elif inpsplit[0] == "d,var.append" or inpsplit[0] == "d,var.apd":
            if len(inpsplit) >= 3:
                try:
                    variables[inpsplit[1]].append(inpsplit[2])
                except AttributeError:
                    return "Variable is not a list"
                except KeyError:
                    return "Variable forgot to exist"
            else:
                return "You need 1 argument to run this command"
            return ""
        elif inpsplit[0] == "d,var.compare" or inpsplit[0] == "d,var.cmp":
            if len(inpsplit) == 3:
                try:
                    left = variables[inpsplit[1]]
                    right = variables[inpsplit[2]]
                    if left == right:
                        return "Left value > right value"
                    if left > right:
                        return "Left value > right value"
                    if left < right:
                        return "Left value < right value"
                except KeyError:
                    return "Invalid variable"
                except ValueError or TypeError:
                    return "Invalid value"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "d,var.len" or inpsplit[0] == "d,var.ln":
            if len(inpsplit) == 2:
                try:
                    return len(variables[inpsplit[1]])
                except NameError:
                    return "Invalid variable"
                except TypeError:
                    return "Variable has no len()"
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "d,var.settype" or inpsplit[0] == "d,var.stp":
            if len(inpsplit) == 3:
                if inpsplit[1] == "str":
                    try:
                        variables[inpsplit[2]] = (
                            str(variables[inpsplit[2]])
                        )
                    except NameError:
                        return "Invalid variable"
                elif inpsplit[1] == "int":
                    if len(inpsplit) == 4:
                        try:
                            variables[inpsplit[2]] = (
                                int(variables[inpsplit[2]])
                            )
                        except NameError:
                            return "Invalid variable"
                        except ValueError:
                            return "Operation failed"
                elif inpsplit[1] == "flt":
                    if len(inpsplit) == 4:
                        try:
                            variables[inpsplit[2]] = (
                                float(variables[inpsplit[2]])
                            )
                        except NameError:
                            return "Invalid variable"
                        except ValueError:
                            return "Operation failed"
                elif inpsplit[1] == "tpl":
                    try:
                        variables[inpsplit[2]] = (
                            tuple(variables[inpsplit[2]])
                        )
                    except NameError:
                        return "Invalid variable"
                elif inpsplit[1] == "set":
                    try:
                        variables[inpsplit[2]] = (
                            set(variables[inpsplit[2]])
                        )
                    except NameError:
                        return "Invalid variable"
                elif inpsplit[1] == "dict":
                    if len(inpsplit) == 4:
                        try:
                            variables[inpsplit[2]] = (
                                dict(variables[inpsplit[2]])
                            )
                        except NameError:
                            return "Invalid variable"
                else:
                    return "invalid datatype"
            else:
                return "You need 3 arguments to run this command"
            return ""
        elif inpsplit[0] == "d,var.addsetitem" or inpsplit[0] == "d,var.asi":
            if len(inpsplit) >= 3:
                try:
                    variables[inpsplit[1]].add(inpsplit[2])
                except AttributeError:
                    return "Variable is not a set"
                except NameError:
                    return "Variable does not exist"
            else:
                return "You need 2 argument to run this command"
            return ""
        elif inpsplit[0] == "g.version" or inpsplit[0] == "g.ver":
            if len(inpsplit) == 1:
                file = open("data/programinfo/version.txt")
                return file.read()
            else:
                return "You need 0 arguments to run this command"
        elif inpsplit[0] == "g.changelog" or inpsplit[0] == "g.chlg":
            if len(inpsplit) == 1:
                file = open("data/programinfo/changelog.txt")
                return file.read()
            else:
                return "You need 0 arguments to run this command"
        elif inpsplit[0] == "d,var.adddictitem" or inpsplit[0] == "d,var.adi":
            if len(inpsplit) >= 4:
                try:
                    variables[inpsplit[1]][inpsplit[2]] = inpsplit[3]
                except AttributeError:
                    return "Variable is not a dictionary"
                except NameError:
                    return "Variable may or may not exist..."
            else:
                return "You need 3 arguments to run this command"
            return ""
        elif inpsplit[0] == "d,file.read" or inpsplit[0] == "d,file.r":
            if len(inpsplit) == 2:
                try:
                    file = open("data//usermadefiles//%s" % inpsplit[1])
                    file.close()
                    return file.read()

                except FileNotFoundError:
                    return "File %s does not exist" % inpsplit[1]
                except PermissionError:
                    return "Access denied"
            else:
                return "You need only 1 argument to run this command"
        elif inpsplit[0] == "d,file.write" or inpsplit[0] == "d,file.w":
            try:
                if len(inpsplit) >= 3:
                    file = open("data//usermadefiles//%s" % inpsplit[1], "w")
                    file.write(" ".join(inpsplit[2:]))
                    file.close()
                else:
                    return "You need 2 arguments to run this command"
            except FileNotFoundError:
                return "File %s does not exist" % inpsplit[1]
            except PermissionError:
                return "Missing permissions or file is in use"
            return ""
        elif inpsplit[0] == "d,file.delete" or inpsplit[0] == "d,file.d":
            try:
                if len(inpsplit) == 2:
                    os.remove("data//usermadefiles//%s" % inpsplit[1])
                else:
                    return "You need 1 argument to run this command"
            except FileNotFoundError:
                return "File %s does not exist" % inpsplit[1]
            except PermissionError:
                return "Missing permissions or file is in use"
            return ""
        elif inpsplit[0] == "d,file.writetovar" or inpsplit[0] == "d,file.wtv":
            if len(inpsplit) == 3:
                try:
                    file = open("data//usermadefiles//%s" % inpsplit[2])
                    variables[inpsplit[1]] = file.read()
                    file.close()
                except FileNotFoundError:
                    return "File %s does not exist" % inpsplit[1]
                except NameError:
                    return "Variable does not exist."
            else:
                return "You need 2 arguments to run this command"
            return ""
        elif inpsplit[0] == "m.round" or inpsplit[0] == "m.rnd":
            try:
                if len(inpsplit) == 2:
                    return round(float(inpsplit[1]))
                elif len(inpsplit) == 3:
                    return m.sround(float(inpsplit[1]), float(inpsplit[2]))
                else:
                    return "You need 2 or 3 arguments to run this command"
            except ValueError:
                return "Invalid arguments"
        elif inpsplit[0] == "s.ctscr" or inpsplit[0] == "s.cts":
            if len(inpsplit) >= 2:
                try:
                    global ctsdb
                    a = cts.CTScr(" ".join(inpsplit[1:]), database=ctsdb)
                    print(a.exec())
                    ctsdb = a.database
                #except Exception:
                #    return("An error occurred")
                finally:
                    pass
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "m.deldecimalpoint" or inpsplit[0] == "m.ddp":
            if len(inpsplit) == 2:
                try:
                    return int(inpsplit[1].replace(".", "", 1))
                except ValueError:
                    return "float or int only"
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "l.not" or inpsplit[0] == "l.n":
            if len(inpsplit) == 2:
                try:
                    return l.l_not(bool(int(inpsplit[1])))
                except Exception:
                    return "Invalid value"
            else:
                return "You need 1 argument to run this command"
        elif inpsplit[0] == "l.and" or inpsplit[0] == "l.a":
            if len(inpsplit) == 3:
                try:
                    return l.l_and(bool(int(inpsplit[1])), bool(int(inpsplit[2])))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "l.nand" or inpsplit[0] == "l.na":
            if len(inpsplit) == 3:
                try:
                    return l.nand(int(inpsplit[1]), int(inpsplit[2]))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "l.or" or inpsplit[0] == "l.o":
            if len(inpsplit) == 3:
                try:
                    return l.l_or(int(inpsplit[1]), int(inpsplit[2]))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "l.nor" or inpsplit[0] == "l.no":
            if len(inpsplit) == 3:
                try:
                    return l.nor(int(inpsplit[1]), int(inpsplit[2]))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "l.xor" or inpsplit[0] == "l.x":
            if len(inpsplit) == 3:
                try:
                    return l.xor(int(inpsplit[1]), int(inpsplit[2]))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "l.xnor" or inpsplit[0] == "l.nx":
            if len(inpsplit) == 3:
                try:
                    return l.xnor(int(inpsplit[1]), int(inpsplit[2]))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "l.is" or inpsplit[0] == "l.i":
            if len(inpsplit) == 3:
                try:
                    return l.l_is(int(inpsplit[1]), int(inpsplit[2]))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "l.nis" or inpsplit[0] == "l.ni":
            if len(inpsplit) == 3:
                try:
                    return l.nis(int(inpsplit[1]), int(inpsplit[2]))
                except Exception:
                    return "Invalid values"
            else:
                return "You need 2 arguments to run this command"
        elif inpsplit[0] == "g.gui" or inpsplit[0] == "g.g":
            def run():
                global inp
                global inpsplit
                inp = entry.get()
                inpsplit = inp.split()
                if len(inpsplit) == 0:
                    inpsplit.append("")
                mainresult = main()
                label2.configure(text=mainresult)
                if getsettings()["log"]:
                    logging.info("(" + inp + "," + mainresult + "," + str(datetime.datetime.now()) + ")")

            if len(inpsplit) == 1:
                window = tk.Tk()
                window.title("CyTerminal v" + get_version())
                window.geometry("800x800")
                label = tk.Label(window, text="Enter command")
                label.pack()
                entry = tk.Entry(window, width=80)
                entry.pack()
                button = tk.Button(window, text="run", command=run)
                button.pack()
                label2 = tk.Label(window, text="", font=("Arial", 7))
                label2.pack()

                window.mainloop()
            else:
                return "only takes 0 arguments"
        elif inpsplit[0] == "g.datetime" or inpsplit[0] == "g.dt":
            x = datetime.datetime.now()
            if len(inpsplit) == 1:
                return x
            elif len(inpsplit) == 2:
                string = inpsplit[1]
                string = string.replace("{", "{e{}")
                string = string.replace("++", "{e+}")
                string = string.replace("##", "{e#}")
                string = string.replace("''", "{e'}")
                string = string.replace("\"\"", "{e\"}")
                string = string.replace("+min", "%M")
                string = string.replace("+c", "%C")
                string = string.replace("+y", "%y")
                string = string.replace("#y", "%Y")
                string = string.replace("'mon", "%b")
                string = string.replace("\"mon", "%B")
                string = string.replace("+mon", "%m")
                string = string.replace("'wd", "%a")
                string = string.replace("\"wd", "%A")
                string = string.replace("+wd", "%w")
                string = string.replace("+d", "%j")
                string = string.replace("'am", "%p")
                string = string.replace("+h", "%I")
                string = string.replace("#h", "%H")

                string = string.replace("+s", "%S")
                string = string.replace("{e+}", "+")
                string = string.replace("{e#}", "#")
                string = string.replace("{e'}", "'")
                string = string.replace("{e\"}", "\"")
                string = string.replace("{e{}", "{")

                return x.strftime(string)
            else:
                return "only takes 0 or 1 arguments"
        elif inpsplit[0] == "l.binary" or inpsplit[0] == "l.b2":
            if len(inpsplit) == 2:
                try:
                    return l.base2(int(inpsplit[1]))
                except ValueError:
                    return "Must be int"
            else:
                return "only takes exactly 1 argument"
        elif inpsplit[0] == "m.fibonacci" or inpsplit[0] == "m.fib":
            import data.extracode.PyLib.maths as m
            if len(inpsplit) == 2:
                try:
                    return m.fibonacci(int(inpsplit[1]))
                except ValueError:
                    return "Must be int"
            else:
                return "only takes exactly 1 argument"

        else:  #If input is invalid
            if inp == "":  #No command
                return "Please enter a command"
            elif "." not in inp:  #No dot (meaning no prefix)
                return "Did you forget the category prefix?"
            elif inp.startswith("."):  #Input starts with a dot
                return "Did you forget the category prefix?"
            else:  #Invalid
                return "Invalid command, perhaps you made a spelling error?"
    except Exception as exception:
        errwind = tk.Tk()
        errwind.geometry("350x200")
        label = tk.Label(errwind, text=f"{type(exception).__name__} {exception} ({exccount})")
        label.pack()
        errwind.mainloop()

        time.sleep(1)
        if exccount == 3:
            exit()
        exccount += 1


g = False
while 1:
    if g == False and getsettings()["autogui"]:
        inp = "g.gui"
        g = True
    else:
        inp = input("Enter command ")
    inpsplit = inp.split(" ")
    if len(inpsplit) == 0:
        inpsplit.append("")
    g = False
    m = str(main())
    print(m)
    if getsettings()["log"]:
        logging.info("(" + inp + "," + m + "," + str(datetime.datetime.now()) + ")")

#Code end
