from functools import reduce
import time
#prerequisite functions
def ctscrMultiply(a, b, *c):
    try:
        return float(a) * float(b)
    except:
        return "Atleast 1 argument is not a number"
def ctscrSubtract(a, b, *c):
    try:
        return float(a) - float(b)
    except:
        return "Atleast 1 argument is not a number"
def ctscrDivide(a, b, *c):
    try:
        return float(a) / float(b)
    except:
        return "Atleast 1 argument is not a number"
class ctscr:
    def __init__(self,script, database=dict()): # ctscr()
        self.script=str(script)
        self.database=dict(database)
    def __str__(self): # str(), print()
        return self.script
    def __len__(self): # len()
        return len(self.scrsplit())
    def __getitem__(self, key): # self[]
        return self.scrsplit()[key]
    def __add__(self,arg): # +
        return ctscr(self.script+";"+str(arg))
    def __sub__(self,arg): # -
        lv1 = self.script.removesuffix(arg)
        lv2 = lv1[:-1]
        return ctscr(lv2)
    def __repr__(self): # repr()
        return "ctscr(\"%s\", database=%s)" % (self.script, self.database)
    def __eq__(self,arg): # ==
        if type(self)==ctscr:
            if repr(self)==repr(arg):
                return True
            else:
                return False
        else:
            return False
    def __ne__(self,arg): # !=
        if type(self)!=ctscr:
            if repr(self)==repr(arg):
                return True
            else:
                return False
        else:
            return False
    def __contains__(self,arg): # in
        if arg in self.scrsplit():
            return True
        else:
            return False

    def scrsplit(self):
        return self.script.split(";")
    def scrfullsplit(self):
        lv1=[]
        for i in self.scrsplit():
            lv1.append(i.split(","))
        return lv1
    def subarg(self,arg,subarg):
        return self.scrfullsplit[arg][subarg-1]
    def keyword(self):
        return self[0]
    def dbadd(self,key,value):
        self.database[key]=value
    def dbdel(self,key):
        self.database.pop(key)
    def dbget(self,key):
        return {key:self.database[key]}
    def exec(self):
        if self.scrsplit()[0].lower()=="echo":
            if len(self.scrsplit())==2:
                if len(self.scrfullsplit()[1])==1:
                    if self.scrsplit()[1].startswith("$"):
                        try:
                            print(self.database[self.scrfullsplit()[1][0][1:]])
                        except KeyError:
                            print("invalid entry: %s" % self.scrfullsplit()[1][0][1:])
                    else:
                        print(self.scrfullsplit()[1][0])
                else:
                    print("argument 1 only takes 1 subargument")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="sum":
            if len(self.scrsplit())==2:
                try:
                    lv1=self.scrfullsplit()[1]
                    lv2=[]
                    for i in lv1:
                        lv2.append(float(i))
                    print(sum(lv2))
                except TypeError:
                    print("invalid values")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="prod":
            if len(self.scrsplit())==2:
                try:
                    lv1=self.scrfullsplit()[1]
                    lv2=[]
                    for i in lv1:
                        lv2.append(float(i))
                    print(reduce(ctscrMultiply, lv2))
                except TypeError:
                    print("invalid values")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="subtract":
            if len(self.scrsplit())==2:
                try:
                    lv1=self.scrfullsplit()[1]
                    lv2=[]
                    for i in lv1:
                        lv2.append(float(i))
                    print(reduce(ctscrSubtract, lv2))
                except TypeError:
                    print("invalid values")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="quotient":
            if len(self.scrsplit())==2:
                try:
                    lv1=self.scrfullsplit()[1]
                    lv2=[]
                    for i in lv1:
                        lv2.append(float(i))
                    print(reduce(ctscrDivide, lv2))
                except TypeError:
                    print("invalid values")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="timer":
            if len(self.scrsplit())==2 or len(self.scrsplit())==3:
                if len(self.scrsplit())==2 and len(self.scrfullsplit()[1])==1:
                    print("Began a timer of %s seconds" % self.scrsplit()[1])
                    time.sleep(float(self.scrsplit()[1]))
                    if len(self.scrsplit())==3:
                        print(self.scrsplit()[2])
                    else:
                        print("Time's up!")
                elif len(self.scrfullsplit()[1])==1 and len(self.scrfullsplit()[2])==1:
                    print("Began a timer of %s seconds" % self.scrsplit()[1])
                    time.sleep(int(self.scrsplit()[1]))
                    if len(self.scrsplit())==3:
                        print(self.scrsplit()[2])
                    else:
                        print("Time's up!")
                else:
                    print("argument 1 and 2 only take 1 subargument")
            else:
                print("only takes 2 arguments")
        elif self.scrsplit()[0].lower()=="round":
            if len(self.scrsplit())==2:
                if len(self.scrfullsplit()[1])==1:
                    try:
                        print(round(float(self.scrsplit()[1])))
                    except:
                        print("invalid values")
                else:
                    print("argument 1 only takes 1 subargument")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="input":
            if len(self.scrsplit())==3:
                if len(self.scrfullsplit()[1])==1 and len(self.scrfullsplit()[2])==1:
                    lv1=input(self.scrsplit()[1])
                    if self.scrsplit()[2].lower()=="py_exec":
                        exec(compile(lv1,"CTscript.py","exec"))
                    elif self.scrsplit()[2].lower()=="echo":
                        print(lv1)
                    elif self.scrsplit()[2].lower()=="none":
                        pass
                    elif self.scrsplit()[2].lower()=="length":
                        print(len(lv1))
                    elif self.scrsplit()[2].lower()=="cts_exec":
                        lv2=ctscr(lv1, database=self.database)
                        lv2.exec()
                        self.database=lv2.database
                    else:
                        print("Invalid mode")
                else:
                    print("arguments 1 and 2 only take 1 subargument")
            else:
                print("only takes 2 arguments")
        elif self.scrsplit()[0].lower()=="cts_terminal":
            if len(self.scrsplit())==2:
                if len(self.scrfullsplit()[1])==1:
                    try:
                        lv1=int(self.scrsplit()[1])
                        lv2=1
                        lv3=ctscr("")
                        lv3.database=self.database
                        while lv1 >= lv2:
                            lv4=input("Line %s/%s: " % (lv2,lv1))
                            lv2+=1
                            lv3.script=lv4
                            lv3.exec()
                        self.database=lv3.database
                    except ValueError:
                        print("invalid line length")
                else:
                    print("argument 1 only takes 1 subargument")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="exit":
            if len(self.scrsplit())==1:
                exit
            else:
                print("only takes 0 arguments")
        elif self.scrsplit()[0].lower()=="db_add":
            if len(self.scrsplit())==3:
                if len(self.scrfullsplit()[1])==1 and len(self.scrfullsplit()[2])==1:
                    self.dbadd(self.scrsplit()[1],self.scrsplit()[2])
                else:
                    print("arguments 1 and 2 only take 1 subargument")
            else:
                print("only takes 2 arguments")
        elif self.scrsplit()[0].lower()=="db_del":
            if len(self.scrsplit())==2:
                if len(self.scrfullsplit()[1])==1 :
                    self.dbdel(self.scrsplit()[1])
                else:
                    print("argument 1 only takes 1 subargument")
            else:
                print("only takes 1 argument")
        elif self.scrsplit()[0].lower()=="db_get":
            if len(self.scrsplit())==2:
                if len(self.scrfullsplit()[1])==1 :
                    print(self.dbget(self.scrsplit()[1]))
                else:
                    print("argument 1 only takes 1 subargument")
            elif len(self.scrsplit())==1:
                print(self.database)
            else:
                print("only takes 1 or 2 arguments")       

        elif len(self.script)==0:
            pass
        elif len(self.scrfullsplit())>1:
            print("keywords don't have subarguments")
        elif len(self.scrfullsplit())==0:
            print("missing keyword")
        else:
            print("invalid keyword")

class mlctscr: #For multi-line scripts
    def __init__(self,scripts):
        self.scripts=scripts
        self.scripts=self.scripts.replace("""
""", "\n")
        self.scrssplit=self.scripts.split("\n")
        self.database=dict("")
    def __str__(self):
        return self.scripts
    def scrssplit(self):
        pass
    def getscripts(self):
        lv1=[]
        for i in self.scrssplit:
            lv1.append(str(i))
        return lv1
    def exec(self):
        lv1=ctscr(";")
        lv1.database=self.database
        for i in self.scrssplit:
            lv1.script=i
            lv1.exec()
        self.database=lv1.database
    def add(self,line):
        self.scrssplit.append(ctscr(line))
        self.scripts+="""
%s""" % line
