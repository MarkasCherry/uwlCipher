# uwlCipher
**Python 3.8**

This is our UWL cipher which uses uwl staff members names to encrypt the message.
You can pass secret code as lock (for example, lock = [41, 64, 11], where lock[ i ] <= 128).


**How to use?**

This is the 3.0 version of the script, it still can be updated to encrypt the message recursively.

At the end of the script you will find this code for testing:

`````
f = open("demoEmail.txt", "r")

encryptedEmail = uwlEncrypt(f.read(), [3, 8, 9])

print(encryptedEmail)

print(uwlDecrypt(encryptedEmail, [3, 8, 9]))
`````

Try changing the demoEmail.txt fail to encrypt and decrypt your own messages!

This version of cipher uses two keys. You must know both to be able to decrypt the secret message.

NOTE: they key for encryption and decryption must match

**Hacking the secret message**

I have also provided a brute force algorithm to hack the example key:

```
# BRUTE FORCE HACKING
import time

start = time.time()
for i in range(128):
    for j in range(128):
        for k in range(128):
            print(uwlDecrypt(encryptedEmail, [i, j, k]))
            print('--------------------------------------------------------')
            print('Time took to decrypt:', time.time() - start)
            print('Keys used:', i, ', ', j, ', ', k)
            print('--------------------------------------------------------')
```



------------------------------------------------------------------------------------------------------------------------

_Cyber Security_

_University of West London;_

_Assignment 2_

_Markas Vysniauskas_

_Student ID: 21372173_
