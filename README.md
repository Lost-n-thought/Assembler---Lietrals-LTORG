Run pass1



```mermaid

 stateDiagram
Asm_file -->Assembly
mot_file --> MOT
Assembly --> each_line 
MOT --> each_line
each_line --> Symbol
MOT --> LC
 LC  -->each_line
Symbol --> LC

```