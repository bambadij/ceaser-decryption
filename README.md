# ceaser-decryption
Caesar's Cipher Decryption

The IT team needs to comply with the companies' policies on data privacy,  

your boss tasks you to write an algorithm to encrypt and decrypt its internal messages using Caesar's Cipher

In cryptography, a Caesar cipher, also known as shift cipher, is one of the simplest and most widely known encryption techniques. 

It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 

For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. 

For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

Plain:  ABCDEFGHIJKLMNOPQRSTUVWXYZ

Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

When encrypting, a person looks up each letter of the message in the “plain” line and writes down the corresponding letter in the “cipher” line.



Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

Deciphering is done in reverse, with a right shift of 3.
