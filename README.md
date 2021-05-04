# uwlCipher
**Python 3.8**

This is a cipher which encrypts a message with a combination of Caesar cipher and our own uwlCipher.
It changes characters to the specific name of a University of West London staff member.

**How to use?**

This is the 2.0 version of the script, it still can be updated

At the end of the script you will find this code for testing:

`````
f = open("demoEmail.txt", "r")

encryptedEmail = uwlEncrypt(f.read(), 156, 663)

print(encryptedEmail)

print(uwlDecrypt(encryptedEmail, 156, 663))
`````

Try changing the demoEmail.txt fail to encrypt and decrypt your own messages!

This version of cipher uses two keys. You must know both to be able to decrypt the secret message.

NOTE: they key for encryption and decryption must match

------------------------------------------------------------------------------------------------------------------------

_Cyber Security_

_University of West London;_

_Assignment 2_

_Markas Vysniauskas_

_Student ID: 21372173_
