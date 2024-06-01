
OP_Codes = {}
memory = {}
def readdata(file_path, print_memory=False, sep=":"):
    global memory
    memory = {}
    try:
        code = open(file_path, "r")
        lines = code.readlines()
    except:
        raise FileExistsError("Invalid File Path: " + str(file_path))
    if "\n" in lines:
        lines.remove("\n")
    for item in lines:
        try:
            #Decimal Addresses
            addr = int(item[0:item.index(sep)])
        except:
            #Hexadecimal Addresses
            addr = int(item[0:item.index(sep)], 16)
        s = item[item.index(sep)+1:len(item)-1].split(sep)
        if "" in s: s.remove("")
        #s -> Total Item
        if s[0][0] == "R":
            #Repeat Handler that repeats the value already specified at a specific address.
            val = s[0][1:]
            if val.startswith("0x"):
                s = memory[int(val, 16)]
            else:
                s = memory[int(val)]
        else:
            for ind, v in enumerate(s):
                if v[0] == "[" and v[len(v)-1] == "]":
                    #Converts to Array Parameter
                    elements = v.strip("[]").split(",")
                    if elements[0].strip().isdigit():
                        s[ind] = [int(element) for element in elements]
                    else:
                        s[ind] = [element.strip(" '\"") for element in elements]
                else:
                    #Converts strings to either intergers, hexadecimal, or strin.g
                    try:
                        if v.startswith("0x"):
                            s[ind] = int(v,16)
                        else:
                            s[ind] = int(v)
                    except:
                        s[ind] = s[ind]
        memory[addr] = s
    print("MEMORY:\n" + str(memory) if print_memory else "")

def run(print_commands=False):
    for n in sorted(memory):
        op = memory[n][0]
        try:
            Function = OP_Codes[op]
        except:
            Function = op
        arguments = tuple(memory[n][1:])
        command = str(Function) + str(arguments)
        if print_commands:
            print(str(n) + ": " + command)
        try:
            exec(("__main__." if __name__!= '__main__' else "") + command)
        except:
            raise ValueError("INVALID OPCODE OR FUNCTION: " + str(op))

if __name__ != '__main__':
    import __main__
