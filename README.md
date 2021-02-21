# LynxCompiler-
  A Program Written in Python to Covert LynxVM Code into Fast effeicent Assembly Code 
  
  
  Progress x86 : 
  
    |------------10%------------|
  
  Progress armhf : 
  
    |------------8%------------|
  
  Supported Architectures and Operating Systems:
 
    Linux: ARMHF
    Linux: x86
    
   Requirments:
    
     Armhf: GNU Assembler 2.3 , GNU ld 2.3
     
     x86: nasm 2.1 , GNU ld 2.3
     
   Program Usage:
   
    lxc [Programname].lyvm [output].asm [Architecture]
    
    ___________________________________________________
    
    Example #1: lxc main.lyvm main.asm x86
                nasm -f elf64 main.asm -o main.o
                ld main.o -o main.sh
    ___________________________________________________
    
    Example #2: lxc main.lyvm main.asm armhf
                as main.asm -o main.o 
                ld main.o -o main.sh 
               
    
   Future: 
   
    Windows: x86
  
  Limitations:
  
    Varibles:
      Varible names can only be 4 characters long 
      
    
  Programming Instructions:
  
    print                   # This will print Plain Text or Numbers not a Varible | Usage [ print Hello World ] 
    
    printv                  # This will print Varibles not Plain Text or Numbers | Usage [ printv Var1 ] 
    
    printi                  # This will print User Input | Usage [ printi Var1 ] 
    
    setcolor                # This will set the text's color | Usage [ setcolor red ] 
    
    jump                    # This will jump to a program section | Usage [ jump TESTSECTION: ]  
    
    var                     # This will set a value to a Varible | Usage [ var Var1 HelloWorld ]  
    
    getint                  # This will Get User Input | Usage [ getint Var1 ]  
    
    exit                    # This will close the Program
    
    
  
