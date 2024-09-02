import string

def caesar_encrypt(message, key):
    shift = key % 26
    # Create translation map for both lowercase and uppercase
    translation_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] +
        string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    )
    encrypted_message = message.translate(translation_table)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = key % 26
    reverse_shift = 26 - shift
    # Create translation map for both lowercase and uppercase
    translation_table = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[reverse_shift:] + string.ascii_lowercase[:reverse_shift] +
        string.ascii_uppercase[reverse_shift:] + string.ascii_uppercase[:reverse_shift]
    )
    message = encrypted_message.translate(translation_table)
    return message

message = 'Hello, its your neighborhood cryptologist!'
key = 3

encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')


