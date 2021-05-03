# uwlCipher
**Python 3.8**

This is a cipher which encrypts a message with a combination of Caesar cipher and our own uwlCipher.
It changes characters to the specific name of a University of West London staff member.

**How to use?**

At this point the cipher is incomplete, we are still testing it.

At the end of the script you will find this code for testing:

`````
message = 'ABC 123 *'

secret = uwlEncrypt(message, 447)

print('ABC 123 * encrypted:')

print(secret)

print('ABC 123 * decrypted:')

print(uwlDecrypt(secret, 447))
`````

Try changing the message and the key varibles to try out different combinations

NOTE: they key for encryption and decryption must match

------------------------------------------------------------------------------------------------------------------------

_Cyber Security_

_University of West London;_

_Assignment 2_

_Markas Vysniauskas_

_Student ID: 21372173_
