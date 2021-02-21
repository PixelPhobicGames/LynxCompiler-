import os, sys, time 

# This is 100% Not the Best code ive ever written 
# But .... It works

# All these classes just make the varibles static 
# 


class srcfile:
    file = 0 # This is the output file 
    readfile = 0 # The read file is the file thats read the convertd in NASM x86 assembly
    
class linecounter:
    count = 1;
    
class Program:
    randomvarnme = 0 # This is a way to make random varible names to store string. You just add 1 to it then it results in string names like r0 and r1  etc 
    arch = 0

    
def DisplayLogo():
     print("  .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.")
     print(".,,.                                                                                             ll")
     print("ll    .,,.                                                                                       ll")
     print("ll   ,l.ll                                                                                       ll")
     print("ll   ll ll                                                                                       ll")
     print("ll   ll ll                                                                                       ll")
     print("ll   ll ll                                                              ..                       ll")
     print("ll   ll ll                 ,l,.                                       .,kl                       ll")
     print("ll   ll ll                 ,l,,,.                                   .,,,l,                       ll")
     print("ll   ll ll                  .,,,,,.                               .,,,,,.                        ll")
     print("ll   ll ll                    .,,,,,.                           .,,,,,.                          ll")
     print("ll   ll ll                      .,,,,,.                       .,,,,,.                            ll")
     print("ll   ll ll                        .,,,,,.                   .,,,,,.          .,,,,,,,,,,,,,,,.   ll")
     print("ll   ll ll                          .,,,,,.               .,,,,,.          .,,lkkkkkkkkkkkkkkl.  ll")
     print("ll   ll ll                            .,,,,,.           .,,,,,.            ll,l,,,,,,,,,,,,,,.   ll")
     print("ll   ll ll                              .,,,,,.       .,,,,,.              llll                  ll")
     print("ll   ll ll                                .,,,,,.   .,,,,,.                llll                  ll")
     print("ll   ll ll                                  .,,,,,,,,,,,.                  llll                  ll")
     print("ll   ll ll                                    .lkkllkl.                    llll                  ll")
     print("ll   ll ll                                   .,,lklll,,.                   llll                  ll")
     print("ll   ll ll                                 .,,,,,,..,,,,,.                 llll                  ll")
     print("ll   ll ll                               .,,,,,.     .,,,,,.               ll,l,,,,,,,,,,,,,,.   ll")
     print("ll   ll ll                             .,,,,,.         .,,,,,.             .,,lkkkkkkkkkkkkkkl.  ll")
     print("ll   ll ll                           .,,,,,.             .,,,,,.             .,,,,,,,,,,,,,,,.   ll")
     print("ll   ll ll                         .,,,,,.                 .,,,,,.                               ll")
     print("ll   ll ll                       .,,,,,.                     .,,,,,.                             ll")
     print("ll   ll ll                      .ll,,.                         .,,ll.                            ll")
     print("ll   ll ll                                                                                       ll")
     print("ll   ll lk,.                                                                                     ll")
     print("ll   ll ,lll,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ll.                                                  ll")
     print("ll   ,l,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                                                   ll")
     print("ll    .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                                                     ll")
     print("ll                                                                                               ll")
     print(".,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.")
        
        
        
#The way this software works it that it interperates each section seperatly starting with the data section and ending with the Text section.

    
def InterperateBssSection(instruction):
    if (Program.arch == "x86"):
        if (instruction[0:3] == "var"):
            srcfile.file.write("    " + instruction[4:8]+"bss" + " " + "resb" + " " + "100\n")
            print("Compiling Instruction * var * ")
        
    
