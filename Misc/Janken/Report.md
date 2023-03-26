# Janken
## Description
As you approach an ancient tomb, you're met with a wise guru who guards its entrance. In order to proceed, he challenges you to a game of Janken, a variation of rock paper scissors with a unique twist. But there's a catch: you must win 100 rounds in a row to pass. Fail to do so, and you'll be denied entry.

### Difficulty: easy
---
In this challenge we are given a compiled binary called janken. Upon running it, we can view the rules for the game:
```
$ ./janken 


                                                                                                                    
                         ▛▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▜                                                                         
                         ▌   じ ゃ ん 拳  ▐                                                                         
                         ▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▟                                                                         
                                                                                                                    
                                                                                                                    
1. ℙ ∟ ₳ Ұ                                                                                                          
2. ℜ ℧ ∟ Ӗ ⅀                                                                                                        
                                                                                                                    
>> 2                                                                                                                
                                                                                                                    
▛▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▜                                          
▚  [*] Rock     is called "Guu"   (ぐう).                                ▞                                          
▞  [*] Scissors is called "Choki" (ちょき).                              ▚                                          
▚  [*] Paper    is called "Paa"   (ぱあ).                                ▞                                          
▞                                                                        ▚                                          
▚  1. Rock > scissors, scissors > paper, paper > rock.                   ▞                                          
▞  2. You have to win [100] times in a row in order to get the prize. 🏆 ▚                                          
▙▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▟ 
```

To win, we must win 100 games of rock paper scissors in a row. If left up to chance, this is not realistic. There must be a way to force a win. I recall seeing this same problem presented in another CTF competition, picoCTF 2022. (RPS in Binary Exploitation category). In that challenge, the win condition was only checking if the player's input contained the winning string. So, by playing all 3 options at once you were guaranteed to win. We can try that here as well:
```
>> 1                                                                                                                
[!] Let the game begin! 🎉                                                                                          
                                                                                                                    
                                                                                                                    
[*] Round [1]:                                                                                                      
                                                                                                                    
Choose:                                                                                                             
                                                                                                                    
Rock 👊                                                                                                             
Scissors ✂                                                                                                          
Paper 📜                                                                                                            
                                                                                                                    
>> rock,paper,scissors                                                                                              
                                                                                                                    
[!] Guru's choice: scissors                                                                                         
[!] Your  choice: rock,paper,scissors                                                                               
                                                                                                                    
[+] You won this round! Congrats!                                                                                   
                                                                                                                    
[*] Round [2]: 
```
The syntax was a little picky, but we see a guaranteed winning combination with `rock,paper,scissors`.

Writing out `rock,paper,scissors` 100 times in a row is boring and tedious, so I channeled my inner programmer and spent twice as long making a script that will do it for me:
```
from pwn import *

p = remote('178.62.64.13', 31174)
win = 'rock,paper,scissors'

#Start game 1 and chain
p.sendline('1')

#Looping sendline is too fast, so I wait for interactive marker >>
for i in range(100):
    p.sendlineafter('>>',win)

response = p.recvallS()
print(response)
```

Now to acquire the flag in extra speedy fashion:
```
$ python RPS.py
[+] Opening connection to 178.62.64.13 on port 31174: Done
[+] Receiving all data: Done (223B)
[*] Closed connection to 178.62.64.13 port 31174
 
[!] Guru's choice: rock                                                                                             
[!] Your  choice: rock,paper,scissors                                                                               
                                                                                                                    
[+] You won this round! Congrats!                                                                                   
[+] You are worthy! Here is your prize: HTB{r0ck_p4p3R_5tr5tr_l0g1c_buG}
```
`HTB{r0ck_p4p3R_5tr5tr_l0g1c_buG}`