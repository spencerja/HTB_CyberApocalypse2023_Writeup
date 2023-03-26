# Drobots
## Description
Pandora's latest mission as part of her reconnaissance training is to infiltrate the Drobots firm that was suspected of engaging in illegal activities. Can you help pandora with this task?

### Difficulty: very easy
---
Visiting the site gives us a generic login page. Trying the classic admin:admin and admin:password failed, so it's time to take a look at the source code supplied. Exploring database.py we see the following configuration:
```
def login(username, password):
    # We should update our code base and use techniques like parameterization to avoid SQL Injection
    user = query_db(f'SELECT password FROM users WHERE username = "{username}" AND password = "{password}" ', one=True)
```
The comment is a pretty plain hint that this SQL query is not well sanitized, and allows for very basic SQL injection.
For our user submission, we will escape the username query with ", then bypass a password check with "OR 1=1 -- ". The end result is we will login if the database can find a user called "" or if the value 1 is equal to 1. Since the latter is always true, we should login. Note that the space after comment lines -- must be present, or else this will be interpreted as minus.

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Drobots/Screencaps/Pasted%20image%2020230325103055.png)

The password will never be checked, so this can be whatever.
Just like that, we are in. And the flag is first up on the table.

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Drobots/Screencaps/Pasted%20image%2020230325103409.png)

`HTB{p4r4m3t3r1z4t10n_1s_1mp0rt4nt!!!}`
