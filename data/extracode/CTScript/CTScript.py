class CTScr:
    def __init__(self, script, database=None, options=None):  # ctscr()
        if options is None:
            options = {}
        if database is None:
            database = {}
        self.script = str(script)
        self.database = dict(database)
        self.options = CTScr.default_options()
        self.options.update(dict(options))
        self.log = []

    def __str__(self):  # str(), print()
        return self.script

    def __len__(self):  # len()
        return len(self.scrsplit())

    def __getitem__(self, arg):  # self[]
        if len(arg) == 1:
            return self.scrsplit()[arg[0]]
        else:
            return self.scrfullsplit()[arg[0]][arg[1]]

    def __add__(self, arg):  # +
        if type(arg) is CTScr:
            return CTScr.Multiline(self.script + ";;;" + arg.script, database={**self.database, **arg.database})
        else:
            return NotImplemented

    def __repr__(self):  # repr()
        return "ctscr('%s', database=%s, options=%s)" % (self.script, self.database, self.options)

    def __eq__(self, arg):  # ==
        if type(self) is CTScr:
            if repr(self) == repr(arg):
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, arg):  # !=
        return not self == arg

    def __contains__(self, arg):  # in
        if arg in self.scrsplit():
            return True
        else:
            return False

    def __bool__(self) -> bool:  #bool()
        if len(self) != 0:
            if self.keyword_valid():
                return True
            else:
                return False
        else:
            return False

    def __delattr__(self, attr):
        raise AttributeError(f"'ctscr' object attribute '{attr}' is undeletable")

    def __setattr__(self, name: str, value):
        if name in ["script", "database", "options", "log"]:
            pass
        elif name in [
            "scrsplit", "scrfullsplit", "instant", "keywords", "type",
            "defaultOptions", "compile", "subarg", "keyword",
            "dbadd", "dbdel", "dbget", "dbclear", "keywordValid",
            "analyze", "exec",
        ] or name.upper() == name or name.startswith("_"):
            raise AttributeError("'ctscr' object attribute '" + name + "' is read-only")
        else:
            raise AttributeError(f"attribute '{name}' does not exist")
        object.__setattr__(self, name, value)

    def __new__(cls: type, obj, *args, **kwargs):
        try:
            out = obj.__ctscr__(*args, **kwargs)
        except AttributeError:
            out = object.__new__(CTScr)
        return out

    def __ctscr__(self):
        return self

    class Multiline:  #For multi-line scripts
        def __init__(self, scripts, database=None, options=None):
            if options is None:
                options = dict()
            if database is None:
                database = dict()
            self.scripts = scripts
            self.database = dict(database)
            self.options = CTScr.default_options()
            self.options.update(dict(options))

        def __str__(self):
            return self.scripts

        def __len__(self):
            return len(self.scrssplit)

        def __repr__(self):  # repr()
            return "ctscr.multiline('%s', database=%s, options=%s)" % (self.scripts, self.database, self.options)

        def scrssplit(self):
            return self.scripts.split(";;;")

        def getscripts(self):
            lv1 = []
            for i in self.scrssplit:
                lv1.append(str(i))
            return lv1

        def exec(self):
            lv1 = CTScr(";")
            lv1.database = self.database
            lv1.options = self.options
            lv2 = []
            for i in self.scrssplit():
                lv1.script = i
                lv2.append(lv1.exec())
            self.database = lv1.database
            self.options = lv1.options
            return lv2

        def add(self, line):
            self.scripts += ";;;%s" % line

    class Interpreter:  #Runs code
        def __init__(self, script="", options=None, modifiers=None):  # ctscr()
            if modifiers is None:
                modifiers = dict()
            if options is None:
                options = dict()
            self.modifiers = CTScr.Interpreter.default_modifiers()
            self.modifiers.update(dict(modifiers))
            self.scrobject = CTScr(script=script, options=options)

        def __str__(self):
            return "<ctscr interpreter object>"

        def __repr__(self):
            return f"ctscr.interpreter(script={self.scrobject.script!r},options={self.scrobject.options!r}" \
                   f",modifiers={self.modifiers!r})"

        def exec(self, script):
            for i in range(self.modifiers["exec_times"]):
                self.scrobject.script = script
                if type(self.modifiers["py_scr"]) is str:
                    exec(self.modifiers["py_scr"])
                if not self.modifiers["errors"]:
                    try:
                        return self.scrobject.exec()
                    except Exception as exception:
                        return f"Exception: {exception}"
                else:
                    return self.scrobject.exec()

        @staticmethod
        def default_modifiers(modifier="all"):
            defaults = {
                "py_scr": None,
                "exec_times": 1,
                "errors": True,
            }
            if modifier == "all":
                return defaults
            else:
                return defaults[modifier]

    class TypeError(TypeError):
        pass

    class ExecError(Exception):
        pass

    @staticmethod
    def instant(script: str, database=None, options=None):  # Instantly runs the code
        if options is None:
            options = {}
        if database is None:
            database = {}
        scr = CTScr(script, database=database, options=options)
        e = scr.exec()
        return e

    @staticmethod
    def keywords() -> set[str]:
        return {"echo", "sum", "prod", "subtract", "quotient", "timer", "round", "input",
                "cts_terminal", "exit", "db_add", "db_del", "db_get", "type", "settypestatic",
                "settypedb"}

    @staticmethod
    def type(arg):
        if type(arg) is CTScr:
            return "single-line ctscript"
        elif type(arg) is CTScr.Multiline:
            return "multi-line ctscript"
        elif type(arg) is CTScr.Interpreter:
            return "ctscript interpreter"
        else:
            raise CTScr.TypeError("Invalid type of arg (%s)" % type(arg))

    @staticmethod
    def default_options(option="all"):
        defaults = {
            "clear": False,
            "log": False
        }
        if option == "all":
            return defaults
        else:
            return defaults[option]

    @staticmethod
    def compile(file: str):
        ctscrfile = open(file).read()
        return CTScr.Multiline(ctscrfile).exec()

    def scrsplit(self):
        return self.script.split(";")

    def scrfullsplit(self):
        lv1 = []
        for i in self.scrsplit():
            lv1.append(i.split(","))
        return lv1

    def subarg(self, arg, subarg):
        return self.scrfullsplit()[arg][subarg - 1]

    def keyword(self):
        return self[0]

    def dbadd(self, key, value):
        self.database[key] = value

    def dbdel(self, key):
        self.database.pop(key)

    def dbget(self, key, nokey=False):
        if not nokey:
            return {key: self.database[key]}
        else:
            return self.database[key]

    def dbclear(self):
        self.database = dict()

    def keyword_valid(self):
        if self.keyword() in CTScr.keywords():
            return True
        else:
            return False

    def analyze(self, is_dict=True):
        if is_dict:
            analysis = {
                "script": self.script,
                "database": self.database,
                "options": self.options
            }
        else:
            analysis = f"script: {self.script}\ndatabase:{self.database}\noptions:{self.options}"
        return analysis

    def exec(self):
        try:
            import time
            from functools import reduce
            if self.scrsplit()[0].lower() == "echo":
                if len(self.scrsplit()) == 2:
                    if len(self.scrfullsplit()[1]) == 1:
                        if self.scrsplit()[1].startswith("$"):
                            try:
                                return self.database[self.scrfullsplit()[1][0][1:]]
                            except KeyError:
                                return "invalid entry: %s" % self.scrfullsplit()[1][0][1:]
                        else:
                            return self.scrfullsplit()[1][0]
                    else:
                        return "argument 1 only takes 1 subargument"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "sum":
                if len(self.scrsplit()) == 2:
                    try:
                        lv1 = self.scrfullsplit()[1]
                        lv2 = []
                        for i in lv1:
                            lv2.append(float(i))
                        return sum(lv2)
                    except TypeError:
                        return "invalid values"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "prod":
                if len(self.scrsplit()) == 2:
                    try:
                        lv1 = self.scrfullsplit()[1]
                        lv2 = []
                        for i in lv1:
                            lv2.append(float(i))

                        def ctscr_multiply(a, b):
                            try:
                                return float(a) * float(b)
                            except ValueError | TypeError:
                                return "Atleast 1 argument is not a number"

                        return reduce(ctscr_multiply, lv2)
                    except TypeError:
                        return "invalid values"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "subtract":
                if len(self.scrsplit()) == 2:
                    try:
                        lv1 = self.scrfullsplit()[1]
                        lv2 = []
                        for i in lv1:
                            lv2.append(float(i))

                        def ctscr_subtract(a, b):
                            try:
                                return float(a) - float(b)
                            except ValueError | TypeError:
                                return "Atleast 1 argument is not a number"

                        return reduce(ctscr_subtract, lv2)
                    except TypeError:
                        return "invalid values"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "quotient":
                if len(self.scrsplit()) == 2:
                    try:
                        lv1 = self.scrfullsplit()[1]
                        lv2 = []
                        for i in lv1:
                            lv2.append(float(i))

                        def ctscr_divide(a, b):
                            try:
                                return float(a) / float(b)
                            except ValueError | TypeError:
                                return "Atleast 1 argument is not a number"

                        return reduce(ctscr_divide, lv2)
                    except TypeError:
                        return "invalid values"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "timer":
                if len(self.scrsplit()) == 2 or len(self.scrsplit()) == 3:
                    if len(self.scrsplit()) == 2 and len(self.scrfullsplit()[1]) == 1:
                        print("Began a timer of %s seconds" % self.scrsplit()[1])
                        time.sleep(float(self.scrsplit()[1]))
                        if len(self.scrsplit()) == 3:
                            return self.scrsplit()[2]
                        else:
                            return "Time's up!"
                    elif len(self.scrfullsplit()[1]) == 1 and len(self.scrfullsplit()[2]) == 1:
                        print("Began a timer of %s seconds" % self.scrsplit()[1])
                        time.sleep(int(self.scrsplit()[1]))
                        if len(self.scrsplit()) == 3:
                            return self.scrsplit()[2]
                        else:
                            return "Time's up!"
                    else:
                        return "argument 1 and 2 only take 1 subargument"
                else:
                    return "only takes 2 arguments"
            elif self.scrsplit()[0].lower() == "round":
                if len(self.scrsplit()) == 2:
                    if len(self.scrfullsplit()[1]) == 1:
                        try:
                            return round(float(self.scrsplit()[1]))
                        except ValueError | TypeError:
                            return "invalid values"
                    else:
                        return "argument 1 only takes 1 subargument"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "input":
                if len(self.scrsplit()) == 3:
                    if len(self.scrfullsplit()[1]) == 1 and len(self.scrfullsplit()[2]) == 1:
                        lv1 = input(self.scrsplit()[1])
                        if self.scrsplit()[2].lower() == "py_exec":
                            exec(compile(lv1, "CTScript.py", "exec"))
                        elif self.scrsplit()[2].lower() == "echo":
                            return lv1
                        elif self.scrsplit()[2].lower() == "none":
                            pass
                        elif self.scrsplit()[2].lower() == "length":
                            return len(lv1)
                        elif self.scrsplit()[2].lower() == "cts_exec":
                            lv2 = CTScr(lv1, database=self.database)
                            lv2.exec()
                            self.database = lv2.database
                        else:
                            return "Invalid mode"
                    else:
                        return "arguments 1 and 2 only take 1 subargument"
                else:
                    return "only takes 2 arguments"
            elif self.scrsplit()[0].lower() == "cts_terminal":
                if len(self.scrsplit()) == 2:
                    if len(self.scrfullsplit()[1]) == 1:
                        try:
                            lv1 = int(self.scrsplit()[1])
                            lv2 = 1
                            lv3 = CTScr("")
                            lv3.database = self.database
                            lv3.options = self.options
                            lv5 = []
                            while lv1 >= lv2:
                                lv4 = input("Line %s/%s: " % (lv2, lv1))
                                lv2 += 1
                                lv3.script = lv4
                                lv5.append(lv3.exec())
                            self.database = lv3.database
                            self.options = lv3.options
                            return lv5
                        except ValueError:
                            return "invalid line length"
                    else:
                        return "argument 1 only takes 1 subargument"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "exit":
                if len(self.scrsplit()) == 1:
                    exit()
                else:
                    return "only takes 0 arguments"
            elif self.scrsplit()[0].lower() == "db_add":
                if len(self.scrsplit()) == 3:
                    if len(self.scrfullsplit()[1]) == 1 and len(self.scrfullsplit()[2]) == 1:
                        self.dbadd(self.scrsplit()[1], self.scrsplit()[2])
                    else:
                        return "arguments 1 and 2 only take 1 subargument"
                else:
                    return "only takes 2 arguments"
            elif self.scrsplit()[0].lower() == "db_del":
                if len(self.scrsplit()) == 2:
                    if len(self.scrfullsplit()[1]) == 1:
                        self.dbdel(self.scrsplit()[1])
                    else:
                        return "argument 1 only takes 1 subargument"
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "db_get":
                if len(self.scrsplit()) == 2:
                    if len(self.scrfullsplit()[1]) == 1:
                        try:
                            return self.dbget(self.scrsplit()[1])
                        except KeyError:
                            return f"invalid key: {self.scrsplit()[1]}"
                    else:
                        return "argument 1 only takes 1 subargument"
                elif len(self.scrsplit()) == 1:
                    return self.database
                else:
                    return "only takes 1 or 0 arguments"
            elif self.scrsplit()[0].lower() == "type":
                if len(self.scrsplit()) == 2:
                    args_n_types_d = dict()
                    for i in self.scrfullsplit()[1]:
                        if i.startswith("$"):
                            if type(self.dbget(i[1:], nokey=True)) != str:
                                i = str(self.dbget(i[1:], nokey=True))
                            else:
                                i = "'" + self.dbget(i[1:], nokey=True) + "'"
                        args_n_types_d[i] = str(type(eval(i)))[8:-2]
                    args_n_types_s = str(args_n_types_d)[1:-1]
                    return args_n_types_s
                else:
                    return "only takes 1 argument"
            elif self.scrsplit()[0].lower() == "settypestatic":
                if len(self.scrsplit()) == 3:
                    if len(self.scrfullsplit()[1]) == 1 and len(self.scrfullsplit()[2]) == 1:
                        if self.scrsplit()[1] == "int":
                            if self.scrsplit()[2].startswith("$"):
                                return int(self.dbget(self.scrsplit()[2][1:], nokey=True))
                            else:
                                return int(self.scrsplit()[2])
                        elif self.scrsplit()[1] == "float":
                            if self.scrsplit()[2].startswith("$"):
                                return float(self.dbget(self.scrsplit()[2][1:], nokey=True))
                            else:
                                return float(self.scrsplit()[2])
                        else:
                            return "invalid datatype"
                    else:
                        print("arguments only take 1 subargument")
                else:
                    print("only takes 2 arguments")
            elif self.scrsplit()[0].lower() == "settypedb":
                if len(self.scrsplit()) == 3:
                    if len(self.scrfullsplit()[1]) == 1 and len(self.scrfullsplit()[2]) == 1:
                        if self.scrsplit()[1] == "int":
                            self.database[self.scrsplit()[2]] = int(self.dbget(self.scrsplit()[2], nokey=True))
                        elif self.scrsplit()[1] == "float":
                            self.database[self.scrsplit()[2]] = float(self.dbget(self.scrsplit()[2], nokey=True))
                        elif self.scrsplit()[1] == "str":
                            self.database[self.scrsplit()[2]] = str(self.dbget(self.scrsplit()[2], nokey=True))
                        else:
                            return "invalid datatype"
                    else:
                        return "arguments only take 1 subargument"
                else:
                    return "only takes 2 arguments"

            elif len(self.script) == 0:
                pass
            elif "," in self.keyword():
                return "keywords don't have subarguments"
            elif len(self.scrfullsplit()) == 0:
                return "missing keyword"
            else:
                return "invalid keyword"
            if self.options["clear"]:
                self.database = {}
            if self.options["log"]:
                self.log.append(self.script)
        except Exception as exc:
            raise CTScr.ExecError(exc)
