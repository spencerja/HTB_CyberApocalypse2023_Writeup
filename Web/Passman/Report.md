# Passman
## Description
Pandora discovered the presence of a mole within the ministry. To proceed with caution, she must obtain the master control password for the ministry, which is stored in a password manager. Can you hack into the password manager?

### Difficulty: easy
---
Visiting the page we are greeted with a login page. We are also presented with the option to create an account. After guessing a few times for user admin, I decide to create a user. Trying username `admin` results in an error, telling us this username is in use. Good to note; for now we will create user `a`.
Registering as user a was successful, and now we see a page where we might submit and store passwords for given addresses. This page operates as a password manager, true to the challenge description and title. A brief check at XSS fails, so let's explore the provided source code.
Interestingly, the `database.js` file shows us more request options than we might have expected. In particular, there is an option to update passwords:
```
    async updatePassword(username, password) {
        return new Promise(async (resolve, reject) => {
            let stmt = `UPDATE users SET password = ? WHERE username = ?`;
            this.connection.query(
                stmt,
                [
                    String(password),
                    String(username)
                ],
                (err, _) => {
                    if(err)
                        reject(err)
                    resolve();
                            }
            )
        });
    }
```
There is no authorization verification here, so perhaps if we can request to change the password of user admin, we can login as admin.
Starting with a post request to register a new user:

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Passman/Screencaps/Pasted%20image%2020230325201148.png)

Revised post request:

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Passman/Screencaps/Pasted%20image%2020230325201127.png)

Response:

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Passman/Screencaps/Pasted%20image%2020230325201228.png)

We have updated the admin password successfully, or so it says. When we attempt to login as admin, we are successful! The flag is given in the password field of admin's saved passwords.

![image](https://github.com/spencerja/HTB_CyberApocalypse2023_Writeup/blob/main/Web/Passman/Screencaps/Pasted%20image%2020230325201439.png)

`HTB{1d0r5_4r3_s1mpl3_4nd_1mp4ctful!!}`

