# Persistence
## Description
Thousands of years ago, sending a GET request to **/flag** would grant immense power and wisdom. Now it's broken and usually returns random data, but keep trying, and you might get lucky... Legends say it works once every 1000 tries.

### Difficulty: very easy
---
The objective for this problem is very straightforward: send a /GET request to IP:PORT/flag and you will receive the flag after ~1000 attempts.  1000 attempts is a rather high number to reach manually, so creating a loop for curl is the way to go:
```
#!/bin/bash
for i in {1..1000}
do
        curl -s 165.232.100.46:31980/flag 
done
```
-s flag makes the curl request silent, otherwise we will get transmission informations on every curl attempt. This loop only runs for 1000 attempts, but if you're watching the program you can have it set to run indefinitely and just manually close it when the flag is seen.
Running the script:
```
$ chmod +x loop.sh
$ ./loop.sh | grep "HTB"
```
grep allows us to filter any uninteresting output and only shows our flag.
Eventually, we see the results pop out at us.
```
HTB{y0u_h4v3_p0w3rfuL_sCr1pt1ng_ab1lit13S!}jW&z3]X8CLb5Q7kR
```
The flag information includes only HTB and the content in brackets. A cleaner grep would have extracted only the flag.
Overall, it seems output of the flag is based on a ~0.1% chance. On average, you will get the flag within 1000 requests but not always.
`HTB{y0u_h4v3_p0w3rfuL_sCr1pt1ng_ab1lit13S!}`