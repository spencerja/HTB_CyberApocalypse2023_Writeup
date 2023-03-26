# Trapped Source
## Description
Intergalactic Ministry of Spies tested Pandora's movement and intelligence abilities. She found herself locked in a room with no apparent means of escape. Her task was to unlock the door and make her way out. Can you help her in opening the door?

### Difficutly: very easy
----------
Upon visiting the given address, we see a locked keypad:
![[Pasted image 20230325101548.png]]

There is not much going on with the page, so we can check the page source with CTRL+U.

In the source code, we see the correct pin:
```
<body>
	<script>
		window.CONFIG = window.CONFIG || {
			buildNumber: "v20190816",
			debug: false,
			modelName: "Valencia",
			correctPin: "8291",
		}
	</script>
```
Just like that, the flag is given:
![[Pasted image 20230325101735.png]]
However, we cannot highlight for easy copy paste. We will inspect the object. Right clicking over the flag, we can Inspect, and the flag is in text:
![[Pasted image 20230325101856.png]]
From here we can right click and "copy inner HTML". Now we have the flag to paste easy, and guaranteed free from spelling errors.

`HTB{V13w_50urc3_c4n_b3_u53ful!!!}`