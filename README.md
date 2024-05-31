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

Each line in the file represents a single Function Call with the first column being the address, the second being the opcode, and the rest of the columns being the function arguments.

***Example Python File for Above File:***
```
Opcodes = {
  0x10: "ADD_TWO_NUMBERS",
  0x20: 'PRINT_5_TIMES",
  0x30: "CUBE"
}

#Parameters for readdata: directory(string), read_out_final_memory(bool)(defaults to False), seperator(string)(defaults to ":")

FunctionOpcoder.readdata("/path/to/file")

#Parameters for run: read_out_commands(bool)(defaults to False)

FunctionOpcoder.run()

```