def InterperateStrSection(instruction):
    if (Program.arch == "x86"):

        if (instruction[0:3] == "var"):
            print("Compiling Instruction * var * ")
            quotechar = ' " '
            srcfile.file.write("    " + instruction[4:8] + " " + "db" + " " +  quotechar +instruction[9:99].replace("\n","") + quotechar + ", 0xa\n")
            srcfile.file.write("    " + instruction[4:8]+ "lent" + ' '+ "equ" + " "+"$" + " "+ "-" +  " "+ instruction[4:8] + "\n")
            
        if (instruction[0:3] == "int"):
            print("Compiling Instruction * int * ")
            srcfile.file.write("    " + instruction[4:8] + " " + "db" + " " +  instruction[9:99].replace("\n","") + "\n")
            #srcfile.file.write("    " + instruction[4:8]+ "lent" + ' '+ "equ" + " "+"$" + " "+ "-" +  " "+ instruction[4:8] + "\n")
        if (instruction[0:6] == "printv"):
            return 

        if (instruction[0:5] == "print"):
            quotechar = ' " '
            srcfile.file.write("    " + "y" + str(Program.randomvarnme) + " " + "db" + " " +  quotechar +instruction[6:99].replace("\n","") + quotechar + ", 0xa\n")
            srcfile.file.write("    " + "y"+str(Program.randomvarnme)+ "lent" + ' '+ "equ" + " "+"$" + " "+ "-" +  " "+ "y"+str(Program.randomvarnme) + "\n")
            print("Compiling Instruction * print * ")
            Program.randomvarnme += 1

    if (Program.arch == "armhf"):

        if (instruction[0:3] == "var"):
            print("Compiling Instruction * var * ")
            quotechar = ' " '
            srcfile.file.write("    " + instruction[4:8] + ":" +" "+ ".ascii" + " " +  quotechar +instruction[9:99].replace("\n","") + quotechar + "\n")
            srcfile.file.write("    " + instruction[4:8] +"lent"+ " " + "=" +" " + ".-"+instruction[4:8] + "\n")
        if (instruction[0:6] == "printv"):
            return 

        if (instruction[0:5] == "print"):
            quotechar = ' " '
            srcfile.file.write("    " + "y" + str(Program.randomvarnme) + ":" +" "+ ".ascii" + " " +  quotechar +instruction[6:99].replace("\n","") + "\134\156"  + quotechar + "\n")
            srcfile.file.write("    " + "y" + str(Program.randomvarnme) +"lent"+ " " + "=" +" " + ".-"+"y" + str(Program.randomvarnme) + "\n")
            print("Compiling Instruction * print * ")
            Program.randomvarnme += 1
        
