# FunctionOpcoder
<h3>A Simple Program for Representing Functions as Opcodes in Python</h3>

***What is it and Why?***

FunctionOpcoder is a small python program that works by taking a list of opcodes and arguments stored in a text file and using a specified dictionary inside the python file, represents those opcodes as functions. Primarly intended for small file size representing of large amounts of functions thats easy to edit and share.

***Example File:***
```
0x1:0x6:10:20
0x2:0x7
0x3:0x8:6
0x4:R0x1
```

Each line in the file represents a single Function Call with the first column containing the addresses for their lines function call which is used to tell which order to call the functions in, the second being the opcodes which represent functions located in the main python program, and the rest of the columns being the function arguments, each of thease sections are seperated by a ":" but can be changed in the main python file. The last line at address 0x4 is a special case as its a repeat opcode meaning it copys the data contained in a speicifed address, in this case it copys from 0x1 and the data at that address is 0x6:10:20 so the reader reads the line as 0x4:0x6:10:20.

Note: Addresses can be represented as a decimal or hexadecimal value and opcodes can be represented as a string, decimal, or hexadecimal value as indicated by the main python file.

***Example Python File for Above File:***
```
FunctionOpcoder.Opcodes = {
  0x10: "ADD_TWO_NUMBERS",
  0x20: "PRINT_5_TIMES",
  0x30: "CUBE"
}

#Parameters for readdata: directory (string) (required), read_out_final_memory (bool) (defaults to False), seperator (string) (defaults to ":")

FunctionOpcoder.readdata("/path/to/file")

#Parameters for run: read_out_commands(bool)(defaults to False)

FunctionOpcoder.run()

```

First a dictionary called Opcodes stores each opcodes corresponding function name. Next readdata is called which reads the data from the specified directory, in this case from the example file. And then run() is called which actually runs the function calls read from the file. 


