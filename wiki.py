import wikipedia
wikipedia.set_lang("en")
instr = input("What would you like to know about? ")
print(wikipedia.summary(instr,sentences=1))