def InterperateTxtSection(instruction):
    if (Program.arch == "x86"):
        if (instruction[0:3] == "asm"):
            print("Compiling Instruction * asm * ")
            srcfile.file.write("    " + instruction[4:99])
        if (instruction[0:8] == "setcolor"):
            print("Compiling Instruction * setcolor * ")
            if (instruction[9:12] == "red"):
                srcfile.file.write("    mov edx," + "9"+'\n')
                srcfile.file.write("    mov ecx," + "color_red"+'\n')
                srcfile.file.write("    mov ebx, 1" + "\n")
                srcfile.file.write("    mov eax, 4" + "\n")
                srcfile.file.write("    int 0x80" + "\n")
            if (instruction[9:13] == "blue"):
                srcfile.file.write("    mov edx," + "9"+'\n')
                srcfile.file.write("    mov ecx," + "color_blue"+'\n')
                srcfile.file.write("    mov ebx, 1" + "\n")
                srcfile.file.write("    mov eax, 4" + "\n")
                srcfile.file.write("    int 0x80" + "\n")
            if (instruction[9:14] == "green"):
                srcfile.file.write("    mov edx," + "9"+'\n')
                srcfile.file.write("    mov ecx," + "color_green"+'\n')
                srcfile.file.write("    mov ebx, 1" + "\n")
                srcfile.file.write("    mov eax, 4" + "\n")
                srcfile.file.write("    int 0x80" + "\n")
            if (instruction[9:14] == "brown"):
                srcfile.file.write("    mov edx," + "9"+'\n')
                srcfile.file.write("    mov ecx," + "color_brown"+'\n')
                srcfile.file.write("    mov ebx, 1" + "\n")
                srcfile.file.write("    mov eax, 4" + "\n")
                srcfile.file.write("    int 0x80" + "\n")
            if (instruction[9:15] == "purple"):
                srcfile.file.write("    mov edx," + "9"+'\n')
                srcfile.file.write("    mov ecx," + "color_purple"+'\n')
                srcfile.file.write("    mov ebx, 1" + "\n")
                srcfile.file.write("    mov eax, 4" + "\n")
                srcfile.file.write("    int 0x80" + "\n")
                
        if (instruction[0:6] == "printv"):
            print("Compiling Instruction * printv * ")
            srcfile.file.write("    mov edx," + instruction[7:11]+"lent"+'\n')
            srcfile.file.write("    mov ecx," + instruction[7:11]+'\n')
            srcfile.file.write("    mov ebx, 1" + "\n")
            srcfile.file.write("    mov eax, 4" + "\n")
            srcfile.file.write("    int 0x80" + "\n")
            return
        if (instruction[0:6] == "printi"):
            print("Compiling Instruction * printi * ")
            srcfile.file.write("    mov edx," + instruction[7:11]+"lent"+'\n')
            srcfile.file.write("    mov ecx," + instruction[7:11]+'bss\n')
            srcfile.file.write("    mov ebx, 1" + "\n")
            srcfile.file.write("    mov eax, 4" + "\n")
            srcfile.file.write("    int 0x80" + "\n")
            return
        if (instruction[0:5] == "print"):
            print("Compiling Instruction * print * ")
            srcfile.file.write("    mov edx," + "y"+str(Program.randomvarnme)+"lent"+'\n')
            srcfile.file.write("    mov ecx," + "y"+str(Program.randomvarnme)+'\n')
            srcfile.file.write("    mov ebx, 1" + "\n")
            srcfile.file.write("    mov eax, 4" + "\n")
            srcfile.file.write("    int 0x80" + "\n")
            Program.randomvarnme += 1
            return
        if (instruction[0:6] == "getint"):
            print("Compiling Instruction * input * ")
            srcfile.file.write("    mov eax, 3\n")
            srcfile.file.write("    mov ebx, 2\n")
            srcfile.file.write("    mov ecx, " +instruction[7:11]+"bss\n")
            srcfile.file.write("    mov edx, 100" + "\n")
            srcfile.file.write("    int 0x80" + "\n")
        if (instruction[0:4] == "exit"):
            print("Compiling Instruction * exit * ")
            srcfile.file.write("    mov eax, 1" + "\n")
            srcfile.file.write("    mov ebx, 0" + "\n")
            srcfile.file.write("    int 0x80" + "\n")
        if (instruction[0:1] == ":"):
            print("Creating New Jump Point")
            jmpname = instruction[1:99]
            srcfile.file.write("_"+jmpname.replace("\n","")+":\n")
            
        if (instruction[0:4] == "jump"):
            print("Compiling Instruction * jump * ")
            srcfile.file.write("    jmp" + " " +"_"+instruction[5:99] +"\n")
        if (instruction[0:4] == "loop"):
            print("Compiling Instruction * loop * ")
            srcfile.file.write("    jmp _start" + "\n")

    if (Program.arch == "armhf"):

        if (instruction[0:3] == "asm"):
            print("Compiling Instruction * asm * ")
            srcfile.file.write("    " + instruction[4:99])
        if (instruction[0:8] == "setcolor"):
            print("Compiling Instruction * setcolor * ")
            if (instruction[9:12] == "red"):
                srcfile.file.write("    MOV R7, #4" + '\n')
                srcfile.file.write("    MOV R0, #1" + '\n')
                srcfile.file.write("    MOV R2, #10" + '\n')
                srcfile.file.write("    LDR R1, =color_red" + '\n')
                srcfile.file.write("    SWI 0" + "\n")
            if (instruction[9:13] == "blue"):
                srcfile.file.write("    MOV R7, #4" + '\n')
                srcfile.file.write("    MOV R0, #1" + '\n')
                srcfile.file.write("    MOV R2, #10" + '\n')
                srcfile.file.write("    LDR R1, =color_blue" + '\n')
                srcfile.file.write("    SWI 0" + "\n")
            if (instruction[9:14] == "green"):
                srcfile.file.write("    MOV R7, #4" + '\n')
                srcfile.file.write("    MOV R0, #1" + '\n')
                srcfile.file.write("    MOV R2, #10" + '\n')
                srcfile.file.write("    LDR R1, =color_green" + '\n')
                srcfile.file.write("    SWI 0" + "\n")
            if (instruction[9:14] == "brown"):
                srcfile.file.write("    MOV R7, #4" + '\n')
                srcfile.file.write("    MOV R0, #1" + '\n')
                srcfile.file.write("    MOV R2, #10" + '\n')
                srcfile.file.write("    LDR R1, =color_brown" + '\n')
                srcfile.file.write("    SWI 0" + "\n")
            if (instruction[9:15] == "purple"):
                srcfile.file.write("    MOV R7, #4" + '\n')
                srcfile.file.write("    MOV R0, #1" + '\n')
                srcfile.file.write("    MOV R2, #10" + '\n')
                srcfile.file.write("    LDR R1, =color_purple" + '\n')
                srcfile.file.write("    SWI 0" + "\n")
        if (instruction[0:6] == "printv"):
            print("Compiling Instruction * printv * ")
            srcfile.file.write("    MOV R7, #4" + '\n')
            srcfile.file.write("    MOV R0, #1" + '\n')
            srcfile.file.write("    LDR R2, " + "="+ instruction[7:11]+"lent" + '\n')
            srcfile.file.write("    LDR R1, " + "="+ instruction[7:11] + '\n')
            srcfile.file.write("    SWI 0" + "\n")
            return

        if (instruction[0:6] == "printi"):
            print("Compiling Instruction * printi * ")
            srcfile.file.write("    MOV R7, #4" + '\n')
            srcfile.file.write("    MOV R0, #1" + '\n')
            srcfile.file.write("    LDR R2, " + "="+ instruction[7:11]+"lent" + '\n')
            srcfile.file.write("    LDR R1, " + "="+ instruction[7:11] + '\n')
            srcfile.file.write("    SWI 0" + "\n")
            return

        if (instruction[0:5] == "print"):
            print("Compiling Instruction * print * ")
            srcfile.file.write("    MOV R7, #4" + '\n')
            srcfile.file.write("    MOV R0, #1" + '\n')
            srcfile.file.write("    LDR R2, " "=" + "y"+str(Program.randomvarnme) +"lent"+ '\n')
            srcfile.file.write("    LDR R1, " + "="+ "y"+str(Program.randomvarnme) + '\n')
            srcfile.file.write("    SWI 0" + "\n")
            Program.randomvarnme += 1
            return
        if (instruction[0:6] == "getint"):
            print("Compiling Instruction * input * ")
            srcfile.file.write("    MOV R7, #3" + '\n')
            srcfile.file.write("    MOV R0, #0" + '\n')
            srcfile.file.write("    MOV R2, #99" + '\n')
            srcfile.file.write("    LDR R1, " + "="+ instruction[7:11] + '\n')
            srcfile.file.write("    SWI 0" + "\n")

        if (instruction[0:4] == "exit"):
            print("Compiling Instruction * exit * ")
            srcfile.file.write("    MOV R7, #1" + '\n')
            srcfile.file.write("    SWI 0" + "\n")
        if (instruction[0:1] == ":"):
            print("Creating New Jump Point")
            jmpname = instruction[1:99]
            srcfile.file.write("_"+jmpname.replace("\n","")+":\n")
            
        if (instruction[0:4] == "jump"):
            print("Compiling Instruction * jump * ")
            srcfile.file.write("    B" + " " +"_"+instruction[5:99] +"\n")
        if (instruction[0:4] == "loop"):
            print("Compiling Instruction * loop * ")
            srcfile.file.write("    jmp _start" + "\n")
