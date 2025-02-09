# my first gr1dl0ck crypto challenge

## Crypto Challenge Set 1
- This is the qualifying set. We picked the exercises in it to ramp developers up gradually into coding cryptography, but also to verify that we were working with people who were ready to write code.
-This set is relatively easy. With one exception, most of these exercises should take only a couple minutes. But don't beat yourself up if it takes longer than that. It took Alex two weeks to get through the set!
- Convert hex to base64
The string:  
`49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d`  
Should produce:  
`SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`  
- Cryptopals Rule
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

## Challenge 2: Fixed XOR

-Write a function that takes two equal-length buffers and produces their XOR combination. 
-If your function works properly, then when you feed it the string:
`1c0111001f010100061a024b53535009181c`
- ... after hex decoding, and when XOR'd against:
`686974207468652062756c6c277320657965`
- should produce:
`746865206b696420646f6e277420706c6179`

## Challenge 3: Single-byte XOR cipher

- The hex encoded string: 

`1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736`

- ... has been XOR'd against a single character. Find the key, decrypt the message. 
- You can do this by hand. But don't: write code to do it for you. 
- How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 




## How Base64 Works
- Base64 is an encoding scheme that converts binary data into a text-based format 
- - using a set of 64 characters (A-Z, a-z, 0-9, "+", and "/"). 
- It is commonly used to encode data for transmission over text-based protocols 
- - such as email (MIME) and HTTP. 
- Base64 ensures that binary data remains intact without modification when transferred between systems.

How Base64 Works
Takes binary data and divides it into 6-bit chunks.
Maps each 6-bit chunk to one of the 64 characters in the Base64 alphabet.
Pads the output with = if necessary to maintain a multiple of 4 characters.
Common Uses of Base64
Encoding images, audio, and files for embedding in emails or web pages.
Storing binary data (like cryptographic keys) in text-based formats (JSON, XML).
Sending data in URL parameters (though URL-safe variants exist).
- Takes binary data and divides it into 6-bit chunks.
- Maps each 6-bit chunk to one of the 64 characters in the Base64 alphabet.
- Pads the output with = if necessary to maintain a multiple of 4 characters.
- Common Uses of Base64
- Encoding images, audio, and files for embedding in emails or web pages.
- Storing binary data (like cryptographic keys) in text-based formats (JSON, XML).
- Sending data in URL parameters (though URL-safe variants exist).
