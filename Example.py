import FunctionOpcoder

out = 0
outputs = {}

def ADD_TWO_CUBE(num1,num2):
    global out
    out = num1**3 + num2**3

def append_out(id):
    global outputs
    outputs[id] = out

def print_vars():
    print("RECENT OUT: " + str(out))
    print("OUTPUTS: " + str(outputs))

def print_3(s):
    for i in range(3):
        print(s)
    
def AVERAGE(array):
    global out
    sum = 0
    for i in array:
        sum += i
    out = sum/len(array)

FunctionOpcoder.OP_Codes = {
    0x3: "ADD_TWO_CUBE",
    0x5: "print_vars",
    0x6: "print_3",
    0x7: "AVERAGE",
    0x8: "append_out"
}

FunctionOpcoder.readdata("Data")
FunctionOpcoder.run()






