# Gunhead
## Description
During Pandora's training, the Gunhead AI combat robot had been tampered with and was now malfunctioning, causing it to become uncontrollable. With the situation escalating rapidly, Pandora used her hacking skills to infiltrate the managing system of Gunhead and urgently needs to take it down.

### Difficulty: very easy
---
Visiting the website we see a lot of text, and the only interactable piece seems to be a pull-up console:

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Gunhead/Screencaps/Pasted%20image%2020230325103826.png)

Our options for commands is extremely limited. Perhaps the provided source code can give us  more insight?
In ReconModel.php, we see how the program handles this ping command:
```
$ cat ReconModel.php 
<?php
#[AllowDynamicProperties]

class ReconModel
{   
    public function __construct($ip)
    {
        $this->ip = $ip;
    }

    public function getOutput()
    {
        # Do I need to sanitize user input before passing it to shell_exec?
        return shell_exec('ping -c 3 '.$this->ip);
    }
}
```
We have a commented note pointing out the lack of sanitization within the shell_exec. We should be able to use this /ping command to execute multiple shell commands when we include a break;
Testing with id:
```
/ping 8.8.8.8; id
```
![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Gunhead/Screencaps/Pasted%20image%2020230325104911.png)

We see the 2nd shows our id. This command injection is successful. We will probe the current directory, and since there's no harm, take a guess that flag.txt is in our current directory:

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Gunhead/Screencaps/Pasted%20image%2020230325105242.png)

We didn't hit it this time, but using this command scheme we can keep using `ls` to poke around for the flag. Or we can try `find`.

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Gunhead/Screencaps/Pasted%20image%2020230325105457.png)

Now we find it in probably the next most likely location, the base directory.

![iamge](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Gunhead/Screencaps/Pasted%20image%2020230325105542.png)

`HTB{4lw4y5_54n1t1z3_u53r_1nput!!!}`
