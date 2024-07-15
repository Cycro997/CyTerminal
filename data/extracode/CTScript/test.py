#CTScript test script
import CTScript as cts

a = cts.CTScr("cts_terminal;3", database={"i": "3"}, options={"log": True})
print(cts.CTScr(a))
print(repr(a))
print(a.scrsplit())
print(a.scrfullsplit())
print(a.exec())