def StartCompilation():
    if (Program.arch == "x86"):
        srcfile.file.write(" ; Source Generated By LXC - Compiler \n")
    if (Program.arch == "armhf"):
        srcfile.file.write("/* Source Generated By LXC - Compiler */\n")

    if (Program.arch == "x86"):
        srcfile.file.write("section .text \n")
        srcfile.file.write("    global _start \n")
    if (Program.arch == "armhf"):
        srcfile.file.write(".text \n")
        srcfile.file.write("    .global _start \n")

    Lines = srcfile.readfile.readlines()
    if (Program.arch == "x86"):
        srcfile.file.write("section .data \n")
        srcfile.file.write("    color_red db  1Bh,'[31;40m' , 0 \n")
        srcfile.file.write("    color_green db  1Bh,'[32;40m' , 0 \n")
        srcfile.file.write("    color_blue db  1Bh,'[34;40m' , 0 \n")
        srcfile.file.write("    color_brown db  1Bh,'[33;40m' , 0 \n")
        srcfile.file.write("    color_purple db  1Bh,'[35;40m' , 0 \n")
    if (Program.arch == "armhf"):
        srcfile.file.write(".data \n")
        srcfile.file.write('    color_red: .ascii  "' + '\134' + '033[1;31;40m"' + '\n')
        srcfile.file.write('    color_green: .ascii  "' + '\134' + '033[1;32;40m"' + '\n')
        srcfile.file.write('    color_blue: .ascii  "' + '\134' + '033[1;34;40m"' + '\n')
        srcfile.file.write('    color_brown: .ascii  "' + '\134' + '033[1;30;40m"' + '\n')
        srcfile.file.write('    color_purple: .ascii  "' + '\134' + '033[1;35;40m"' + '\n')
    while (True):

        
        InterperateStrSection(Lines[linecounter.count - 1])
        linecounter.count += 1
        
        if (linecounter.count == len(Lines) + 1):
            print("Progress: 30%")
         
            break
            
    Program.randomvarnme = 0

    if (Program.arch == "x86"):
        srcfile.file.write("section .bss \n")

        linecounter.count = 1
    
        while (True):

            
            InterperateBssSection(Lines[linecounter.count - 1])
            linecounter.count += 1
            
            if (linecounter.count == len(Lines) + 1):
                print("Progress: 60%")
            
                break
    else :
        print("Progress: 60%")

    if (Program.arch == "x86"):
        srcfile.file.write("section .text \n")
    if (Program.arch == "armhf"):
        srcfile.file.write(".text \n")

    linecounter.count = 1
    srcfile.file.write("_start:	\n")

    while (True):
        
        InterperateTxtSection(Lines[linecounter.count - 1])
        linecounter.count += 1
        
        if (linecounter.count == len(Lines) + 1):
            print("Progress: 90%")
            break
    
    

    
def Start():
    os.system("clear")
    print("Software By Liquid")
    if (sys.argv[1] == "--help"):
        print("Usage: lxc [main].lyvm [output].asm [arch]")
        sys.exit()
        
    srcfile.readfile = open(sys.argv[1],"r")
    srcfile.file = open(sys.argv[2],"w")
    Program.arch = sys.argv[3]
    DisplayLogo()
    time.sleep(2)
    print("Starting Compilaton:")
    print("Progress: 0%")
    StartCompilation()
    print("Progress: 100%")
    print("Assembly Successfully generated")
    srcfile.file.close
    
Start()
