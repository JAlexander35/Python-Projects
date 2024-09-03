Python script implemenets the Caesar cipher, a basic encryption technique.

## What is Caesar Cipher? 
![pexels-cottonbro-7319085](https://github.com/user-attachments/assets/33511948-0d30-4f85-a8b9-e85208b4a4f7)

The Caesar cipher is a simple substitution cipher named after Julius Caesar, who is believed to have usedit to communicate secretly with his generals. It is one of the oldest and most straightforward encryption techniques.
In a Caesar cipher, each letter in the plaintext (the message you want to encrypt) is shifted by a fixed number of positions down or up the alphabet. This fixed number is called the key.

# Functions:
![Screenshot 2024-09-02 123114](https://github.com/user-attachments/assets/68cec800-8c04-45d5-8540-4ec3b1367713)
**caesar_encrypt(message, key):**

Purpose: Encrypts the input message using the Caesar cipher.

How it works:
- It calculates a shift value based on the provided '**key**'. The shift is taken modulo 26 to handle cases where the key might be larger than the alphabet.
- A translation table is created using '**str.maketrans**' to map each letter in the alphabet to a new letter shifted by the key positions. The same shift is applied to both uppercase and lowercase letters.
- The translate method applies this translation table to the message, resulting in an encrypted message.

**caesar_decrypt(encrypted_message, key)**

Purpose: Decrypts the '**encrypted_message**' using the Caesar cipher by reversing the encryption process.

How it works:

- It calculates a reverse shift (26 minus the shift) to undo the encryption.
- A translation table is created to map each letter back to its original position.
- The **translate** method is used to apply this translation, yielding the original message.

# Output:
![Screenshot 2024-09-02 123120](https://github.com/user-attachments/assets/992fa725-9a6f-49c6-bc40-74b1e07f660b)
- Encrypted message: "Khoor, lwv brxu qhljkerukrrg fubswrorjlvw!"
- Decrypted message: "Hello, its your neighborhood cryptologist!"
