# FunctionOpcoder
<h3>A Simple Program for Representing Functions as Opcodes in Python</h3>

***What is it and Why?***
FunctionOpcoder is a small program I wrote for python3 that works by taking a list of opcodes and arguments
and using a specified dictionary, represents those opcodes as functions.
Primarly intended for small file size representing for programs with large amounts of functions.

Format:

Example File:
```
0x1:0x6:10:20
0x2:0x7
0x3:0x8-6
0x4:R0x1
```

Each line in the file represents a single Function Call with the first column being the address, the second being the opcode, and the rest of the columns being the Function

Example Python File for Above File:
```
Opcodes = {
  0x10: "ADD_TWO_NUMBERS",
  0x20: 'PRINT_5_TIMES",
  0x30: "CUBE"
}

FunctionOpcoder.readdata("/path/to/file")

FunctionOpcoder.run()

```





